from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from biotrainer.protocols import Protocol
from typing import Dict, Optional, NamedTuple, List

from .bio_model import BioModel


@dataclass
class TaskDescription:
    name: str
    explanation: str
    protocol: Optional[Protocol] = None
    references: Dict[str, str] = field(default_factory=dict)


class BioTask(ABC):
    def description(self) -> TaskDescription:
        return TaskDescription(name=self.get_task_name(),
                               explanation=self.get_task_explanation(),
                               protocol=self.get_task_protocol(),
                               references=self.get_task_references())

    def generate_task_markdown(self) -> str:
        description = self.description()
        md = f"# {description.name}\n\n"
        md += f"{description.explanation}\n\n"
        md += "### Summary\n"
        if description.protocol is not None:
            md += f"* **Type (Biotrainer Protocol)**: `{description.protocol.name}`\n"
        if description.references:
            md += "* **Reference(s)**:\n"
            md += ",".join(f"[{link_name}]({link})" for link_name, link in description.references.items())
        md += "\n"
        return md

    @abstractmethod
    def get_task_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_task_explanation(self) -> str:
        raise NotImplementedError

    def get_task_protocol(self) -> Optional[Protocol]:
        return None

    @abstractmethod
    def get_task_references(self) -> Dict[str, str]:
        raise NotImplementedError

    def __getitem__(self, key):
        """
        This enables accessing the models for the task in a dict-like way.

        :param key: Model name
        :return: Model instance if the model name is found
        """
        return getattr(self, key)

    def model_dict(self):
        return {attr: getattr(self, attr) for attr in dir(self) if isinstance(getattr(self, attr), BioModel)}

    def model_list(self) -> List[BioModel]:
        return list(self.model_dict().values())


class BioTaskCollection(NamedTuple):
    def __getitem__(self, key):
        return getattr(self, key)

    def task_dict(self) -> Dict[str, BioTask]:
        return {attr: getattr(self, attr) for attr in dir(self) if isinstance(getattr(self, attr), BioTask)}

    def task_list(self) -> List[BioTask]:
        return list(self.task_dict().values())
