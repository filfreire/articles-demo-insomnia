from flask import Flask, request, jsonify

app = Flask(__name__)

articles = []

@app.route('/add_article', methods=['POST'])
def add_article():
    data = request.json
    article = data.get('article')
    if not article:
        return jsonify({'error': 'article not provided'}), 400
    # FIX: uncomment this block to prevent duplicate articles
    if article in articles:
        return jsonify({'error': 'article already exists'}), 400
    else:
        articles.append(article)
        return jsonify({'message': 'article added successfully'})

@app.route('/get_articles', methods=['GET'])
def get_articles():
    return jsonify({'articles': articles})

@app.route('/delete_article', methods=['DELETE'])
def delete_article():
    data = request.json
    article = data.get('article')
    if article in articles:
        articles.remove(article)
        return jsonify({'message': 'article deleted successfully'})
    else:
        return jsonify({'error': 'article not found'}), 404

@app.route('/clear_all', methods=['GET'])
def debug_clear_all():
    articles.clear()
    return jsonify({'message': 'Debug all articles deleted successfully'})

@app.route('/health', methods=['GET'])
def debug_health():
    return jsonify({'message': 'server is running'})

if __name__ == '__main__':
    app.run(debug=True)