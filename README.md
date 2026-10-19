# 👗 Fashion Design Assistant ChatBot

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-3.5%20Flash-4285F4?logo=google&logoColor=white)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-000000?logo=vercel&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

An AI-powered conversational fashion styling assistant built with **Flask**, **HTML/CSS/JavaScript**, and **Google Gemini** (with OpenAI compatibility). It provides instant styling recommendations, color coordination advice, fabric guidance, and wardrobe tips in a sleek ChatGPT-style interface.

---

## ✨ Features

- 🎨 **Expert Fashion Guidance**: Get tailored advice on color combinations, fabrics, dress codes, seasonal styles, and outfit matching.
- ⚡ **Powered by Google Gemini**: Built on Google's high-speed, cost-free `gemini-3.5-flash-lite` model with intelligent fallback to `gemini-3.5-flash` and `gemini-3.8-flash`.
- 🌓 **Dark Mode Toggle**: Seamless one-click dark/light theme switcher with smooth transitions.
- 📝 **Markdown-Rendered Answers**: Supports rich text formatting (bolding, bulleted lists, numbered items, and headers) using Marked.js.
- 💬 **Dynamic Chat Interface**: Animated "Typing..." state, smooth auto-scrolling, and responsive layout for mobile and desktop screens.
- ☁️ **1-Click Free Vercel Deployment**: Configured out-of-the-box for Vercel Serverless Functions with zero hosting costs.
- 🛡️ **Secure Secret Management**: API keys are isolated in local `.env` and Vercel Environment Variables, safely excluded from version control.

---

## 📁 Project Structure

```text
fashion_chatbot/
├── api/
│   └── index.py            # Vercel serverless function entry point
├── public/
│   └── static/
│       └── style.css       # CDN edge-cached static stylesheet
├── static/
│   └── style.css           # Local development stylesheet
├── templates/
│   └── index.html          # Chat interface template (Jinja2)
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules (secrets, virtualenv, caches)
├── app.py                  # Core Flask backend application
├── requirements.txt        # Python dependency manifest
└── vercel.json             # Vercel routing and rewrite configuration
```

---

## 🚀 Getting Started (Local Development)

### 1. Prerequisites
- Python 3.10 or higher
- A free Google Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

### 2. Clone the Repository
```bash
git clone https://github.com/barina-shafiq/Fashion_ChatBot.git
cd Fashion_ChatBot
```

### 3. Create and Activate Virtual Environment (Optional but Recommended)
- **Windows (PowerShell)**:
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Your API Key
Create a `.env` file in the project root:
```bash
cp .env.example .env
```
Open `.env` and paste your Gemini API key:
```env
GEMINI_API_KEY=AIzaSyYourGeminiApiKeyHere
```

### 6. Run the App
```bash
python app.py
```
Open your browser and navigate to **`http://127.0.0.1:5000`**.

---

## ☁️ Free Deployment on Vercel

This repository is pre-configured for free deployment on **Vercel**:

1. **Push your code to GitHub**:
   Ensure your latest code is committed and pushed to your GitHub repository.
2. **Import to Vercel**:
   - Go to [vercel.com](https://vercel.com) and log in with GitHub.
   - Click **"Add New..."** → **"Project"**.
   - Select your `Fashion_ChatBot` repository and click **Import**.
3. **Set Environment Variables**:
   Under the **Environment Variables** section, add:
   | Key | Value | Description |
   | :--- | :--- | :--- |
   | `GEMINI_API_KEY` | `AIzaSy...` | *(Required)* Your Google Gemini API Key |
   | `GEMINI_MODEL` | `gemini-3.5-flash-lite` | *(Optional)* Override the default model |
4. **Deploy**:
   - Click **Deploy**.
   - In less than a minute, Vercel will provide your live deployment URL (e.g. `https://fashion-chatbot.vercel.app`).

---

## 🔑 How to Get a Free Google Gemini API Key

1. Visit **[Google AI Studio](https://aistudio.google.com/apikey)**.
2. Sign in with your Google account.
3. Click **"Create API key"**.
4. Copy the generated key (starts with `AIzaSy...`).
5. Paste it into your Vercel Environment Variables or local `.env` file.

---

## 🛠️ Supported AI Providers

The application dynamically detects configured credentials and selects the best provider:

| Provider | Environment Variable | Default Model | Free Tier |
| :--- | :--- | :--- | :--- |
| **Google Gemini** *(Recommended)* | `GEMINI_API_KEY` | `gemini-3.5-flash-lite` | ✅ Yes (Generous free limits) |
| **OpenAI** | `OPENAI_API_KEY` | `gpt-4o-mini` | 💳 Pay-as-you-go |
| **GitHub Models** | `GITHUB_TOKEN` | `openai/gpt-4o` | ⚠️ Limited availability |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
