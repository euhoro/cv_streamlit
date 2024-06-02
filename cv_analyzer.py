import streamlit as st


def main():
    st.title("CV Analyzer")

    # Upload file
    uploaded_file = st.file_uploader("Choose a text file", type="txt")

    if uploaded_file is not None:
        # Read file
        cv_text = uploaded_file.read().decode("utf-8")

        # Display CV content
        st.subheader("CV Content")
        st.text(cv_text)

        # Calculate and display number of words
        words = cv_text.split()
        num_words = len(words)
        st.subheader("Word Count")
        st.write(f"The CV contains {num_words} words.")

        # Calculate and display number of unique words
        unique_words = set(words)
        num_unique_words = len(unique_words)
        st.subheader("Unique Word Count")
        st.write(f"The CV contains {num_unique_words} unique words.")


if __name__ == "__main__":
    main()
