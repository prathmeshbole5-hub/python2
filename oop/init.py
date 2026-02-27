#__init__() method
#is an insatnce method
# is uswed to create and intializwe the attribute during the object creation 

class student:
    """
    this is to create tudent to manage student info and activites 
    """

    def __init__(self,name,roll):
        print("calling the intializer")
        self.name = name
        self.roll = roll
    def study(self,n_hours):
        print(f"the studet studies for{n_hours}hours a day ")

    def sports(self,sports_name):
        print(f"the tudent plays {sports_name}")

student1=student("john",10001)
student2=student("carol",10022)

print(student1.name,student1.roll)
print(student2.name,student2.roll)