import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class BusinessAnalystAgent:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        # Load data once when agent starts
        self.sales_df = pd.read_csv('data/sales.csv')
        self.inv_df = pd.read_csv('data/inventory.csv')
        self.mkt_df = pd.read_csv('data/marketing.csv')

    def analyze(self, user_query):
        # We provide the data summaries to the LLM so it knows the context
        context = f"""
        Sales Data Summary: {self.sales_df.head(5).to_string()}
        Inventory Data Summary: {self.inv_df.head(5).to_string()}
        Marketing Data Summary: {self.mkt_df.head(5).to_string()}
        """
        
        prompt = f"""
        You are a 24/7 Digital Analyst for an MSME. 
        Context Data: {context}
        
        User Question: {user_query}
        
        Task:
        1. Analyze the data for patterns.
        2. Perform Causal Reasoning (If sales are down, check if inventory was low or marketing spend decreased).
        3. Provide a clear, actionable recommendation.

        Return your response in this exact format:
        **Observation**: [What is happening]
        **Root Cause**: [Why it happened based on data]
        **Recommendation**: [What the owner should do]
        """
        
        response = self.model.generate_content(prompt)
        return response.text