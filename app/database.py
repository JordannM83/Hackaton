from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# RÈGLE: PostgreSQL OBLIGATOIRE - SQLite INTERDIT
# Configuration PostgreSQL par défaut, peut être overridée par .env
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://holbies_user:holbies_password@localhost:5432/holbies_db")

# Validation: Vérifier que l'URL est bien PostgreSQL
if not DATABASE_URL.startswith("postgresql://"):
    raise ValueError("❌ ERREUR: Seul PostgreSQL est autorisé. SQLite est interdit dans ce projet.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
