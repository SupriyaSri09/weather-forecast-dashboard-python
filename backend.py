import requests

API_KEY="262c0bbffdf6bb4f948ee3e315d2ec23"

#sample URL
#https://api.openweathermap.org/data/2.5/forecast?q=London, us&appid=262c0bbffdf6bb4f948ee3e315d2ec23
def get_data(location,days):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={API_KEY}"
    content = requests.get(url)
    data = content.json()
    filtered_data = data["list"]

    #filter data based on days
    number_of_records= 8*days
    filtered_data = filtered_data[:number_of_records]
    print(filtered_data)
    return filtered_data

if __name__ == "__main__":
    get_data("Tokyo",2)
