# AI_Chatbot

🤖 AI-Powered Chatbot
A simple AI-powered chatbot built using Flask and NLP techniques. Supports predefined intents and logs all user interactions to a SQLite database.

🚀 Features
Context-aware responses using custom intent-matching
Simple Flask web interface
User interaction logs stored in SQLite
Easily extendable with NLP libraries (e.g., Hugging Face Transformers)
🛠️ Tech Stack
Python
Flask
SQLite
Basic NLP (intent matching using JSON)
📁 Project Structure
ai_chatbot/
├── app.py
├── chatbot/
│   ├── model.py
│   └── intents.json
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── chatbot.db
├── requirements.txt
└── README.md
⚙️ Installation
git clone https://github.com/YOUR_USERNAME/ai-chatbot.git
cd ai-chatbot
pip install -r requirements.txt
python app.py
Then open http://127.0.0.1:5000 in your browser.

🧠 Customize
Edit chatbot/intents.json to add new intents and responses.

📦 Deployment on Render
Create a new Web Service on Render
Connect your GitHub repo
Set the build and start command:
Build Command: pip install -r requirements.txt
Start Command: python app.py
Add web: gunicorn app:app in a Procfile for production
📝 License
MIT License
