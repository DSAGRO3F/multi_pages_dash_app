# -*- coding: utf-8 -*-
import dash
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
from dash import dcc
from dash.dependencies import Input, Output
from dash import dash_table
import dash_bootstrap_components as dbc


import plotly.express as px
#import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

dash.register_page(__name__,
                   path='/analytics-dashboard',
                   title='Analytics Dashboard 1',
                   name='Analytics Dashboard 1',
                   location="sidebar")

"""This code works"""

# layout = html.Div([
#     dcc.Store(id='store', data=df.to_dict('records')),
#     html.Div([
#         html.H1('Full table', style={'textAlign': 'center'}),
#         html.Br(),
#         dash_table.DataTable(data=[], id='table', page_size=10),
#         html.Br(),
#         html.Br()]),
#     html.Div([
#         html.H2('Table from selected continent'),
#         dcc.Dropdown(id='dropdown-continent', options=df['continent'].unique(), value='Europe'),
#         html.Br(),
#         html.Br(),
#         dash_table.DataTable(
#             id='table-continent',
#             columns=[{"name":i, "id": i} for i in df.columns],
#             fixed_columns={'headers': True, 'data': 1},
#             page_size=15),
#         ]),
#     ])
        

layout = dbc.Row([
    dbc.Col([
        html.H1('Full table', style={'textAlign': 'center'}),
        html.Br(),
        html.Hr(),
        dash_table.DataTable(data=[], id='table', page_size=10),
        html.Br(),
        html.Br(),
        ]),
    dbc.Row([
        dbc.Col([
            html.H2('Table from selected continent'),
            html.Br(),
            html.Br(),
            dcc.Dropdown(id='dropdown-continent', options=df['continent'].unique(), value='Europe'),
            dash_table.DataTable(
                id='table-continent',
                columns=[{"name":i, "id": i} for i in df.columns],
                fixed_columns={'headers': True, 'data': 1},
                page_size=15),
            ]),
        dbc.Col([
            html.H2('Graph from selected continent'),
            html.Br(),
            html.Br(),
            dcc.Graph(id='graph-from-selected-continent', figure={})]),
        ]),
    ])

@callback(
    Output('store', 'data'),
    Input('store', 'data'))
def fn_store(data):
    if data == {}:
        data = df.to_dict('records')
    return data



@callback(
    Output('table', 'data'),
    Input('store', 'data'))
def fn_table(data):
    return data



@callback(
    [Output('table-continent', 'data'),
      Output('table-continent', 'columns')],
    Input('dropdown-continent', 'value'))
def fn_dropdown(continent):
    df_c = df[df['continent'] == continent]
    return df_c.to_dict('records'), [{"name":i, "id": i} for i in df_c.columns]



@callback(
    Output('graph-from-selected-continent', 'figure'),
    Input('table-continent', 'data'))
def fn_graph(data):
    df = pd.DataFrame(data)
    fig = px.scatter(df,
                     x='gdpPercap',
                     y='lifeExp',
                     color='country',
                     hover_name='continent',
                     size='pop')
    return fig










