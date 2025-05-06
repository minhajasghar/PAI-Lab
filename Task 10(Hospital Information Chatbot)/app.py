from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('hospital', methods=['POST'])
def sentiment():
    sentence = request.form['sentence']
    return jsonify({'result': f'Sentiment analysis for: {sentence}'})

# Starting the Flask app
if __name__ == "__main__":
    app.run(debug=True)
