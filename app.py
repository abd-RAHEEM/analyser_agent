import streamlit as st
from agents.agent_core import BusinessAnalystAgent

# UI Setup
st.set_page_config(page_title="AI Digital Analyst", layout="wide")
st.title("📊 MSME Digital Analyst")
st.subheader("Real-time Business Intelligence & Causal Insights")

# Initialize Agent
agent = BusinessAnalystAgent()

# Sidebar for Status
with st.sidebar:
    st.success("System: Online")
    st.info("Connected to: Sales, Inventory, Marketing")

# Main Input
user_input = st.text_input("Ask your business question (e.g., 'Why did revenue dip on Tuesday?')")

if user_input:
    with st.spinner("Analyzing causal links..."):
        result = agent.analyze(user_input)
        
        # Displaying the result in a nice Card format
        st.markdown("### 🧠 Analyst Findings")
        st.info(result)

# Visualizing the "fragmented" data to show the integration
st.divider()
st.write("### Integrated Data Streams")
col1, col2, col3 = st.columns(3)
col1.dataframe(agent.sales_df.head(3))
col2.dataframe(agent.inv_df.head(3))
col3.dataframe(agent.mkt_df.head(3))