from .protein_tasks import AdenoAssociatedVirusFitnessTask, ConservationTask, GB1BindingTask, MeltomeTask, \
    MultiLigandBindingSiteTask, SecondaryStructureTask, SingleAminoAcidVariantEffectTask, SubCellularLocationTask

from ..base import BioTaskCollection


class ProteinTasks(BioTaskCollection):
    adeno_associated_virus_fitness: AdenoAssociatedVirusFitnessTask = AdenoAssociatedVirusFitnessTask()
    conservation: ConservationTask = ConservationTask()
    gb1_binding: GB1BindingTask = GB1BindingTask()
    meltome: MeltomeTask = MeltomeTask()
    multi_ligand_binding_site: MultiLigandBindingSiteTask = MultiLigandBindingSiteTask()
    secondary_structure: SecondaryStructureTask = SecondaryStructureTask()
    single_amino_acid_variant_effect: SingleAminoAcidVariantEffectTask = SingleAminoAcidVariantEffectTask()
    sub_cellular_location: SubCellularLocationTask = SubCellularLocationTask()


__all__ = ['ProteinTasks']
