import plotly.graph_objects as go

def line(*args, plot_bgcolor='rgb(255, 228, 181)', paper_bgcolor='rgb(245, 245, 220)'):
    fig = go.Figure()
    colors = ['black', 'peru', 'green']

    for i, series in enumerate(args):
        fig.add_trace(go.Scatter(x=series.index, y=series.values, mode='lines', 
                                  name=f"Series {i + 1}", line=dict(color=colors[i])))

    fig.update_layout(title='Multiple Time Series Plot',
                      xaxis_title='Date',
                      yaxis_title='Value',
                      xaxis=dict(tickangle=-45),
                      showlegend=True,
                      plot_bgcolor='palegoldenrod',
                      paper_bgcolor='bisque')
    
    fig.show()

