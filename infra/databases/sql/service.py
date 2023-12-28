from typing import Dict, List, Any
from sqlalchemy import create_engine, and_
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
        
    def filter_by(self, model: ModelInterface, criteria: Dict[str, Any]) -> List[ModelInterface]:
        """
        Filter entities based on provided criteria.

        Args:
            criteria (Dict[str, Any]): A dictionary of filter criteria.

        Returns:
            List[Any]: A list of entities that match the criteria.
            :param model: ModelInterface model that mapped to entity
        """
        try:
            entity_class = self.model_to_entity_mapping.get(model)
            if not entity_class:
                raise ValueError(f"No entity mapped for model type {type(model)}")
            query = self.session.query(entity_class)
            for field, values in criteria.items():
                if isinstance(values, dict):
                    # For range values like min and max
                    if "min" in values and "max" in values:
                        query = query.filter(and_(
                            getattr(entity_class, field) >= values["min"],
                            getattr(entity_class, field) <= values["max"]
                        ))
                    else:
                        raise ValueError("Invalid range criteria")
                else:
                    # For exact match criteria
                    query = query.filter(getattr(entity_class, field) == values)
            entities: List[EntityInterface] = query.all()
            models = []
            for entity in entities:
                model_cls = self.__get_model_class_for_entity(type(entity))
                model_instance = model_cls.from_dict(entity.to_dict())
                models.append(model_instance)
            return models
        except Exception as e:
            self.logger.error(e)
            raise e
        
    def __get_model_class_for_entity(self, entity_class: EntityInterface) -> ModelInterface:
        for model_cls, mapped_entity_cls in self.model_to_entity_mapping.items():
            if mapped_entity_cls == entity_class:
                return model_cls
        raise ValueError(f"No model mapped for entity type {entity_class}")

        
    def delete(self, entity_id):
        pass

    def get_by_id(self, entity_id):
        pass

    def get_all(self):
        pass
