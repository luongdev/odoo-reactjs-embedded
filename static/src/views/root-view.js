/** @odoo-module **/

import App from '@p-plugin/js/components/app/index';


const {createRoot} = ReactDOM;

export class RootView extends owl.Component {
    static template = owl.tags.xml`
        <t t-name="rootViewTemplate" owl="1">
            <div id="p_root"></div>
        </t>
    `

    constructor(prt, _) {
        super(prt, _);
        this.componentRef = prt.componentRef;

    }

    mounted() {
        // const root = ReactDOM.createRoot();
        ReactDOM.render(React.createElement(App), this.componentRef.el);
        // root.render();
    }
}