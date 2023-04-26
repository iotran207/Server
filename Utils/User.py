import sqlite3

class UserData:
    def __init__(self):
        self.db = sqlite3.connect("database.sqlite")
        self.database = self.db.cursor()

    def CreateUser(self,id,name,password,role,org,city,birthday,clas):
        self.database.execute("INSERT INTO DATA_USER VALUES (?,?,?,?,?,?,?,?)", (id,name,password,role,org,city,birthday,clas))
        self.db.commit()

    def GetUser(self,id,password):
        self.database.execute("SELECT * FROM DATA_USER WHERE user_id = ? AND user_password = ?", (id,password))
        data=self.database.fetchone()
        if(data == None):
            raise Exception("Không tìm thấy tài khoản")
        else:
            return{
                "id":data[0],
                "name":data[1],
                "password":data[2],
                "role":data[3],
                "org":data[4],
                "city":data[5],
                "birthday":data[6],
                "class":data[7]
            }

    