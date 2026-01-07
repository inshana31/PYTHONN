python={"haleema","ashik","nihal"}
data_science={"inshu","abu","nihal"}
python.add("kavya")
print(python)
data_science.remove("abu")
print(data_science)
both=python&data_science
print(both)
print(python - data_science)
print(python|data_science)
course= {
      "python": len(python),
      "data_science":len(data_science)
}
print(course)

for x ,count  in course.items():
   print(f"course:{course}")
   break

growth_dict = {course: count * 2 for course, count in course.items()}
print("Expected growth:", growth_dict)
