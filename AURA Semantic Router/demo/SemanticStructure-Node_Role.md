# 📑 AURA Context Assembly Package
* **Target Node Scope:** `/core/auth_provider`
* **Active Routing Mode:** `ROLE:CODER`

## 1. Directory Topology
```
└── auth.php
```
---

## 2. Assembled Semantic Layers

### 📂 Node [`/core/auth_provider`] ──► Слой: `MANIFEST`

```yaml
identity:
  node: "/core/auth_provider"
  type: "system_core"
  subsystem: "Security"
  criticality: "mission_critical"
dependencies:
  upstream: ["/gateway/ingress"]
```

---

### 📂 Node [`/core/auth_provider`] ──► Слой: `ORGAN`

```yaml
organ_identity:
  node: "/core/auth_provider"
  engine_pattern: "Stateless_Service"
runtime_interfaces:
  methods:
    - name: "validateSession"
      input_format: "JWT_String"
      output_format: "Boolean"
```

---
