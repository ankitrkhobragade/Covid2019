import pandas as pd
import dash
from dash import html,Input,Output,dcc
import plotly.graph_objs as go
import plotly.express as px


external_stylesheets = [
    {
        "href":"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
        "rel":"stylesheet",
        "integrity":"sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
        "crossorigin":"anonymous"
    }
]
p_data=pd.read_csv("state_wise_daily data file IHHPET.csv")
total_cases=p_data['Status'].shape[0]
active=p_data[p_data['Status']=='Confirmed'].shape[0]
recovered=p_data[p_data['Status']=='Recovered'].shape[0]
death=p_data[p_data['Status']=='Deceased'].shape[0]

option1 = [

    {'label':'All','value':'All'},
    {'label': 'Hospitalized', 'value': 'Hospitalized'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'}

]

option2 = [

    {'label':'All','value':'All'},
    {'label': 'Mask', 'value': 'Mask'},
    {'label': 'Sanitizer', 'value': 'Sanitizer'},
    {'label': 'Oxygen', 'value': 'Oxygen'}

]

option3 = [
    {'label': 'All', 'value': 'Status'},
    {'label':'Red Zone','value':'Red Zone'},
    {'label': 'Blue Zone', 'value': 'Blue Zone'},
    {'label': 'Green Zone', 'value': 'Green Zone'},
    {'label': 'Orange Zone', 'value': 'Orange Zone'}

]

app=dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout = html.Div([

                html.H1('Covid DashBoard',style={'textAlign':'center','color':'red'}),

                html.Div([

                        html.Div([

                                    html.Div([
                                        html.Div([
                                             html.H1("Total Cases",style={'textAlign':'center','color':'#fff'}),
                                             html.H1(total_cases,style={'textAlign':'center','color':'#fff'}),
                                         ],className='card-body')
                                     ],className='card bg-danger' ),

                        ],className='col-md-3'),

                        html.Div([
                                     html.Div([
                                        html.Div([
                                             html.H1("Active Cases",style={'textAlign':'center','color':'#fff'}),
                                             html.H1(active,style={'textAlign':'center','color':'#fff'}),
                                         ],className='card-body')
                                     ],className='card bg-info' ),
                        ],className='col-md-3'),

                        html.Div([

                                     html.Div([
                                        html.Div([
                                             html.H1("Recov. Cases",style={'textAlign':'center','color':'#fff'}),
                                             html.H1(recovered,style={'textAlign':'center','color':'#fff'}),
                                         ],className='card-body')
                                     ],className='card bg-warning' ),

                        ],className='col-md-3'),
                        html.Div([

                                     html.Div([
                                        html.Div([
                                             html.H1("Total Death",style={'textAlign':'center','color':'#fff'}),
                                             html.H1(death,style={'textAlign':'center','color':'#fff'}),
                                         ],className='card-body')
                                     ],className='card bg-success' ),

                        ],className='col-md-3')

                ],className='row'),


                html.Div([

                    html.Div([
                        html.Div([
                            html.Div([
                                dcc.Dropdown(id='plot-graph',options=option2,value='All'),
                                dcc.Graph(id='graph')
                            ],className='card-body'),
                        ],className='card'),
                    ],className='col-md-6'),


                    html.Div([
                        html.Div([
                            html.Div([
                                dcc.Dropdown(id='my_drop',options=option3,value='Status'),
                                dcc.Graph(id='the_graph')
                            ],className='card-body'),
                        ],className='card'),
                    ],className='col-md-6'),


                ],className='row'),


                html.Div([

                    html.Div([
                        html.Div([
                            html.Div([
                                dcc.Dropdown(id='picker',options=option1,value='All',
                                             clearable=False,placeholder='Select a Category',
                                             multi=False),   #style={'display':'inline-block'}),
                                dcc.Graph(id='bar')
                            ],className='card-body'),
                        ],className='card'),
                    ],className='col-md-12'),


                ],className='row'),


            ],className="Container")


@app.callback(Output('graph','figure'),[Input('plot-graph','value')])
def update_graph(type):
     if type=='All':
         return {
             'data': [go.Line(x=p_data['Status'],y=p_data['Total'])],
             'layout': go.Layout(title='Comodities Total Count', plot_bgcolor = 'pink')
         }

     if type == 'Mask':
         return {
             'data': [go.Line(x=p_data['Status'], y=p_data['Mask'])],
             'layout': go.Layout(title='Comodities Total Count', plot_bgcolor='pink')
         }

     if type == 'Sanitizer':
         return {
             'data': [go.Line(x=p_data['Status'], y=p_data['Sanitizer'])],
             'layout': go.Layout(title='Comodities Total Count', plot_bgcolor='pink')
         }

     if type == 'Oxygen':
         return {
             'data': [go.Line(x=p_data['Status'], y=p_data['Oxygen'])],
             'layout': go.Layout(title='Comodities Total Count', plot_bgcolor='pink')
         }




@app.callback(Output('the_graph','figure'),[Input('my_drop','value')])
def update_graph(value):
   #if value=='Red Zone':
     #   return {
     #       'data' : [go.Pie(x=p_data[''],labels=p_data[''])]
      #      'layout' : go.Layout(title="",plot_bgcolor='')
     #   }

    piechart = px.pie(data_frame=p_data,names=value,hole=0.5)
    return piechart





#@app.callback(Output('bar','figure'),[Input('picker','value')])
@app.callback(Output('bar','figure'),Input('picker','value'))
def update_graph(category):
    if category == 'All':
        return {'data': [go.Bar(x = p_data['State'],y=p_data['Total'])],
                'layout': go.Layout(xaxis={'title':'Sate Total Count'},plot_bgcolor='orange')
                }
    if category == 'Hospitalized':
        return {'data': [go.Bar(x=p_data['State'], y=p_data['Hospitalized'])],
                'layout': go.Layout(xaxis={'title': 'Sate Total Count'}, )
                }
    if category == 'Recovered':
        return {'data': [go.Bar(x=p_data['State'], y=p_data['Recovered'])],
                'layout': go.Layout(xaxis={'title': 'Sate Total Count'}, )
                }
    if category == 'Deceased':
        return {'data': [go.Bar(x=p_data['State'], y=p_data['Deceased'])],
                'layout': go.Layout(xaxis={'title': 'Sate Total Count'}, )
                }


if __name__=="__main__":
    app.run(Debug=True)
