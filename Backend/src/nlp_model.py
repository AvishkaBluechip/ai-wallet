from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import json

class NLPModel:
    def __init__(self):
        self.model = None
        self.tokenizer = None

    def load_model(self, model_path, tokenizer_path):
        self.model = load_model(model_path)
        
        # Load the tokenizer configuration
        with open(tokenizer_path, 'r') as file:
            tokenizer_data = json.load(file)
        
        # Debugging print statement
        print("Loaded tokenizer data:", tokenizer_data)
        
        # Recreate the tokenizer
        self.tokenizer = Tokenizer()
        
        # Extract and parse tokenizer configuration
        tokenizer_config = tokenizer_data.get('config', {})
        word_index_str = tokenizer_config.get('word_index', '{}')
        word_index = json.loads(word_index_str)  # Convert JSON string to dictionary
        
        self.tokenizer.word_index = word_index

    def predict_intent(self, text):
        sequence = self.tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, padding='post', maxlen=20)
        predictions = self.model.predict(padded_sequence)
        intent = predictions.argmax()
        probability = predictions[0][intent]
        return intent, probability

    def _get_intents_list(self):
        """Helper method to get the list of intents."""
        # This should match the order in which intents were used during training
        # Adjust this method according to how you store/retrieve your intent labels
        return ["greeting", "goodbye", "connect_wallet", "check_balance", "predict_transactions"]