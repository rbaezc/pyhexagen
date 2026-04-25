# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-04-24

### Added
- **Core Library Architecture**: Implementation of the Hexagonal (Ports & Adapters) scaffolding engine.
- **Dynamic Resource Generation**: `gen-resource` command with support for custom attributes (name:type).
- **Architecture Enforcement**: Use of `abc.ABC` for Domain Ports to ensure strict contract implementation.
- **Pure Domain layer**: Logic confined to standard `dataclasses` with zero external dependencies.
- **Infrastructure Layer**: SQLAlchemy 2.0 (Async) integration with automatic model generation.
- **API Layer**: FastAPI integration with Pydantic V2 DTOs and automatic validation.
- **Dependency Injection**: Pre-wired container using `dependency-injector`.
- **Global Exception Mapping**: Built-in system to translate Domain Exceptions to HTTP Status Codes.
- **Structured Logging**: Production-ready JSON logging and human-readable dev console output.
- **Automated Documentation**: MkDocs integration with `mkdocstrings`.
- **CI/CD Quality**: GitHub Actions workflow with 85% test coverage enforcement.
- **Development Toolchain**: Ruff configuration for linting and formatting.
- **Containerization**: Multi-stage Dockerfile and docker-compose (PostgreSQL) setup.

### Changed
- Refactored `src/web` to `src/api` for better modern API standards.

### Fixed
- Initial boilerplate integration issues between layers.

---
*PyHexaGen v0.1.0 - The Architectural Guardian.*
