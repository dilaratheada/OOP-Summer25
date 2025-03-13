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
  'courses' : ['Economy ', 'OOP', 'French', 'Psycology']
}

students = [student1,student2,student3]

for index, student in enumerate(students):
  print(f"Student{index}: {student['first_name']} - Index Number: {student['index_number']}")