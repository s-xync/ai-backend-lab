from sqlalchemy import create_engine, false
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:pass@localhost:5432/ai_lab"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
