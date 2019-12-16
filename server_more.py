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
@app.route("/food_menu")
def food_menus_page():
	foods = views.get_food_menus()

	# split foods list with respect to day.
	# note that SQL query in views.get_food_menus() is written in a way that returned table is ordered by day.
	# therefore, only one iteration is sufficent
	food_menus = [] # initialize list that will hold food menu which are split with respect to day
	day = foods[0].day # initilize day with the day of the first food
	i = 0 # start day from 0
	for food in foods: # iterate over the entire table
		if food.day == day: # as long as day remains same, add rows with that day to food_menus[i]
			# TODO: map table so food elements have the order soup, main, side, extra
			if food.repast == "lunch":
				food_menus[i][0].append(food) # food_menus[0] which corresponds to lunch
			else: #dinner
				food_menus[i][1].append(food) # food_menus[1] which corresponds to dinner
		else: # if another day is reached
			day = food.day # update day to the new one
			i += 1 # so that upcoming course's grades are written to the next index of courses
	
	return render_template("student_grades.html", menus=food_menus)
