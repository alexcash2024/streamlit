import streamlit as st
import pandas as pd
import plotly.express as px
table=pd.DataFrame({"column1":[1,2,3,4,5,6,7],"column2":[22,45,90,78,65,78,100]})
st.title("HI STREAMLIT IS POWERFUL WEB APPLICATION")
st.write(table)
st.text("streamlit is used by data science for them to create statistical app in datascience.")
st.text("Streamlit is used by data science for them to create visualization app in datascience.")

## Add visualization to streamlit
heatmap_fig=px.imshow(table.values,x=table.columns,y=table.index,color_continuous_scale="Viridis")
st.plotly_chart(heatmap_fig,use_container_width=True)

#pie chart
pie_chart_fig=px.pie(table,values="column2",names="column1",title="Pie Chart")
st.plotly_chart(pie_chart_fig,use_container_width=True)

##Bar Plot
bar_plot_fig=px.bar(table,x="column1",y="column2",title="Bar plot")
st.plotly_chart(bar_plot_fig,use_container_width=True)

##Treemap
treemap_data=pd.DataFrame({
    "category":["Bola","Ahmad","Musa","Shola","Adamu","Grace","Blessing"],
    "Subcategory":["Biologist","Engineer","Full stack Developer","Medical Doctor","Nurse","Data Scientist","Trader"],
    "value":[10,20,30,40,50,60,70]})
treemap_fig=px.treemap(treemap_data,path=["category","Subcategory"],values="value")
st.plotly_chart(treemap_fig,use_container_width=True)

# map
choropleth_data=pd.DataFrame({
    "country":["Nigeria", "Ghana","Togo", "Benin","senegal","Cameroon","Nigeria"],
    "value":[10,20,30,40,50,60,70]})
st.title("choropleth Map for Country")
st.write(choropleth_data)
st.title("choropleth maps visualize geographical data.")
choropleth_fig=px.choropleth(choropleth_data,locations="country",locationmode="country names",color="value",title="choropleth Map",color_continuous_scale="deep")
st.plotly_chart(choropleth_fig,use_container_width=True)
