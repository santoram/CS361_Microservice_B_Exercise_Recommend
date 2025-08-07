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
    with open('Recommended Exercises.json', 'r') as infile:
        recommended_exercises = json.load(infile)
        exercises = recommended_exercises.get(target_muscle_group)
        print("Exercises found")
    if exercises:
        response_data = exercises
        print(response_data)
        return Response(json.dumps(response_data), mimetype='application/json', status=200)




if __name__ == '__main__':
    # check to make sure the file path exsists before execution
    # note this is running on port 8000
    app.run(host='127.0.0.1', port=5002, debug=True)