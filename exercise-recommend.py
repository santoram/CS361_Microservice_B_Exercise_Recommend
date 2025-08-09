import json
from flask import Flask, request, Response

app = Flask(__name__)

print('server listening on port 5002...')

@app.route('/exercise-recommend', methods=['GET'])
def get_suggested_exercise():
    """
    Provides a list of exercises based on the target muscle group provided
    """
    target_muscle_group = request.args.get('name')
    print(target_muscle_group)
    if not target_muscle_group:
        return Response(json.dumps('invalid query parameter'), mimetype='application/json', status=400)
    
    try:
        with open('Recommended Exercises.json', 'r') as infile:
            recommended_exercises = json.load(infile)
    except FileNotFoundError:
        return Response(json.dumps('File not found.', mimetype='application/json', status=500))
    
    exercises = recommended_exercises.get(target_muscle_group)    
    if exercises:
        print('found some exercises')
        response_data = exercises
    
    print("sending over!")
    return Response(json.dumps(response_data), mimetype='application/json', status=200)

if __name__ == '__main__':
    # check to make sure the file path exsists before execution
    # note this is running on port 5002
    app.run(host='127.0.0.1', port=5002, debug=True)