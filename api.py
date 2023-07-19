import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"
API_KEY = "b6907d289e10d714a6e88b30761fae22"
LOCATION = "London,us"

def get_weather_data(date):
    response = requests.get(API_URL, params={"q": LOCATION, "appid": API_KEY})
    if response.status_code == 200:
        weather_data = response.json()
        for forecast in weather_data["list"]:
            if forecast["dt_txt"].startswith(date):
                return forecast["main"]["temp"]
        return None
    else:
        print("Failed to fetch weather data.")
        return None

def get_wind_speed(date):
    response = requests.get(API_URL, params={"q": LOCATION, "appid": API_KEY})
    if response.status_code == 200:
        weather_data = response.json()
        for forecast in weather_data["list"]:
            if forecast["dt_txt"].startswith(date):
                return forecast["wind"]["speed"]
        return None
    else:
        print("Failed to fetch wind speed data.")
        return None

def get_pressure(date):
    response = requests.get(API_URL, params={"q": LOCATION, "appid": API_KEY})
    if response.status_code == 200:
        weather_data = response.json()
        for forecast in weather_data["list"]:
            if forecast["dt_txt"].startswith(date):
                return forecast["main"]["pressure"]
        return None
    else:
        print("Failed to fetch pressure data.")
        return None

def main():
    while True:
        print("Menu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice (0/1/2/3): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_data(date)
            if temperature is not None:
                print(f"The temperature on {date} is {temperature} Kelvin.")
            else:
                print("Data not available for the given date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"The wind speed on {date} is {wind_speed} m/s.")
            else:
                print("Data not available for the given date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"The pressure on {date} is {pressure} hPa.")
            else:
                print("Data not available for the given date.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
