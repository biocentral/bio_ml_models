from typing import Dict, Optional

from biotrainer.protocols import Protocol

from .protein_models import AAVFitnessModelFLIP, ConservationModelFLIP, GB1BindingModelFLIP, MeltomeModelFLIP, \
    MultiLigandBindingSiteModelFLIP, SecondaryStructureModelFLIP, SAVModelFLIP, SCLModelFLIP

from ..base import BioTask


class AdenoAssociatedVirusFitnessTask(BioTask):
    aav_flip: AAVFitnessModelFLIP = AAVFitnessModelFLIP()

    def get_task_name(self) -> str:
        return "Adeno Associated Virus Fitness Prediction Task."

    def get_task_explanation(self) -> str:
        return ("Predict a fitness score for each "
                "[AAV capsid protein](https://www.uniprot.org/uniprotkb/P03135/entry) mutation.")

    def get_task_protocol(self) -> Optional[Protocol]:
        return Protocol.sequence_to_value

    def get_task_references(self) -> Dict[str, str]:
        return {"Uniprot P03135": "https://www.uniprot.org/uniprotkb/P03135/entry",
                "Paper - Deep diversification of an AAV capsid protein by machine learning":
                    "https://doi.org/10.1038/s41587-020-00793-4"}


class ConservationTask(BioTask):
    conservation_flip: ConservationModelFLIP = ConservationModelFLIP()

    def get_task_name(self) -> str:
        return "Conservation Score Prediction Task."

    def get_task_explanation(self) -> str:
        return "Predict a conservation score for each residue in a protein sequence."

    def get_task_protocol(self) -> Optional[Protocol]:
        return Protocol.residue_to_class

    def get_task_references(self) -> Dict[str, str]:
        return {"Paper - Embeddings from protein language models predict conservation and variant effects":
                    "https://doi.org/10.1007/s00439-021-02411-y"}


class GB1BindingTask(BioTask):
    gb1_flip: GB1BindingModelFLIP = GB1BindingModelFLIP()

    def get_task_name(self) -> str:
        return "GB1 Binding Score Prediction Task."

    def get_task_explanation(self) -> str:
        return "Predict a binding score for each variant of the GB1 protein."

    def get_task_protocol(self) -> Optional[Protocol]:
        return Protocol.sequence_to_value

    def get_task_references(self) -> Dict[str, str]:
        return {"Paper - Adaptation in protein fitness landscapes is facilitated by indirect paths":
                    "https://doi.org/10.7554/eLife.16965"}


class MeltomeTask(BioTask):
    meltome_flip: MeltomeModelFLIP = MeltomeModelFLIP()

    def get_task_name(self) -> str:
        return "Meltome Temperature Prediction Task."

    def get_task_explanation(self) -> str:
        return "Predict the meltome temperature value of a protein."

    def get_task_protocol(self) -> Optional[Protocol]:
        return Protocol.sequence_to_value

    def get_task_references(self) -> Dict[str, str]:
        return {"Paper - Meltome atlas—thermal proteome stability across the tree of life":
                    "https://doi.org/10.1038/s41592-020-0801-4"}


class MultiLigandBindingSiteTask(BioTask):
    mlbs_flip: MultiLigandBindingSiteModelFLIP = MultiLigandBindingSiteModelFLIP()

    def get_task_name(self) -> str:
        return "MultiLigand Binding Sites Prediction Task."

    def get_task_explanation(self) -> str:
        return "Predict binding sites of ligands for protein residues."

    def get_task_protocol(self) -> Optional[Protocol]:
        return Protocol.residue_to_class

    def get_task_references(self) -> Dict[str, str]:
        return {"Possible encoding of binding sites": "https://github.com/J-SNACKKB/FLIP/tree/main/splits/bind#legend",
                "Paper - Protein embeddings and deep learning predict binding residues for various ligand classes":
                    "https://doi.org/10.1038/s41598-021-03431-4"}


class SecondaryStructureTask(BioTask):
    sst_flip: SecondaryStructureModelFLIP = SecondaryStructureModelFLIP()

    def get_task_name(self) -> str:
        return "Secondary Structure Prediction Task."

    def get_task_explanation(self) -> str:
        return "Predict the secondary structure for each residue in a protein sequence."

    def get_task_protocol(self) -> Optional[Protocol]:
        return Protocol.residue_to_class

    def get_task_references(self) -> Dict[str, str]:
        return {"FLIP Dataset": "https://github.com/J-SNACKKB/FLIP/tree/main/splits/secondary_structure"}


class SingleAminoAcidVariantEffectTask(BioTask):
    sav_flip: SAVModelFLIP = SAVModelFLIP()

    def get_task_name(self) -> str:
        return "Single Amino Acid Variant Effect Prediction Task."

    def get_task_explanation(self) -> str:
        return "Predict if a single amino acid variant of a protein sequence has an effect."

    def get_task_protocol(self) -> Optional[Protocol]:
        return Protocol.sequence_to_class

    def get_task_references(self) -> Dict[str, str]:
        return {"Paper - Embeddings from protein language models predict conservation and variant effects":
                    "https://doi.org/10.1007/s00439-021-02411-y"}


class SubCellularLocationTask(BioTask):
    scl_flip: SCLModelFLIP = SCLModelFLIP()

    def get_task_name(self) -> str:
        return "Subcellular Location Prediction Task."

    def get_task_explanation(self) -> str:
        return "Predict the subcellular location for a protein."

    def get_task_protocol(self) -> Optional[Protocol]:
        return Protocol.sequence_to_class

    def get_task_references(self) -> Dict[str, str]:
        return {"Paper - Light attention predicts protein location from the language of life":
                    "https://doi.org/10.1093/bioadv/vbab035"}
