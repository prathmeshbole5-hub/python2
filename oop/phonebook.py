class phonebook:
    phone_directory =[]

    def __init__(self,name,phone_number):
        self.name =name
        self.phone=phone_number
        phonebook.phone_directory.append(self)


    def show_contact(self):
        return f"name:{self.name},contact number:{self.phone}"
    
    @classmethod
    def show_all_contact(cls):
        if len(cls.phone_directory)==0:
            print("no contact found in directory ")
        else :
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, searchname):
        for contact in cls.phone_directory:
            if contact.name.lower() == searchname.lower():
                return contact.phone
        return None

c1 = phonebook("john", 987687686)
c2 = phonebook("alice", 99797868)
c3 = phonebook("carol",999959498)
# print(phonebook.phone_directory)

# print(c1.show_contact())

# print(c1.show_all_contact())

# contact show all conatct
print(phonebook.search_contact("john"))
print(phonebook.search_contact("mark"))