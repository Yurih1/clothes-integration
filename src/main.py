from fastapi import FastAPI
from contact_handlers.handlers import CreateUserHandlers, UpdateUserHandlers
from contact_handlers.parameter_contact import *
import requests
import uvicorn
import os

app = FastAPI()


@app.get("/")
def path_default():
    # TODO: iria retornar um json padrao do front.
    return "bem vindo!"


@app.post("/create_contact/")
async def post_create_contact(data: UserData):
    instance = CreateUserHandlers(data.username)

    created_contact = instance.create_contact(data)

    return created_contact

@app.post("/update_contact")
def post_update_contact(data: FullDataUser):
    user_data = UpdateUserHandlers(data.email)
    
    result = user_data.update_full_data_contact(data)

    return result

@app.get("/address/{cep}")
def search_address_by_cep(cep: str):
    response = requests.get(os.environ["VIACEP"] + f"{cep}" + "/json/")
    return response.json()


@app.post("/new_password")
def post_update_password(email: EmailUser):
    instance = UpdateUserHandlers(email.email)
    
    new_password = instance.new_password_generator()

    if new_password == 201:
        return "Nova senha criada e enviada por e-mail."
    else:
        return "Ocorreu algum erro ao gerar uma nova senha. Tente novamente mais tarde."


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
