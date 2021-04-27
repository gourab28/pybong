from fastapi import FastAPI
import bangla

app = FastAPI()

bangla_date = bangla.get_date()

@app.get("/")
async def root():
    return (bangla_date)
