import json

def serializerDB(jsonify_resp):
    """
    Takes the jsonify results and dumps to json
    """
    items = []
    if len(jsonify_resp.response) > 1:
        for item in jsonify_resp.response:
            result = json.loads(item)
            items.append(result)
    else:
        items = json.loads(jsonify_resp.response[0])
    return json.dumps(items)