from flask import Flask, request, jsonify
from flask_cors import CORS  # This imports the CORS fix
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # This tells your browser to allow the connection

# Put your AI Studio key here
genai.configure(api_key="AIzaSyAKPYL0Kx1VVQaHSmuV-Gmupka9JJBSW9I")
model = genai.GenerativeModel('gemini-pro')

# A health-check route so you know the server is alive
@app.route('/', methods=['GET'])
def home():
    return "✅ Backend is running and ready for the frontend!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # host='0.0.0.0' is the magic bridge between Ubuntu and Windows
    app.run(host='0.0.0.0', port=5000, debug=True)