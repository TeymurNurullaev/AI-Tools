
# AITools / AURA NexusCompiler

### Project Description

AURA NexusCompiler is a system tool designed for the automatic generation of semantic topologies and distributed memory systems within large-scale software codebases. The script scans the target directory of a project, filters out technical noise, and compiles distributed directory-level description files (`manifest.md`) into a single engineering specification. The resulting document acts as a universal context bridge, enabling any modern LLM (OpenAI, Claude, YandexGPT) to instantly comprehend the project's architecture, business logic, and inter-system connections without ingesting raw source code.

### Solved Problems and Target Audience

* **LLM Context Window Suffocation:** Large projects exceed the context limits of models or clutter them with infrastructure noise (libraries, styles). The tool compresses the architecture into pure meanings, saving up to 90% of the AI's active context window.
* **Model Hallucinations:** LLMs frequently mistake the actual purpose of isolated modules. The script delivers a rigorous source of truth, eliminating incorrect code interpretations.
* **Documentation Decay:** Centralized technical specifications degrade as the system scales. This approach distributes documentation into folders ("DNA passports"), embedding documentation maintenance into the active development process.

**Target Audience:**

* **AI Agents:** For rapid, error-free onboarding and alignment within a complex codebase.
* **System Architects:** For monitoring the geometry, structural bounds, and general topology of an expanding system.
* **Developers:** For instant understanding of unfamiliar modules and workflows via local node manifests.

### Output Data Structure (3 Blocks)

The compiler outputs a unified Markdown file structured into three logical layers:

1. **System Overview:** Top-level global project context extracted from the root directory manifest.
2. **Directory Topology:** A clean, filtered pseudographic directory tree stripped of uninformative and system files.
3. **Component Manifests:** A sequential registry of all discovered local directory passports encapsulated inside strict `Context Boundary` zones.

### `manifest.md` Format Specification

Every directory that requires mapping for the AI should contain a lightweight `manifest.md` file using the following structure:

```yaml
---
node: "/Public/Module/AI"
type: "core_module"
subsystem: "BDGSite AI Engine"
db_relations:
  - table: "ai_sessions"
    type: "write/read"
  - table: "company_registry"
    type: "read_only"
external_connections:
  - system: "Qdrant Vector DB"
    protocol: "gRPC"
---
```

# Category Purpose
Description of the business logic and the specific role of this node in the ecosystem.

## Internal Architecture and Relative Paths
* `Router.php` — Description of a specific file.

## Inter-system Connections and Data Flows
1. Detailed mapping of traffic and data propagation inside the module.


### Setup and Configuration

Runtime behavior is managed inside the `MANUAL ARCHITECTURE CONFIGURATION BLOCK` within the script:

* `TARGET_DIR`: The absolute path to the target project directory to be scanned.
* `OUTPUT_MARKDOWN_FILE`: The absolute path where the final report specification file will be written.
* `IGNORE_DEEP_SCAN`: A list of paths for selective scan blocking. Paths without a trailing `*` prevent the scanner from entering the folder entirely. Paths ending with `/*` reveal only the first-level contents of the directory.
* `EXCLUDE_DIR_NAMES_STR`: A semicolon-separated string of folder names to show in the tree but skip deep scanning (`css;js;lib;.git`).
* `EXCLUDE_EXTENSIONS_STR`: A list of file extensions completely excluded from the final report layout.
* `COMMENTS_MAP`: A dictionary establishing hardcoded base comments for key tree nodes.

### Usage Instructions

1. Place a `manifest.md` file into the root directory of your project and additional manifest files into subdirectories requiring indexing.
2. Open `NexusCompiler.py` and fill in the configuration block variables to match your server configuration.
3. Execute the compiler tool from your terminal interface:

```bash
python3 NexusCompiler.py

```

4. Upload or feed the generated `directory_structure.md` file to your LLM workspace as the foundational context before initializing development operations.


by AURA (Gemini Personal Agent) and TeymurNurullaev (Human)
