from fastapi import FastAPI
from Utils.User import UserData
from pydantic import BaseModel
import requests
import uvicorn
import random
from Utils.Org import OrgData,SheetData,DataBus

class User(BaseModel):
    id: int = None
    name: str =None
    password: str = None
    role: str = None
    org: str = None
    city: str = None
    birthday: str = None
    clas: str = None

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

app = FastAPI()
userData = UserData()

@app.get("/")
async def root():
    return "api dàng riêng cho relax-project\nTác giả: Lê Trần Hoàng Lân 10 tin-THPT Chuyên Hà Tĩnh"

@app.post("/CreateUser")
async def CreateUser(user: User):
    randomID = random.randint(100000,999999)
    try:
        userData.CreateUser(randomID,user.name,user.password,user.role,user.org,user.city,user.birthday,user.clas)
        return {"status": "success", "message": randomID}
    except Exception as error:
        if(error == "UNIQUE constraint failed: DATA_USER.ID"):
            errorCreate = "UNIQUE constraint failed: DATA_USER.ID"
            while(errorCreate == "UNIQUE constraint failed: DATA_USER.ID"):
                try:
                    randomID = random.randint(100000,999999)
                    userData.CreateUser(randomID,user.name,user.password,user.role,user.org,user.city,user.birthday,user.clas)
                except Exception as errorCreate:
                    print(errorCreate)
        elif(error == "UNIQUE constraint failed: DATA_USER.NAME"):
            return {"status": "error", "message": "Tên tài khoản đã tồn tại"}
        else:
            print(error)
            return {"status": "error", "message": "Lỗi không xác định"}
        
@app.post("/GetUser")
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
        r = requests.post("https://api.simsimi.vn/v1/simtalk", headers = {"Content-Type": "application/x-www-form-urlencoded"}, data = {"text": f"{message.content}", "lc": "vn"})
        return {"status": "success", "message": r.json()["message"]}
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
    
@app.post("/GetDataFromQR")
async def GetDataFromQR(data:QR):
    try:
        user = UserData()
        return {"status": "success", "message":user.GetUserFromQR(data.id)}
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
    


