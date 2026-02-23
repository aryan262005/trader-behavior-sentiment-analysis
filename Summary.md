## **Methodology**

* **This project analyzes trader performance under different market sentiment regimes using the Fear \& Greed Index.**



**The workflow consisted of:**

1. **Data Cleaning \& Alignment**

* **Converted timestamps to daily level.**
* **Merged trader transaction data with sentiment classification by date.**
* **Created derived features such as win indicator and trader frequency segments.**



**2. Performance Analysis**

* **Compared average PnL and win rates across sentiment regimes.**

**Compared average PnL and win rates across sentiment regimes.**



**3.Behavioral Segmentation**

* **Segmented traders into Frequent vs Infrequent groups.**
* **Applied KMeans clustering to identify behavioral archetypes based on:** **Average PnL**
* 
**&nbsp;                                                                        Position size** 

                                                                         **Win rate** 

**4.Interactive Exploration**

* **Built a Streamlit dashboard to dynamically filter performance by sentiment and trader segment.**

## 

## **Key Insights**

**1.Performance Improves During Extreme Greed**

* **Average PnL and win rates are higher in Extreme Greed regimes.**
* **Suggests stronger directional momentum and clearer market structure.**



**2. Frequent Traders Slightly Outperform**

* **Frequent traders show higher win rates (~2% improvement).**
* **Indicates experience and active participation may contribute to better execution.**



**3. Behavior Adjusts With Sentiment**

* **Trade frequency increases during Greed.**
* **Long positions dominate in bullish sentiment periods.**
* **Suggests sentiment-driven behavioral bias.**



**4. Distinct Behavioral Archetypes Exist**

* **Clustering reveals high-risk traders, consistent performers, and low-performance participants.**
* **Performance dispersion highlights importance of strategy discipline.**



## **Strategy Recommendations**

1. **Sentiment-Adaptive Exposure**

* **Increase position size and participation during Extreme Greed regimes.**
* **Reduce leverage and tighten risk controls during Fear conditions.**



**2. Segment-Based Participation Rules**

* **Allow higher trade frequency for experienced (frequent) traders during volatile markets.**
* **Restrict overtrading among infrequent traders in uncertain regimes.**



**3. Behavior-Aware Risk Controls**

* **Monitor long-bias concentration during Greed periods.**
* **Implement dynamic position limits to avoid sentiment-driven overexposure.**



## **Conclusion**

**Market sentiment meaningfully influences both trader behavior and performance.**

**Incorporating sentiment-aware rules and trader segmentation can improve risk management and decision-making frameworks.**



