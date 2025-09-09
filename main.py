from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"ok": True, "msg": "CreditWise is alive"}

@app.get("/__health")
def health():
    return {"ok": True}
