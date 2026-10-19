# Fashion Design Chatbot with Flask and GPT-4o (GitHub Models API)

A Flask-based AI chatbot assistant for fashion design, powered by OpenAI/GPT-4o via the GitHub Models API, featuring a responsive ChatGPT-style UI with dark mode support.

---

## Features

- 💬 ChatGPT-style conversational interface with markdown support (headings, bold, lists)
- 🌓 Dark mode toggle
- ⚡ Responsive message layout with typing indicator
- ☁️ Deployable to **Vercel** with 1-click Git integration for $0 / Free
- 🛡️ Environment variable support for API tokens

---

## Local Setup

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd fashion_chatbot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your GitHub Personal Access Token (PAT)**:
   - Generate a token at [GitHub Settings > Personal Access Tokens](https://github.com/settings/tokens)
   - Set the environment variable:
     - **Windows (PowerShell)**: `$env:GITHUB_TOKEN="your_token_here"`
     - **Windows (CMD)**: `set GITHUB_TOKEN=your_token_here`
     - **Linux/Mac**: `export GITHUB_TOKEN="your_token_here"`

4. **Run the application**:
   ```bash
   python app.py
   ```
   Open your browser at `http://127.0.0.1:5000`.

---

## Deploy to Vercel for Free

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Configure project for Vercel deployment"
   git push origin master
   ```

2. **Deploy on Vercel**:
   - Go to [vercel.com](https://vercel.com) and sign in with GitHub.
   - Click **"Add New..."** > **"Project"**.
   - Select your `fashion_chatbot` repository and click **Import**.
   - Under **Environment Variables**:
     - **Name**: `GITHUB_TOKEN`
     - **Value**: *Your GitHub Personal Access Token*
   - Click **Deploy**.
   - Your chatbot will be live with a free `.vercel.app` URL!