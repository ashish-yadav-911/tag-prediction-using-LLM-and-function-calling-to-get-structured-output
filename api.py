from canonizer import get_response
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/topic_tagging', methods=['POST'])
def topic_tagger():
    # Get JSON data from the request
    data = request.get_json()
    tag_list=[]

    for i in data[0:3]:
        response=get_response(i)
        tag_list.append(response)
        
    print(json.dumps(tag_list))

    return json.dumps(tag_list)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8003")