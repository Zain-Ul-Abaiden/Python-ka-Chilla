# import libraries

import streamlit as st
import plotly.express as px


# import dataset

st.title("Plotly with Streamlit")
df = px.data.gapminder()
st.write(df)
st.write(df.columns)

# summary stats
st.write(df.describe())


# data management
year_option = df['year'].unique().tolist()

year = st.selectbox("Which year do you want to see?", year_option, 0)
# df = df[df['year'] == year]

# ploting

fig = px.scatter(df, x='gdpPercap', y='lifeExp', color='country', size='pop', hover_name='country', log_x=True, size_max=55, range_x=[100, 100000], range_y=[20, 90], animation_frame='year', animation_group= 'country', title='Life Expectancy vs GDP per Capita')
fig.update_layout(width=800, height=500)

st.write(fig)
