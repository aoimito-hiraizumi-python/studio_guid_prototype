from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

from flask_login import LoginManager
from flask_login import login_required

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("admin_welcome.html")

@app.route("/admin_signup")
def signup():
    return render_template("admin_signup.html")

@app.route("/admin_login")
def login():
    return render_template("admin_login.html")

@app.route("/admin_studio_pick")
def studio_pick():
    return render_template("admin_studio_pick.html")

@app.route("/admin_class")
def show_class():
    return render_template("admin_class.html")

@app.route("/admin_agency")
def show_agency():
    return render_template("admin_agency.html")

@app.route("/admin_weekly")
def show_weekly():
    return render_template("admin_weekly.html")

@app.route("/admin_index")
def index():
    return render_template("admin_index.html")

@app.route("/admin_program")
def program_register():
    return render_template("admin_program.html")
    
@app.route("/admin_ir")
def ir_register():
    return render_template("admin_ir.html")

@app.route("/admin_schedule")
def schedule_register():
    return render_template("admin_schedule.html")

@app.route("/admin_agency_register")
def agency_register():
    return render_template("admin_agency_register.html")

@app.route("/admin_weekly_register")
def weekly_register():
    return render_template("admin_weekly_register.html")
    
@app.route("/admin_mypage")
def mypage():
    return render_template("admin_mypage.html")


if __name__ == "__main__":
    app.run(debug=True,)
