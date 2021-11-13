import streamlit as st

from modules.simple_ml_models import SentimentModel


@st.cache
def load_model():
    return SentimentModel()


if __name__ == '__main__':
    sentiment_model = load_model()

    sent_map = {
        1: "Positive",
        0: "Neutral",
        -1: "Negative"
    }

    title = "=> Sentiment_model <="
    st.markdown(f"<h1 style='text-align: center; color: red;'> "
                f"{title} </h1>", unsafe_allow_html=True)

    with st.form("my_form"):

        input_text = st.text_area('input_text')
        submitted = st.form_submit_button('Submit')

        if submitted:
            sentiment = sentiment_model(text=input_text)
            output_text = f"Sentiment ≈ {sent_map.get(sentiment)}"
            st.markdown(f"<h2 style='text-align: center; color: blue;'> {output_text} </h2>", unsafe_allow_html=True)

            if sentiment == 1:
                st.balloons()
