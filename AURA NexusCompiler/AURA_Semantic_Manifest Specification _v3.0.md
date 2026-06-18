# 📑 AURA Semantic Manifest Specification (v3.0)
### Protocol Extension: Distributed Semantic Memory & Inter-System DNA Exchange

This document defines the strict YAML standard for the distributed semantic metadata blocks (`manifest.md`) used by the **AURA NexusCompiler** and the **AI Net** protocol. Version 3.0 transitions the manifest from a static documentation blueprint into an active runtime handshake layer for autonomous digital organisms.


```yaml
# ==============================================================================
# AURA SEMANTIC MANIFEST METADATA SCHEMA v3.0
# ==============================================================================

# --- BLOCK 1: IDENTITY & COORDINATION CORNERSTONE ---
identity:
  node: "/Context/Assembly"         # Target-relative or global URI of the system node.
  type: "memory_layer"               # Node archetype. Allowed values: [root_manifest, system_core, memory_layer, gateway_router, execution_agent, data_sink]
  subsystem: "Context Assembly"     # Human & machine readable name of the functional block.
  version: "2026.3.1"                # SemVer or epoch-based version tracking the state of this node.
  stability_layer: "stable"          # Operational maturity. Allowed: [experimental, active, stable, legacy]
  criticality: "high"               # Systemic importance. Allowed: [low, medium, high, mission_critical]

# --- BLOCK 2: SYSTEM ARCHITECTURAL RELATIONS ---
architecture_relations:
  db_relations:
    - table: "ai_sessions"
      mode: "write/read"            # Access vector. Allowed: [read_only, write_only, write/read]
      purpose: "Logs and synchronizes interactive user context matrices and execution tokens."
    - table: "company_registry"
      mode: "read_only"
      purpose: "Validates incoming traffic headers against registered enterprise cryptographic keys."
  
  external_connections:
    - system: "Qdrant Vector DB"
      protocol: "gRPC"              # Transmission layer protocol: [gRPC, HTTPS/REST, WebSockets, MQTT, Redis-RESP]
      endpoint: "vector-cluster:6334"
      purpose: "Retrieval of deep semantic knowledge layers and associative weights."

# --- BLOCK 3: HARD & SOFT DEPENDENCY MATRICES ---
dependencies:
  upstream:                         # What this node requires to run successfully
    - node: "/BDGSite"
      type: "hard"                  # Strict coupling. If this node fails or is missing, current node dies.
      purpose: "Requires pre-routed, validated transaction packets with extracted company keys."
  downstream:                       # Nodes that rely directly on this node
    - node: "/Worker/Consultant"
      type: "soft"                  # Loose coupling. Can operate with degraded functionality if missing.
      purpose: "Consumes compiled context arrays to execute linguistic agent pipelines."

# --- BLOCK 4: RESOURCE PROFILES & LIMITATIONS ---
resource_profiles:
  load_expectations:
    target_rps: "250"               # Expected or tested baseline requests per second.
    peak_rps: "1000"                # Max throughput capacity before rate-limiting triggers.
  resilience:
    timeout_ms: "450"               # Maximum processing time before throwing an execution exception.
    retry_policy: "exponential_backoff_3" # Error recovery routine string.
    offline_capability: false       # True if node can maintain logic execution without external network connections.

# --- BLOCK 5: EVOLUTIONARY & MIGRATION MARKERS ---
evolution:
  potential: "high"                 # Likelihood of algorithmic changes. Allowed: [low, medium, high]
  migration_path: "v2_to_v3_schema" # Pointer to translation layer script for database or state changes.
  domain_ontology: "cognitive_layer" # Knowledge Graph categorization tag for autonomous indexing.

# --- BLOCK 6: SECURITY & AUDIT POLICIES ---
security_policies:
  access_level: "private"          # Exposure level. Allowed: [public, internal, private, isolated]
  encryption: "TLS_1.3"             # Wire encryption standard used for all node egress.
  audit_vector: "syslog_structured" # Target handler for logging telemetry data and access checks.
```


## 📘 Detailed Field-by-Field Specification & AI Utility

### Block 1: Identity & Coordination Cornerstone

* **`identity.node`** (String)
* *Purpose:* The absolute structural anchor point of the component.
* *AI Utility:* Acts as the coordinate system within the AI Net graph. When two systems query each other via `/semantic-ping`, the AI uses this string to map out the system's layout.


* **`identity.type`** (Enum)
* *Purpose:* Categorizes the functional role of the folder/module.
* *AI Utility:* Allows LLMs to instantly apply correct cognitive heuristics. If a directory is tagged as a `gateway_router`, the AI focuses on security and parsing; if it's an `execution_agent`, the AI looks for operational decision-making loops.


* **`identity.subsystem`** (String)
* *Purpose:* Logical group identification.
* *AI Utility:* Groups disparate folder paths into a unified organizational branch.


* **`identity.version`** (String)
* *Purpose:* Tracks development iteration.
* *AI Utility:* Crucial for determining version drift. When systems interact, the AI reads this to check if its cached execution strategies are up-to-date.


* **`identity.stability_layer`** & **`identity.criticality`** (Enum)
* *Purpose:* Defines code maturity and organizational risk.
* *AI Utility:* Dictates the AI's risk-management profile. If an agent is tasked with refactoring a module marked as `mission_critical`, it will apply maximum regression verification steps.



### Block 2: System Architectural Relations

* **`architecture_relations.db_relations`** (Array)
* *Purpose:* Maps every database entity touched by this module.
* *AI Utility:* Prevents database corruption and race conditions. Before an AI agent executes code or alters a SQL query, it checks the `mode` (`read_only` vs `write/read`) to ensure it doesn't violate database governance policies.


* **`architecture_relations.external_connections`** (Array)
* *Purpose:* Outlines the external network footprints of the module.
* *AI Utility:* Enables autonomous API mapping. The AI reads the `protocol` and `endpoint` to instantly configure internal transport drivers without needing human intervention.



### Block 3: Hard & Soft Dependency Matrices

* **`dependencies.upstream`** & **`dependencies.downstream`** (Array)
* *Purpose:* Declares a strict lineage of what a module depends on, and who depends on it.
* *AI Utility:* **The core of network graph generation.** If an AI agent changes code in `/BDGSite`, it scans the downstream dependencies to find out that `/Context/Assembly` might be broken by this change, allowing it to proactively run validation tests. The `type` (`hard` vs `soft`) tells the AI whether a failure in an external module should completely halt execution or merely degrade service performance.



### Block 4: Resource Profiles & Limitations

* **`resource_profiles.load_expectations`** (Map)
* *Purpose:* Establishes volume boundaries for execution.
* *AI Utility:* Helps AI workers scale infrastructure dynamically. If real-time telemetry spikes past `peak_rps`, the supervisor AI can spawn duplicate containers for this specific node.


* **`resource_profiles.resilience`** (Map)
* *Purpose:* Code execution boundaries and error routines.
* *AI Utility:* Sets the timeout windows. If an AI agent writes an internal connection script, it extracts `timeout_ms` directly from the DNA to set execution boundaries inside the code.



### Block 5: Evolutionary & Migration Markers

* **`evolution.potential`** & **`evolution.migration_path`** (String/Enum)
* *Purpose:* Signals how volatile the node is and how to upgrade it.
* *AI Utility:* Helps the network plan deprecation schedules. An AI architect can crawl the network and flag legacy structures with low evolutionary potential for scheduled termination.


* **`evolution.domain_ontology`** (String)
* *Purpose:* Semantic classification tag.
* *AI Utility:* Links the raw codebase directly to an enterprise-wide **Knowledge Graph**. The AI uses this tag to correlate the actual code with conceptual business rules.



### Block 6: Security & Audit Policies

* **`security_policies.access_level`** (Enum)
* *Purpose:* Security exposure firewall marker.
* *AI Utility:* **Absolute safety guardrail.** If a node is set to `isolated` or `private`, the internal routing mechanism blocks the AI from ever exposing this data or structure via public-facing APIs or `/semantic-ping` requests.


* **`security_policies.encryption`** & **`security_policies.audit_vector`** (String)
* *Purpose:* Audit trails and security compliance tracking.
* *AI Utility:* Allows the AI to automatically enforce data safety policies, ensuring that compliance logs are continuously generated according to architectural requirements.
