import streamlit as st


def page1():
    st.title("Page 1: CV Analyzer")
    uploaded_file = st.file_uploader("Choose a text file", type="txt")

    if uploaded_file is not None:
        cv_text = uploaded_file.read().decode("utf-8")
        words = cv_text.split()
        num_words = len(words)
        st.subheader("Word Count")
        st.write(f"The CV contains {num_words} words.")
        unique_words = set(words)
        num_unique_words = len(unique_words)
        st.subheader("Unique Word Count")
        st.write(f"The CV contains {num_unique_words} unique words.")
