```yaml
node: "/Public/Module/AI"
type: "core_module"
subsystem: "BDGSite AI Engine"
version: "2026.1.4"
stability_layer: "stable"
db_relations:
  - table: "ai_sessions"
    type: "write/read"
    purpose: "Logs and syncs interactive user session tokens and dialogue history"
  - table: "company_registry"
    type: "read_only"
    purpose: "Validates incoming payloads against active authorization keys"
external_connections:
  - system: "Qdrant Vector DB"
    protocol: "gRPC"
    endpoint: "vector-core.internal:6334"
    purpose: "Extracts semantic memory layers and contextual knowledge weights"
  - system: "Neocortex LLM Gateway"
    protocol: "HTTPS/REST"
    endpoint: "https://api.neocortex.ai/v1"
    purpose: "Orchestrates payload token streaming to external models (OpenAI/Claude)"
```

# 📂 Node Profile: /Public/Module/AI

## 1. System Overview & Core Responsibility
This directory serves as the primary computational runtime and semantic orchestration gate of the application engine. It functions as an isolated subsystem designed to isolate heavy business logic from raw, unverified web traffic. 

The main objective of this node is to intercept incoming interaction streams, resolve context ownership boundaries via secure keys, construct clean vector memory frames, and securely stream context payloads to the linguistic processing core (LLM).

## 2. Directory Topology & Relative Path Blueprint
* `Router.php` — **Semantic Pre-Router.** Intercepts incoming requests and parses intent before resource-heavy application objects are instantiated.
* `Worker/` — **Execution Agents.** Contains distinct, isolated operational runtimes handling specific agent types:
  * `Worker/Consultant.php` — Handles public-facing customer inquiries and transactional scripts.
  * `Worker/Support.php` — Interfaces with low-level diagnostic logs and configuration arrays.
* `Context/` — **Context Assembly Framework.** Coordinates and sanitizes prompt matrices:
  * `Context/Assembly.php` — Stitches historical short-term session logs with long-term vector embeddings.
* `Bridge/` — **Infrastructure Connectors.** Abstract transport drivers masking outward API payloads (`Neocortex.php`, `Qdrant.php`).

## 3. Data Flows & Inter-System Connections
