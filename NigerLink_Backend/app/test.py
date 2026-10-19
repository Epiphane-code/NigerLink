from sqlalchemy import delete

from app.database.database import SessionLocal
from app.models.palacetemporaire import PalaceTemporaire


with SessionLocal() as db:
    result = db.execute(
        delete(PalaceTemporaire)
    )

    db.commit()

    print(f"{result.rowcount} palaces supprimés.")