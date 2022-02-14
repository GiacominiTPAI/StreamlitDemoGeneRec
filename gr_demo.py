from operator import concat
import streamlit as st
import pandas as pd
import time
import json
from bokeh.models.widgets import Div

def gr_link ():
        js = "window.open('https://www.generecommender.com/en/dashboard?screen=signup')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

with open('data.json', 'r') as f:
  data = json.load(f)


st.title('GeneRecommender - Demo')


dis=st.selectbox('Chose the disease you are studying', ['Select your disease',"Alzheimer's Disease, C0002395", 'Diabetes Mellitus, Non-Insulin-Dependent, C0011860','Obesity, C0028754'])
if dis != "Select your disease":

        df=pd.DataFrame(data[dis]['input'])
        df.reset_index(drop=True)

        col_title=concat(dis, " Input Genes")
        df.columns=[col_title]

        col1, col2 = st.columns([2, 1])

        col1.dataframe(df[col_title])
        col2.write("")
        col2.write("")
        col2.button('Edit gene list or choose a different disease', on_click=gr_link)
        ask=st.button('Ask AI for suggestion')
        bar_placeholder = st.empty()
        if ask:
                with bar_placeholder.container():
                        st.subheader("Artificial Intelligence processing...")
                        my_bar = st.progress(0)
                        for percent_complete in range(100):
                                time.sleep(0.1)
                                my_bar.progress(percent_complete + 1)
                bar_placeholder.empty()        

                st.subheader('Artificial Intelligence Reccomendations')
                c = st.container()
                for elem in data[dis]['output']:
                        with c.expander(elem[0], expanded=False):
                                col1, col2 = st.columns([1, 1])
                                col1.write(elem[1])
                                col2.button('Inspect Gene Resources', key=elem, on_click=gr_link)

col1, col2 = st.columns([1, 1])
col1.text('GeneRecommender Full Version Tutorial')
col1.video("https://youtu.be/KLPNX5XXMQQ")
col2.text('GeneRecommender for Life Science Researchers')
col2.video("https://www.youtube.com/G8QKXORcets")



