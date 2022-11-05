from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dto.categorieschema import CategorieSchema
from db.database import get_db
from .categorieservice import CategorieService


router = APIRouter(prefix="/categorie", tags=["categorie"])



@router.get("/")
def getallCategorie(db:Session = Depends(get_db)):
    return CategorieService.getAll()(db=db)

@router.post("/")
def createServce(request: CategorieSchema, db: Session = Depends(get_db)):
    return CategorieService.create_categorie(request=request, db=db)


@router.get("/{categorieid}")
def showCategorie(categorieid:int, db: Session = Depends(get_db)):
    return CategorieService.show_categorie(categorieid=categorieid, db=db)

@router.put("/{categorieid}")
def updateCategorie(categorieid:int, request:CategorieSchema, db: Session= Depends(get_db)):
    return CategorieService.update_categorie(categorieid=categorieid, request=request, db=db)

@router.delete("/{categorieid}")
def deleteCategorie(categorieid:int, db: Session = Depends(get_db)):
    return CategorieService.delete_categorie(categorieid=categorieid, db=db)