weather_data = {
    "London":{"Temperature":"15°C", "Conditions":"Cloudy","Wind_Speed":"5km/h"},
    "Paris":{},
    "Berlin":{},
    "Dublin":{},
    "Madrid":{}
}

def Display_weather():
    
    user_request = input("What City would you like the weather for?:")
    location = user_request.lower()

    for  city in weather_data:
        if location == city.lower():
            print(f"City: {city}")

Display_weather()