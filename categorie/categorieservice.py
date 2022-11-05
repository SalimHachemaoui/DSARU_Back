from sqlalchemy.orm.session import Session
from models.categoriemodel import CategorieModel
from dto.categorieschema import CategorieSchema



class CategorieService:
    def getAll(db:Session):
        return db.query(CategorieModel).all()

    def create_categorie(request: CategorieSchema, db: Session):
        new_categorie = CategorieModel(
            name=request.name,
            image=request.image,
            description=request.description,

        )

        db.add(new_categorie)
        db.commit()
        db.refresh(new_categorie)

        return new_categorie

    def show_categorie(categorieid: int, db: Session):
        show_c = db.query(CategorieModel).filter(CategorieModel.id == categorieid).first()


        response = {
            "id": show_c.id,
            "name": show_c.name,
            "image": show_c.image,
            "description": show_c.description,


        }

        return response


    def update_categorie(categorieid: int, request: CategorieSchema, db: Session):
        categorie_id = db.query(CategorieModel).filter(CategorieModel.id == categorieid).first()

        categorie_id.name = request.name
        categorie_id.description = request.description
        categorie_id.image = request.image


        db.commit()

        return categorie_id

    def delete_categorie(categorieid: int, db: Session):
        del_categorie = (
            db.query(CategorieModel).filter(CategorieModel.id == categorieid).first()
        )

        db.delete(del_categorie)
        db.commit()

        return "Done"
