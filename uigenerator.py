import streamlit as st;
import pandas as pd;

from collections import Counter;

class UIGenerator:
    def __init__(self):
        st.set_page_config(layout="wide");

    def drawTable(self, quotes: list) -> None:
        df = pd.DataFrame(quotes);
        st.dataframe(df, width="content");

    def drawBarChart(self, quotes: list) -> None:
        df = pd.DataFrame(quotes);
        counts = (df["author"].value_counts().rename_axis("Author").reset_index(name="Quotes"));

        st.bar_chart(counts, x="Author", y="Quotes");