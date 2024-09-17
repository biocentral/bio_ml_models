import os
from pathlib import Path

from bio_ml_models import BioModelCollection

GENERATED_HINT = "\n\n<!--- This file was created automatically. Please do not modify manually. --->\n"


def create_docs_directory():
    docs_dir = Path("../docs")
    if not docs_dir.exists():
        os.mkdir(docs_dir)
        print("Created docs directory..")
    return docs_dir


def generate_docs(docs_dir: Path):
    collection = BioModelCollection()
    domains = collection.domain_dict()

    for domain_name, domain in domains.items():
        domain_dir = docs_dir / domain_name
        domain_dir.mkdir(exist_ok=True)

        tasks = domain.task_dict()
        for task_name, task in tasks.items():
            task_dir = domain_dir / task_name
            task_dir.mkdir(exist_ok=True)
            task_md = task.generate_task_markdown() + GENERATED_HINT
            with open(task_dir / f'{task_name}.md', 'w') as task_md_f:
                task_md_f.write(task_md)

            models = task.model_dict()
            for model_name, model in models.items():
                model_md = model.generate_model_markdown() + GENERATED_HINT
                with open(task_dir / f'{model_name}.md', 'w') as model_md_f:
                    model_md_f.write(model_md)


def update_readme(readme_path: Path):
    collection = BioModelCollection()
    domains = collection.domain_dict()

    # Generate the new content
    new_content = "## Available Tasks\n\n"
    for domain_name, domain in domains.items():
        domain_name = domain_name.capitalize()
        new_content += f"<details>\n\n<summary><b>{domain_name}</b></summary>\n\n"
        tasks = domain.task_dict()
        for task_name, task in tasks.items():
            models = task.model_dict()
            task_description = task.description()
            new_content += f"- **{task_name}**: {task_description.explanation} ({len(models)} model(s) available)\n"
        new_content += "\n</details>\n\n"

    # Read the current README content
    with open(readme_path, 'r') as readme_f:
        content = readme_f.read()

    # Find the section to replace
    start_marker = "## Available Tasks"
    end_marker = "## Installation"
    start_index = content.find(start_marker)
    end_index = content.find(end_marker, start_index)

    if start_index == -1 or end_index == -1:
        raise ValueError("Could not find the section to replace in the README")

    # Replace the section
    updated_content = (
        content[:start_index] +
        new_content +
        content[end_index:]
    )

    with open(readme_path, 'w') as readme_f:
        readme_f.write(updated_content)

    print(f"README updated successfully at {readme_path}")


def main(args=None):
    docs_dir = create_docs_directory()
    generate_docs(docs_dir=docs_dir)
    update_readme(Path("../README.md"))


if __name__ == '__main__':
    main()
