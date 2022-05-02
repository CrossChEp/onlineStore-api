import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from api_routers import user_router, auth_router, product_router, bag_router, orders_router

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:63343",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount('/api/static', StaticFiles(directory='static'), name='/api/static')
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(product_router)
app.include_router(bag_router)
app.include_router(orders_router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
