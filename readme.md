## Run Application:

# Using Makefile Method
1. Put environment variables according to .env.examples
2. bash make install
3. bash make run

# Manual Method
1. Put environment variables according to .env
2. run python3 install -r requirements.txt 
3. run python3 api.py

## API Documentation

# Method and Endpoints
* Method: POST
* Endpoints: https://host:port_number/topic_tagging, 
--> "apply /topic_tagging to api URL to access correct endpoint"

# Input Data formatting
* Content-Type - JSON
* Format and Schema: data=[{"topic_tittle":"Content"},{"":""}]
For example:
--> input_data = [
    {
        "Modi": "Is Modi a dictator of democracy? Opposition believes him to be a dictator."
    },
    {
        "Artificial intelligence": "AI is ruling the world right now, and will probably rule the future."
    },
    {
        "Delhi pollution": "Delhi pollution is at an all-time high at 521 AQI. AQI stands for Air Quality Index."
    }
    ]

# Repsonse Format
* Format: {'topic': 'topic_name', 'tag': 'tag_name'}
--> For Example:
> {'topic': 'Modi', 'tag': 'Politics'}
> {'topic': 'Artificial intelligence', 'tag': 'Current Event'}
> {'topic': 'Delhi pollution', 'tag': 'Current Event'}