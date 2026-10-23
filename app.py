from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Frontend ko allow karega

# Simple AI Logic - MCA level ke liye perfect!
def predict_ai(attendance, assignment, internal, study_hours):
    # Percentage nikalo
    per = (attendance * 0.4) + (assignment/20*100 * 0.2) + (internal/30*100 * 0.3) + (study_hours*10 * 0.1)
    per = round(per, 1)
    
    # Pass/Fail
    result = "Pass" if per >= 50 else "Fail"
    return result, per

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    result, per = predict_ai(
        data['attendance'],
        data['assignment_marks'],
        data['internal_marks'],
        data['study_hours']
    )
    return jsonify({'result': result, 'percentage': per})

@app.route('/')
def home():
    return "AI Backend Running!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)