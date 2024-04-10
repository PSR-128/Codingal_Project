import requests

def get_air_quality_data(city):
    waqi_token = 'a5ce4f19eae698a8cd0088d064a2876a218d614c'
    response = requests.get(f'https://api.waqi.info/feed/{city}/?token={waqi_token}')
    if response.ok:
        data = response.json()
        if 'data' in data:
            air_quality_data = data['data'].get('iaqi', {})
            # Print the structure of air_quality_data to identify the correct keys
            print(air_quality_data)
        else:
            print('No air quality data available for the specified city.')
    else:
        print('Failed to retrieve air quality data.')

# Replace 'your_city_name' with the desired city
get_air_quality_data('Mumbai')
