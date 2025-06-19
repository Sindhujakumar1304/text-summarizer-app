import streamlit as st
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Add bundled punkt data folder path
nltk.data.path.append('./nltk_data')

# Download punkt if not already present (won't redownload if bundled)
nltk.download('punkt', download_dir='./nltk_data')

st.title("Text Summarizer with LexRank")

user_text = st.text_area("Enter text to summarize", height=300)

sentences_count = st.slider("Summary length (sentences)", 1, 10, 3)

if st.button("Summarize"):
    if user_text.strip() == "":
        st.warning("Please enter some text to summarize!")
    else:
        try:
            parser = PlaintextParser.from_string(user_text, Tokenizer("english"))
            summarizer = LexRankSummarizer()
            summary = summarizer(parser.document, sentences_count=sentences_count)

            st.subheader("Summary:")
            for sentence in summary:
                st.write("-", sentence)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
