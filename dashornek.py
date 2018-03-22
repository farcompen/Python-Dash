
#! -*- coding:utf- 8 -*- 

import dash
import dash_core_components as dcc 
import dash_html_components as html 
import bitcoin as btc

btc = btc.btcVeriAl()
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Dash uygulama'),
    dcc.Graph(
        id='dashornek',
        figure={
            'data': [
                {'x':btc.xEkseniOlustur() , 'y': btc.DegerDondur(),  'type': 'line', 'name': 'Bitcoin'},
              
            ],
            'layout': {
                'title': 'dash örnek uygulama btc/USD endeks'
            }
        }
    )
])

if __name__ =='__main__':
    app.run_server (debug= True)

