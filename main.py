from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="")
@app.post("/get_token")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username + "token"}

@app.get("/")
async def root(token: str = Depends(oauth2_scheme)):
    return {"message": f"Hello {token.replace('token', '')}"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

if __name__ == '__main__':
    register_tortoise(
        app,
        db_url="",
        modules={"models": ["user"]},
        generate_schemas=True,
        add_exception_handlers=True,

    )