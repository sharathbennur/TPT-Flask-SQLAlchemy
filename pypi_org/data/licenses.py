import datetime
import sqlalchemy
from pypi_org.data.modelbase import SqlAlchemyBase
import uuid


class License(SqlAlchemyBase):
    __tablename__ = 'licenses'

    id = sqlalchemy.Column(sqlalchemy.String,
                           default=lambda: str(uuid.uuid4()).replace('-', ''),
                           primary_key=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now,
                                     index=True)
    description = sqlalchemy.Column(sqlalchemy.String)
