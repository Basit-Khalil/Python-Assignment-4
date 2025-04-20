import streamlit as st
import random

# Sample quotes list
quotes = [
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "The only limit to our realization of tomorrow is our doubts of today.", "author": "F. D. Roosevelt"},
    {"text": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
    {"text": "Great things never come from comfort zones.", "author": "Unknown"}
]

st.set_page_config(page_title="InspoQuotes", layout="centered")

st.title("🌟 InspoQuotes")
st.subheader("Your Daily Dose of Inspiration")

# Session state to save favorites
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# Pick a random quote
if "current_quote" not in st.session_state:
    st.session_state.current_quote = random.choice(quotes)

quote = st.session_state.current_quote
st.markdown(f"### _\"{quote['text']}\"_")
st.write(f"— {quote['author']}")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✨ New Quote"):
        st.session_state.current_quote = random.choice(quotes)
        st.experimental_rerun()

with col2:
    if st.button("❤️ Save to Favorites"):
        if quote not in st.session_state.favorites:
            st.session_state.favorites.append(quote)
        st.success("Saved!")

with col3:
    st.markdown(
        f"[🔗 Tweet This](https://twitter.com/intent/tweet?text={quote['text']} — {quote['author']})",
        unsafe_allow_html=True,
    )

# Show favorites
if st.session_state.favorites:
    st.write("---")
    st.subheader("💾 Saved Quotes")
    for q in st.session_state.favorites:
        st.markdown(f"> _\"{q['text']}\"_ — **{q['author']}**")
