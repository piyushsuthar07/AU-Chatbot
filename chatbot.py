from intents import intents
from utils import clean, get_response
#import GUI

print("Academy Chatbot is Online")
print("Type 'bye' to exit")

while True:
    user_input = input("You: ")
    user_input = clean(user_input)

    response = get_response(user_input, intents)
    print("Bot:", response)

    if "bye" in user_input:
        break