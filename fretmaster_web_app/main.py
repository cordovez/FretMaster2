from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from config import Settings
from routes import router

settings = Settings()


def get_app() -> FastAPI:
    """Create a FastAPI app with the specified settings."""

    app = FastAPI(**settings.fastapi_kwargs)

    app.include_router(router)
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app


app = get_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
