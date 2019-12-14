from flask import Blueprint, Flask, render_template, request, redirect, url_for
import views_more


site = Blueprint('site', __name__)


@site.route("/student/<string:stu_num>")
def student_page():
	student = views.get_student(stu_num)
	
	# name, username, id, fac_name, gpa, comp_credits
	name = student[1]
	username = student[2]
	faculty = student[4]
	gpa = student[5]
	compltd_crd = student[6]
	
	return render_template("student.html", name=name, username=username, stu_num=stu_num,
	                                       faculty=faculty, gpa=gpa, compltd_crd=compltd_crd)


@site.route("/student/<string:stu_num>/courses")
def student_courses_page():
	courses = views.get_courses(stu_num)
	return render_template("student_courses.html", courses=courses)
