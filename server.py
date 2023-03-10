import json
from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'something_special'


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    for club in clubs:
        if club['email'] == request.form['email']:
            return render_template('welcome.html', club=club, competitions=competitions)
    flash("This email is not valid please try again")
    return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        if datetime.strptime(foundCompetition['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
            flash("This competition is over you can't purchase places")
            return render_template('welcome.html', club=foundClub, competitions=competitions)
        else:
            return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    points_available = int(club['points'])
    placesRequired = int(request.form['places'])
    if placesRequired <= 0:
        flash("You can't select 0 or less places")

    elif placesRequired > 12:
        flash("You can't purchase more then 12 places")

    elif placesRequired <= points_available:
        club['points'] = points_available - placesRequired
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        flash('Great-booking complete!')

    else:
        flash('You need more points')

    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/showClubsPoints')
def displayClubsPoints():
    return render_template('display_points.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))



