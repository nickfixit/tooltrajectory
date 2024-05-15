import pandas as pd
import plotly.express as px

def create_timeline(data):
    df = pd.DataFrame(data)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    fig = px.timeline(df, x_start="Timestamp", x_end="Timestamp", y="Figure", text="Snippet", title="Key Figures and Events in History", hover_data=['Title'])
    fig.update_yaxes(categoryorder="total ascending")
    fig.update_layout(hovermode="x unified")
    fig.show()
 