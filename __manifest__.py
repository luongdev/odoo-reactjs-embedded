{
    'name': 'p-plugin',
    'version': '0.0.1',
    'sequence': 2,
    'depends': ['base', 'bus'],
    'data': [
        'xml/templates.xml',
        'xml/actions.xml',
        'xml/menu.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_common': [
            'p-plugin/static/src/lib/react.development.js',
            'p-plugin/static/src/lib/react-dom.development.js',
            'p-plugin/static/src/js/components/**/*.js'
        ],
        'web.assets_backend': [
            'p-plugin/static/src/views/root-view.js',
        ],
        'web.assets_backend_prod_only': [
            'p-plugin/static/src/js/main.js'
        ],
        'web.assets_qweb': [
            'p-plugin/static/src/views/root-view.js'
        ]
    },
    'license': 'LGPL-3',
}
