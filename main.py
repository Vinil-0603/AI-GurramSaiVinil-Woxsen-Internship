import streamlit as st
from scraper import scrape_news
from embeddings import create_embeddings
from chatbot import chat

# Set wide mode by default
st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    articles = scrape_news()  # Scrape all articles (45 days)
    return create_embeddings(articles)  # Create embeddings for all articles

st.title("Aluminum Industry News Chatbot")

# Create two columns
left_column, right_column = st.columns(2)

# Left column: Chatbot interface
with left_column:
    st.markdown("<h1 style='text-align: center;'>Ask Your Question</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Explore the latest aluminum industry news with our AI-powered chatbot.</p>", unsafe_allow_html=True)

    # Increase input box height using CSS
    st.markdown(
        """
        <style>
        textarea[data-testid="stTextArea"] {
            height: 100px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    user_input = st.text_input("Enter your question here:")

    if user_input:
        embeddings = load_data()
        
        # Add a spinner while generating the response
        with st.spinner("Thinking..."):
            response = chat(user_input, embeddings)

        # Display chatbot response in a box
        st.markdown(
            f"""
            <div style='border: 1px solid #ccc; padding: 10px; border-radius: 5px;'>
                **Chatbot:** {response}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Right column: Latest News Articles (display only the latest 5)
with right_column:
    st.header("Latest News Articles")
    latest_articles = scrape_news()[:5]  # Get only the latest 5 articles
    for article in latest_articles:
        st.markdown(f"## **{article['title']}**")
        st.write(f"**Summary:** {article['description']}")
        st.write(f"**Date:** {article['date']}")
        st.write(f"[Read More]({article['url']})")
        st.write("---")
