/** @odoo-module **/

const {Component} = React;

import Test from '@p-plugin/js/components/test/test'

// const {Button, Toast, Tabs, Form, Item} = dx;
console.log(dx)

export const longtabs = [
    {text: 'user'},
    {text: 'analytics'},
    {text: 'customers'},
    {text: 'search'},
    {text: 'favorites'},
    {text: 'additional'},
    {text: 'clients'},
    {text: 'orders'},
    {text: 'shipment'},
];


export default class App extends Component {


    render() {
        return (
            <div className="row dx-viewport">
                <div className="col-12 col-md-12">
                    {/*<Button*/}
                    {/*    width={120}*/}
                    {/*    text="Contained"*/}
                    {/*    type="success"*/}
                    {/*    stylingMode="contained"*/}
                    {/*/>*/}
                    {/*<Tabs*/}
                    {/*    dataSource={longtabs}*/}
                    {/*    scrollByContent={false}*/}
                    {/*    showNavButtons={false}*/}
                    {/*/>*/}
                    {/*<Toast*/}
                    {/*    visible={true}*/}
                    {/*    message={'Oi doi oi, lang nuoc oiiii'}*/}
                    {/*    type={'error'}*/}
                    {/*    displayTime={600}*/}
                    {/*/>*/}
                </div>
            </div>
        )
    }

}