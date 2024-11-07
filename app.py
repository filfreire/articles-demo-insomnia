from flask import Flask, request, jsonify, Response

app = Flask(__name__)

articles = []

@app.route('/add_article', methods=['POST'])
def add_article():
    data = request.json
    article = data.get('article')
    if not article:
        return jsonify({'error': 'article not provided'}), 400
    # Validate that article has the required fields
    required_fields = ['author', 'title', 'publisher', 'year']
    for field in required_fields:
        if field not in article:
            return jsonify({'error': f'{field} is required'}), 400
    # Check for duplicates based on 'author' and 'title'
    for existing_article in articles:
        if existing_article['author'] == article['author'] and existing_article['title'] == article['title']:
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
    if not article:
        return jsonify({'error': 'article not provided'}), 400
    # Validate that 'author' and 'title' are provided
    required_fields = ['author', 'title']
    for field in required_fields:
        if field not in article:
            return jsonify({'error': f'{field} is required'}), 400
    # Find and remove the article
    for existing_article in articles:
        if existing_article['author'] == article['author'] and existing_article['title'] == article['title']:
            articles.remove(existing_article)
            return jsonify({'message': 'article deleted successfully'})
    else:
        return jsonify({'error': 'article not found'}), 404

@app.route('/clear_all', methods=['GET'])
def debug_clear_all():
    articles.clear()
    return jsonify({'message': 'All articles deleted successfully'})

@app.route('/health', methods=['GET'])
def debug_health():
    return jsonify({'message': 'server is running'})

@app.route('/get_articles_bibtex', methods=['GET'])
def get_articles_bibtex():
    bibtex_entries = []
    for article in articles:
        # Generate a citation key using the author's last name and year
        author_last_name = article['author'].split()[-1]
        citation_key = f"{author_last_name}{article['year']}"
        bibtex_entry = f"@book{{{citation_key},\n"
        bibtex_entry += f"  author = {{{article['author']}}},\n"
        bibtex_entry += f"  title = {{{article['title']}}},\n"
        bibtex_entry += f"  publisher = {{{article['publisher']}}},\n"
        bibtex_entry += f"  year = {{{article['year']}}}\n"
        bibtex_entry += "}\n"
        bibtex_entries.append(bibtex_entry)
    bibtex_output = "\n".join(bibtex_entries)
    return Response(bibtex_output, mimetype='application/x-bibtex')


if __name__ == '__main__':
    app.run(debug=True)