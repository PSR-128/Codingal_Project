from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/get_aqi')
def get_aqi():
    city = request.args.get('city')
    waqi_token = 'a5ce4f19eae698a8cd0088d064a2876a218d614c'
    response = requests.get(f'https://api.waqi.info/feed/{city}/?token={waqi_token}')
    if response.ok:
        data = response.json()
        if 'data' in data and 'aqi' in data['data']:
            aqi = data['data']['aqi']
            air_quality_data = {
                'Dew': data['data']['iaqi'].get('dew', {}).get('v'),
                'Humidity': data['data']['iaqi'].get('h', {}).get('v'),
                'Pressure': data['data']['iaqi'].get('p', {}).get('v'),
                'Temperature': data['data']['iaqi'].get('t', {}).get('v'),
                'Wind Speed': data['data']['iaqi'].get('w', {}).get('v'),
                'Wind Gust Speed': data['data']['iaqi'].get('wg', {}).get('v'),
                'PM-2.5': data['data']['iaqi'].get('pm25', {}).get('v'),
                'PM-10': data['data']['iaqi'].get('pm10', {}).get('v'),
                'CO2': data['data']['iaqi'].get('co', {}).get('v'),
                'O3': data['data']['iaqi'].get('o3', {}).get('v'),
                'N2': data['data']['iaqi'].get('no2', {}).get('v'),
                'S2': data['data']['iaqi'].get('so2', {}).get('v')
            }# this is dict for aqi data

            return jsonify({'aqi': aqi, 'air_quality_data': air_quality_data})
    return jsonify({'error': 'AQI data not available for the specified city'})

@app.route('/news_content')
def news_content():
    api_key = 'XlmQZDkCfwzWUhtKQmIJazy2C8dwh5y4 '
    response = requests.get(f'https://newsapi.org/v2/everything?q=renewable+energy&apiKey={api_key}&pageSize=12')
    if response.ok:
        news_data = response.json()
        articles = []
        for article in news_data.get('articles', []):
            articles.append({'title': article['title'], 'content': article['content']})
        return render_template('news.html', articles=articles)
    else:
        return render_template('news.html', articles=[])
        
@app.route('/aqi.html')
def aqi_page():
    city = request.args.get('city')
    response = requests.get(f'http://127.0.0.1:5000/get_aqi?city={city}')
    if response.ok:
        data = response.json()
        if 'aqi' in data:
            aqi = data['aqi']
            air_quality_data = data.get('air_quality_data', {})
            return render_template('aqi.html', aqi=aqi, air_quality_data=air_quality_data)

    return render_template('aqi.html', error='AQI data not available for the specified city')
    
# Routes for other pages
@app.route('/home.html')
def home_page():
    return render_template('home.html')

@app.route('/quiz.html')
def quiz_page():
    return render_template('quiz.html')

@app.route('/clean_energy.html')
def clean_energy_page():
    return render_template('clean_energy.html')

@app.route('/news.html')
def news_page():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
