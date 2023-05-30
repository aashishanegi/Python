class student:
    def details(self):
        a=str(input("Enter your name"))
        b=str(input("Enter your class"))
        c=str(input("Enter your roll no"))
        d=int(input("Enter your age"))
        self.d=d
        return d
class register(student):
    def result(self):
        q=details()
        if(q>=18):
            print("Student has been registered for the course")
        else:
            print("Student didn't met eligibility criteria")
p=register()
p.result()
