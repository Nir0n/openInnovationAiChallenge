import uuid
from abc import ABCMeta

import numpy as np
from sqlalchemy import Column, Float, Integer, ARRAY, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from infra.interfaces.entity_interface import EntityInterface

Base = declarative_base()


class CombinedMeta(ABCMeta, DeclarativeMeta):
    pass


class Image(Base, EntityInterface, metaclass=CombinedMeta):
    __tablename__ = 'images'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    depth = Column(Float, nullable=False)
    image = Column(ARRAY(Integer), nullable=False)

    __table_args__ = (
        Index('index_depth', 'depth'),
    )

    @classmethod
    def from_dict(cls, data: dict) -> EntityInterface:
        if 'depth' in data and 'image' in data and isinstance(data['image'], np.ndarray):
            return cls(depth=float(data['depth']), image=data['image'].astype(int).tolist())
        else:
            raise ValueError("Required data missing for image entity creation")

    def to_dict(self) -> dict:
        return {'depth': self.depth, 'image': self.image}
