# News Aggregator

## Overview
This is a Python desktop application that helps users fetch and view news articles based on selected categories. It uses NewsAPI to get the news headlines and adds extra information like author and publish date through web scraping. The application also includes visualizations to show news trends and patterns. A GUI is included to make it easy for users to interact with the app.


## Features
- Fetch news articles by category using NewsAPI
- Use web scraping to get additional article details
- Clean and combine the data using processing logic
- Display various visualizations like source distribution, sentiment analysis, and trending keywords
- Easy-to-use GUI built with Tkinter
- Second GUI interface shows news with images
- Unit testing is included for each module

## Prerequisites
Before you begin, ensure you have the following:
- Python 3.8 or above
- NewsAPI key (you can get it from https://newsapi.org)

## Installation
To install News Aggregator, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/dharmavathiuts/Information-Aggregator-with-Web-API-and-Scraping
   ```
2. Navigate to the project directory:
   ```sh
   cd Information-Aggregator-with-Web-API-and-Scraping   
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Download NLTK data:
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')

## Setup
Create a `config/config.json` file and add your API key:
```json
{
  "news_api_key": "your_api_key_here"
}
```

## Usage
Run the application:
```sh
python main.py
```
To run image based GUI
```
python url_IMG.py
```
The GUI will launch, allowing you to select news categories and view articles.


## Testing
To run tests and ensure the application functions as expected, follow these steps:

Navigate to the project's root directory.
Run the test suite using the following command:
```sh
python -m unittest discover -s tests
```
This will execute all tests located in the tests directory, verifying each component's functionality.

## Modules
- news_api.py – fetches data from NewsAPI
- web_scraper.py – scrapes article details
- data_processor.py – combines and cleans data
- data_visualization.py – creates charts and plots
- gui_app.py – main GUI interface
- url_IMG.py – image-based news GUI
- tests/ – all test scripts
- main.py – entry point to launch the application

## License
This project is for educational purposes only.



### Explanation
This README file includes detailed instructions and descriptions, structured to make it easy for users and developers to understand and work with the project:
- Features: Outlines the capabilities of the application.
- Prerequisites and Installation: Guides on how to get started with the necessary tools and dependencies.
- Setup: Instructions for setting up the environment needed to run the app, including API keys.
- Usage: How to run the application and interact with its features.
- Testing: How to run the tests to ensure the application functions as expected.
- Modules: Descriptions of the different Python scripts and their roles.
