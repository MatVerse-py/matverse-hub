import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import datetime

# Sample data for the repositories
repositories = [
    {'name': 'Repo1', 'status': 'success', 'time': '2026-04-24 10:00:00'},
    {'name': 'Repo2', 'status': 'failure', 'time': '2026-04-24 10:05:00'},
    # Add remaining repositories here...
]

# Convert to DataFrame
repo_df = pd.DataFrame(repositories)

# Dashboard layout
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Container([
        html.H1('Repository Indexing Dashboard'),
        dcc.Interval(id='interval-component', interval=60*1000, n_intervals=0),  # Refresh every minute
        dcc.Graph(id='success-rate-chart'),
        html.Div(id='failed-repos'),
        html.Div(id='timing-info'),
    ])
])

# Callbacks
@app.callback(
    [dash.dependencies.Output('success-rate-chart', 'figure'),
     dash.dependencies.Output('failed-repos', 'children'),
     dash.dependencies.Output('timing-info', 'children')],
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_dashboard(n):
    # Here you would implement logic to fetch updated repository data
    success_count = (repo_df['status'] == 'success').sum()
    failure_count = (repo_df['status'] == 'failure').sum()
    total_repos = len(repo_df)

    success_rate = (success_count / total_repos) * 100
    failed_repos = repo_df[repo_df['status'] == 'failure']['name'].tolist()

    # Timing information
    current_time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    # Create success rate chart
    figure = {
        'data': [{
            'x': ['Success', 'Failure'],
            'y': [success_count, failure_count],
            'type': 'bar',
        }],
        'layout': {
            'title': f'Success Rate: {success_rate:.2f}%'
        }
    }

    failed_repos_list = html.Ul([html.Li(repo) for repo in failed_repos])
    timing_info = f'Last updated: {current_time}'

    return figure, failed_repos_list, timing_info

if __name__ == '__main__':
    app.run_server(debug=True)
