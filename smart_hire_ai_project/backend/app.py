from flask import Flask, request, jsonify
from services.resume_parser import parse_transcript
from services.github_api import fetch_github_profile

app = Flask(__name__)

@app.route("/api/voice-resume", methods=["POST"])
def voice_resume():
    data = request.get_json()
    transcript = data.get("transcript", "")
    resume = parse_transcript(transcript)
    return jsonify({"resume": resume})

@app.route("/api/github/<username>")
def github_profile(username):
    data = fetch_github_profile(username)
    return jsonify(data)

@app.route("/api/linkedin-demo")
def linkedin_demo():
    fake = {
        "name": "Jane Doe",
        "headline": "Senior Software Engineer",
        "experience": [
            "Company A (2019–2023): Senior Engineer",
            "Company B (2016–2019): Engineer"
        ],
        "education": ["B.Tech in CS — XYZ University"],
        "skills": ["Python", "Django", "React", "SQL"]
    }
    return jsonify(fake)

if __name__ == "__main__":
    app.run(debug=True)
