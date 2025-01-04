from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

@app.route('/health/system', methods=['GET'])
def health_check():
    return jsonify({"health": "All systems operational"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
