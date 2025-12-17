def clean(text):
    return text.lower().strip()


def get_response(user_input, intents):
    for intent in intents.values():   # ✅ fixed
        for keyword in intent["keywords"]:
            if keyword in user_input:
                return intent["response"]

    return "Sorry, I didn't understand that. Please ask something else."
