import streamlit as st
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Make sure punkt is downloaded at runtime
with st.spinner("Setting up..."):
    nltk.download('punkt')

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
