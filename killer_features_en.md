# PyHexaGen: The Elite Hexagonal Scaffolding Tool for Python

PyHexaGen is designed for architects and senior developers who demand rigorous structure, clean separation of concerns, and production-ready defaults. It doesn't just generate boilerplate; it enforces **Software Engineering Excellence**.

## 🚀 Killer Features

### 1. Architectural Rigor (Ports & Adapters)
- **Nominal Subtyping via `abc.ABC`**: Unlike tools that rely on duck-typing (Protocols), PyHexaGen uses Abstract Base Classes to enforce strict contracts. If an Adapter doesn't implement a Port method, Python will fail at instantiation, preventing runtime bugs.
- **Pure Domain Models**: Your business logic sits in "Vanilla Python" `dataclasses` with **zero external dependencies**. No Pydantic in the domain—keeping your "Heart of Software" truly decoupled.

### 2. Intelligent Type-Safe Generation
- **Dynamic Attribute Mapping**: Generate full vertical slices with one command:
  `gen-resource Product name:str price:float stock:int`
- **Multi-Layer Synchronization**: The tool automatically maps these attributes across:
  - **Domain Entities** (Dataclasses)
  - **Infrastructure Models** (SQLAlchemy 2.0 Async)
  - **API Layer DTOs** (Pydantic V2)

### 3. Production-Ready "Day 1" Infrastructure
- **Global Domain Exception Mapping**: Includes a built-in handler that catches Domain Exceptions and translates them into standard HTTP status codes (404, 400, etc.), keeping your API layer incredibly thin.
- **Dual-Mode Structured Logging**: 
  - **Production**: High-performance JSON logging for ELK/CloudWatch/Datadog.
  - **Development**: Human-readable, color-coded console output.
- **Modern Toolchain**: Pre-configured with **Ruff** (linting/formatting), **MkDocs** (automated documentation), and **GitHub Actions** (CI/CD with 85% coverage enforcement).

### 4. Enterprise-Grade Dependency Injection
- **`dependency-injector` Integration**: Uses the most robust DI container in the Python ecosystem to wire up your application, making it highly testable and modular.

## 🎯 Value Proposition

PyHexaGen bridges the gap between **Rapid Prototyping** and **Enterprise Architecture**. It allows you to move at the speed of a startup while maintaining the structural integrity of a legacy-proof system.

**"Built by Architects, for Architects."**
