from flask import Flask, request, jsonify

app = Flask(__name__)

# Risk scoring logic (same as in model.ipynb)
def calculate_risk(data):
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

# API endpoint
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()

        # Validate input
        required_fields = ['avg_speed', 'harsh_brakes', 'night_drives', 'phone_usage']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Calculate risk and premium
        risk_score = calculate_risk(data)
        premium = 1000 + (risk_score * 100)

        return jsonify({
            "risk_score": risk_score,
            "adjusted_premium": premium
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
