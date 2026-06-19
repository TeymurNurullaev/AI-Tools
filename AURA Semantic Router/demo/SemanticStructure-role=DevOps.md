# 📑 AURA Context Assembly Package
* **Target Node Scope:** `/`
* **Active Routing Mode:** `ROLE:DEVOPS`

## 1. Directory Topology
```
├── core/
│   ├── auth_provider/
│   │   └── auth.php
│   └── database_proxy/
├── modules/
│   ├── billing/
│   └── blog/
│       ├── .session
│       ├── blog.Modul.php
│       └── bloglist.tpl
├── private/
│   └── lib/
└── public/
    ├── css/
    └── js/
```
---

## 2. Assembled Semantic Layers

### 📂 Node [`/core/auth_provider`] ──► Слой: `GUARDRAILS`

```yaml
security_policies:
  access_level: "isolated"
data_sensitivity:
  contains_credentials: true
  public_exposure_allowed: false
```

---

### 📂 Node [`/`] ──► Слой: `MANIFEST`

```yaml
identity:
  node: "/"
  type: "root_manifest"
  subsystem: "Ecosystem Root"
```

---

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

### 📂 Node [`/modules/blog`] ──► Слой: `MANIFEST`

```yaml
identity:
  node: "/modules/blog"
  type: "execution_agent"
  subsystem: "Content"
  criticality: "medium"
```

---
