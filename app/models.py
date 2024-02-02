from typing import Optional, List
from sqlmodel import (
    SQLModel,
    Field,
    create_engine,
    select,
    Session,
    Relationship
)

# cria engine do banco
engine = create_engine('sqlite:///database.db')


# estrutura tabela no banco de dados
class Pessoa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    idade: int

    Livros: List['livro'] = Relationship(back_populates='livros')


class Livro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str

    pessoa_id: Optional[int] = Field(default=None, foreign_key='pessoa.id')
    pessoa: Optional[Pessoa] = Relationship(back_populates='livros')


# cria o banco de dados
SQLModel.metadata.create_all(engine)
