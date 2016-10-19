from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    # raise Exception('pause here, please')

    
    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    # grades = request.args.get('github')
    grades = hackbright.get_grades_by_github(github)

    student_info = render_template('student_info.html', 
                                    first=first, last=last, github=github, 
                                    grades=grades)

    return student_info
    # return "%s is the GitHub account for %s %s" % (github, first, last)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/new-student", methods=['POST'])
def student_add():
    """Add a student."""
    new_student = request.form.get('new_student')

    print new_student

    # flash('The new student was successfully added!')

    return render_template('new_student.html')

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
