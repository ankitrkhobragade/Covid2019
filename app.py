import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load data
p_data = pd.read_csv("state_wise_daily data file IHHPET.csv")

# Calculate stats
total_cases = p_data['Status'].shape[0]
active = p_data[p_data['Status'] == 'Confirmed'].shape[0]
recovered = p_data[p_data['Status'] == 'Recovered'].shape[0]
death = p_data[p_data['Status'] == 'Deceased'].shape[0]

# UI
st.title("🦠 Covid Dashboard")

# Top stats
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Cases", total_cases)
col2.metric("Active Cases", active)
col3.metric("Recovered", recovered)
col4.metric("Total Deaths", death)

# Dropdown for first graph
st.subheader("🛠️ Commodity Distribution")
option2 = ['All', 'Mask', 'Sanitizer', 'Oxygen']
type = st.selectbox("Select Commodity", option2)

if type == 'All':
    fig = go.Figure(go.Scatter(x=p_data['Status'], y=p_data['Total'], mode='lines'))
elif type == 'Mask':
    fig = go.Figure(go.Scatter(x=p_data['Status'], y=p_data['Mask'], mode='lines'))
elif type == 'Sanitizer':
    fig = go.Figure(go.Scatter(x=p_data['Status'], y=p_data['Sanitizer'], mode='lines'))
else:
    fig = go.Figure(go.Scatter(x=p_data['Status'], y=p_data['Oxygen'], mode='lines'))

fig.update_layout(title="Commodity Total Count", plot_bgcolor='pink')
st.plotly_chart(fig)

# Pie chart for zones
st.subheader("📊 Zone-wise Distribution")
option3 = ['Status', 'Red Zone', 'Blue Zone', 'Green Zone', 'Orange Zone']
value = st.selectbox("Select Zone", option3)
fig2 = px.pie(data_frame=p_data, names=value, hole=0.5)
st.plotly_chart(fig2)

# Bar chart for state-wise data
st.subheader("📈 State-wise Stats")
option1 = ['All', 'Hospitalized', 'Recovered', 'Deceased']
category = st.selectbox("Select Category", option1)

if category == 'All':
    fig3 = go.Figure(go.Bar(x=p_data['State'], y=p_data['Total']))
elif category == 'Hospitalized':
    fig3 = go.Figure(go.Bar(x=p_data['State'], y=p_data['Hospitalized']))
elif category == 'Recovered':
    fig3 = go.Figure(go.Bar(x=p_data['State'], y=p_data['Recovered']))
else:
    fig3 = go.Figure(go.Bar(x=p_data['State'], y=p_data['Deceased']))

fig3.update_layout(title='State Total Count', xaxis_title="States", plot_bgcolor="orange")
st.plotly_chart(fig3)
