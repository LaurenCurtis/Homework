room = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, "CM241": 1411}
instructor =  {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', "CM241": 'Lee'}
time = {'CS101': "8:00 am", 'CS102': "9:00 am", 'CS103': "10:00 am", 'NT110': "11:00 am", "CM241": "1:00 pm"}

course_num = input('Enter in your course number:')

print('Room Number: ',room[course_num])
print('Class Instructor: ',instructor[course_num])
print('Class Time: ',time[course_num])