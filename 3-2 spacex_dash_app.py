# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Component variables
site_list=[{'label': 'All Sites', 'value': 'ALL'}]
sites = spacex_df['Launch Site'].unique()
for site in sites:
    site_list.append({'label': site, 'value': site})
# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site != 'ALL':
        filtered_df = filtered_df.loc[filtered_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df,names='class', title='Launch Success Counts')
    else:
        fig = px.pie(filtered_df, values='class', names='Launch Site', title='Launch Success Counts')
    return fig

@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")])
def get_scatter_plot(site, payload):
    filtered_df = spacex_df
    if site != 'ALL':
        filtered_df = filtered_df.loc[filtered_df['Launch Site'] == site]
    filtered_df = filtered_df[(filtered_df['Payload Mass (kg)'] >= payload[0]) & (filtered_df['Payload Mass (kg)'] <= payload[1])]
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', color='Booster Version Category', title='Payload vs. Outcome')
    return fig

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown'),
                                dcc.Dropdown(site_list, 'ALL', id='site-dropdown', placeholder='Select a Launch Site here', searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0',
                                                    10000: '10000',
                                                    max_payload: str(max_payload)},
                                                value=[min_payload, max_payload]),
                                # Task 4: add scatterplot
                                html.Div(dcc.Graph(id='success-payload-scatter-chart'))])


# Run the app
if __name__ == '__main__':
    app.run_server()
