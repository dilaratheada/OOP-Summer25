student1 = {
  'first_name' : 'Ada',
  'last_name' : 'Ozgurel',
  'index_number' : '35465',
  'nationality' : 'Turkish',
  'starting_date' : '13-03-2025',
  'courses' : ['Math2', 'OOP', 'Polish', 'Logistics']
}

student2 = {
  'first_name' : 'Berk',
  'last_name' : 'Saritas',
  'index_number' : '35236',
  'nationality' : 'Turkish',
  'starting_date' : '13-03-2025',
  'courses' : ['Math1', 'OOP', 'English', 'Logistics']
}

student3 = {
  'first_name' : 'Eylul',
  'last_name' : 'Kilagoz',
  'index_number' : '35536',
  'nationality' : 'Turkish',
  'starting_date' : '13-03-2025',
  'courses' : ['Math ', 'OOP', 'English', 'Logistics']
}

students = [student1,student2,student3]

def add_student(first_name, last_name, index_number, nationality, starting_date, courses):
  new_student = {
    'first_name' : first_name,
    'last_name' : last_name,
    'index_number' : index_number,
    'nationality' : nationality,
    'staring_date' : starting_date,
    'courses' : courses
  }

  students.append(new_student)
  print(f"Student {first_name} {last_name} added to the students.")

for index, student in enumerate(students):
  print(f"Student{index}: {student['first_name']} - Index Number: {student['index_number']}")
