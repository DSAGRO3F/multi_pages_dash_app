import dash
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
from dash import dcc
from dash.dependencies import Input, Output
from dash import dash_table
import dash_bootstrap_components as dbc


import plotly.express as px
#import plotly.graph_objects as go

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
df = px.data.gapminder()

print(f'df.info() {df.info()}')


dash.register_page(__name__, 
                   path='/geo-analytics',
                   title='Geo_analytics',
                   name='Geo_analytics',
                   location="sidebar")

print(f'df.head() ==> {df.head()}')

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2('Table from selected year'),
            html.Br(),
            dash_table.DataTable(data=[],
                                 id='full-table-geo',
                                 columns=[],
                                 fixed_columns={'headers':True, 'data':1},
                                 page_size=15,
                                 style_cell={'padding': '5px'},
                                 style_header={'backgroundColor': 'white',
                                               'fontWeight': 'bold',
                                               'border': '1px solid pink'},
                                 style_data={ 'border': '1px solid blue' }
                                 )
            ]),
        dbc.Col([
            html.H2('Graph'),
            html.Br(),
            dbc.Select(id='select-input', 
                       options=[{"label": str(year), "value": str(year)} for year in df['year'].unique()],
                       value=max(df['year'].unique())),
            dcc.Graph(id='geo', figure={})])
        ])
    ])


@callback(
    Output('store-df-geo', 'data'),
    Input('store-df-geo', 'data'))
def fn_store(data):
    if data == {}:
        data = df.to_dict('records')
        
    # print(f'type(data) --- {type(data)}')
    # print(f'list data --- {data[0:2]}')
    # print(f'df_geo ---- {pd.DataFrame(data).head()}')
    return data



@callback(
    [Output('full-table-geo', 'data'),
     Output('full-table-geo', 'columns')],
    [Input('store-df-geo', 'data'),
     Input('select-input', 'value')]
    )
def fn_table_from_selected_year(data, year):
    df = pd.DataFrame(data)
    year = int(year)
    print(f'year {year}')
    df_from_selected_year = df[df['year'] == year]
    
    print(f'df + df_from_selected_year:  {df.head()} -- {df_from_selected_year.head()}')
    
    records = df_from_selected_year.to_dict('records')
    columns = [{"name": col, "id": col} for col in df_from_selected_year.columns]
    return records, columns




@callback(
    Output('geo', 'figure'),
    Input('full-table-geo', 'data')
    )
def fn_graph(data):
    print(f'data type --- {type(data)}')
    df = pd.DataFrame(data)
    print(f'df_graph: {df.head()}')
    
    
    fig = px.choropleth(df, locations="iso_alpha",
                        color="lifeExp",
                        hover_name="country",
                        projection= 'natural earth',
                        title= 'Life Expectancy by Year',
                        color_continuous_scale=px.colors.sequential.Plasma)

    fig.update_layout(title=dict(font=dict(size=28), x=0.5, xanchor='center'),
                        margin=dict(l=60, r=60, t=50, b=50))
    
    return fig





