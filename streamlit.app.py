import streamlit
streamlit.title('My parents new healthy dinners')
streamlit.title('My moms new healthy dinners')
streamlit.header('Today menu')
streamlit.text('breakfast, dinner & lunch')
streamlit.text('🥋,📓 ')
streamlit.header('🥋 - Shirt,📓 - Book')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)




