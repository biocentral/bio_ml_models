from __future__ import annotations

from typing import Optional, Dict, Tuple
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from biotrainer.protocols import Protocol
from biotrainer.inference.inferencer import Inferencer

from ..utils import get_model_data_dir


@dataclass
class ModelDescription:
    name: str
    task: str
    dataset: (str, str)
    dataset_license: (str, str)
    embedder: str
    model_format: str
    authors: Dict[str, str] = field(default_factory=dict)
    references: Dict[str, str] = field(default_factory=dict)


class BioModel(ABC):
    model_file_path: str

    def __init__(self):
        self.model_file_path = str(get_model_data_dir() / self.get_model_file_path())

    @abstractmethod
    def get_model_file_path(self) -> str:
        raise NotImplementedError(f"{self.__class__.__name__} must define 'get_model_file_path' as a method!")

    def generate_model_markdown(self) -> str:
        description = self.description()
        md = f"# {description.name}\n\n"
        md += f"{description.task}\n\n"
        md += "### Summary\n"
        md += f"* **Dataset**: [{description.dataset[0]}]({description.dataset[1]})\n"
        md += f"* **Dataset License**: [{description.dataset_license[0]}]({description.dataset_license[1]})\n"
        md += f"* **Embedder**: `{description.embedder}`\n"
        md += f"* **Model Format**: {description.model_format}\n"
        if description.authors:
            md += f"* **Model Author(s):** "
            md += ",".join(f"[{author_name}]({link})" for author_name, link in description.authors.items())
            md += "\n"
        if description.references:
            md += "* **Reference(s)**: "
            md += ",".join(f"[{link_name}]({link})" for link_name, link in description.references.items())
        md += "\n"
        return md

    @abstractmethod
    def description(self) -> ModelDescription:
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_model_task(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_model_dataset(self) -> Tuple[str, str]:
        raise NotImplementedError

    @abstractmethod
    def get_model_dataset_license(self) -> Tuple[str, str]:
        raise NotImplementedError

    @abstractmethod
    def get_model_authors(self) -> Dict[str, str]:
        raise NotImplementedError

    @abstractmethod
    def get_model_references(self) -> Dict[str, str]:
        raise NotImplementedError

    @abstractmethod
    def predict(self, model_input):
        pass


class ONNXModel(BioModel, ABC):

    @abstractmethod
    def protocol(self) -> Optional[Protocol]:
        return None

    def predict(self, model_input):
        return Inferencer.from_onnx_with_embeddings(model_path=self.model_file_path, embeddings=model_input,
                                                    protocol=self.protocol())


class BiotrainerModel(BioModel, ABC):
    _inferencer: Optional[Inferencer] = None

    def description(self) -> ModelDescription:
        self._ensure_loaded()
        return ModelDescription(
            name=self.get_model_name(),
            task=self.get_model_task(),
            dataset=self.get_model_dataset(),
            dataset_license=self.get_model_dataset_license(),
            embedder=self._inferencer.embedder_name,
            model_format="[biotrainer](https://github.com/sacdallago/biotrainer)",
            authors=self.get_model_authors(),
            references=self.get_model_references()
        )

    def _ensure_loaded(self):
        if self._inferencer is None:
            self._inferencer = Inferencer.create_from_out_file(out_file_path=self.model_file_path)[0]

    def predict(self, input_data):
        self._ensure_loaded()
        prediction_dict = self._inferencer.from_embeddings(embeddings=input_data)
        return prediction_dict["mapped_predictions"]
