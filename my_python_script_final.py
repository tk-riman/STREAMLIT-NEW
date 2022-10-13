#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly as pt
import plotly.express as px
import streamlit as st


# In[2]:


height_v_country = pd.read_csv("Height of Male and Female by Country 2022.csv")
tipping_dataset = pd.read_csv("tips.csv")
global_plastic_prod = pd.read_csv("global-plastics-production.csv")

# In[3]:


fig_1 = px.box(height_v_country, x="Male Height in Cm", title="Male Height in Cm")


# In[4]:


fig_2 = px.violin(height_v_country, y="Female Height in Cm", title="Female Height in Cm")


# In[5]:


fig_3 = px.histogram(height_v_country, x="Country Name", y="Male Height in Cm", title="Average Height Vs. Country")


# In[6]:


fig_4 = px.scatter(tipping_dataset, x="total_bill", y="tip", color="sex", size="size", title="Tip V. Total Bill")


# In[7]:


fig_5 = px.line(global_plastic_prod, x="Year", y="Global plastics production (million tonnes)", title="Global Plastic Generation V. Years")


# In[8]:


interactive_plot_1 = st.container()
interactive_plot_2 = st.container()
interactive_plot_3 = st.container()
interactive_plot_4 = st.container()
interactive_plot_5 = st.container()
interactive_plot_6 = st.container()


# In[14]:


with interactive_plot_1:
    st.header("Have you ever wondered whether your height is average or not?")
    st.text("Check this out, Let's start with the boys!")
    st.plotly_chart(fig_1, use_container_width=True)


# In[15]:


with interactive_plot_2:
    st.title("Now, let's check it for the girls!")
    st.plotly_chart(fig_2, use_container_width=True)


# In[16]:


with interactive_plot_3:
    st.title("Maybe a histogram can change our perspective")
    st.header("Don't be startled, this is the avergae of total heights per country!")
    st.plotly_chart(fig_3, use_container_width=True)
    st.dataframe(height_v_country)


# In[17]:


with interactive_plot_5:
    st.header("Is the plastic Waste Generation Increasing Throughout the Years?")
    st.text("it seems so, here we see that with the passage of time, more tonnes of plastic waste is generated")
    st.plotly_chart(fig_5, use_container_width=True)
    st.text("Click the Donate Button and Help Combat Plastic Waste")
    result = st.button("Donate Button")
    st.write(result)
    if result:
        st.write("https://crisisrelief.un.org/donate")
    


# In[25]:


with interactive_plot_4:
    
    sex_list = ['All'] + tipping_dataset['sex'].unique().tolist()
    st.header("Do tables with higher bills also tip higher?")
    st.write('You can choose the sex from box')
    s_selected = st.selectbox('Which sex do you want to choose for the filter?', sex_list, key='start_station')

    # display the collected input
    st.write('You selected : ' + str(s_selected))

    # you can filter the data based on user input and display the results in a plot
    if s_selected != 'All':
        display_data = tipping_dataset[tipping_dataset['sex'] == s_selected]
        

    else:
        display_data = tipping_dataset.copy()
        
   
    fig_8 = px.scatter(display_data, x="total_bill", y="tip", size="size", title="Tip V. Total Bill")

    st.plotly_chart(fig_8, use_container_width=True) 
    
    
with interactive_plot_6:
    st.header("How tips differ according to size?")
    st.text("You can choose the size from the slider below ")
    size = st.slider('Size',1, 6)
    slider_data = tipping_dataset[tipping_dataset['size'] == size]
    fig_6 = px.histogram(slider_data, x="sex", y="total_bill",color="sex", title="sex vs total bill")

    st.plotly_chart(fig_6, use_container_width=True)


# In[ ]:




