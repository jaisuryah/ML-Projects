import torch
from transformers import MarianMTModel, MarianTokenizer

# Load pre-trained model and tokenizer
model_name = 'Helsinki-NLP/opus-mt-en-hi'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Function for translation
def translate(text, model, tokenizer):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    # Translate text
    outputs = model.generate(**inputs, max_length=128, num_beams=4, early_stopping=True)
    # Decode translated text
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

# Take user input for English text
english_text = input("Enter the English text you want to translate to Hindi: ")

# Translate to Hindi
hindi_translation = translate(english_text, model, tokenizer)

# Print translated text
print("English:", english_text)
print("Hindi:", hindi_translation)
