import pandas as pd
import streamlit as sg
import plotly.express as px

option=["GDP","Happiness","Generosity"]

df=pd.read_csv("assignment/happy.csv")


sg.title("In Search for Happiness")
x_Axis_selected_option=sg.selectbox(label="Select the data for x axis",options=option)

match x_Axis_selected_option:
    case "GDP":
        x_Array=df["gdp"]
    case "Happiness":
        x_Array = df["happiness"]
    case "Generosity":
        x_Array = df["generosity"]


y_Axis_selected_option=sg.selectbox(label="Select the data for y axis",options=option)

match y_Axis_selected_option:
    case "GDP":
        y_Array=df["gdp"]
    case "Happiness":
        y_Array = df["happiness"]
    case "Generosity":
        y_Array = df["generosity"]

sg.subheader(f"{x_Axis_selected_option} and {y_Axis_selected_option}")



figure= px.scatter(x=x_Array,y=y_Array,labels={"x":x_Axis_selected_option,"y":y_Axis_selected_option})
sg.plotly_chart(figure)


