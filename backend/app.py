from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests

# Load .env variables (Groq API key)
load_dotenv()

app = Flask(__name__)

# Step 1: Rule-based fallback safety tips
def generate_rule_based_tips(data):
    tips = []
    if data['avg_speed'] > 80:
        tips.append("Maintain speed under 80 km/h for safety.")
    if data['harsh_brakes'] > 5:
        tips.append("Avoid harsh braking to reduce wear and tear.")
    if data['night_drives'] > 3:
        tips.append("Limit night driving to reduce fatigue and accident risk.")
    if data['phone_usage'] > 0:
        tips.append("Avoid using mobile phones while driving.")
    if not tips:
        tips.append("Excellent driving behavior. Keep it up!")
    return "\n".join(tips)

# Step 2: Groq AI Safety Tips using LLaMA3-8B
def get_ai_tips(prompt):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None  # No API key provided

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "messages": [
                {"role": "system", "content": "You are a helpful driving safety assistant."},
                {"role": "user", "content": prompt}
            ],
            "model": "llama3-8b-8192"  # ✅ Using LLaMA 3 (8B)
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions",
                                 headers=headers, json=payload)
        return response.json()['choices'][0]['message']['content'].strip()

    except Exception as e:
        print("Groq API error:", e)
        return None

# Step 3: Risk Scoring Logic
def calculate_risk_score(data):
    score = 0
    if data['avg_speed'] > 80:
        score += 2
    if data['harsh_brakes'] > 5:
        score += 2
    if data['night_drives'] > 3:
        score += 1
    if data['phone_usage'] > 0:
        score += 2
    return score

# Step 4: API Endpoint
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    # Risk score & premium
    risk_score = calculate_risk_score(data)
    premium = 1000 + (risk_score * 100)

    # Groq Prompt
    prompt = f"""Suggest 3 safety tips for a driver with:
- Average speed: {data['avg_speed']} km/h
- Harsh brakes: {data['harsh_brakes']}
- Night drives: {data['night_drives']}
- Phone usage: {data['phone_usage']}"""

    # Try AI safety tips → fallback to rule-based
    safety_tips = get_ai_tips(prompt)
    if not safety_tips:
        safety_tips = generate_rule_based_tips(data)

    return jsonify({
        "risk_score": risk_score,
        "adjusted_premium": premium,
        "safety_tips": safety_tips
    })

# Step 5: Run the server
if __name__ == '__main__':
    app.run(debug=True)
