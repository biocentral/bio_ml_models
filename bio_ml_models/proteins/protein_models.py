from typing import Dict, Tuple

from ..base import BiotrainerModel


class AAVFitnessModelFLIP(BiotrainerModel):
    def get_model_file_path(self) -> str:
        return "proteins/adeno_associated_virus_fitness/aav_flip/output/out.yml"

    def get_model_name(self) -> str:
        return "AAV FLIP Model"

    def get_model_task(self) -> str:
        return "Model to predict adeno associated virus fitness."

    def get_model_dataset(self) -> Tuple[str, str]:
        return "FLIP:aav_seven_vs_many", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/aav"

    def get_model_dataset_license(self) -> Tuple[str, str]:
        return "None/AFL-3", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/aav#data-licensing"

    def get_model_authors(self) -> Dict[str, str]:
        return {"Joaquim Gómez": "https://github.com/joaquimgomez", "Sebastian Franz": "https://github.com/SebieF"}

    def get_model_references(self) -> Dict[str, str]:
        return {"auto_eval": "https://github.com/J-SNACKKB/autoeval"}


class ConservationModelFLIP(BiotrainerModel):
    def get_model_file_path(self) -> str:
        return "proteins/conservation/conservation_flip/output/out.yml"

    def get_model_name(self) -> str:
        return "Conservation FLIP model."

    def get_model_task(self) -> str:
        return "Model to predict conservation of protein residues."

    def get_model_dataset(self) -> Tuple[str, str]:
        return "FLIP:conservation_sampled", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/conservation"

    def get_model_dataset_license(self) -> Tuple[str, str]:
        return "None/AFL-3/CC BY 4.0", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/conservation#data-licensing"

    def get_model_authors(self) -> Dict[str, str]:
        return {"Joaquim Gómez": "https://github.com/joaquimgomez", "Sebastian Franz": "https://github.com/SebieF"}

    def get_model_references(self) -> Dict[str, str]:
        return {"auto_eval": "https://github.com/J-SNACKKB/autoeval"}


class GB1BindingModelFLIP(BiotrainerModel):
    def get_model_file_path(self) -> str:
        return "proteins/gb1_binding/gb1_flip/output/out.yml"

    def get_model_name(self) -> str:
        return "GB1 FLIP model."

    def get_model_task(self) -> str:
        return "Model to predict the binding ability of GB1 protein variants."

    def get_model_dataset(self) -> Tuple[str, str]:
        return "FLIP:gb1_two_vs_rest", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/gb1"

    def get_model_dataset_license(self) -> Tuple[str, str]:
        return "CC BY 4.0/AFL-3", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/gb1#data-licensing"

    def get_model_authors(self) -> Dict[str, str]:
        return {"Joaquim Gómez": "https://github.com/joaquimgomez", "Sebastian Franz": "https://github.com/SebieF"}

    def get_model_references(self) -> Dict[str, str]:
        return {"auto_eval": "https://github.com/J-SNACKKB/autoeval"}


class MeltomeModelFLIP(BiotrainerModel):
    def get_model_file_path(self) -> str:
        return "proteins/meltome/meltome_flip/output/out.yml"

    def get_model_name(self) -> str:
        return "Meltome FLIP model."

    def get_model_task(self) -> str:
        return "Model to predict the meltdown temperature of proteins."

    def get_model_dataset(self) -> Tuple[str, str]:
        return "FLIP:meltome_mixed_split", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/meltome"

    def get_model_dataset_license(self) -> Tuple[str, str]:
        return "Free/No License/AFL-3", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/meltome#data-licensing"

    def get_model_authors(self) -> Dict[str, str]:
        return {"Joaquim Gómez": "https://github.com/joaquimgomez", "Sebastian Franz": "https://github.com/SebieF"}

    def get_model_references(self) -> Dict[str, str]:
        return {"auto_eval": "https://github.com/J-SNACKKB/autoeval"}


class MultiLigandBindingSiteModelFLIP(BiotrainerModel):
    def get_model_file_path(self) -> str:
        return "proteins/multi_ligand_binding_site/binding_flip/output/out.yml"

    def get_model_name(self) -> str:
        return "MultiLigand BindingSite FLIP model."

    def get_model_task(self) -> str:
        return "Model to predict binding of protein residues for multiple types of ligands."

    def get_model_dataset(self) -> Tuple[str, str]:
        return "FLIP:bind_from_publication", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/bind"

    def get_model_dataset_license(self) -> Tuple[str, str]:
        return "None/AFL-3/CC BY 4.0", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/bind#data-licensing"

    def get_model_authors(self) -> Dict[str, str]:
        return {"Joaquim Gómez": "https://github.com/joaquimgomez", "Sebastian Franz": "https://github.com/SebieF"}

    def get_model_references(self) -> Dict[str, str]:
        return {"auto_eval": "https://github.com/J-SNACKKB/autoeval"}


class SecondaryStructureModelFLIP(BiotrainerModel):

    def get_model_file_path(self) -> str:
        return "proteins/secondary_structure/secondary_structure_flip/output/out.yml"

    def get_model_name(self) -> str:
        return "Secondary Structure FLIP model."

    def get_model_task(self) -> str:
        return "Model to predict the secondary structures of proteins."

    def get_model_dataset(self) -> Tuple[str, str]:
        return ("FLIP:secondary_structure_sampled",
                "https://github.com/J-SNACKKB/FLIP/tree/main/splits/secondary_structure")

    def get_model_dataset_license(self) -> Tuple[str, str]:
        return "AFL-3", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/secondary_structure#data-licensing"

    def get_model_authors(self) -> Dict[str, str]:
        return {"Joaquim Gómez": "https://github.com/joaquimgomez", "Sebastian Franz": "https://github.com/SebieF"}

    def get_model_references(self) -> Dict[str, str]:
        return {"auto_eval": "https://github.com/J-SNACKKB/autoeval"}


class SAVModelFLIP(BiotrainerModel):

    def get_model_file_path(self) -> str:
        return "proteins/single_aminoacid_variants/sav_flip/output/out.yml"

    def get_model_name(self) -> str:
        return "SAV FLIP Model."

    def get_model_task(self) -> str:
        return "Model to predict single amino acid variant effects on proteins."

    def get_model_dataset(self) -> Tuple[str, str]:
        return "FLIP:sav_mixed", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/sav"

    def get_model_dataset_license(self) -> Tuple[str, str]:
        return "None/AFL-3/CC BY 4.0", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/sav#data-licensing"

    def get_model_authors(self) -> Dict[str, str]:
        return {"Joaquim Gómez": "https://github.com/joaquimgomez", "Sebastian Franz": "https://github.com/SebieF"}

    def get_model_references(self) -> Dict[str, str]:
        return {"auto_eval": "https://github.com/J-SNACKKB/autoeval"}


class SCLModelFLIP(BiotrainerModel):

    def get_model_file_path(self) -> str:
        return "proteins/sub_cellular_location/scl_flip/output/out.yml"

    def get_model_name(self) -> str:
        return "SCL FLIP model."

    def get_model_task(self) -> str:
        return "Model to predict the sub-cellular location of proteins."

    def get_model_dataset(self) -> Tuple[str, str]:
        return "FLIP:scl_mixed_hard", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/scl"

    def get_model_dataset_license(self) -> Tuple[str, str]:
        return "CC BY 4.0/AFL-3", "https://github.com/J-SNACKKB/FLIP/tree/main/splits/scl#data-licensing"

    def get_model_authors(self) -> Dict[str, str]:
        return {"Joaquim Gómez": "https://github.com/joaquimgomez", "Sebastian Franz": "https://github.com/SebieF"}

    def get_model_references(self) -> Dict[str, str]:
        return {"auto_eval": "https://github.com/J-SNACKKB/autoeval"}
