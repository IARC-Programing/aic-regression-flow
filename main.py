from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
items = []


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if 0 <= item_id < len(items):
        return jsonify(items[item_id])
    return jsonify({'error': 'Item not found'}), 404


@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    items.append(data)
    return jsonify({'id': len(items) - 1, 'item': data}), 201


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if 0 <= item_id < len(items):
        data = request.get_json()
        items[item_id] = data
        return jsonify({'id': item_id, 'item': data})
    return jsonify({'error': 'Item not found'}), 404


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        deleted = items.pop(item_id)
        return jsonify({'deleted': deleted})
    return jsonify({'error': 'Item not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
