import uvicorn
from fastapi import FastAPI

from api_routers import user_router, auth_router, product_router, bag_router, orders_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(product_router)
app.include_router(bag_router)
app.include_router(orders_router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
