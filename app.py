from flask import Flask, render_template, json, request, redirect
from collections import defaultdict
import finalcc

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route('/admissions', methods = ['POST'])
def admissions():
    gpa = request.form['gpa'].encode('ascii', 'ignore')
    act = request.form['act'].encode('ascii', 'ignore')
    sat = request.form['sat'].encode('ascii', 'ignore')
    ethnicity = request.form['ethnicity'].encode('ascii', 'ignore')
    activities = request.form['activities'].encode('ascii', 'ignore')
    volunteer = request.form['volunteer'].encode('ascii', 'ignore')
    if volunteer == "I volunteer!":
    	volunteer = 1
    else:
    	volunteer = 0

    info_dict = defaultdict(lambda:0)
    info_dict['GPA'] = gpa
    info_dict['ACT'] = act
    info_dict['SAT'] = sat
    info_dict['volunteer'] = volunteer
    info_dict[ethnicity] = 1
    info_dict['activities'] = activities
    print(info_dict)
    reject, waitlist, accept = finalcc.classifyme(info_dict)
    accept = str(round(accept * 100, 2)) + '%'
    waitlist = str(round(waitlist * 100,2)) + '%'
    reject = str(round(reject * 100,2)) + '%'
    return render_template("admissions.html", accept= accept, waitlist = waitlist, reject= reject)

if __name__ == "__main__":
	app.run()