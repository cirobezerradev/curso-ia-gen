from pydantic import BaseModel

class Pessoa(BaseModel):
    id: int
    nome: str

p1 = Pessoa(id='123', nome='Ciro')

print(type(p1.id))
