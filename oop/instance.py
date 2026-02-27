# define inside a class whioch is bound to associated with the inatance /objectf 


class student:
    """
    thsi is a class tudent to manage the info a nd c ertifiavte 
    """


    def study(self,n_hours ):
        print(f"self is:{self}")
        print(f"the student study {n_hours}hours a day")

student1=student()
print(f"the object:{student1}")
student1.study(3)

student2 =student()
print(f"the object: {student2}")
student2.study(2)





"""
when we call an instance method using the object of the class python passes object itsel """

"""when we call an instance method using the object /instance of the class ,python pass the object itself as the first argument to that method that first argument is by standard itself """