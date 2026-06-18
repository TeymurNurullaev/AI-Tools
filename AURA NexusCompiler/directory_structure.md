## 1. System Overview

```yaml
node: "/"
type: "root_manifest"
system: "Demo Ecosystem"
subsystem: "Orchestrator Core"
```

# Demo Ecosystem Overview
This is a root manifest demonstrating the AURA Semantic Architecture.

## 2. Directory Topology

```
/demo_project/   <-- Корень семантического ядра a
├── BDGSite/  <-- Семантический пре-роутер (Перехват company_key)
│   └── Action/
│       ├── mainController.php
│       └── mainRouter.php
├── Context/  <-- Пространство сборки контекста и слоев состояний
│   └── Assembly.php  <-- Сборщик слоев памяти (Context Assembly Engine)
├── Public/
│   ├── css/
│   └── js/
└── Tempfile/
```

## 3. Component Manifests

### 📂 Node: `/BDGSite`
> **Context Boundary:** Ниже представлен манифест управления контекстом узла.

```yaml
node: "/BDGSite"
type: "system_core"
subsystem: "Core Gateway Engine"
```

# Core Gateway Engine
This module handles pre-routing and traffic interception.

---

### 📂 Node: `/Context`
> **Context Boundary:** Ниже представлен манифест управления контекстом узла.

```yaml
node: "/Context"
type: "memory_layer"
subsystem: "Context Assembly Engine"
```

# Context Assembly Engine
Responsible for stitching vector data with live prompt matrices.

---
