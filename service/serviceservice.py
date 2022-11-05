from fastapi import Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from db.database import get_db
from models.servicemodel import ServiceModel
from dto.serviceschema import ServceSchema
from db.hashing import Hashing

class Serviceservice:
    def get_all_servce(db: Session):
        return db.query(ServiceModel).all()

    def create_servce(request: ServceSchema, db: Session):
        new_service = ServiceModel(
            name=request.name,
            image=request.image,
            description=request.description,

        )

        db.add(new_service)
        db.commit()
        db.refresh(new_service)

        return new_service

    def show_service(serviceid: int, db: Session):
        show_s = db.query(ServiceModel).filter(ServiceModel.id == serviceid).first()


        response = {
            "id": show_s.id,
            "name": show_s.name,
            "image": show_s.image,
            "description": show_s.description,
            "user_id":show_s.user_id,
            "created_at":show_s.created_at,
            "updated_at":show_s.updated_at,

        }

        return response
    #getserviceby user
    def getServiceByUserid(userid: int, db: Session):
        service_by_userid=(db.query(ServiceModel).filter(ServiceModel.user_id == userid).all())
        return service_by_userid

    # getservicebycategorie
    def getServiceByCategorie( categorieid: int, db: Session):
        service_by_categorieid = (db.query(ServiceModel).filter(ServiceModel.categorie_id== categorieid).all())
        return service_by_categorieid


    # Lanjutlagi
    def update_service(serviceid: int, request: ServceSchema, db: Session):
        service_id = db.query(ServiceModel).filter(ServiceModel.id == serviceid).first()

        service_id.name = request.name
        service_id.description = request.description
        service_id.image = request.image


        db.commit()

        return service_id

    def delete_service(serviceid: int, db: Session):
        del_service = (
            db.query(ServiceModel).filter(ServiceModel.id == serviceid).first()
        )

        db.delete(del_service)
        db.commit()

        return "Done"


