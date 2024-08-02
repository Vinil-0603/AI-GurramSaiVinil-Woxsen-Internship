# Aluminum Industry News Chatbot

This is an AI-powered chatbot that provides information and answers questions about the aluminum industry based on recent news articles.

## Features

- **Web Scraping:** Scrapes the latest news articles related to the aluminum industry from a specified source.
- **Embeddings:** Uses OpenAI's embedding model to create vector representations of the news articles.
- **Chatbot:** Utilizes OpenAI's GPT-4 model to answer questions based on the embedded news articles.
- **Streamlit Interface:** Provides a user-friendly interface built with Streamlit.

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/Vinil-0603/AI-GurramSaiVinil-Woxsen-Internship.git)  
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key:**
   - Create an account on OpenAI (if you haven't already).
   - Obtain your API key from the OpenAI dashboard.
   - Create a `.env` file in the project directory and add the following line:
     ```bash
     OPENAI_API_KEY=your_api_key
     ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run main.py
   ```

2. **Ask questions in the chatbot interface:**
   - Type your question in the input box on the left side of the interface.
   - The chatbot will provide a response based on the latest news articles.
