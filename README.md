# Sustainable Cities — Clean Energy & Air Quality App 🌍

A Flask + HTML web app that helps users check live air quality, learn about clean energy, and test their knowledge with a daily quiz.

## Overview

This project is a small multi-page web app built around sustainability and clean energy, backed by the [World Air Quality Index (WAQI)](https://waqi.info/) API and [NewsAPI](https://newsapi.org/).

### Pages

| Page | File | Description |
|---|---|---|
| Home | `home.html` | Landing page — "Clean Energy" / Sustainable Cities intro |
| Air Quality Checker | `aqi.html` | Look up current & historical AQI for a chosen city |
| Clean Energy | `clean_energy.html` | Bento-grid layout with clean energy content |
| Daily Quiz | `quiz.html` | A daily clean-energy trivia quiz |

### Backend

The Flask backend (`Python backend:-aqi.py`) exposes these routes:

- `GET /get_aqi?city=<city>` — current AQI + pollutant breakdown (PM2.5, PM10, CO, O₃, NO₂, SO₂, etc.) for a city, via the WAQI API
- `GET /get_historical_aqi_plot?city=<city>` — historical AQI trend as a Plotly chart (JSON), via the `ozon3` package
- `GET /get_good_aqi_cities` — filters a candidate city list down to those with AQI ≤ 100
- `GET /news_content` — renewable-energy news via NewsAPI
- Page routes for `home.html`, `quiz.html`, `clean_energy.html`, `aqi.html`

`AQI_documentation.py` is a small standalone script demonstrating a direct call to the WAQI API for a single city (Mumbai).

> **Note:** This project doesn't contain a trained predictive model, so there's no model accuracy to report here — it's a data-lookup/visualization app rather than a machine learning one.

## Getting Started

### Prerequisites

```bash
pip install flask requests ozon3 plotly pandas
```

### Configuration

The backend currently has the WAQI and NewsAPI keys hardcoded in `Python backend:-aqi.py`. Before deploying or sharing this publicly, it's worth moving these into environment variables instead, e.g.:

```python
import os
WAQI_TOKEN = os.environ["WAQI_TOKEN"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]
```

### Run

```bash
python "Python backend:-aqi.py"
```

Then visit `http://127.0.0.1:5000/` in your browser.

## Project Structure

```
Codingal_Project/
├── Python backend:-aqi.py   # Flask app & API routes
├── AQI_documentation.py     # Standalone WAQI API example
├── home.html                # Landing page
├── aqi.html                 # Air quality checker page
├── clean_energy.html        # Clean energy info page
└── quiz.html                 # Daily clean energy quiz
```

## License

No license specified yet — add one (e.g. MIT) if you plan to share or accept contributions to this project.
