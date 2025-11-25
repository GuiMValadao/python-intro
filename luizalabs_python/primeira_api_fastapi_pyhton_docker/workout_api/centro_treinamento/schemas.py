from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

from workout_api.contrib.schemas import (
    BaseSchema,
)


class CentroTreinamento(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="CT King",
            max_length=20,
        ),
    ]
    nome: Annotated[
        str, Field(description="Endereço do CT", example="Rua X, Q02", max_length=60)
    ]
    nome: Annotated[
        str, Field(description="Proprietário do CT", example="Marcos", max_length=30)
    ]
