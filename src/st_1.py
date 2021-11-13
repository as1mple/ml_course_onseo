import streamlit as st

from modules.simple_ml_models import HousePriceModel


@st.cache
def load_model():
    return HousePriceModel()


if __name__ == '__main__':
    house_price_model = load_model()

    title = "=> HousePriceModel <="
    st.markdown(f"<h1 style='text-align: center; color: red;'> "
                f"{title} </h1>", unsafe_allow_html=True)

    with st.form("my_form"):

        n_floors = st.number_input('N floors', min_value=1, max_value=10, value=1)
        area = st.slider('Area', min_value=1, max_value=300, value=50)

        heating = st.radio('Heating', "A B C".split())

        submitted = st.form_submit_button('Submit')
        if submitted:
            result_price = house_price_model(n_floors=n_floors, area=area, heating=heating)
            output_text = f"Price ≈ {result_price}"
            st.markdown(f"<h2 style='text-align: center; color: blue;'> {output_text} </h2>",
                        unsafe_allow_html=True)
