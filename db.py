from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://testdb:ouganda77@localhost:5432/testdb')  # Локальный сервер
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

try:
    conn = engine.connect()
    print("Успешное подключение к базе данных!")
    conn.close()
except Exception as e:
    print(f"Ошибка подключения: {e}")