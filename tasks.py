from invoke import task


@task
def lint(c):
    project_folder = "./study/"
    c.run(f"python -m isort --project vanadiko {project_folder}")
    c.run(
        f"python -m autoflake --in-place --recursive --remove-all-unused-imports --ignore-init-module-imports {project_folder}"
    )
    c.run(f"python -m black {project_folder}")
