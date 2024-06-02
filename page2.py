import streamlit as st


def page2():
    st.title("Page 2: Text Statistics")
    uploaded_file = st.file_uploader("Choose a text file", type="txt")

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
        sentences = text.split('.')
        num_sentences = len(sentences)
        st.subheader("Sentence Count")
        st.write(f"The text contains {num_sentences} sentences.")
        avg_sentence_length = sum(len(sentence.split()) for sentence in sentences) / num_sentences
        st.subheader("Average Sentence Length")
        st.write(f"The average sentence length is {avg_sentence_length:.2f} words.")
