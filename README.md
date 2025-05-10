# News Aggregator

## Overview
The News Aggregator is a Python-based desktop application that consolidates current news from various sources, providing a user-friendly interface to browse news by category. It fetches news data via the NewsAPI, enriches it through web scraping to gather additional details, and uses data visualization techniques to offer insights into the news distribution.

## Features
- **Dynamic News Fetching**: Fetch news dynamically by category using the NewsAPI.
- **Data Enrichment**: Enhance news data through web scraping techniques.
- **Data Visualization**: Visualize news statistics to identify trends and distributions.
- **Interactive GUI**: User-friendly interface built with Tkinter, facilitating easy navigation and interaction.
- **Category Filtering**: Filter news based on categories like Business, Technology, Sports, and more.

## Prerequisites
Before you begin, ensure you have the following:
- Python 3.8 or newer.
- API key from [NewsAPI](https://newsapi.org/).

## Installation
To install News Aggregator, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/77puriram/news-aggregator
   ```
2. Navigate to the project directory:
   ```sh
   cd news-aggregator
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

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
- **news_api.py**: Handles fetching news from the NewsAPI.
- **web_scraper.py**: Scrapes additional data from news articles.
- **data_processor.py**: Processes and cleans the fetched and scraped data.
- **data_visualization.py**: Generates visualizations of the news data.
- **gui.py**: Manages the graphical user interface.


## License
This project is licensed under ....................

## Acknowledgments
- NewsAPI for providing the news data.
- Python Software Foundation for the comprehensive software stack.


### Explanation
This README file includes detailed instructions and descriptions, structured to make it easy for users and developers to understand and work with the project:
- **Features**: Outlines the capabilities of the application.
- **Prerequisites and Installation**: Guides on how to get started with the necessary tools and dependencies.
- **Setup**: Instructions for setting up the environment needed to run the app, including API keys.
- **Usage**: How to run the application and interact with its features.
- **Testing**: How to run the tests to ensure the application functions as expected.
- **Modules**: Descriptions of the different Python scripts and their roles.
- **License and Acknowledgments**: Legal information and credits.