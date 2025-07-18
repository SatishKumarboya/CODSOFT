import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    if re.search(r"\b(hi|hello|hey)\b", user_input):
        return "Hello! How can I assist you today?"
    elif re.search(r"\bname\b", user_input):
        return "I'm CodSoft Bot, your friendly assistant!"
    elif re.search(r"\binternship\b", user_input):
        return "We offer internships in Web Development, Data Science, and more!"
    elif re.search(r"\bthank(s| you)\b", user_input):
        return "You're welcome! 😊"
    elif re.search(r"\bhelp\b", user_input):
        return "You can ask me about internships, roles, or general queries."
    else:
        return "I'm not sure I understand. Could you please rephrase?"

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("ChatBot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)
