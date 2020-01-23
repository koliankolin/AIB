from flask import Flask, render_template

app = Flask(__name__)

mock_data = [
    {
        'id': 1,
        'home_team': 'Liverpool',
        'away_team': 'Man Utd',
        'prob_home_win': 0.99,
        'prob_away_win': 0.01,
        'pred_total_goals': 2.75,
        'pred_total_corners': 7.87,
        'pred_total_yellow_cards': 3.56,
        'pred_home_goals': 2.5,
        'pred_away_goals': 0.5,
        'pred_home_corners': 6.76,
        'pred_away_corners': 1.01,
        'pred_home_yellow_cards': 0.05,
        'pred_away_yellow_cards': 3.51,
    }
]

@app.route('/')
def home():
    return render_template('main.html', preds=mock_data)

@app.route('/about')
def about():
    return '<h1>About</h1>'

if __name__ == '__main__':
    app.run(debug=True)