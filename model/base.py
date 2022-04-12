from odoo import models, fields, api
from odoo.addons.base.models.assetsbundle import AssetsBundle, JavascriptAsset, CompileError
from subprocess import Popen, PIPE
from odoo.tools import misc
import logging
_logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    _name = 'p.base'


class BabelJavascriptAsset(JavascriptAsset):

    def get_command(self):
        return [
            '/Users/dot/.node/16/bin/babel',
            '--presets=/Volumes/workspace/dev/odoo/node_modules/babel-preset-react'
        ]

    def compile(self, source):
        command = self.get_command()
        try:
            compiler = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        except Exception:
            raise CompileError("Could not execute command %r" % command[0])

        (out, err) = compiler.communicate(input=source.encode('utf-8'))
        if compiler.returncode:
            cmd_output = misc.ustr(out) + misc.ustr(err)
            if not cmd_output:
                cmd_output = u"Process exited with return code %d\n" % compiler.returncode
            raise CompileError(cmd_output)
        return out.decode('utf8')

class AssetsBundleBabel(AssetsBundle):

    def __init__(self, bundle_name, files, env=None, css=True, js=True):
        super(AssetsBundleBabel, self).__init__(bundle_name, files, env=env, css=css, js=js)
        for idx, js in enumerate(self.javascripts):
            if js.url.startswith('/p-plugin/static/src/js/components') and js.url.endswith('.js'):
                print('file {}'.format(js.url))
                self.javascripts[idx] = BabelJavascriptAsset(self, url=js.url, filename=js._filename, inline=js.inline)

    def transpile_babel(self):
        def handle_compile_error(e, source):
            error = self.get_preprocessor_error(e, source=source)
            _logger.warning(error)
            self.css_errors.append(error)
            return ''

        if self.javascripts:
            need_transpile = [asset for asset in self.javascripts if isinstance(asset, BabelJavascriptAsset)]
            compiled = ''
            if len(need_transpile) > 0:
                source = '\n'.join([asset.content for asset in need_transpile])
                compiler = need_transpile[0].compile
                try:
                    compiled = compiler(source)
                    return compiled
                except CompileError as e:
                    return handle_compile_error(e, source=source)
            else:
                return compiled

    def js(self, **kwargs):
        attachments = self.get_attachments('js')
        if not attachments or True:
            content = ';\n'.join([asset.minify() for asset in self.javascripts if not isinstance(asset, BabelJavascriptAsset)])
            content = content + ';\n' + self.transpile_babel()
            return self.save_attachment('js', content)
        return attachments[0]


class QWeb(models.AbstractModel):
    _inherit = 'ir.qweb'

    def get_asset_bundle(self, bundle_name, files, env=None, css=True, js=True):
        return AssetsBundleBabel(bundle_name, files, env=env, css=css, js=js)

