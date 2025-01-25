from fastapi import FastAPI
from view.actors import router as actors_router
from view.movies import router as movies_router


app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.include_router(actors_router, prefix="/actors", tags=["actors"])
app.include_router(movies_router, prefix="/movies", tags=["movies"])

@app.get("/")
async def root():
    return {"message": "Hello, Landing Page of Movies Rest Services"}
