import mysql.connector
from flask import Blueprint, render_template, request, flash, jsonify, session, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from website.models import Note
from website._init_ import db
import json

mydp = mysql.connector.connect(host="localhost", user="root", password="Qaisaleh12010@auc", database="premier_league",
                               auth_plugin='mysql_native_password')
if mydp:
    print("connected")
    mycursor = mydp.cursor()
else:
    print("Notconnected")

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/view_results', methods=['GET', 'POST'])
@login_required
def re_sults():
    return render_template("print_reviews.html", user=current_user)


@views.route('/1', methods=['GET', 'POST'])
def view_1():
    if request.method == 'POST':
        date_game = request.form.get('game_date')
        HomeClub = request.form.get('HomeClub')
        AwayClub = request.form.get('AwayClub')
        stars = request.form.get('rate')
        comment = request.form.get('comment')
        sql1 = "insert into `review_match` values (%s,%s,%s,%s,%s, %s)"

        val = (session['email'], str(date_game), str(HomeClub), str(AwayClub), stars, comment)
        try:
            mycursor.execute(sql1, val)
            mydp.commit()
            flash('Review added!', category='success')
            return redirect(url_for('views.home'))
        except Exception as e:
            flash('Error! Data not matched', category='error')

    return render_template("sub1.html", user=current_user)


@views.route('/2', methods=['GET', 'POST'])
def view_2():
    records = []

    if request.method == 'POST':
        date_game = request.form.get('game_date')
        HomeClub = request.form.get('HomeClub')
        AwayClub = request.form.get('AwayClub')
        if len(str(date_game))>0 and len(str(HomeClub))>0 and len(str(AwayClub))>0:
            sql1 = "select username, rate, text_review  from review_match as review inner join fan as fan on " \
                   "review.fan_email = fan.email  where game_date_m = %s AND game_clubHome = %s AND game_clubAway = %s "

            val = (str(date_game), str(HomeClub), str(AwayClub))

            mycursor.execute(sql1, val)
            records = mycursor.fetchall()
            print(records)
            flash('Done!', category='success')

    return render_template("sub2.html", user=current_user, records=records)


@views.route('/3', methods=['GET', 'POST'])
def view_3():
    players_s=[]
    if request.method == 'POST':
        Nationality = request.form.get('Nationality')
        sql1 = "select fName, lNAme, current_club, LL_Season_club, LLL_Season_club, LLLL_Season_club  from `player` " \
               "where nationality = %s "
        val = (Nationality,)
        mycursor.execute(sql1, val)
        players_s = mycursor.fetchall()
        flash('Done!', category='success')

    return render_template("sub3.html", user=current_user, players_s=players_s)


@views.route('/4', methods=['GET', 'POST'])
def view_4():
    sql1 = "select a ,COUNT(*)from(SELECT clubHome as a FROM match_game where goalsHome > goalsAway " \
           "union all SELECT clubAway as a FROM premier_league.match_game  where goalsHome < goalsAway) as T group by " \
           "a order by Count(*) desc ; "
    sql2 = "select a ,COUNT(*)from(SELECT clubHome as a FROM premier_league.match_game where goalsHome > goalsAway) " \
           "as T group by a order by Count(*) desc "

    sql3 = "select club ,sum(Ycard) from(SELECT clubHome as club , YcardsHome as Ycard  FROM match_game " \
           "union all SELECT clubAway  as club , YcardsAway as Ycard   FROM match_game  ) as T group by " \
           "club order by sum(Ycard) desc ; "

    sql4 = "select club ,sum(fouls) from(SELECT clubHome as club , foulsHome as fouls  FROM premier_league.match_game " \
           "  union all SELECT clubAway  as club , foulsAway as fouls   FROM premier_league.match_game  ) as T group " \
           "by club order by sum(fouls) desc ; "

    sql5 = "select club ,sum(shots) from(SELECT clubHome as club , shotsHome as shots  FROM premier_league.match_game " \
           "union all SELECT clubAway  as club , shotsAway as shots   FROM premier_league.match_game  ) as T group by " \
           "club order by sum(shots) desc ; "
    mycursor.execute(sql1)
    records = mycursor.fetchall()

    mycursor.execute(sql2)
    home_won = mycursor.fetchall()

    mycursor.execute(sql3)
    Ycard = mycursor.fetchall()

    mycursor.execute(sql4)
    fouls = mycursor.fetchall()

    mycursor.execute(sql5)
    shots = mycursor.fetchall()
    return render_template("sub4.html", user=current_user, result=records, home_won=home_won, Ycard=Ycard, fouls=fouls,
                           shots=shots)


@views.route('/5', methods=['GET', 'POST'])
def view_5():
    if request.method == 'POST':
        season = request.form.get('Season')

        if len(season) > 0:
            sql1 = "select a ,COUNT(*)from( SELECT clubHome as a FROM premier_league.match_game where goalsHome > " \
                   "goalsAway AND season = %s union all SELECT clubAway as a FROM premier_league.match_game where " \
                   "goalsHome < goalsAway  AND season = %s) as T group by a order by Count(*) desc ; "

            val = (str(season), str(season))

            mycursor.execute(sql1, val)
            records = mycursor.fetchall()
            return render_template("sub5.html", user=current_user, records=records)

    return render_template("sub5.html", user=current_user, records=[])


@views.route('/6', methods=['GET', 'POST'])
def view_6():
    squad = []
    stad_name=[]
    if request.method == 'POST':
        Club = request.form.get('Club')
        if len(str(Club))>0:
            sql1 = "SELECT name_club, name_stadium, building_date, capacity, pich_width, pich_len, address FROM club " \
                   "inner join stadium   on owner = name_club where name_club = %s; "
            sql2 = "SELECT fName, lNAme FROM club inner join player  on current_club = name_club where name_club = %s;"
            val = (str(Club),)
            mycursor.execute(sql1, val)
            stad_name = mycursor.fetchall()
            mycursor.execute(sql2, val)
            squad = mycursor.fetchall()
            flash('Done!', category='success')

    return render_template("sub6.html", user=current_user, squad=squad, stad_name= stad_name)


@views.route('/7', methods=['GET', 'POST'])
def view_7():
    records=[]
    if request.method == 'POST':
        fname = request.form.get('Name')
        lname = request.form.get('lName')
        sql1 = "select * from `player` where fName = %s  AND lNAme = %s"

        val = (str(fname), str(lname))

        mycursor.execute(sql1, val)
        records = mycursor.fetchall()
        flash('Done!', category='success')

    return render_template("sub7.html", user=current_user, records=records)


@views.route('/8', methods=['GET', 'POST'])
def view_8():
    records = []
    if request.method == 'POST':
        Stadium = request.form.get('Stadium')
        sql1 = "select owner from `stadium` where name_stadium = %s "

        val = (str(Stadium),)

        mycursor.execute(sql1, val)
        records = mycursor.fetchall()
        flash('Done!', category='success')

    return render_template("sub8.html", user=current_user, records=records)


@views.route('/9', methods=['GET', 'POST'])
def view_9():
    records = []
    Position =""
    if request.method == 'POST':
        Position = request.form.get('Position')
        sql1 = "select fName, lNAme from `player` where position = %s "
        val = (str(Position),)
        mycursor.execute(sql1, val)
        records = mycursor.fetchall()
        flash('Done!', category='success')

    return render_template("sub9.html", user=current_user, records=records, Position=Position)


@views.route('/10', methods=['GET', 'POST'])
def view_10():
    records = []
    City =""
    if request.method == 'POST':
        City = request.form.get('City')
        if len(str(City)) > 0:
            sql1 = "select owner from stadium WHERE address LIKE '%" + str(City) + "%'"
            mycursor.execute(sql1)
            records = mycursor.fetchall()
            flash('Done!', category='success')

    return render_template("sub10.html", user=current_user, records=records, City=City)
