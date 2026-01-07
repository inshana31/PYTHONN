course="""              Python is a high-level, interpreted programming language  course known for its simplicity and readability. It supports multiple programming          """
print(len(course))

print(course[:50])

print(course.replace("python","PYTHON"))
print(course.lower())

print(course.strip())
print(course)
b=course.split(",")
print(b)

a="course" in course
print(a)

f="The course description is {} characters long and has {} words.".format(course,len(course))
print(f)