from shared.database import SessionLocal


def Gat_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.closed()