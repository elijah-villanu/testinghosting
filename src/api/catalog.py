from fastapi import APIRouter
import sqlalchemy
from src import database as db

router = APIRouter()

with db.engine.begin() as connection:
    result = connection.execute(sqlalchemy.text("SELECT quantity, resource_name FROM inventory"))
    print(result.fetchall())


@router.get("/catalog/", tags=["catalog"])
def get_catalog():
    """
    Each unique item combination must have only a single price.
    """

    return [
            {
                "Stuff": 5
            }
        ]

