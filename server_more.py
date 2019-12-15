# from flask import Blueprint, Flask, render_template, request, redirect, url_for
# import views_more
#
#
# app\
# = Blueprint('app'
# 				, __name__)
#
#
#
# @app.route("/student/<string:stu_num>")
# def student_page():
# 	student = views.get_student(stu_num)
#
# 	# name, username, id, fac_name, gpa, comp_credits
# 	name = student[1]
# 	username = student[2]
# 	faculty = student[4]
# 	gpa = student[5]
# 	compltd_crd = student[6]
#
# 	return render_template("student.html", name=name, username=username, stu_num=stu_num,
# 	                                       faculty=faculty, gpa=gpa, compltd_crd=compltd_crd)
#
#
# @app.route("/student/<string:stu_num>/courses")
# def student_courses_page():
# 	courses = views.get_courses(stu_num)
# 	return render_template("student_courses.html", courses=courses)
#
#
# @app.route("/student/<string:stu_num>/attendance")
# def student_attendance_page():
# 	courses = views.get_attendance(stu_num)
# 	return render_template("student_attendance.html", courses=courses)
#
#
# @app.route("/student/<string:stu_num>/grades")
# def student_grades_page():
# 	grades = views.get_grades(stu_num)
#
# 	# split courses list with respect to crn.
# 	# note that SQL query in views.get_grades() is written in a way that returned table is ordered by crn.
# 	# therefore, only one iteration is sufficent
# 	courses = [] # initialize list that will hold grades which are split by course
# 	crn = grades[0].crn # initilize crn with the first course's crn
# 	i = 0
# 	for grade in grades: # iterate over the entire table
# 		if grade.crn == crn: # as long as crn remains same, add rows with that crn to courses[i]
# 			courses[i].append(grade)
# 		else: # if another crn is reached
# 			crn = grade.crn # update crn to the new one
# 			i++ # so that upcoming course's grades are written to the next index of courses
#
# 	return render_template("student_grades.html", courses=courses)
