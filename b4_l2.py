from datetime import datetime

class User:
    def __init__(self, name, password) :
        self.name = name
        self.password = password
    def welcome(self):
        print (f"Welcome {self.name}")
    def check_password(self, password):
        return self.password == password
    
class SubscribedUser(User):
    def __init__(self, name, password, datetime):
        super().__init__(name, password)
        self.datetime = datetime
        
    def is_expired(self):
        return datetime.now() > self.datetime
        
        
    
user = User('mindx', '12345')
user.welcome()                                
print(user.check_password('1234'))           


expiration_date = datetime(2023, 1, 1)
s_user = SubscribedUser('s_mindx', '1234', expiration_date)
s_user.welcome()                             
print(s_user.check_password('1234'))         
print(s_user.is_expired()) 