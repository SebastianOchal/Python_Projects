weather_data = {
    "London":{"Temperature":"14°C", "Conditions":"Heavy Rain","Wind_Speed":"16km/h"},
    "Paris":{"Temperature":"7°C", "Conditions":"Rain","Wind_Speed":"16km/h"},
    "Berlin":{"Temperature":"5°C", "Conditions":"Partly Sunny","Wind_Speed":"11km/h"},
    "Dublin":{"Temperature":"10°C", "Conditions":"Cloudy","Wind_Speed":"17km/h"},
    "Madrid":{"Temperature":"9°C", "Conditions":"Sunny","Wind_Speed":"3km/h"}
}

def Display_weather():
    print(50*"=")
    print("Here are the avalible cities, Type their name to get the weather data")
    for data in weather_data:
        print(data)
    print(50*"=")
    user_request = input("What City would you like the weather for?:")
    location = user_request.lower()

    for  city in weather_data:
        if location == city.lower():
            print(f"City: {city}")

Display_weather()