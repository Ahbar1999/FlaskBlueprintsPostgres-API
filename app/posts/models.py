from sqlalchemy import Column, String, Integer, DateTime 
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
import arrow
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Post(Base):
    __tablename__ = 'Posts'
    id = Column(Integer(), primary_key=True)
    message = Column(String(100), nullable=False)
    location = Column(Geometry('POINT'), nullable=False, unique=True)
    created = Column(DateTime, default=datetime.utcnow()) 
    def serialize(self):
        # print(self.id, self.message, to_shape(self.location).wkt)
        return { 
                'id': self.id, 
                'message': self.message, 
                'location': to_shape(self.location).wkt,
                'created': arrow.get(self.created).humanize()
                }
