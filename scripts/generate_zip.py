import os
import shutil

from bio_ml_models.utils import get_model_data_dir_name_versioned

model_data_name = get_model_data_dir_name_versioned()

if not os.path.exists(f"../{model_data_name}"):
    print(f"Model data directory does not exist: ../{model_data_name}!")
    exit(1)

shutil.make_archive(f"../{model_data_name}", 'zip', f"../{model_data_name}",
                    verbose=True)
