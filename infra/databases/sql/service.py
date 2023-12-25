from typing import Dict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from logging import Logger
from infra import DatabaseInterface, EntityInterface
from core.interfaces import ModelInterface


class SqlDatabaseService(DatabaseInterface):
    def __init__(self, logger: Logger, db_url, model_to_entity_mapping: Dict[ModelInterface, EntityInterface]):
        self.logger = logger
        self.engine = create_engine(db_url)
        self.SessionFactory = sessionmaker(bind=self.engine)
        self.session = scoped_session(self.SessionFactory)
        self.model_to_entity_mapping = model_to_entity_mapping

    def save(self, model: ModelInterface):
        entity_class = self.model_to_entity_mapping.get(type(model))
        if not entity_class:
            raise ValueError(f"No entity mapped for model type {type(model)}")
        entity = entity_class.from_dict(model.to_dict())
        try:
            self.session.add(entity)
            self.session.commit()
        except Exception as e:
            self.logger.error(e)
            self.session.rollback()
            raise e

    def delete(self, entity_id):
        pass

    def get_by_id(self, entity_id):
        pass

    def get_all(self):
        pass
