from typing import Union, Annotated
from fastapi import FastAPI, status, Cookie, Response, Header, APIRouter
from schemas.item import ItemIn
from views import item as v

router = APIRouter(prefix="/items")
database_exemplo = [
    {"item_id": 1, "name": "maçã", "existent": True},
    {"item_id": 2, "name": "laranja", "existent": True},
    {"item_id": 3, "name": "pessego", "existent": False},
    {"item_id": 4, "name": "morango", "existent": True},
    {"item_id": 5, "name": "manga", "existent": False},
    {"item_id": 6, "name": "abacaxi", "existent": True},
]


# status_code permite definir a resposta à ação.
@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=v.ItemOut
)  # ou status_code=201
async def create_item(item: ItemIn):
    database_exemplo.append(
        item.model_dump()
    )  # model dump retorna a representação da classe item como um dicionário
    return item


# @router.get("/")
# def read_root():
#     return {"Hello": "World"}


# Queryparameters. skip: indica o primeiro valor da base de dados a ser acessado
# e limit indica o último valor.
@router.get("/", response_model=list[v.ItemOut])
def read_items(
    response: Response,
    limit: int,
    existent: bool,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    response.set_cookie(key="user", value="user@email")  # Define um cookie
    print(f"Cookie: {ads_id}")  # Lê um cookie
    print(f"User-agent: {user_agent}")
    return [
        item
        for item in database_exemplo[skip : skip + limit]
        if item["existent"] is existent
    ]
    # items = []
    # for item in database_exemplo:
    #     if len(item) == limit:
    #         break
    #     if item["existent"] is existent:
    #         items.append(item)
    # return items


# Pathparameter. Por exemplo, digitando o ip/items/3?q=alguma%consulta
# retorna o valor de retorno, como 3 em item_id e alguma consulta em q.


@router.get("/{item_id}", response_model=v.ItemOut)
def read_item(item_id: int, name: Union[str, None] = None):
    return {"item_id": item_id, "name": name}
