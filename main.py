from flask import Flask, request, jsonify
import sys
import importlib

# fmt:off
sys.path.append("./classes")
sys.path.append("./model")

from model import linear_regression as rrg
from classes import experiment as exp, ml_profile as mlp
importlib.reload(rrg)
importlib.reload(exp)
importlib.reload(mlp)
# fmt:on

app = Flask(__name__)

db = mlp.db

try:
    db.connect()
    db.create_tables([mlp.MLProfile])
except Exception as e:
    print(f"Error creating tables: {e}")


@app.route('/profiles', methods=['POST'])
def create_profile():
    data = request.get_json()
    new_profile = mlp.MLProfile.create(
        name=data['name'],
        profile_id=data['profile_id'],
        test_size=data['test_size'],
        epoch=data['epoch'],
        batch_size=data['batch_size'],
        input_columns=','.join(data['input_columns']),
        target_column=data['target_column'],
        model_name=data['model_name']
    )
    new_profile.save()
    print('Create Profile:', new_profile.id)

    return jsonify({'id': new_profile.id, 'item': data}), 201


@app.route('/profiles', methods=['GET'])
def get_profiles():
    data = mlp.MLProfile.select()
    return jsonify([
        {
            'id': profile.id,
            'name': profile.name,
            'profile_id': profile.profile_id,
            'test_size': profile.test_size,
            'epoch': profile.epoch,
            'batch_size': profile.batch_size,
            'input_columns': profile.input_columns.split(','),
            'target_column': profile.target_column
        } for profile in data
    ]), 200


@app.route('/profiles/<string:profile_id>', methods=['PUT'])
def update_profile(profile_id):
    data = request.get_json()
    print('Update Profile:', profile_id, data)
    query = mlp.MLProfile.update(
        **data).where(mlp.MLProfile.profile_id == profile_id)
    if query.execute():
        return jsonify({'id': profile_id, 'item': data}), 200
    return jsonify({'error': 'Profile not found'}), 404


# @app.route('/items/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     if 0 <= item_id < len(items):
#         deleted = items.pop(item_id)
#         return jsonify({'deleted': deleted})
#     return jsonify({'error': 'Item not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3201)

    @app.teardown_appcontext
    def close_db(exception):
        if not db.is_closed():
            db.close()
