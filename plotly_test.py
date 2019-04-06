'''import plotly as py
py.tools.set_credentials_file(username='timrpeterson', api_key='6q8IMr6wbUGZp1TM9gNX')
py.tools.set_config_file(world_readable=False,
                             sharing='private')'''


import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

py.plot(data, filename = 'basic-line', auto_open=True)
