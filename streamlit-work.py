import pandas as pd
import streamlit as st
from plotnine import *

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
fig = (ggplot(df.loc[df.name == selected_name].loc[df.sex == selected_gender]) +
       geom_line(aes(x = 'year', y = 'n')) +
       labs(title = Title))

# Delpoy the graph
st.pyplot(ggplot.draw(fig))
