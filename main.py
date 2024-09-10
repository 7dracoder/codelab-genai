import os

from flask import Flask, request

import google.auth
import vertexai
from vertexai.generative_models import GenerativeModel

_, project = google.auth.default()

app = Flask(__name__)

@app.route("/")
def hello_world():
    vertexai.init(project=project, location="us-central1")
    model = GenerativeModel("gemini-1.5-flash")
    animal = request.args.get("animal", "dog") 
    prompt = f"Give me 10 fun facts about {animal}. Return this as html without backticks."
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
