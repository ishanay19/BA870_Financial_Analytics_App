# BA870_Financial_Analytics_App

##### 🎯 Goal
Build a Streamlit-based web app that:
Collects real-time and historical social media data and stock prices.
Analyzes sentiment of social media posts using NLP.
Correlates sentiment with stock price movements.
Displays results in interactive visual dashboards.

##### Initial repo structure:
sentiment-stock-app/
│
├── data/                   # Store raw data (optional, avoid large files)
├── models/                 # Any saved models (e.g., finetuned sentiment model)
├── utils/                  # Helper scripts (e.g., sentiment.py, fetch_data.py)
├── app/                    # Streamlit app components
│   ├── dashboard.py        # Main Streamlit UI
│   ├── sentiment_engine.py # Sentiment analysis functions
│   └── stock_data.py       # Stock price fetching functions
├── requirements.txt        # Python dependencies
├── .env                    # API keys and secrets
├── config.yaml             # Config file for easy param tweaks
└── README.md               # Project overview

- WHAT FINANCIAL ANALYTICS PROBLEM DO YOU PLAN TO SOLVE?
We will create a real-time financial web app that analyzes sentiment from social media posts (Twitter, Reddit, StockTwits) and correlates it with stock price movements. The goal is to determine the extent to which social media sentiment influences stock prices and provide real-time insights and forecasts for investors.

- WHAT (HISTORICAL) DATA DO YOU PLAN TO USE TO TRAIN YOUR MODEL(S)?
We plan to use historical stock price data from Yahoo Finance, Alpha Vantage, or Quandl along with past social media posts from Twitter, Reddit, and StockTwits. We will label and analyze historical sentiment trends using NLP models (FinBERT, VADER) and correlate them with stock price fluctuations.

- WHAT "REAL TIME" DATA DO YOU PLAN TO USE FOR YOUR TESTING/FORECASTS/RECOMMENDATIONS?
We will use:
Yahoo Finance API for real-time stock price updates.
Twitter API, Reddit API, StockTwits API to fetch and analyze social media posts about selected stocks.
Web scraping (if necessary) to collect additional sentiment data.
Our app will update in real-time to provide dynamic sentiment scores and their correlation with stock price changes.

- WHAT TYPE(S) OF MACHINE LEARNING MODELS DO YOU PLAN TO USE?
NLP-based Sentiment Analysis Models (FinBERT, VADER) for analyzing social media sentiment.
Time Series Analysis using Rolling Correlation, Pearson Correlation, and Granger Causality to measure sentiment impact on stock prices.
Regression Models (Linear Regression, Logistic Regression) for predicting stock price changes based on sentiment trends.
Random Forest/XGBoost for feature importance analysis and classification of sentiment impact on price movements.

- WHAT TYPE VISUAL OUTPUT DO YOU PLAN TO USE FOR YOUR DASHBOARD?
Our dashboard will include:
Line Charts showing real-time stock price and sentiment trends.
Scatter Plots visualizing correlation between sentiment score and stock price movement.
Sentiment Score Gauges to display live sentiment strength.
Heatmaps for sector-wise sentiment analysis.
Interactive Sliders to allow users to adjust parameters (time window, stock selection).
Live News & Social Media Feed showing analyzed posts contributing to sentiment scores.
