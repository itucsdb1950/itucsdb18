@app.route("/student/<int:stu_num>")
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
