import unittest

from bio_ml_models import BioModelCollection
from bio_ml_models.base import BiotrainerModel


class ProteinsTests(unittest.TestCase):

    def test_loading(self):
        collection = BioModelCollection()
        for task in collection.proteins.task_list():
            for model in task.model_list():
                if isinstance(model, BiotrainerModel):
                    model._ensure_loaded()
                    self.assertTrue(model._inferencer is not None)
