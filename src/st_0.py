import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

if __name__ == '__main__':
    st.markdown("<h1 style='text-align: center; color: red;'>=> DEMO Version <=</h1>", unsafe_allow_html=True)
    data = pd.DataFrame(np.random.rand(20, 20),
                        columns=list(map(lambda x: f"column_{x}", range(20))))
    st.dataframe(data)

    fig = plt.figure()
    plt.plot(data.column_1, data.column_1)
    st.pyplot(fig)

    image = np.random.randint(low=0,
                              high=256,
                              size=(512, 512, 3))
    st.image(image)
