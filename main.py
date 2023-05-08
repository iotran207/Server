from fastapi import FastAPI, File, UploadFile
from Utils.User import UserData
from pydantic import BaseModel
import random
from Utils.Org import OrgData,SheetData,DataBus
from Utils.Chatbot import ChatBot
import shutil
import os
from Utils.User import DeepFaceCheck


class User(BaseModel):
    id: int = None
    name: str =None
    password: str = None
    role: str = None
    org: str = None
    city: str = None
    birthday: str = None
    clas: str = None
    phone: int = None
    car: str = None
    price: int = None
    token: str = None

class StudenReason(BaseModel):
    org: str = None
    id: int = None
    reason: str = None
    note: str = None

class Message(BaseModel):
    content: str = None

class QR(BaseModel):
    id: int = None

class Bus(BaseModel):
    org: str = None
    bus_id: str = None
    note: str = None
    user_id: str = None

class Schedule(BaseModel):
    org: str = None
    id: int = None
    collumn : str = None

class Daily(BaseModel):
    org: str = None
    id: int = None

app = FastAPI()
userData = UserData()

@app.get("/")
async def root():
    return "api dàng riêng cho relax-project\nTác giả: Lê Trần Hoàng Lân 10 tin-THPT Chuyên Hà Tĩnh"

@app.post("/CreateUser")
async def CreateUser(user: User):
    randomID = random.randint(100000,999999)
    try:
        userData.CreateUser(randomID,user.name,user.password,user.role,user.org,user.city,user.birthday,user.clas,user.phone,user.car,user.price,user.token)
        return {"status": "success", "message": randomID}
    except Exception as error:
        if(error == "UNIQUE constraint failed: DATA_USER.ID"):
            errorCreate = "UNIQUE constraint failed: DATA_USER.ID"
            while(errorCreate == "UNIQUE constraint failed: DATA_USER.ID"):
                try:
                    randomID = random.randint(100000,999999)
                    userData.CreateUser(randomID,user.name,user.password,user.role,user.org,user.city,user.birthday,user.clas,user.phone,user.car,user.price,user.token)
                except Exception as errorCreate:
                    print(errorCreate)
        elif(error == "UNIQUE constraint failed: DATA_USER.NAME"):
            return {"status": "error", "message": "Tên tài khoản đã tồn tại"}
        else:
            print(error)
            return {"status": "error", "message": "Lỗi không xác định"}
        
@app.post("/Login")
async def GetUser(user: User):
    try:
        data=userData.GetUser(user.id,user.password)
        return {"status": "success", "message": data}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Đăng nhập thất bại"}

@app.post("/Assistant")
async def Assistant(message: Message):
    try:
        wait=1
        return {"status": "success", "message": ChatBot(message.content,wait=wait)}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Lỗi không xác định"}
    
@app.post("/ReasonStudent")
async def ReasonStudent(reason: StudenReason):
    try:
        org = OrgData(reason.org)
        org.InsertToData(reason.id,reason.reason,reason.note)
        return {"status": "success", "message": "Đã gửi yêu cầu"}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Lỗi không xác định"}
    
@app.post("/GetUserFromID")
async def GetUserFromID(user: User):
    try:
        data = userData.GetUserFromID(user.id)
        return {"status": "success", "message": data}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Lỗi không xác định"}
    
@app.post("/CheckBus") 
async def CheckBus(data:Bus):
    try:
        bus = DataBus(data.bus_id,data.org)
        return {"status": "success", "message":bus.InsertToData(data.user_id,data.note)}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Lỗi không xác định"}
    
@app.post("/DeleteUser")
async def DeleteUser(user: User):
    try:
        userData.DeleteUser(user.id)
        return {"status": "success", "message": "Đã xóa thành công"}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Lỗi không xác định"}

@app.post("/AddToken")
async def AddToken(user: User):
    try:
        userData.AddToken(user.id,user.token)
        return {"status": "success", "message": "Đã thêm token"}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Lỗi không xác định"}
    
@app.post("/GetToken")
async def GetToken(user: User):
    try:
        return {"status": "success", "message": userData.GetToken(user.id)}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Lỗi không xác định"}
    
@app.post("/Schedule")
async def Schedule(user: Schedule):
    try:
        print(user)
        sheet = SheetData(org=user.org,ID=user.id)
        sheet.InsertToData(user.collumn)
        return {"status": "success", "message": "Đã thêm điểm danh"}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Lỗi không xác định"}
    
@app.post("/Daily")
async def Daily(user:Daily):
    try:
        sheetdata = SheetData(org=user.org,ID=user.id)
        sheetdata.Daily()
        return {"status": "success", "message": "Đã thêm điểm danh"}
    except Exception as error:
        return {"status": "error", "message": "Lỗi không xác định"}

@app.post("/CheckImage")
async def CheckImage(file_upload: UploadFile = File(),org:str=None):
    try:
        shutil.copyfileobj(file_upload.file, open(f"Temp/{file_upload.filename}", 'wb'))
        face = DeepFaceCheck(org)
        check = face.CheckFace(f"{file_upload.filename}")
        return {"status": "success", "message": check}
    except Exception as error:
        print(error)
        return {"status": "error", "message": "Lỗi không xác định"}