# PyHexaGen: The Architectural Guardian for Python/FastAPI 🛡️🐍

"Don't build a Big Ball of Mud. Scaffold a Citadel."

[![Architecture: Hexagonal](https://img.shields.io/badge/Architecture-Hexagonal-blueviolet)](https://github.com/rbaezc/pyhexagen)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://github.com/rbaezc/pyhexagen)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/rbaezc/pyhexagen/blob/main/LICENSE)

---

## 🚀 Why PyHexaGen?

Python projects often suffer from "Big Ball of Mud" syndrome as they scale. PyHexaGen enforces **Software Engineering Excellence** from Day 1 by providing a professional-grade scaffolding that implements the **Ports & Adapters** pattern with high rigour.

### Key Value Pillars:
- **Enforced Boundaries**: Pure Domain logic with zero external dependencies.
- **Dynamic Scaffolding**: Generate full vertical slices (Domain, Infra, API) in seconds.
- **Production-Ready**: Built-in structured logging, exception mapping, and CI/CD pipelines.

---

## ✨ Killer Features

### 1. Architectural Guardrails
- **Nominal Subtyping (`abc.ABC`)**: We don't rely on simple duck-typing. We enforce formal contracts so your Adapters never miss a required method.
- **Pure Domain Models**: Your business logic lives in vanilla Python `dataclasses`. No Pydantic, no SQLAlchemy in the core. Pure, testable, and immortal.

### 2. Intelligent Type-Safe Generation
Generate a full enterprise-grade resource with a single CLI command:
```bash
python -m pyhexagen gen-resource Product name:str price:float stock:int
```
PyHexaGen automatically creates:
- ✅ **Domain Entities** with typed fields.
- ✅ **Infrastructure Models** (SQLAlchemy 2.0 Async).
- ✅ **API Layer DTOs** (Pydantic V2) with validation.
- ✅ **Wiring & DI** (via `dependency-injector`).

### 3. Enterprise Infrastructure Out-of-the-box
- **Global Exception Mapping**: Automatically maps Domain Exceptions to HTTP Status Codes.
- **Structured JSON Logging**: Pre-configured for ELK/Datadog/CloudWatch.
- **Full CI/CD**: Ready-to-use GitHub Actions with 85% test coverage enforcement.
- **Instant Documentation**: Integrated MkDocs with automated API reference.

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/rbaezc/pyhexagen.git
cd pyhexagen

# Install dependencies
pip install -r requirements.txt
```

---

## 📖 Quick Start

### 1. Initialize your Project
```bash
python -m pyhexagen init MyAwesomeProject
```

### 2. Generate a Resource
```bash
python -m pyhexagen gen-resource MyAwesomeProject Order order_id:str total:float
```

### 3. Run with Docker
```bash
cd MyAwesomeProject
docker-compose up --build
```

---

## 🛡️ The Architectural Promise

PyHexaGen doesn't just give you files; it gives you a **System**. It sets the boundaries that prevent code rot and ensures your application remains maintainable for years to come.

**Built by Architects, for Architects.**

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
