import google.genai as genai
genai.configure(api_key="API KEY HERE")
model = genai.GenerativeModel("gemini-2.5-flash")

print(" AI Chatbot Ready! Ask anything.\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "end":
        print("Chatbot: Finished")
        break
    
    try:
        response = model.generate_content(user_input)
        print("Chatbot:", response.text)
    except Exception as e:
        print("Error:", e)