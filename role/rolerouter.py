from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.serviceschema import ServceSchema
from db.database import get_db

from .roleservice import Roleservice

router = APIRouter(prefix="/role", tags=["role"])

@router.get("/")
def getallRole(db:Session = Depends(get_db)):
    return Roleservice.get_all_role(db=db)

@router.post("/")
def createServce(request: ServceSchema, db: Session = Depends(get_db)):
    return Roleservice.create_role(request=request, db=db)

@router.get("/{roleid}")
def showService(roleid:int, db: Session = Depends(get_db)):
    return Roleservice.show_service(roleid=roleid, db=db)

@router.put("/{roleid}")
def updateService(roleid:int, request:ServceSchema, db: Session= Depends(get_db)):
    return Roleservice.update_service(roleid=roleid, request=request, db=db)

@router.delete("/{roleid}")
def deleteService(roleid:int, db: Session = Depends(get_db)):
    return Roleservice.delete_service(roleid=roleid, db=db)

@router.get("/rolebyuser/{userid}")
def RoleByUser(userid:int, db:Session = Depends(get_db)):
    return Roleservice.getRoleByUserid(userid=userid, db=db)

