from flask import Flask, request, jsonify
import nltk
import datetime as datetime
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Define the patterns and responses for the chatbot
pairs = [
    [
        r"what (.*) you (.*)",
        ["I am a chatbot, happy to help you with your questions."]
    ],
    [
        r"hi(.*)",
        ["Hello! How can I help you?"]
    ],
    [
        r"(.*) time (.*)",
        [
            "The current time is " +
            datetime.datetime.now().time().strftime("%H:%M:%S")
        ]
    ],
    [
        r"(.*) date (.*)",
        [
            "The current date is " +
            datetime.datetime.now().strftime("%Y-%m-%d")
        ]
    ],
    [
        r"quit(.*)",
        ["Bye! Have a great day!"]
    ],
    [
        r"what is your name",
        ["My name is Chatbot"]
    ]
]

reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i'm"        : "you are",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you",
    "today"      : "date",
    "now"        : "time",
    "how are you" : "I am Fine"
}

def chatbot():
    # Initialize the chatbot
    print("Hi! I am a chatbot. How can I help you?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()