from sqlalchemy.orm.session import Session
from models.rolemodel import RoleModel
from dto.roleschema import RoleSchema


class Roleservice:
    def get_all_role(db: Session):
        return db.query(RoleModel).all()

    def create_role(request: RoleSchema, db: Session):
        new_role = RoleModel(
            name=request.name,


        )

        db.add(new_role)
        db.commit()
        db.refresh(new_role)

        return new_role

    def show_role(roleid: int, db: Session):
        show_s = db.query(RoleModel).filter(RoleModel.id == roleid).first()


        response = {
            "id": show_s.id,
            "name": show_s.name,
            "user":show_s.user_id,
            "created_at":show_s.created_at,
            "updated_at":show_s.updated_at,

        }

        return response


    #Roleby user
    def getRoleByUserid(userid: int, db: Session):
        role_by_userid=(db.query(RoleModel).filter(RoleModel.user_id == userid).all())
        return role_by_userid



    # Lanjutlagi
    def update_role(roleid: int, request: RoleSchema, db: Session):
        role_id = db.query(RoleModel).filter(RoleModel.id == roleid).first()

        role_id.name = request.name


        db.commit()

        return role_id

    def delete_role(roleid: int, db: Session):
        del_service = (
            db.query(RoleModel).filter(RoleModel.id == roleid).first()
        )

        db.delete(del_service)
        db.commit()

        return "Done"


