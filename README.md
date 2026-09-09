# Keyword-Based Sentiment Classifier Chatbot

## Overview
A simple chatbot built with Streamlit that classifies user messages into 
emotional categories (happy, sad, anxious, angry, neutral, or crisis-related 
language) using keyword matching, and responds with a corresponding canned 
reply. Built as a learning project to explore chatbot UI design and 
rule-based text classification logic.

## Demo

### Neutral / happy conversation
![Happy conversation]
![image alt](https://github.com/Himanshidhiman/EmoBot-Streamlit-Emotion-Classifier/blob/d545dc0dd836a604e718897c0fa1961ce165f62c/Screenshot%202026-09-09%20102457.png)

### Crisis-keyword detection
![image alt](https://github.com/Himanshidhiman/EmoBot-Streamlit-Emotion-Classifier/blob/232096601008b2e7adfee433b666906ea54f5502/Screenshot%202026-09-09%20102651.png)


### Initial chat screen
![image alt](image_url)


## How It Works
The app scans user input for predefined keywords associated with each 
emotion category. If a match is found, it returns a randomly selected reply 
from that category. If the input contains crisis-related language (e.g., 
phrases about self-harm), the app displays a prominent message directing 
the user to call 988 (the US Suicide & Crisis Lifeline).

**Note:** This is a rule-based keyword classifier, not a machine learning 
or NLP-based model. It does not use sentiment analysis, language models, or 
any trained classifier — detection is limited to exact keyword/phrase 
matches defined in the code. It is a technical demo of chatbot UI and 
classification logic, not a validated or clinically-informed support tool.

## Features
- Real-time chat interface built with Streamlit's chat components
- Keyword-based emotion classification across 5 categories
- Crisis-keyword detection with a static safety message (does not replace 
  professional support)
- Chat history within a session, with a "Clear Chat" option

## Tech Stack
- Python
- Streamlit

## Getting Started

### Prerequisites
- Python 3.x

### Installation
```bash
git clone https://github.com/Himanshidhiman/keyword-sentiment-chatbot.git
cd keyword-sentiment-chatbot
pip install -r requirements.txt
```

### Run
```bash
streamlit run app.py
```

## Limitations
- Keyword matching only — no semantic understanding, so it can easily miss 
  or misclassify messages that don't contain the exact listed words
- Crisis detection is based on a small, static phrase list and should not 
  be relied upon as a safety mechanism
- Built for learning/demonstration purposes only

## Author
**Himanshi**  
[LinkedIn](https://linkedin.com/in/himanshi001) | [GitHub](https://github.com/Himanshidhiman)
