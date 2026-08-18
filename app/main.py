from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "devops-demo"}

@app.get("/health")
def health_check():
    return {"status": "ok"}