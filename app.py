from flask import Flask, render_template, request, jsonify
from utils import download_single, download_multiple, download_by_username

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download_single', methods=['POST'])
def download_single_route():
    url = request.json.get('url')
    result = download_single(url)
    return jsonify(result)

@app.route('/download_multiple', methods=['POST'])
def download_multiple_route():
    urls = request.json.get('urls')
    result = download_multiple(urls)
    return jsonify(result)

@app.route('/download_by_username', methods=['POST'])
def download_by_username_route():
    username = request.json.get('username')
    result = download_by_username(username)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
