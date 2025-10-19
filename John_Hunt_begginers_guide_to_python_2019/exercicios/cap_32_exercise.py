# Exercício capítulo 32- conjuntos

exam = { 'Andrew' , 'Kirsty' , 'Beth' , 'Emily' , 'Sue' }
project = { 'Kirsty' , 'Emily' , 'Ian' , 'Stuart' }

print( 'exam:' , exam)
print( 'project:' , project)

# • Which students took both the exam and submitted a project? R: Emily, Kirsty
# R = exam & project
# • Which students only took the exam? Andrew, Sue, Beth
# R = exam - project
# • Which students only submitted the project? Ian, Stuart
# R = project - exam
# • List all students who took either (or both) of the exam and the project. Emily, Sue, Andrew, Kirsty, Beth, Ian, Stuart
# R = exam | project
# • List all students who took either (but not both) of the exam and the project. R: Sue, Andrew, Beth, Ian, Stuart
# R = exam ^ project