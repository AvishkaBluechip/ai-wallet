from flask import Flask
app = Flask(__name__)

from src.config import Config
from src.coinbase_client import CoinbaseClient  # Assuming you have this class to interact with Coinbase API
from src.nlp_model import NLPModel
from src.responses import generate_response
import json

def main():
    # Load intents once when the server starts
    def load_intents():
        with open(Config.INTENTS_FILE) as file:
            return json.load(file)

    intents = load_intents()
    model = NLPModel()
    model.load_model("models/chatbot_model.keras", "models/tokenizer.json")  # Pass model and tokenizer paths
    coinbase_client = CoinbaseClient()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting chat...")
            break

        intent, probability = model.predict_intent(user_input)
        if intent == 'connect_wallet':
            response = "Connecting to your wallet..."
            # Implement wallet connection logic here
            # e.g., connect_wallet_function()
        elif intent == 'check_balance':
            balance = coinbase_client.get_account_balance()
            response = f"Your balance is {balance} BTC."
        elif intent == 'predict_transactions':
            response = "Predicting your transactions..."
            # Implement transaction prediction logic here
            # e.g., predict_transactions_function()
        else:
            response = generate_response(intent, intents)

        print(f"Bot: {response}")

if __name__ == '__main__':
    main()
