from gui_app import NewsAggregatorGUI
import json

if __name__ == "__main__":
    # Load API key from config file
    with open('config/config.json') as config_file:
        config = json.load(config_file)
    
    api_key = config['news_api_key']

    app = NewsAggregatorGUI(api_key)
    app.mainloop()