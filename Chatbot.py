import random
import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime
import pytz

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you', ['I am fine, thank you!', 'I am doing well, thanks!']),
    (r'what is your name', ['My name is ConvoBot.', 'I am a ConvoBot.', 'I go by ConvoBot.']),
    (r'what can you do', ['I can chat with you!', 'I can answer your questions.', 'I can provide information.']),
    (r'(.*) age (.*)', ['I do not have an age.', 'Age is just a number for me.']),
    (r'(.*) (location|located) (.*)', ['I exist in the virtual world.', 'You can find me wherever you are!']),
    (r'(.*) (weather|temperature) (.*)', ['I do not have access to weather information.', 'You can check the weather on your phone or computer.']),
    (r'what is the time', ['The current Indian time is ' + datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%H:%M:%S')]),
    (r'what is the date', ['Today\'s Indian date is ' + datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d')]),
    (r'how old are you', ['I am a computer program, so I do not age.', 'Age is not applicable to me.']),
    (r'who created you', ['I was created by a team of developers.', 'My creators are human programmers.']),
    (r'can you help me', ['Of course! What do you need help with?', 'I will do my best to assist you.']),
    (r'(.*) (love|hate) (.*)', ['Feelings are complex and subjective.', 'Love and hate are human emotions.']),
    (r'(.*)', ['Sorry, I did not understand that.', 'Could you please rephrase that?', 'I am still learning!'])
]

chatbot = Chat(patterns, reflections)

def get_current_indian_datetime():
    current_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%H:%M:%S')
    current_date = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d')
    return current_date, current_time

def chat():

    indian_date, indian_time = get_current_indian_datetime()
    print(f"Welcome! Current Session date is {indian_date} and time is {indian_time}. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':

            indian_date, indian_time = get_current_indian_datetime()
            print(f"Goodbye! Session end time is {indian_date} and time is {indian_time}.")
            break
        else:
            response = chatbot.respond(user_input)
            print("ConvoBot:", response)

if __name__ == "__main__":
    chat()
