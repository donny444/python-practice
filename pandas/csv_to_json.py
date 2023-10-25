import pandas as pd;

student_marks = pd.read_csv("data/student_marks.csv");
student_marks.to_json("data/student_marks.json");
student_marks = pd.read_json("data/student_marks.json");

print(student_marks);
student_marks.info();