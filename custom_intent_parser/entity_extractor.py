from abc import ABCMeta, abstractmethod, abstractproperty


class EntityExtractor(object):
    __metaclass__ = ABCMeta

    _entities = []

    @abstractproperty
    def entities(self):
        pass

    @abstractproperty
    def fitted(self):
        pass

    def check_fitted(self):
        if not self.fitted:
            raise ValueError("EntityExtractor must be fitted before "
                             "calling the 'fit' method.")

    @entities.setter
    def entities(self, value):
        self._entities = value

    @abstractmethod
    def fit(self, queries):
        pass

    @abstractmethod
    def get_entities(self, text):
        pass

    @classmethod
    @abstractmethod
    def from_dataset(cls, dataset):
        pass
