from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Homepage route


@app.route('/')
def index():
    return render_template('index.html')

# Chatbot route for handling user queries


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    response = generate_response(user_message)
    return jsonify({'response': response})

# Function to generate chatbot responses


def generate_response(message):
    if 'crop' in message.lower():
        return 'For the current season, grow rice or wheat depending on your region.'
    elif 'fertilizer' in message.lower():
        return 'Use organic fertilizers like compost for better yield.'
    elif 'weather' in message.lower():
        return 'The weather today is sunny with moderate humidity.'
    else:
        return 'I am still learning about agriculture. Please ask about crops, weather, or fertilizers.'


if __name__ == '__main__':
    app.run(debug=True)
