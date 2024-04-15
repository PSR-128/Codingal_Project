from flask import Flask, request, jsonify, render_template, Response, send_file
import requests
import ozon3 as ooo
import plotly.graph_objects as go
import pandas as pd

app = Flask(__name__)

# API Keys and configuration
WAQI_TOKEN = 'a5ce4f19eae698a8cd0088d064a2876a218d614c'
NEWS_API_KEY = 'XlmQZDkCfwzWUhtKQmIJazy2C8dwh5y4 '
o3 = ooo.Ozon3(WAQI_TOKEN)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/get_aqi')
def get_aqi():
    city = request.args.get('city')
    response = requests.get(f'https://api.waqi.info/feed/{city}/?token={WAQI_TOKEN}')
    if response.ok:
        data = response.json()
        if 'data' in data and 'aqi' in data['data']:
            return jsonify({
                'aqi': data['data']['aqi'],
                'air_quality_data': {k: data['data']['iaqi'].get(k, {}).get('v', 'N/A') for k in
                                     ['dew', 'h', 'p', 't', 'w', 'wg', 'pm25', 'pm10', 'co', 'o3', 'no2', 'so2']}
            })
    return jsonify({'error': 'AQI data not available for the specified city'})


def plot_historical_aqi(city):
    data = o3.get_historical_data(city=city)
    if isinstance(data, pd.DataFrame):
        data = data.dropna(subset=['date'])
        dates = data['date']
        fig = go.Figure()

        for pollutant in ['pm2.5', 'pm10', 'o3', 'co', 'no2', 'so2']:
            if pollutant in data.columns:
                fig.add_trace(go.Scatter(x=dates, y=data[pollutant], mode='lines+markers', name=pollutant.upper()))

        fig.update_layout(
            title=f'Historical Air Quality Data for {city} (2014 - Present)',
            xaxis_title='Date',
            yaxis_title='Concentration',
            legend_title='Pollutants'
        )

        # Return plot as JSON for web integration
        return fig.to_json()
    else:
        return jsonify({'error': 'Data is not in the expected format'}), 400

# Use this in a Flask route
@app.route('/get_historical_aqi_plot')
def get_historical_aqi_plot():
    city = request.args.get('city')
    plot_json = plot_historical_aqi(city)
    if isinstance(plot_json, str):
        return Response(plot_json, mimetype='application/json')
    else:
        return plot_json



@app.route('/get_good_aqi_cities')
def get_good_aqi_cities_route():
    good_cities = [city for city in [
        "Tokyo", "Delhi", "Shanghai", ...  # Add your full list of cities here
    ] if requests.get(f'https://api.waqi.info/feed/{city}/?token={WAQI_TOKEN}').ok and requests.get(f'https://api.waqi.info/feed/{city}/?token={WAQI_TOKEN}').json()['data']['aqi'] <= 100]
    return jsonify(good_cities)

@app.route('/news_content')
def news_content():
    response = requests.get(f'https://newsapi.org/v2/everything?q=renewable+energy&apiKey={NEWS_API_KEY}&pageSize=12')
    articles = [{'title': article['title'], 'content': article['content']} for article in response.json().get('articles', [])] if response.ok else []
    return render_template('news.html', articles=articles)

# Additional routes for other pages
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

if __name__ == '__main__':
    app.run(debug=True)
