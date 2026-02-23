import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Config

st.set_page_config(page_title="Trader Behavior Dashboard",layout="wide")
st.title("Trader Behavior & Sentiment Dashboard")
st.markdown("Interactive exploration of trader performance under different market sentiment regimes.")

# Loading Data

@st.cache_data
def load_data():
    # NOTE: Run the notebook first to generate merged_data.csv locally
    return pd.read_csv("merged_data.csv")

merged = load_data()

st.sidebar.markdown("---")
st.sidebar.write(f"Total Trades in Dataset: {len(merged)}")

merged = merged.dropna(subset=['classification', 'Trader_Frequency'])

# Sidebar Filters

st.sidebar.header("Filters")
sentiment = st.sidebar.selectbox("Select Sentiment",sorted(merged['classification'].unique()))
segment = st.sidebar.selectbox("Select Trader Frequency",merged['Trader_Frequency'].unique())
filtered = merged[(merged['classification'] == sentiment) & (merged['Trader_Frequency'] == segment)]

# Key Metrics
st.subheader("Key Performance Metrics")

col1, col2, col3 = st.columns(3)

if len(filtered) > 0:
    col1.metric("Average PnL", f"{filtered['Closed PnL'].mean():.2f}")
    col2.metric("Win Rate", f"{filtered['win'].mean():.2%}")
    col3.metric("Total Trades", len(filtered))
else:
    col1.metric("Average PnL", "N/A")
    col2.metric("Win Rate", "N/A")
    col3.metric("Total Trades", 0)

st.divider()
# Charts Section
col4, col5 = st.columns(2)

if len(filtered) > 0:

    # PnL Distribution
    with col4:
        st.subheader("PnL Distribution")

        fig, ax = plt.subplots()
        ax.hist(filtered['Closed PnL'], bins=30)
        ax.set_xlabel("Closed PnL")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

    # Long / Short Breakdown
    with col5:
        st.subheader("Long vs Short Distribution")

        long_short = filtered['Side'].value_counts()

        fig2, ax2 = plt.subplots()
        ax2.bar(long_short.index, long_short.values)
        ax2.set_xlabel("Side")
        ax2.set_ylabel("Trade Count")
        st.pyplot(fig2)

else:
    st.info("No data available for selected filters.")

st.divider()
# Summary Insight
st.subheader("Insight Summary")

st.markdown("""
This dashboard allows dynamic exploration of trader behavior 
under varying sentiment regimes.

- Performance improves during Extreme Greed.
- Frequent traders exhibit slightly higher win rates.
- Long bias increases during Greed periods.

Use the sidebar filters to explore segment-level behavior.

""")
