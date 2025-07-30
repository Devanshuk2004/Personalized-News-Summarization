# 📰 Personalized News Summarization

## 📌 Overview
Personalized News Summarization is a machine learning-based system that:
- Summarizes long news articles into concise summaries.
- Detects favorable/unfavorable bias in the news.
- Provides an API (FastAPI) and Chrome Extension for real-time summarization.

This project is ideal for:
- **Readers** who want short unbiased news.
- **Developers** who want to integrate summarization/bias detection into their apps.
- **Researchers** studying bias in media.

---

## 🚀 Features
- **AI Summarization Model** – Shortens lengthy news articles.
- **Bias Detection** – Identifies favorable/unfavorable bias.
- **Chrome Extension** – Summarize any web page directly in the browser.
- **REST API** – Fast, JSON-based integration.
- **Cloud Deployment** – Easily deployable to Render or similar platforms.

---

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository
bash
git clone https://github.com/Devanshuk2004/Personalized-News-Summarization.git
cd Personalized-News-Summarization

**###2️⃣ Create Virtual Environment & Install Dependencies**
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt

**3️⃣ Download Model Files**
cd Phase1
python download.py

**▶️ Running the Application Locally**
cd Phase3
uvicorn integration_main:app --reload --host 127.0.0.1 --port 8002


**🌐 Deploying on Render**
1.Push repository to GitHub (exclude checkpoints via .gitignore).
2.Create a new Web Service on Render.

3.Build command:
pip install -r requirements.txt

4.Start command:
uvicorn Phase3.integration_main:app --host 0.0.0.0 --port 10000

**🧩 Chrome Extension Setup**
1.Open Chrome → chrome://extensions
2.Enable Developer Mode
3.Click Load Unpacked
4.Select chrome_extension folder
5.Use the popup to summarize the open page.

**👨‍💻 Author**
Devanshu Katiyar
GitHub: Devanshuk2004




