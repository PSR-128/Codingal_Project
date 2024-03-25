from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('aqi.html')

@app.route('/get_aqi')
def get_aqi():
    city = request.args.get('city')  # Changed 'requests' to 'request'
    response = requests.get(f'https://api.waqi.info/feed/{city}/?token=a5ce4f19eae698a8cd0088d064a2876a218d614c')
    data = response.json()
    if 'data' in data and 'aqi' in data['data']:
        aqi = data['data']['aqi']
        return jsonify({'aqi': aqi})
    else:
        return jsonify({'error': 'AQI data not available for the specified city'})

@app.route('/home.html')
def home_page():
    return render_template('home.html')  # Rendering home.html

@app.route('/quiz.html')
def quiz_page():
    return render_template('quiz.html')  # Renders quiz.html

@app.route('/aqi.html')
def aqi_page():
    return render_template('aqi.html')  # Renders quiz.html

@app.route('/clean_energy.html')
def clean_energy_page():
    return render_template('clean_energy.html')  # Renders quiz.html

if __name__ == '__main__':
    app.run(debug=True)
