from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tagd():
    print(request.json)
    return jsonify({'message': 'Tag created successfully!'}), 200
