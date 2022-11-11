#streamlit.stop()
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title(' My parents new healthy diner')
streamlit.title('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text(' 🥗 Kate, Spinach & Rocket smoothie')
streamlit.text(' 🐔 Hard-boiled Free-Range egg')
streamlit.text(' 🥑🍞 Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list) 

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


#streamlit.stop()
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('from streamlit')")
my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('from streamlit')")
my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('from streamlit')")
my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('from streamlit')")
my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('from streamlit')")

