import nltk
from nltk.chat.util import Chat, reflections
import random

# Define a set of pairs (patterns and responses)
pairs = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hey there! How are you doing?']),
    (r'what is your name?', ['I am a chatbot, but you can call me whatever you like!']),
    (r'how are you?', ['I’m doing great! How about you?', 'I’m functioning at full capacity, thanks for asking!']),
    (r'(.) your (.)', ['I am just a bot, so I don’t have personal experiences, but I am here to help!']),
    (r'bye', ['Goodbye! It was nice chatting with you.', 'Take care! See you soon!']),
    (r'what can you do?', ['I can help with information, answer your questions, or just chat with you! What do you need help with today?']),
    (r'how old are you?', ['I don’t have an age, but I’m always learning and improving!']),
    (r'what is your favorite color?', ['I don’t have a favorite, but I think all colors are beautiful!']),
    (r'where are you from?', ['I don’t have a physical location, I exist in the digital world, always ready to chat with you!']),
    (r'what is your purpose?', ['My purpose is to chat and assist you with anything you need. What would you like to talk about?']),
    (r'(.) weather (.)', ['I can’t check the weather directly, but you can find it easily online or through an app.']),
    (r'(.) help (.)', ['I am here to help! What can I do for you today?']),
    (r'can you tell me a joke?', ['Sure! Why don’t skeletons fight each other? They don’t have the guts!']),
    (r'(.*) (sad|upset|down)', ['I’m sorry to hear that. Want to talk about it?', 'I’m here for you! What’s on your mind?']),
    (r'(.) love (.)', ['Love is a beautiful thing, don’t you think?', 'Love makes the world go round! What’s your take on it?']),
    (r'(.*) (good|great|awesome)', ['That’s awesome to hear! What’s been going well for you?', 'Nice! Keep it up, it sounds like things are going well.']),
    (r'(.*)', ['Hmm, I’m not sure how to respond to that, but I’m here to listen if you want to talk more!']),
]

# Create a chatbot with the defined patterns and responses
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    if response:
        print("Chatbot:", response)
    else:
        print("Chatbot: I didn't quite understand that, but I’m always here to chat!")
    
    if user_input.lower() == "bye":
        break
