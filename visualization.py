# visualization.py
import plotly.express as px

def generate_pie_chart(data):
    return px.pie(
        data, names='Category', values='Amount', title="Expenses by Category",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

def generate_line_chart(data):
    return px.line(
        data, x='Date', y='Amount', title="Spending Over Time",
        line_shape="spline", markers=True,
        color_discrete_sequence=["#3b78e7"]
    )
