from random import choice, randint

def get_response(user_input: str) -> str:
    # return NotImplementedError("Code is missing...")
    lowered: str = user_input.lower()

    if lowered == '':
        return "I'm sorry, I didn't catch that. Could you repeat it?"
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'bye' in lowered:
        return 'Goodbye!'
    elif 'roll dice' in lowered:
        return str(randint(1, 100))
    elif 'coin flip' in lowered:
        return choice(['Heads', 'Tails'])
    elif 'how are you' in lowered:
        return 'I am doing well, thank you for asking.'
    elif 'what is your name' in lowered:
        return 'My name is Rain-Bot.'
    elif 'what is your purpose' in lowered:
        return 'I am here to assist you with your needs.'
    else:
        return choice([
            'I am sorry, I do not understand.',
            'What do you mean?',
            'Could you please clarify?',
            'I am not sure what you are asking.',
            'I am not programmed to understand that.',
            'Do you mind repeating that?',
            'Do you mind rephrasing that?',
            'Could you please rephrase that?',
            'Mind repeating that?',
            'May you repeat that?',
            'Would you mind repeating that?',
        ])

    