from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/get_aqi')
def get_aqi():
    city = request.args.get('city')
    response = requests.get(f'https://api.waqi.info/feed/{city}/?token=a5ce4f19eae698a8cd0088d064a2876a218d614c')
    data = response.json()
    if 'data' in data and 'aqi' in data['data']:
        aqi = data['data']['aqi']
        return jsonify({'aqi': aqi})
    else:
        return jsonify({'error': 'AQI data not available for the specified city'})


@app.route('/news_content')
def news_content():
    # Make a request to the News API endpoint
    response = requests.get('https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key=94b4958687e44ec381ee8088a34bf7d3')
    if response.ok:
        # Extract news content from the response
        news_content = response.text
        return render_template('news.html', news_content=news_content)
    else:
        return 'Failed to fetch news content'

# Routes for other pages
@app.route('/home.html')
def home_page():
    return render_template('home.html')

@app.route('/quiz.html')
def quiz_page():
    return render_template('quiz.html')

@app.route('/aqi.html')
def aqi_page():
    return render_template('aqi.html')

@app.route('/clean_energy.html')
def clean_energy_page():
    return render_template('clean_energy.html')

@app.route('/news.html')
def news_page():
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug=True)
