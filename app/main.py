from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from .database import engine
from . import models
from .routes import auth, tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register routers
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Task Manager API!"}


# Custom OpenAPI schema with auth
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Task Manager API",
        version="1.0.0",
        description="Manage your tasks with FastAPI and JWT authentication",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            if "security" not in openapi_schema["paths"][path][method]:
                openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
