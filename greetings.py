import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm a chatbot",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, I don't have an age."]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse ;)",]
    ],
    [
        r"(.*) created ?",
        ["I was created by OpenAI's GPT model.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am located in the internet',]
    ],
    [
        r"quit",
        ["Bye for now. Take care!", "Goodbye!"]
    ],
]

# Define a function to start the chat
def chatbot():
    print("Hi, I'm Chatbot. How can I help you today? Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Call the chatbot function to start the conversation
if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
    nltk.download("nps_chat")
    chatbot()
