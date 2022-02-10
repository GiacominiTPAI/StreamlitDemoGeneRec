import streamlit as st
import pandas as pd
import plotly.express as px

def color_negative_red(value):
  """
  Colors elements in a dateframe
  green if positive and red if
  negative. Does not color NaN
  values.
  """

  if value < 0.5:
    color = 'red'
  elif value > 0.5:
    color = 'green'
  else:
    color = 'black'

  return 'color: %s' % color



data=pd.read_csv('Data.csv')
st.title('DeepProphet Evaluation system')
st.subheader('Evaluarion data:')

c1, c2, c3 = st.columns(3)
c1.metric("Evaluated Algorithms", str(data['algorithm'].nunique()))
c2.metric("Evaluated Datasets", str(data['dataset'].nunique()))
c3.metric("Evaluated Buckets", str(data['bucket'].nunique()))

st.dataframe(data)

col1, col2= st.columns(2)

alg=col1.multiselect('Chose the algorithm:', data['algorithm'].unique(),default =data['algorithm'].unique())
d_set=col2.multiselect('Chose the test dataset:', data['dataset'].unique(), default =data['dataset'].unique())
buck=col1.multiselect('Chose the bucket:', data['bucket'].unique(), default =data['bucket'].unique())
metr=col2.multiselect('Chose the test metric:', data['metric'].unique(), default = data['metric'].unique())

if metr != list(['pr_curve']):
    #st.text(metr)
    dt=data[(data['algorithm'].isin(alg)) & (data['dataset'].isin(d_set))& (data['bucket'].isin(buck))& (data['metric'].isin(metr))]
    dt=dt.drop(['metric_sub','point_k'], axis=1)
    st.table(dt.style.applymap(color_negative_red, subset=['value']))
else:
    #st.text(metr)
    dt=data[(data['algorithm'].isin(alg)) & (data['dataset'].isin(d_set))& (data['bucket'].isin(buck))& (data['metric'].isin(metr))]
    dt_p= dt[dt["metric_sub"]=="precision"]
    dt_r= dt[dt["metric_sub"]=="recall"]
    dt = pd.merge(dt_p, dt_r, how="inner", on=['time_stamp','algorithm','dataset','bucket','point_k'])
    dt["curve"] = dt["time_stamp"].astype(str) +'-'+ dt["algorithm"] +'-'+ dt["dataset"] +'-'+ dt["bucket"].astype(str)
    dt = dt.sort_values(by="point_k")
    fig = px.line(dt, x='value_x', y='value_y',color='curve', title='Precision recall curve')
    st.plotly_chart(fig, use_container_width=True)

