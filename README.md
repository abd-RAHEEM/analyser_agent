#  MSME Digital Analyst Agent

A powerful, AI-driven business intelligence dashboard designed for Micro, Small, and Medium Enterprises (MSMEs). This agent integrates fragmented data sources—Sales, Inventory, and Marketing—to provide real-time causal insights and actionable recommendations using Google's Gemini 2.5 Flash model.

## 🚀 Key Features

*   **Integrated Data View**: Unifies disparate CSV data streams (Sales, Inventory, Marketing) into a single analytical context.
*   **Natural Language Querying**: Ask complex business questions in plain English (e.g., *"Why did sales drop on Tuesday?"*).
*   **Causal Reasoning Engine**: Beyond simple correlation, the agent investigates *why* things happened (e.g., linking a sales dip to low inventory or reduced marketing ad spend).
*   **Structured Output**: Delivers insights in a clear format: **Observation**, **Root Cause**, and **Recommendation**.
*   **User-Friendly Interface**: Built with Streamlit for a clean, accessible experience.

## 🛠️ Tech Stack

*   **Python**: Core programming language.
*   **Streamlit**: Web application framework for the dashboard.
*   **Google Generative AI (Gemini 2.5 Flash)**: The brain behind the reasoning and analysis.
*   **Pandas**: For efficient data manipulation and processing.
*   **Python-DotEnv**: For secure environment variable management.

## 📂 Project Structure

```bash
digital-analyst-agent/
├── agents/
│   └── agent_core.py    # Logic connecting DataFrames and Gemini API
├── data/
│   ├── sales.csv        # Historical sales data
│   ├── inventory.csv    # Stock level logs
│   └── marketing.csv    # Ad spend and campaign data
├── .env                 # API Key configuration (create this)
├── .gitignore           # Git ignore rules
├── app.py               # Main Streamlit application entry point
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## ⚙️ Installation & Setup

Follow these steps to get the agent running on your local machine.

### 1. Prerequisities
*   Python 3.9 or higher installed.
*   A valid [Google Gemini API Key](https://aistudio.google.com/app/apikey).

### 2. Clone the Repository
```bash
git clone https://github.com/abd-RAHEEM/analyser_agent
cd digital-analyst-agent
```

### 3. Install Dependencies
It is recommended to use a virtual environment.
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
Create a `.env` file in the root directory to store your API credentials securely:

```bash
# .env
GOOGLE_API_KEY=your_actual_api_key_here
```

### 5. Run the Application
Start the Streamlit server:
```bash
streamlit run app.py
```

The app should open automatically in your browser at `http://localhost:8501`.

## 💡 Usage Example

1.  **Check Data**: Scroll to the bottom of the page to see the currently loaded `Sales`, `Inventory`, and `Marketing` data streams.
2.  **Ask a Question**: In the input box, type:
    > "Analyze the impact of marketing spend on our recent sales performance."
3.  **Get Insights**: The agent will process the data and return:
    *   **Observation**: Current trends in the data.
    *   **Root Cause**: The causal link discovered.
    *   **Recommendation**: A specific business action to take.

## 🤝 Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any features, bug fixes, or documentation improvements.
