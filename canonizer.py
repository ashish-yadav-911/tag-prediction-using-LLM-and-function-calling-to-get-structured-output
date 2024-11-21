from openai import OpenAI
import os,json
from dotenv import load_dotenv
from prompt import prompt_canoninzer

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# function schema
function_schema = {
    "name": "topic_tag",
    "description": "Predicts a tag for the given topic based on the description.",
    "parameters": {
        "type": "object",
        "properties": {
            "topic": {
                "type": "string",
                "description": "The name of the topic being discussed."
            },
            "tag": {
                "type": "string",
                "description": "The tag predicted by the LLM for the given topic."
            }
        },
        "required": ["topic", "tag"]
    }
}

def get_response(input_json):
    #system prompt
    prompt = prompt_canoninzer
    
    # function calling
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": str(input_json)}
        ],
        functions=[function_schema],
        function_call={"name": "topic_tag"}  # functon initialization
    )

    try:
        function_call = response.choices[0].message.function_call
        result = function_call.arguments
        # collecting response data from llm
        data = json.loads(result)
        return data
    except (KeyError, AttributeError, IndexError) as e:
        print(f"Error accessing response: {e}")
        return None


input_data = [
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

if __name__ == "__main__":
    for i in input_data:
        response=get_response(i)
        print(response)
