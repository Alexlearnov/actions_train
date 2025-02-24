from sqlalchemy import text, create_engine, ForeignKey, Table, Column, Integer, String, MetaData, insert, select
from sqlalchemy.orm import Session, declarative_base



engine = create_engine(url="sqlite+pysqlite:///:memory:", echo=True)


metadata = MetaData()


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # имя таблицы

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    
    
    

buyers_table = Table(
    "buyers",  # Имя таблицы
    metadata,  # Объект метаданных
    Column("id", Integer, primary_key=True),  # Первичный ключ'
    Column("surname", String, nullable=False),  # Внешний ключ
    Column("name", String, nullable=False),  # Столбец с ограничением NOT NULL
)


with engine.connect() as connection:
    metadata.create_all(bind=engine)
    Base.metadata.create_all(engine)
    
    values = [{"name": 1, "surname": 2}, {"name": 3, "surname": 4}, {"name": 1, "surname": 2}]
    values_user = [{"name": 1, "email": "2"}, {"name": 3, "email": "4"}, {"name": 1, "email": "3"}]
    
    for val in values:
        connection.execute(
            insert(buyers_table).values(val),
        )
    
    for val in values_user:
        connection.execute(
            insert(User).values(val),
        )

    connection.commit()


stmt = select(User) #.where(User.email == "ksjdfhgjksdfhgjk")

with Session(engine) as session:
    scalars_result = session.execute(stmt)
    if scalars_result:
        for row in scalars_result:
            print(row)



