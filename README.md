# Trader Behavior & Sentiment Analysis

Data-driven analysis of trader performance under Fear & Greed market sentiment regimes, including behavioral segmentation, clustering, and a Streamlit dashboard.

---

## Project Objective

This project investigates:

- How trader performance (PnL, win rate) changes across sentiment regimes
- Whether trader behavior shifts during Fear vs Greed periods
- Behavioral segmentation of traders
- Actionable strategy recommendations

---

## Key Insights

- Performance improves during Extreme Greed regimes.
- Frequent traders exhibit slightly higher win rates.
- Long bias increases in bullish sentiment periods.

---

## Trader Segmentation

- Frequent vs Infrequent traders
- KMeans clustering to identify behavioral archetypes:
  - High-risk traders
  - Consistent performers
  - Low-performance traders

---

## Streamlit Dashboard

An interactive dashboard was built to explore:

- Performance by sentiment
- Trader segments
- PnL distribution
- Long/Short behavior

Run locally:

```bash
pip install -r requirements.txt
streamlit run app.py
