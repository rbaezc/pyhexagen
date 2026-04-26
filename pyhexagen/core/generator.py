import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

class HexaGenerator:
    def __init__(self, project_name: str, base_path: str):
        self.project_name = project_name
        self.base_path = Path(base_path) / project_name
        self.template_dir = Path(__file__).parent.parent / "templates"
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def init_project(self, db_type: str):
        """Creates the initial directory structure."""
        dirs = [
            "src/domain/models",
            "src/application/use_cases",
            "src/application/ports",
            "src/infrastructure/repositories",
            "src/infrastructure/persistence",
            "src/api/routers",
            "tests"
        ]
        
        for d in dirs:
            (self.base_path / d).mkdir(parents=True, exist_ok=True)
            # Create __init__.py files
            init_file = self.base_path / d / "__init__.py"
            init_file.touch()

        # Initial main files
        self._create_from_template("pyproject.toml.j2", "pyproject.toml", {"project_name": self.project_name})
        self._create_from_template("requirements.txt.j2", "requirements.txt", {"project_name": self.project_name})
        self._create_from_template("main.py.j2", "main.py", {"project_name": self.project_name})
        self._create_from_template("README.md.j2", "README.md", {"project_name": self.project_name})
        self._create_from_template("Dockerfile.j2", "Dockerfile", {"project_name": self.project_name})
        self._create_from_template("docker-compose.yml.j2", "docker-compose.yml", {"project_name": self.project_name})
        self._create_from_template("mkdocs.yml.j2", "mkdocs.yml", {"project_name": self.project_name})
        self._create_from_template("ruff.toml.j2", "ruff.toml", {"project_name": self.project_name})
        self._create_from_template("github_ci.yml.j2", ".github/workflows/ci.yml", {"project_name": self.project_name})
        self._create_from_template("config.py.j2", "src/config.py", {"project_name": self.project_name})
        self._create_from_template("domain_exceptions.py.j2", "src/domain/exceptions.py", {})
        self._create_from_template("logging_config.py.j2", "src/infrastructure/logging.py", {})
        self._create_from_template("exception_handler.py.j2", "src/infrastructure/exception_handler.py", {})
        self._create_from_template("container.py.j2", "src/infrastructure/container.py", {"db_type": db_type})
        self._create_from_template("health_router.py.j2", "src/api/routers/health.py", {})
        self._create_from_template("conftest.py.j2", "tests/conftest.py", {})
        
        if db_type == "sqlalchemy":
            self._create_from_template("database.py.j2", "src/infrastructure/persistence/database.py", {})

    def generate_resource(self, resource_name: str, attributes: list = None):
        """Generates the Hexagonal layers for a specific resource."""
        slug = resource_name.lower()
        context = {
            "resource_name": resource_name,
            "attributes": attributes or []
        }
        
        # 1. Domain Entity
        self._create_from_template("entity.py.j2", f"src/domain/models/{slug}.py", context)
        
        # 2. Application Port
        self._create_from_template("repository_port.py.j2", f"src/application/ports/{slug}_repository.py", context)
        
        # 3. Application Use Case
        self._create_from_template("use_case.py.j2", f"src/application/use_cases/create_{slug}.py", context)
        
        # 4. Infrastructure Model (SQLAlchemy)
        self._create_from_template("infrastructure_model.py.j2", f"src/infrastructure/persistence/models.py", context)
        
        # 5. Infrastructure Adapter (Repository Implementation)
        self._create_from_template("adapter_repository.py.j2", f"src/infrastructure/repositories/{slug}_repository.py", context)
        
        # 6. Web Router
        self._create_from_template("web_router.py.j2", f"src/api/routers/{slug}.py", context)

        # 7. Unit Tests
        self._create_from_template("test_use_case.py.j2", f"tests/test_{slug}_use_case.py", context)

    def _create_from_template(self, template_name: str, output_path: str, context: dict):
        template = self.env.get_template(template_name)
        content = template.render(**context)
        dest = self.base_path / output_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        with open(dest, "w") as f:
            f.write(content)
