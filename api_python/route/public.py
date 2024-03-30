from datetime import datetime
from fastapi import APIRouter, Body, Header
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from db import Database
import funcoes as fn
import json
from models.person import GetPerson, SetPerson
from models.phone import GetPhone, SetPhone


class Public():
    def __init__(self) -> None:

        self.dictErrorResponse = {
            200: {"mensagem": "Sucesso!"},
            400: {"mensagem": "Erro na requisição!"},
            401: {"mensagem": "Não autorizado!"},
            403: {"mensagem": "Não autenticado!"},
            404: {"mensagem": "Não encontrado!"}
        }

        self.person_router = APIRouter(prefix='/public', tags=['Person'])

        self.person_router.add_api_route('/person',
                                         self.get_person,
                                         methods=['GET'],
                                         response_model=GetPerson,
                                         responses=self.dictErrorResponse)
        
        self.person_router.add_api_route('/person',
                                         self.post_person,
                                         methods=['POST'],
                                         response_model=SetPerson,
                                         responses=self.dictErrorResponse)
        
        self.person_router.add_api_route('/person',
                                         self.update_person,
                                         methods=['PUT'],
                                         responses=self.dictErrorResponse)
        
        self.person_router.add_api_route('/person',
                                         self.delete_person,
                                         methods=['DELETE'],
                                         responses=self.dictErrorResponse)
        
    async def get_person(self):
        pass

    async def post_person(self):
        pass

    async def update_person(self):
        pass

    async def delete_person(self):
        pass