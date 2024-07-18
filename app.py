from flask import Flask, render_template, session, redirect, url_for, g, request
from forms import registrationform, loginform, bookingform, adminloginform,reviewform
from random import randint
from flask_session import Session
from database import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

#admin username=admin and password=1234

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "eamons-super-secret-key"
Session(app)
app.teardown_appcontext(close_db)


@app.before_request
def logged_in_user():
    g.user = session.get("userid", None)


def loginrequired(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return view(*args, **kwargs)

    return wrapped_view


@app.route("/")
def index():
    db = get_db()
    haircuts = db.execute("""SELECT * FROM haircuts;""").fetchall()
    return render_template("index.html", haircuts=haircuts)


@app.route("/haircuts")
def haircuts():
    db = get_db()
    haircuts = db.execute("""SELECT * FROM haircuts;""").fetchall()
    return render_template("index.html", haircuts=haircuts)


@app.route("/haircut/<int:haircutid>")
def haircut(haircutid):
    db = get_db()
    haircut = db.execute(
        """SELECT * FROM haircuts 
    WHERE haircutid=?;""",
        (haircutid,),
    ).fetchone()
    return render_template("haircut.html", haircut=haircut)


@app.route("/booking/<int:haircutid>", methods=["GET", "POST"])
@loginrequired
def booking(haircutid):
    form = bookingform()
    db = get_db()
    haircut = db.execute(
        """SELECT * FROM haircuts WHERE haircutid=?;""", (haircutid,)
    ).fetchone()
    userid = g.user
    form.userid.data = g.user
    if form.validate_on_submit():
        apptdate = form.apptdate.data
        appttime = form.appttime.data
        apptdate = str(apptdate)
        appttime = str(appttime)

        name = haircut["name"]
        price = haircut["price"]
        db.execute(
            """INSERT INTO appointments (userid,apptdate,appttime,haircutname,price) VALUES (?,?,?,?,?);""",
            (userid, apptdate, appttime, name, price),
        )
        db.commit()
        appt = db.execute(
            """SELECT * FROM appointments WHERE userid=? ORDER BY apptid DESC;""",
            (userid,),
        ).fetchone()
        apptid=int(appt['apptid'])

        # appointments= db.execute("""SELECT * FROM appointments""")
        return redirect(url_for('yourappt', apptid=apptid))
    return render_template("booking.html", haircut=haircut, form=form)


@app.route("/yourappt/<int:apptid>",methods=['GET','POST'])
def yourappt(apptid):
    db = get_db()
    form=reviewform()
    userid=g.user
    appt = db.execute("""SELECT * FROM appointments WHERE apptid=?;""",(apptid,)).fetchone()
    print(4)
    if form.validate_on_submit():
        print(5)
        review=form.review.data
        review=str(review)
        db.execute('''INSERT INTO reviews (userid,review) VALUES (?,?);''',(userid,review),)
        db.commit()
        return redirect(url_for('yourappt', apptid=apptid, form=form))
    return render_template("yourappt.html", appt=appt, form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = registrationform()
    if form.validate_on_submit():
        userid = form.userid.data
        password1 = form.password1.data
        password2 = form.password2.data
        db = get_db()
        clashinguser = db.execute(
            """SELECT * FROM users WHERE userid = ?;""", (userid,)
        ).fetchone()
        if clashinguser is not None:
            form.userid.errors.append("Username already taken!")
        else:
            db.execute("""INSERT INTO users (userid,password) VALUES (?,?);""",(userid, generate_password_hash(password1)),)
            db.commit()
            return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginform()
    if form.validate_on_submit():
        userid = form.userid.data
        password = form.password.data
        db = get_db()
        clashinguser = db.execute(
            """SELECT * FROM users WHERE userid = ?;""", (userid,)
        ).fetchone()
        if clashinguser is None:
            form.userid.errors.append("User doesn't exist")
        elif not check_password_hash(clashinguser["password"], password):
            form.password.errors.append("Wrong password, try again!")
        else:
            session.clear()
            session["userid"] = userid
            nextpage = request.args.get("next")
            if not nextpage:
                return redirect("haircuts")
            return redirect(nextpage)
    return render_template("login.html", form=form)

@app.route('/adminlogin', methods=['GET','POST'])
def adminlogin():
    form = adminloginform()
    if form.validate_on_submit():
        userid = form.userid.data
        password = form.password.data
        if userid=='admin' and password=='1234':
            g.user='admin'
            session.clear()
            session["userid"] = userid
            return redirect(url_for('admin'))
        else:
            form.password.errors.append('Wrong username or password, try again (hint user=admin, password=1234)')
    return render_template("adminlogin.html", form=form)


@app.route('/admin')
def admin():
    db = get_db()
    appointments = db.execute('''SELECT * FROM appointments;''').fetchall()
    reviews = db.execute('''SELECT * FROM reviews''' ).fetchall()
    
    return render_template('admin.html',appointments=appointments, reviews=reviews)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("haircuts"))
