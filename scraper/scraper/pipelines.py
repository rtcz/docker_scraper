import os
from typing import Optional

import scrapy
import sqlalchemy as db
from scrapy import Spider
from sqlalchemy import Integer, String, BigInteger
from sqlalchemy.orm import DeclarativeBase, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Apartment(Base):
    __tablename__ = "apartments"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(255), nullable=False)
    locality = mapped_column(String(255))
    price = mapped_column(BigInteger)
    image_url = mapped_column(String(255))


class PostgresPipeline:

    def __init__(self, db_uri: str):
        self._db_uri = db_uri
        self._session = None  # type: Optional[Session]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(db_uri=os.environ.get('DB_URI'))

    def open_spider(self, spider: Spider):
        # create DB connection
        engine = db.create_engine(self._db_uri)
        self._session = Session(engine)

        # start with fresh table
        Apartment.__table__.drop(engine, checkfirst=True)
        Apartment.__table__.create(engine)

    def close_spider(self, spider: Spider):
        self._session.commit()
        self._session.close()

    def process_item(self, item, spider: Spider) -> scrapy.Item:
        self._session.add(Apartment(**item))
        return item
