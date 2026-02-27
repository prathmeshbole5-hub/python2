

class student:
    """
    this is to create tudent to manage student info and activites 
    """

    college_name ="ABC COLLEGE"
    departments = ["arts","commerce","science"]

    def __init__(self,name,roll):
        print("calling the intializer")
        self.name = name
        self.roll = roll
    def study(self,n_hours):
        print(f"the studet studies for{n_hours}hours a day ")

    def sports(self,sports_name):
        print(f"the tudent plays {sports_name}")

student1 = student("john",1001)
help(student)

print(student1.departments)
print(student1.college_name)
print(student.departments)
print(student.college_name)
