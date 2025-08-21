🤖 Streamlit Chatbot (Groq LLaMA-3)

A simple chatbot built with Streamlit and powered by Groq’s LLaMA-3 models (llama3-8b-8192, llama3-70b-8192).

This project was originally designed for OpenAI’s GPT models but has been updated to use Groq API — which is faster and free to start.

🚀 Features

Interactive chatbot UI built with Streamlit

Uses Groq’s LLaMA-3 models for responses

Easy setup with config.json for API key

Lightweight and fast

📦 Installation

Clone this repository:

git clone https://github.com/your-username/groq-streamlit-chatbot.git

cd groq-streamlit-chatbot

Create and activate a virtual environment (recommended):

python -m venv venv

source venv/bin/activate # Mac/Linux

venv\\Scripts\\activate # Windows

Install dependencies:

pip install -r requirements.txt

⚙️ Configuration

Get your Groq API Key from Groq Cloud

.

Create a file src/config.json with the following structure:

{

"GROQ\_API\_KEY": "your\_api\_key\_here"

}

▶️ Run the App

streamlit run src/main.py

🛠 Requirements

requirements.txt:

groq

streamlit==1.34.0

📚 Example

Input:

"Who is Jon Snow in Game of Thrones?"

Output (LLaMA-3 response):

"Jon Snow is a fictional character in the series Game of Thrones, raised as the illegitimate son of Eddard Stark. He later learns of his true heritage and plays a central role in the war against the White Walkers."
