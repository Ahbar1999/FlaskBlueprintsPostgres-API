from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker
from .models import Post

engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()
# print(session.info) 

Faker.seed(0)
fake = Faker()

inspector = inspect(engine)
if inspector.has_table('Posts'):
    Post.__table__.drop(engine)
Post.__table__.create(engine) 

# populate db 
if not session.query(Post).all():
    faker = Faker()
    for i in range(20):
        coordinates = faker.latlng()
        session.add(Post(message=f'this is the message no.: {i}', location=f'POINT( {coordinates[0]} {coordinates[1]} )'))
        session.commit()
