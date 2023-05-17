from flask import Blueprint, jsonify, request
from .models import GPT, db

api = Blueprint('api', __name__)
   

@api.route('/api/prompt/qa', methods=['POST'])
def generate_prompt():
    print('hello world')
    return jsonify({})
    data = request.get_json()
    question = data.get('question')

    # db.session.add(GPT)
    # db.session.commit()

    gpt = GPT(question, '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')

    return jsonify({
        'message': 'qa generated successfully',
        'status': 200,
        'data': gpt
    })

