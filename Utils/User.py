import sqlite3
import os
from deepface import DeepFace
import random
import shutil

class UserData:
    def __init__(self):
        self.db = sqlite3.connect("database.sqlite")
        self.database = self.db.cursor()

    def CreateUser(self,id,name,password,role,org,city,birthday,clas,phone,car,price,token):
        self.database.execute("INSERT INTO DATA_USER VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (id,name,password,role,org,city,birthday,clas,phone,car,price,token))
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
                "class":data[7],
                "phone":data[8],
                "car":data[9],
                "price":data[10]
            }        
        
    def GetUserFromID(self,id):
        self.database.execute("SELECT * FROM DATA_USER WHERE user_id = ?", (id,))
        data=self.database.fetchone()
        if(data == None):
            raise Exception("Không tìm thấy tài khoản")
        else:
            return{
                "id":data[0],
                "name":data[1],
                "role":data[3],
                "org":data[4],
                "city":data[5],
                "birthday":data[6],
                "class":data[7],
                "phone":data[8],
                "car":data[9]
            }
    
    def DeleteUser(self,id):
        self.database.execute("DELETE FROM DATA_USER WHERE user_id = ?", (id,))
        self.db.commit()

    def AddToken(self,id,token):
        self.database.execute("UPDATE DATA_USER SET token = ? WHERE user_id = ?", (token,id))
        self.db.commit()
    
    def GetToken(self,id):
        self.database.execute("SELECT token FROM DATA_USER WHERE user_id = ?", (id,))
        data=self.database.fetchone()
        if(data == None):
            raise Exception("Không tìm thấy tài khoản")
        else:
            return data[0]
    
    def ChangePassword(self,id,oldpassword:str,newpassword:str):
        try:
            self.database.execute("UPDATE DATA_USER SET user_password = ? WHERE user_id = ? AND user_password = ?", (newpassword,id,oldpassword))
            self.db.commit()
        except Exception as error:
            raise Exception(error)
        
    def DeleteRole(self,id:int,role:str):
        try:
            data_role = self.GetUserFromID(id)["role"]
            list_role = data_role.split(" ")
            if(role not in list_role):
                return "Không tồn tại role"
            else:
                list_role.remove(role)
                data_role_replace = "".join(list_role)
                self.database.execute("UPDATE DATA_USER SET user_role = ? WHERE user_id = ?", (data_role_replace,id))
                self.db.commit()
                return "Đã xóa role thành công"
        except Exception as error:
            raise Exception(error)
    
    def AddRole(self,id:int,role:str):
        try:
            data_role = self.GetUserFromID(id)["role"]
            list_role = data_role.split(" ")
            if(role in list_role):
                return "Role đã tồn tại"
            else:
                list_role.append(" "+role)
                data_role_replace = "".join(list_role)
                self.database.execute("UPDATE DATA_USER SET user_role = ? WHERE user_id = ?", (data_role_replace,id))
                self.db.commit()
                return "Đã thêm role thành công"
        except Exception as error:
            raise Exception(error)
        
class DeepFaceCheck:
    def __init__(self,org):
        self.org = org

    def AddImage(self,img_name:str,id):
        try:
            DeepFace.detectFace(f"Temp/{img_name}")
            shutil.move(f"{img_name}",f"Dataset/{self.org}/{id}/{random.randint(1,999)}.png")
        except:
            raise Exception("Không tìm thấy khuôn mặt")

    def CheckFace(self,img_name:str):
        for id in os.listdir(f"Dataset/{self.org}"):
            for img in os.listdir(f"Dataset/{self.org}/{id}"):
                try:
                    result = DeepFace.verify(f"Dataset/{self.org}/{id}/{img}",f"Temp/{img_name}")
                    print(result)
                    if(result["verified"] == True):
                        return id
                except:
                    pass
        return None



    