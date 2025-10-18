class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    def __init__(self, firstName: str, lastName: str, idNumber: int, scores: list):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    #
    # Write your constructor here
    
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        GRADING_SCALE = {'T': range(40), 'D':range(40, 55), 'P':range(55, 70),
         'A':range(70, 80), 'E': range(80, 90), 'O':range(90, 101)}
        print(GRADING_SCALE)
        avg_grade = sum(self.scores)/len(self.scores)
        for key in GRADING_SCALE:
            if round(avg_grade) in GRADING_SCALE[key]:
                return key
        
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())