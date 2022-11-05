from pydantic import BaseModel



class ServceSchema(BaseModel):
    name: str
    image: str
    description: str
