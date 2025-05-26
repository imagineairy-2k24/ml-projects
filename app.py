def get_travel_suggestion(budget, season, interest):
    budget = budget.lower()
    season = season.lower()
    interest = interest.lower()

    if budget == "low":
        if season == "summer" and interest == "adventure":
            return "Rishikesh (River Rafting)"
        elif season == "winter" and interest == "culture":
            return "Jaipur (Heritage Forts)"
        elif season == "monsoon" and interest == "relaxation":
            return "Munnar (Hill Station, Kerala)"
        else:
            return "Try exploring local weekend destinations!"

    elif budget == "medium":
        if season == "summer" and interest == "culture":
            return "Hampi (Historical Ruins)"
        elif season == "winter" and interest == "relaxation":
            return "Manali (Snow Retreat)"
        elif season == "monsoon" and interest == "adventure":
            return "Cherrapunji (Trekking & Caves)"
        else:
            return "Explore national gems like Udaipur or Darjeeling!"

    elif budget == "high":
        if season == "summer" and interest == "relaxation":
            return "Bali, Indonesia (Luxury Beach Resorts)"
        elif season == "winter" and interest == "adventure":
            return "Switzerland (Ski & Snowboarding)"
        elif season == "monsoon" and interest == "culture":
            return "Kyoto, Japan (Temple Trails)"
        else:
            return "Premium international tour packages await!"

    else:
        return "Sorry, we couldn't understand your budget preference."

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    suggestion = None
    if request.method == 'POST':
        budget = request.form['budget']
        season = request.form['season']
        interest = request.form['interest']
        suggestion = get_travel_suggestion(budget, season, interest)
    return render_template('index.html', suggestion=suggestion)

if __name__ == '__main__':
    app.run(debug=True)
