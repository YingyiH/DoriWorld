from models.user import User
import json
import operator


class Score():
    def __init__(self,filename = None):
        if filename == None:
           self.filename = "user.json"
        self.filename = filename
        self.username = ""
        self._users = []
        self.load_from_json()
        
    def __str__(self):
        return f"{Score.self.username}"

    def __len__(self):
        return len(self._users)

    def load_from_json(self):
        with open(self.filename, 'r') as data:
            file = json.load(data)

        self.username =  file["name"]
        for information in file["users"]:
            self._users.append(User(information["username"], information["grades"]))
        
    def get_users(self,sorted_by=None):
        sorted_users = []
        if sorted_by == None:
            sorted_users = self._users
        else:
            if (sorted_by == "username"):
                sorted_users = sorted(self._students, key=operator.attrgetter("name"))
                # return sorted(self._students, key= lambda x:x.name)  # you should use copy the student list if you want to assign it again or return the sorted list directly
            elif (sorted_by == "grade"):
                sorted_users = sorted(self._students, key=operator.attrgetter("grade"))
                # return sorted(self._students, key= lambda x:x.gpa , reverse = True)  # you should use copy the student list if you want to assign it again or return the sorted list directly
        return sorted_users

    def to_dict(self):
        dict =  {
            "username": self.username,
            "grades": [item.to_dict() for item in self._users] # Be careful here should use []
        }
        return dict

    def save(self):
        with open(self.filename, 'w') as data:
            json.dump(self.to_dict(),data)

    def add_user(self,username,grades):
        exists = False
        if(username == ""):
            raise ValueError
        else:
            self._users.append(User(username,grades))
            
        for item in self._users:
            if (item.username != username):
                continue
            else:
                exists = True
                break

        if exists == False:
            raise TypeError
        
        return exists