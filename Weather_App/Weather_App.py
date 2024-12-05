weather_data = {
    "London":{"Temperature":"14°C", "Conditions":"Heavy Rain","Wind_Speed":"16km/h"},
    "Paris":{"Temperature":"7°C", "Conditions":"Rain","Wind_Speed":"16km/h"},
    "Berlin":{"Temperature":"5°C", "Conditions":"Partly Sunny","Wind_Speed":"11km/h"},
    "Dublin":{"Temperature":"10°C", "Conditions":"Cloudy","Wind_Speed":"17km/h"},
    "Madrid":{"Temperature":"9°C", "Conditions":"Sunny","Wind_Speed":"3km/h"}
    }
    
def menu():
    print(50*"=")
    print("Here are the avalible cities, Type their name to get the weather data")
    for data in weather_data:
        print(data)
    print(50*"=")
    display_weather()

def display_weather():
    user_request = input("What City would you like the weather for?:")
    location = user_request.lower()
    city_found = False
    for city in weather_data:
        if location == city.lower():
            print(50*"=")
            print(f"City: {city}")
            print(50*"=")
            print(f"Temperature: |{weather_data[city]["Temperature"]}|")
            print(f"Conditions:  |{weather_data[city]["Conditions"]}|")
            print(f"Wind Speed:  |{weather_data[city]["Wind_Speed"]}|")
            print(50*"=")
            leave()
            city_found = True
    if city_found == False:
        print("this city does not exist")
        menu()
        
def leave(Exit_message = "Would you like to Exit? Yes or No: "):
    check_again = input(Exit_message)
    answer = check_again.lower()
    if answer == "yes":
        print("ok bye")
    elif answer == "no":
        menu()
    else:
        print("That was not an option please try again")
        leave()
    
menu()