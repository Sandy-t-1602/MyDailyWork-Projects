import requests
import json

OpenWeatherAPIKey = "7ac9d05ea567ac00f0fa3bcc892ef007"
API_URL = "http://api.openweathermap.org/data/2.5/weather?"

def start_program():
    print("************************************")
    print("Weather Forecast  Application")
    print("************************************")
    print("Version : 1.0")
    print("************************************")
    print("Made by Santhosh T")
    print("************************************")
    info_before_search()

def info_before_search(): 
    print("\nIMPORTANT NOTE : This program requires a network connection to collect Weather data from the Weather Servers... So, please make sure to have a stable internet connection throughout the program...!")
    print("")
    input_city()
    
def input_city():
    global CityName
    CityName = input("Enter the name of the city: ")
    collect_data()

def collect_data():
    Full_URL = API_URL + "appid=" + OpenWeatherAPIKey + "&q=" + CityName

    try:
        response = requests.get(Full_URL)
        response.raise_for_status()
        WeatherData = response.json()

        if WeatherData["cod"] != "404":
            Info = WeatherData["main"]
            
            Temp = Info["temp"]
            Temp_Celsius = Temp - 273.15
            
            Pressure = Info["pressure"]

            Humidity = Info["humidity"]

            Details = WeatherData["weather"][0]["description"]

            print("\nTemprature (in Celsius): {:.2f}".format(Temp_Celsius))
            print("\nAtmospheric Pressure (in hPa):", Pressure)
            print("\nHumidity (in percentage):", Humidity)
            print("\nWeather Description:", Details)
            exit_program()

        else:
            print("\nCity Not Found.Please Try Again...!!")
            input_city()

    except requests.exceptions.HTTPError as HttpErr:
        print("\nHTTP Error")
        print("\nINFORMATION :", HttpErr)
        print("\nRestarting the application...")
        start_program()
    except requests.exceptions.ConnectionError as ConErr:
        print("\nConnection Error")
        print("\nINFORMATION :", ConErr)
        print("\nRestarting the application...")
        start_program()
    except requests.exceptions.Timeout as TimeOutErr:
        print("\nConnection Time Out")
        print("\nINFORMATION :", TimeOutErr)
        print("\nRestarting the application...")
        start_program()
    except requests.exceptions.RequestException as ReqErr:
        print("\nError Occured - Request Failed")
        print("\nINFORMATION :", ReqErr)
        print("\nRestarting the application...")
        start_program()

def exit_program():
    print("")
    AskAgain = str(input("Do you want to search another city? (Y/N): "))
    UppercaseAA = AskAgain.upper()
    
    if UppercaseAA == 'Y':
        print("")
        input_city()
    elif UppercaseAA == 'N':
        print("\nApplication is Closed...!")
    else:
        print("\nWRONG INPUT!! PLEASE TRY AGAIN!!")
        exit_program()

start_program()
