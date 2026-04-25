import typer
from typing import Optional
import os
from pyhexagen.core.generator import HexaGenerator

app = typer.Typer(help="PyHexaGen: Hexagonal Architecture Scaffolding for Python")

@app.command()
def init(
    project_name: str = typer.Argument(..., help="Name of the project to initialize"),
    db_type: str = typer.Option("sqlalchemy", "--db", help="Database adapter type (sqlalchemy, motor)")
):
    """
    Initialize a new hexagonal project structure.
    """
    typer.echo(f"Initializing {project_name} with {db_type}...")
    generator = HexaGenerator(project_name, os.getcwd())
    generator.init_project(db_type)
    typer.echo("Project structure created successfully!")

@app.command()
def gen_resource(
    project_path: str = typer.Argument(..., help="Path to the existing project"),
    resource_name: str = typer.Argument(..., help="Name of the resource (e.g., User, Order)"),
    attributes: Optional[list[str]] = typer.Argument(None, help="Attributes in format name:type (e.g. name:str age:int)")
):
    """
    Generate Domain, Application, and Infrastructure layers for a resource with attributes.
    """
    typer.echo(f"Generating resource {resource_name} in {project_path}...")
    
    # Parse attributes
    parsed_attrs = []
    if attributes:
        for attr in attributes:
            if ":" in attr:
                name, kind = attr.split(":", 1)
                parsed_attrs.append({"name": name, "type": kind})
            else:
                parsed_attrs.append({"name": attr, "type": "str"})

    generator = HexaGenerator(os.path.basename(project_path), os.path.dirname(project_path))
    generator.generate_resource(resource_name, parsed_attrs)
    typer.echo(f"Resource {resource_name} generated successfully!")

if __name__ == "__main__":
    app()
