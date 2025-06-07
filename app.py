from flask import Flask, request, render_template
from logic import evaluate_hand
from model.card_detector import detect_cards

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    image = request.files['image']
    cards = detect_cards(image)
    recommendation = evaluate_hand(cards['hole_cards'], cards['board_cards'])
    return render_template("result.html", **cards, recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)
