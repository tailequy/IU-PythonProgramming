class People:
    def __init__(self, name, dob, nationality):
        self.name = name
        self.dob = dob
        self.nationality = nationality
    def show_info(self):
        print(f"Hi, my name is {self.name}. I was born on {self.dob} in {self.nationality}.")
class Student(People):
    def __init__(self,name, dob, nationality,major, university):
        super().__init__(name, dob, nationality)
        self.major = major
        self.university = university
    def show_info(self):
        super().show_info()
        #People.show_info(self)
        print(f"I am studying at {self.university}, and my major is {self.major}")

student1= Student("Alice","13.10.2000","German","AI","IU")
student1.show_info()
