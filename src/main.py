from fastapi import FastAPI
from factory.core import CreateUserCore, UpdateUserCore
import requests
import uvicorn
from factory.parameter import UserData, EmailUser
from factory.models import User

app = FastAPI()


@app.get("/")
def path_default():
    # TODO: iria retornar um json padrao do front.
    return "bem vindo!"


@app.post("/create_contact/")
async def post_create_contact(data: UserData):
    instance = CreateUserCore()

    # TODO: cria o id do user. COM O BD PRONTO, FAZER UM TRY AQUI
    id_generated = instance.create_id_to_client()

    # Cria hash da senha
    create_hash_pass = instance.encrypt_password(data.password)

    data = {
        "id": id_generated,
        "usuario": data.username,
        "senha": create_hash_pass
    }

    # TODO: feature: Aqui será enviado para o bd os dados do novo usuario do sistema. 
    # TODO: Se 201, retorna um sucess para a requisição. se não o status code do erro.
    return {"data": data}


@app.get("/address/{cep}")
def search_address_by_cep(cep: str):
    response = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
    return response.json()


@app.post("/new_password/")
def post_update_password(mail: EmailUser):
    instance = UpdateUserCore(mail.mail)
    
    new_password = instance.new_password_generator()

    if new_password == 201:
        return "Nova senha criada e enviada por e-mail."
    else:
        return "Ocorreu algum erro ao gerar uma nova senha. Tente novamente mais tarde."

@app.post("/forgot_user/")
def forgot_user(mail: EmailUser):
    instance = User(mail.mail)
    
    user = instance.get_user_by_mail()
    
    return user


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
