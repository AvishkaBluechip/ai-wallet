def generate_response(intent, intents):
    # Check if 'intents' is a dictionary and has the 'intents' key
    if not isinstance(intents, dict) or 'intents' not in intents:
        return "Sorry, I don't understand that."
    
    for i in intents['intents']:
        if i.get('tag') == intent:
            # Check if 'responses' is a list and has at least one response
            if isinstance(i.get('responses'), list) and len(i['responses']) > 0:
                return i['responses'][0]
            else:
                return "Sorry, I don't have a response for that."
    
    return "Sorry, I don't understand that."
