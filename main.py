from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()

class AccessToken(BaseModel):
    token: str

SECRET_TOKEN = "secret_token"

def verify_token(token: AccessToken = Depends()):
    if token.token != SECRET_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid access token")
    return token

@app.post("/test")
def get_private_data(token: AccessToken = Depends(verify_token)):
    return {"message": "Access token Verified"}
