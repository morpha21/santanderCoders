import plotly.graph_objects as go

import matplotlib.pyplot as plt

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

def double_pie_chart(data: list, labels: list, titles: list):
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)  

    fig, axs = plt.subplots(1, 2)

    plt.subplots_adjust(wspace=0.5)

    # Plot 1
    axs[0].pie(data[0], explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    axs[0].axis('equal')  
    axs[0].set_title(titles[0]) 

    # Plot 2
    axs[1].pie(data[1], explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    axs[1].axis('equal')
    axs[1].set_title(titles[1])

    plt.show()