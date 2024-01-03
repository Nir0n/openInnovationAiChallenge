from fastapi import FastAPI
import uvicorn
from repr.api.routes import router

# Albemic configs
from alembic.config import Config
from alembic import command

app = FastAPI()


def upgrade_database():
    alembic_cfg = Config("infra/databases/sql/alembic.ini")
    command.upgrade(alembic_cfg, "head")


upgrade_database()
app.include_router(router, prefix='/api')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
