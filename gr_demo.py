from operator import concat
#from turtle import onclick
import streamlit as st
import pandas as pd
#from streamlit_player import st_player
import time
import webbrowser

def gr_link ():
        print("go")
        webbrowser.open_new_tab("https://www.generecommender.com/en/dashboard?screen=signup")


data={ 'cancer':
                {
                'input': {'il6','tnf','appo'},
                'output':  {'pollo1','pollo2','pollo3'}
                                                },
        'diabetes':{
                'input': {'yosd','dcs','dcs','cane','gatto'},
                'output':  {'coniglio','dd','adw'}
                                                },
        'alzheimer':{
                'input': {'dccds','kkcs','soi','mvsd'},
                'output':  {'i','d','a'}
                                                }}


st.title('GeneRecommender - Demo')


dis=st.selectbox('Chose the disease you are studying', ['Select your disease','cancer', 'diabetes','problemi'])
if dis != "Select your disease":

        df=pd.DataFrame(data[dis]['input'])
        df.reset_index(drop=True)

        col_title=concat(dis, " Input Genes")
        df.columns=[col_title]

        col1, col2 = st.columns([1, 1])

        col1.dataframe(df[col_title])
        col2.write("")
        col2.write("")
        col2.button('Edit gene list or choose a different disease', on_click=gr_link)
        ask=st.button('Ask AI for suggestion')
        bar_placeholder = st.empty()
        if ask:
                print("banana")
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
                        with c.expander(elem, expanded=False):
                                col1, col2 = st.columns([1, 1])
                                col1.write("banana  " + elem)
                                col2.button('Inspect Gene Resources', key=elem, on_click=gr_link)

col1, col2 = st.columns([1, 1])
col1.text('GeneRecommender Full Version Tutorial')
col1.video("https://youtu.be/KLPNX5XXMQQ")
col2.text('GeneRecommender for Life Science Researchers')
col2.video("https://www.youtube.com/G8QKXORcets")



