from operator import concat
import streamlit as st
import pandas as pd
import time
import json
from bokeh.models.widgets import Div

import modal
#import streamlit_modal as modal
import streamlit.components.v1 as components

def gr_link ():
        js = "window.open('https://www.generecommender.com/en/dashboard?screen=signup')"  # New tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)


def open_modal():
        with modal.container():
                st.subheader('Exploit the full potential of Artificial Intelligence')
                st.markdown("GeneRecommender is built on an extremely advanced neural network able to scan millions of papers. Registering with your academic email you will access the full functionalities of the system and you will be able to use advanced Machine Learning as a support for your research.")
                st.markdown("""Registering you will be able to:
- Edit the input, inserting any disease or gene involved in your study
- Get up to 30 recommended genes per query
- Explore the output through a vast number of online resources""")
                col1, col2 = st.columns([1, 1])
                col1.text('Full Version Tutorial')
                col1.video("https://youtu.be/KLPNX5XXMQQ")
                col2.text('AI for Life Science Researchers')
                col2.video("https://www.youtube.com/G8QKXORcets")
                
                st.button('Sign up to www.GeneRecommender.com',key="modal", on_click=gr_link)




with open('data.json', 'r') as f:
  data = json.load(f)


st.title('GeneRecommender - Demo')

st.markdown("""This is a demo of the GeneRecommender platform with limited functionalities. This advanced Artificial Intelligence system is able to suggest which genes might be involved in your research. The required inputs are:
- One or more diseases
- Genesymbols of proteins you already know to be related""")
st.button('Sign up to www.GeneRecommender.com',key="main", on_click=gr_link)


dis=st.selectbox('Chose a disease', ['Select disease',"Alzheimer's Disease, C0002395", 'Diabetes Mellitus, Non-Insulin-Dependent, C0011860','Obesity, C0028754'])
if dis != "Select disease":

        df=pd.DataFrame(data[dis]['input'])
        df.reset_index(drop=True)

        col_title=concat(dis, " Input Genes")
        df.columns=[col_title]

        col1, col2 = st.columns([2, 1])

        col1.dataframe(df[col_title])
        col2.write("")
        col2.write("")
        col2.button('Edit gene list or choose a different disease', on_click=open_modal)
        ask=st.button('Ask AI for suggestion')
        bar_placeholder = st.empty()
        if ask:
                with bar_placeholder.container():
                        st.subheader("Artificial Intelligence processing...")
                        my_bar = st.progress(0)
                        for percent_complete in range(50):
                                time.sleep(0.1)
                                my_bar.progress(percent_complete*2 + 1)
                bar_placeholder.empty()        

                st.subheader('Artificial Intelligence Reccomendations')
                c = st.container()
                for elem in data[dis]['output']:
                        with c.expander(elem[0], expanded=False):
                                col1, col2 = st.columns([1, 1])
                                col1.write(elem[1])
                                col2.button('Inspect Gene Resources', key=elem, on_click=open_modal)
                c.button('Get more genes', key=elem, on_click=open_modal)





