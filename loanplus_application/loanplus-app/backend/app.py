import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
# Enable CORS to allow requests from the Frontend EC2 instance
CORS(app)

# Database Configuration (Set these via environment variables on EC2)
DB_HOST = os.getenv('DB_HOST', 'your-rds-endpoint.amazonaws.com')
DB_USER = os.getenv('DB_USER', 'admin')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'YourPasswordHere')
DB_NAME = os.getenv('DB_NAME', 'loanplus_db')

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "LoanPlus Backend"}), 200

@app.route('/api/apply', methods=['POST'])
def apply_loan():
    data = request.get_json()

    # Required field verification
    required_fields = ['fullName', 'email', 'mobileNumber', 'uidNumber', 'panNumber', 'cibilScore', 'loanType']
    for field in required_fields:
        if not data.get(field):
            return jsonify({'error': f'Missing required field: {field}'}), 400

    try:
        cibil = int(data['cibilScore'])
        if cibil < 300 or cibil > 900:
            return jsonify({'error': 'CIBIL score must be between 300 and 900'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid CIBIL score format'}), 400

    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO loan_applications 
                (full_name, email, mobile_number, uid_number, pan_number, cibil_score, loan_type)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                data['fullName'],
                data['email'],
                data['mobileNumber'],
                data['uidNumber'],
                data['panNumber'],
                cibil,
                data['loanType']
            ))
        conn.commit()
        conn.close()

        return jsonify({
            'message': 'Loan application submitted successfully!',
            'status': 'SUCCESS'
        }), 201

    except Exception as e:
        app.logger.error(f"Database error: {str(e)}")
        return jsonify({'error': 'Internal server error while processing application'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
