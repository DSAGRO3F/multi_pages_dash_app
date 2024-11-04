# -*- coding: utf-8 -*-
import dash
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
from dash import dcc
from dash.dependencies import Input, Output
from dash import dash_table
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, 
                use_pages=True,
                external_stylesheets=[dbc.themes.SPACELAB])

sidebar = dbc.Nav(
    [dbc.NavLink(
        
        [html.Div(page['name'], className='ms-2')],
        
        href=page['path'],
        
        active='exact') for page in dash.page_registry.values()],
    
    vertical=True,
    pills=True,
    className='bg-light')




app.layout = dbc.Container([
    html.Div([
        dcc.Store(id='store', data={}, storage_type='local'),
        dcc.Store(id='store-min', data={}, storage_type='local'),
        dcc.Store(id='store-max', data={}, storage_type='local'),
        dcc.Store(id='store-value', data={}, storage_type='local'),
        dcc.Store(id='store-marks', data={}, storage_type='local')
        ]),

    
    dbc.Row([
        dbc.Col(
            html.Div("Gdp -- Life exp Analysis",
            style={'fontsize':100, 'textAlign': 'center', 'font-weight': 'bold'}))
        ]),
    
    
    html.Hr(),
    
    
    dbc.Row([
        dbc.Col([
            sidebar],
            xs=4,
            sm=4,
            md=2,
            lg=2,
            xxl=2),
        dbc.Col([
            dash.page_container],
            xs=8,
            sm=8,
            md=10,
            lg=10,
            xxl=10)])
    ], 
    fluid=True)

if __name__ == '__main__':
    app.run(debug=True)
















