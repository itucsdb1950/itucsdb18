from flask import Flask, render_template, request, redirect, url_for
import views_more


app = Flask(__name__)


@app.route("/student/<string:stu_num>")
def student_page():
	student = views.get_student(stu_num)
	
	# name, username, id, fac_name, gpa, comp_credits
	name = student[1]
	username = student[2]
	stu_num = student[3]
	faculty = student[4]
	gpa = student[5]
	compltd_crd = student[6]
	
	return render_template("student.html", name=name, username=username, stu_num=stu_num,
	                                       faculty=faculty, gpa=gpa, compltd_crd=compltd_crd)
