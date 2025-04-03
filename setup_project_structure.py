import os

# Define your project structure
folders = [
    "data",
    "models",
    "utils",
    "app"
]

# Files to create
files = {
    "requirements.txt": "",
    ".env": "# Add your API keys here\n",
    "README.md": "# Real-Time Financial Sentiment Analysis Web App\n",
    "config.yaml": "# Global parameters (e.g., default ticker, refresh rate)\n",
    "app/dashboard.py": "# Streamlit dashboard entry point\n",
    "app/sentiment_engine.py": "# Sentiment analysis utilities\n",
    "app/stock_data.py": "# Stock data fetching functions\n",
}

# Create folders and add a .gitkeep file inside each
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, ".gitkeep"), "w") as f:
        pass  # keeps directory tracked in Git

# Create files with starter content
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Project directory structure created!")
