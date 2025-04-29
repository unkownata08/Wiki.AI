import wikipedia


wikipedia.set_lang("en")

def get_wikipedia_answer(query):
    try:
       
        summary = wikipedia.summary(query, sentences=2)  
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Here are some options: {e.options}"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "The request timed out. Please try again."
    except wikipedia.exceptions.RedirectError:
        return "The query resulted in a redirect. Try a different query."
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chatbot():
    print("Hello! I am your Wikipedia-based chatbot, created by ATA-UR-REHMAN. Ask me anything, and I'll search Wikipedia for an answer!")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "exit" or user_input == "bye":
            print("Goodbye! Have a great day!")
            break
        else:
            
            answer = get_wikipedia_answer(user_input)
            print(f"Bot: {answer}")


chatbot()
