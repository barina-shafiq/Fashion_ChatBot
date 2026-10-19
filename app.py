import os
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

# Read token from environment variable (configured in Vercel or local .env)
API_KEY = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_API_KEY")

client = None
if API_KEY:
    client = OpenAI(
        base_url="https://models.github.ai/inference",
        api_key=API_KEY
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"response": "Please enter a message to begin."}), 400

    api_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_API_KEY")
    if not api_token:
        return jsonify({
            "response": "Error: GITHUB_TOKEN is not configured. Please set the GITHUB_TOKEN environment variable in Vercel or in your local .env file."
        }), 500

    try:
        chat_client = client
        if not chat_client:
            chat_client = OpenAI(
                base_url="https://models.github.ai/inference",
                api_key=api_token
            )

        response = chat_client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant for a fashion design shop."},
                {"role": "user", "content": prompt}
            ],
            model="openai/gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1
        )
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
