# Start configuration

import sys

from sqlalchemy import Table, Column, ForeignKey, Integer, String, Numeric, Date

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


parents_puppies_association_table = Table('association', Base.metadata, 
    Column('puppy_id', Integer, ForeignKey('puppy.id')),
    Column('parent_id', Integer, ForeignKey('parent.id'))
    )


class Shelter (Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    address = Column(String(250))
    city = Column(String(80))
    state = Column(String(20))
    zipCode = Column(String(10))
    website = Column(String)


class Puppy (Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(6), nullable = False)
    dateOfBirth = Column(Date)
    picture = Column(String)
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    weight = Column(Numeric(10))
    profile = relationship("Profile", uselist=False, back_populates=('puppy'))
    # parents = relationship("Parent", secondary=parents_puppies_association_table, back_populates="puppies")
    parents = relationship("Parent", secondary=parents_puppies_association_table, back_populates="puppy")



class Profile (Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    puppy_id = (Integer, ForeignKey('puppy.id'))
    description = Column(String(250), nullable=False)
    special_needs = Column(String(500))
    puppy = relationship("Puppy", back_populates=('profile'))



class Parent (Base):
    __tablename__ = "parent"
    id = Column(Integer,  primary_key=True)
    firstName = Column(String(250))
    surname = Column(String(250))
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zipCode = Column(String)
    # puppies = relationship("Puppy", secondary=parents_puppies_association_table, back_populates="parents")
    puppies = relationship("Puppy", secondary=parents_puppies_association_table, back_populates="parent")






engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)