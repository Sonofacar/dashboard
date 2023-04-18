import pandas as pd
import plotly.express as px
import streamlit as st

# Load the data
df = pd.read_csv('popular_names.csv')

# Set up the dashboard
st.title('Popular Baby Names')

# Get user input
genders = ['M', 'F']
selected_name = st.text_input('Name','John')
selected_gender = st.selectbox('Gender', genders)

# Making the graph
Title = 'Popularity of ' + selected_name + ' by year since 1910'
fig = px.line(df.loc[df.name == selected_name, :].loc[df.sex == selected_gender], x = 'year', y = 'n', hover_data = ['n'])
fig.update_layout(title = Title)

# Delpoy the graph
st.plotly_chart(fig)
