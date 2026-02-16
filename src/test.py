import google.generativeai as genai

# Paste your API key here
genai.configure(api_key="PASTE_YOUR_API_KEY_HERE")

print("Connecting to Google AI...")
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Reply with the word SUCCESS")
    print("AI Reply:", response.text)
except Exception as e:
    print("FATAL ERROR:", e)