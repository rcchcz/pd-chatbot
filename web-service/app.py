from flask import Flask, request, jsonify

import bot
bot.bot_trainning()

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def send_message():
    if request.method == 'POST':
        input_text = request.json.get('message')
        return jsonify({'response': bot.bot_answer(input_text)})

if __name__ == '__main__':
    app.run(debug=False)
