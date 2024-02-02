import strawberry
from typing import Optional
from strawberry.fastapi import GraphQLRouter


def create_app(idade: int, nome: str):
    person = Person(nome=nome, idade=idade)

    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)

    return person


""""""


@strawberry.type
class Pessoa:
    id: Optional[int]
    nome: str
    idade: int


""""""


@strawberry.type
class Query:

    @strawberry.field
    def all_pessoa(self) -> list[Pessoa]:
        query = select(Person)
        with Session(engine) as session:
            result = session.execute(query).scalars().all()
        return result


@strawberry.type
class Mutation:
    create_pessoa: Pessoa = strawberry.field(resolver=create_app)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)

graphql_app = GraphQLRouter(schema)
