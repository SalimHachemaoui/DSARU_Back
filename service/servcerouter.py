from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.serviceschema import ServceSchema
from db.database import get_db

from .serviceservice import Serviceservice

router = APIRouter(prefix="/service", tags=["service"])

@router.get("/")
def getallService(db:Session = Depends(get_db)):
    return Serviceservice.get_all_servce(db=db)

@router.post("/")
def createServce(request: ServceSchema, db: Session = Depends(get_db)):
    return Serviceservice.create_servce(request=request, db=db)

@router.get("/{serviceid}")
def showService(serviceid:int, db: Session = Depends(get_db)):
    return Serviceservice.show_service(serviceid=serviceid, db=db)

@router.put("/{serviceid}")
def updateService(serviceid:int, request:ServceSchema, db: Session= Depends(get_db)):
    return Serviceservice.update_service(serviceid=serviceid, request=request, db=db)

@router.delete("/{serviceid}")
def deleteService(serviceid:int, db: Session = Depends(get_db)):
    return Serviceservice.delete_service(serviceid=serviceid, db=db)

@router.get("/servicebyuser/{userid}")
def serviceByUser(userid:int, db:Session = Depends(get_db)):
    return Serviceservice.getServiceByUserid(userid=userid, db=db)


@router.get("/servicebyCategorie/{categorieid}")
def serviceByCategorie(categorieid:int, db:Session = Depends(get_db)):
    return Serviceservice.getServiceByCategorie(categorieid=categorieid, db=db)