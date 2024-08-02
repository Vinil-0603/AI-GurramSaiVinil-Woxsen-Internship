import streamlit as st
from scraper import scrape_news
from embeddings import create_embeddings
from chatbot import chat

# Set wide mode by default
st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    articles = scrape_news()
    return create_embeddings(articles)

st.title("Aluminum Industry News Chatbot")

# Create two columns
left_column, right_column = st.columns(2)

# Left column: Chatbot interface
with left_column:
    st.markdown("<h1 style='text-align: center;'>Ask Your Question</h1>", unsafe_allow_html=True)  # Larger, centered title
    st.markdown("<p style='text-align: center;'>Explore the latest aluminum industry news with our AI-powered chatbot.</p>", unsafe_allow_html=True)  # Descriptive text
    user_input = st.text_input("Enter your question here:")

    if user_input:
        embeddings = load_data()
        response = chat(user_input, embeddings)

        # Display chatbot response in a box
        st.markdown(
            f"""
            <div style='border: 1px solid #ccc; padding: 10px; border-radius: 5px;'>
                Chatbot Response: {response}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Right column: Latest News Articles
with right_column:
    st.header("Latest News Articles")
    articles = scrape_news()
    for article in articles[:5]:
        st.markdown(f"## **{article['title']}**")  # Use Markdown for larger title
        st.write(f"**Summary:** {article['description']}")
        st.write(f"**Date:** {article['date']}")
        st.write(f"[Read More]({article['url']})")
        st.write("---")