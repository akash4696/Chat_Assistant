from flask import Flask, request, jsonify, render_template
from query_parser import parse_query
from database import get_db_connection
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure index.html is inside a 'templates' folder

@app.route('/query', methods=['POST'])
def handle_query():
    try:
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({"error": "No query provided"}), 400

        sql_query, params = parse_query(user_query)
        if not sql_query:
            return jsonify({"error": "Unsupported query format"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query, params)
        results = cursor.fetchall()
        conn.close()

        if results:
            return jsonify({"results": [dict(row) for row in results]})
        else:
            return jsonify({"message": "No results found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Bind to 0.0.0.0 and use the PORT environment variable
    port = int(os.getenv('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port)
