import os
from urllib.parse import urlparse
from flask import Flask, request, jsonify, render_template
from openai import OpenAI

# Load local .env file if available (useful for local development)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Explicitly resolve template and static directories so it works both locally and on Vercel
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# WSGI Middleware to fix Vercel rewrite paths so Flask receives the true request route
class VercelPathFixer:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        matched_path = environ.get("HTTP_X_MATCHED_PATH")
        if matched_path:
            environ["PATH_INFO"] = urlparse(matched_path).path
        else:
            path_info = environ.get("PATH_INFO", "")
            if path_info.startswith("/api/index"):
                environ["PATH_INFO"] = path_info[len("/api/index"):] or "/"
            elif path_info.startswith("/api"):
                environ["PATH_INFO"] = path_info[len("/api"):] or "/"
        return self.wsgi_app(environ, start_response)

app.wsgi_app = VercelPathFixer(app.wsgi_app)

def get_ai_client_and_model():
    """
    Returns (client, model_name, error_message).
    Supports Gemini API (recommended & free), OpenAI API, and GitHub Models.
    """
    # 1. Google Gemini API (Recommended, 100% Free at https://aistudio.google.com)
    gemini_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if gemini_key:
        client = OpenAI(
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            api_key=gemini_key
        )
        return client, "gemini-1.5-flash", None

    # 2. Standard OpenAI API
    openai_key = os.environ.get("OPENAI_API_KEY")
    if openai_key:
        client = OpenAI(api_key=openai_key)
        return client, "gpt-4o-mini", None

    # 3. GitHub Models Token (legacy)
    github_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_API_KEY")
    if github_token:
        client = OpenAI(
            base_url="https://models.github.ai/inference",
            api_key=github_token
        )
        return client, "openai/gpt-4o", None

    return None, None, "No API key configured. Please add GEMINI_API_KEY (from https://aistudio.google.com) in your Vercel Environment Variables or local .env file."

@app.route("/")
@app.route("/api")
@app.route("/api/index")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
@app.route("/api/chat", methods=["POST"])
@app.route("/api/index/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"response": "Please enter a message to begin."}), 400

    client, model, err = get_ai_client_and_model()
    if err:
        return jsonify({"response": f"Configuration Error: {err}"}), 500

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful, knowledgeable fashion designer and stylist assistant. Provide stylish, creative, and practical advice on fabrics, colors, outfits, and fashion trends."
                },
                {"role": "user", "content": prompt}
            ],
            model=model,
            temperature=0.8,
            max_tokens=2048,
        )

        # Safely extract response whether object or text
        if hasattr(response, "choices") and response.choices:
            content = response.choices[0].message.content
        elif isinstance(response, str):
            content = response
        else:
            content = str(response)

        return jsonify({"response": content})
    except Exception as e:
        return jsonify({"response": f"API Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
