from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

from luizalabs_python.primeira_api_fastapi_pyhton_docker.workout_api.contrib.schemas import (
    BaseSchema,
)


class Atleta(BaseSchema):
    nome = Annotated(
        str, Field(description="Nome do atleta", example="João", max_length=50)
    )
    cpf = Annotated(
        str, Field(description="CPF do atleta", example="1234567890", max_length=11)
    )
    idade = Annotated(int, Field(description="Idade do atleta", example="24"))
    peso = Annotated(PositiveFloat, Field(description="Peso do atleta", example=70.5))
    altura = Annotated(
        PositiveFloat, Field(description="Altura do atleta", example=1.75)
    )
    sexo = Annotated(str, Field(description="Sexo do atleta", example="M", max_lengt=1))
