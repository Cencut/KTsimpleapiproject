import requests
import matplotlib.pyplot as plt

# OpenWeatherMap API Key (replace with your own)
api_key = 'c9cbbe50f604f7c1656644b278d9075a'

# City to get weather data for
city = 'Astana'

# API endpoint for daily weather data
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract relevant data from the API response
    weather_data = response.json()

    # Check the structure of the response
    print(weather_data)

    # Extract temperature data for each day in the next 8 days
    display_days = 8
    display_temperatures = []

    for forecast in weather_data['list'][:display_days]:  # Extract data for the next 8 days
        temperature = forecast['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        display_temperatures.append(temperature)

    # Plot the line chart
    plt.plot(range(1, display_days + 1), display_temperatures, marker='o')

    # Adding labels and title
    plt.xlabel('Day')
    plt.ylabel('Temperature (\u00b0C)')
    plt.title(f'Daily Temperature Forecast for the Next {display_days} Days in {city}')

    # Display the plot
    plt.show()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text)  # Print the response content for more information
