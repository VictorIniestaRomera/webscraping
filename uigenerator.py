import streamlit as st;
import pandas as pd;

class UIGenerator:
    def __init__(self):
        pass;

    def drawTable(self, quotes: list) -> None:
        st.set_page_config(layout="wide");

        df = pd.DataFrame(quotes);
        st.dataframe(df, width="content");