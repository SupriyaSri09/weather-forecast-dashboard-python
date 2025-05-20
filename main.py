import streamlit as sg
import plotly.express as px
from backend import get_data

sg.title("Weather forecast for Next Days")
place = sg.text_input("Place")
forcast_days=sg.slider("Forecast Days",min_value=1,max_value=5,
                       help="Please select the number of days to be forecasted")
option=sg.selectbox("Select data to view",options=["Temperature","Sky"])
sg.subheader(f"{option} for next {forcast_days} days in {place}")



if place:
    #call th function
    data = get_data(place,forcast_days)
# filter data based on option
    if option == "Temperature":
        temperatures = [item["main"]["temp"] for item in data]
        dates = [item["dt_txt"] for item in data]
        print("************Temo**********")
        print(temperatures)
        print("************Dates**********")
        print(dates)

        figure = px.line(x=dates, y=temperatures, labels={"x": "date", "y": "temperature"})
        sg.plotly_chart(figure)

    elif option == "Sky":
        weather_data = [item["weather"][0]["main"] for item in data]
        print("************Weather Data**********")
        print(weather_data)
        image_dict = {"Clear" : "images/clear.png","Clouds" : "images/cloud.png","Rain" : "images/rain.png","snow" : "images/snow.png"}
        image_path = [image_dict[mood] for mood in weather_data]
        print("************Image path**********")
        print(image_path)
        sg.image(image_path,width=115)




