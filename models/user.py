
class User():
    def __init__(self,username=None,grades=None):
        if username == None:
            self.username = "unknown"
        self.username = username 
        if grades == None:
            self.grades = []
        else:
            self.grades = grades

    def __str__(self):
        return f'{self.username} {self.grades}'

    def to_dict(self):
        return  {
            "username": self.username,
            "grades": self.grades
        }

    def add_grade(self,grade):
        # if (type(grade) != int or str(grade).isdigit() == False):
        #     raise ValueError
        if(type(grade) == int or str(grade).isdigit() == True ):
            if (int(grade) >= 0):
                self.grades.append(int(grade))
            else:
                raise ValueError
        else:
            raise ValueError
        

        