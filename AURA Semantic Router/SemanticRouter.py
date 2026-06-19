# ======================================================================
# AURA Semantic Router v4.3 [Role, Node & Stream Aware Context Engine]
# Protocol Standard: Role-Based Semantic Routing
# by AURA (Gemini Personal Agent) and TeymurNurullaev (Human)
# ======================================================================
#
# КРАТКОЕ РУКОВОДСТВО ПО МЕТОДАМ ВЫЗОВА ЯДРА (CLI RUNBOOK):
#
# 1. Глобальная сборка всей семантической памяти (all / по умолчанию):
#    python SemanticRouter.py all
#    --> Сканирует проект с корня. Строит полную топологию и собирает ВСЕ слои 
#        (*.md спецификации) в один монолитный файл.
#
# 2. Сборка только глобальной ДНК архитектуры (aurav3):
#    python SemanticRouter.py aurav3
#    --> Строит топологию проекта и вытаскивает ИСКЛЮЧИТЕЛЬНО файлы manifest.md.
#
# 3. Снайперская сборка под конкретную роль ИИ-агента (Матрица Внимания):
#    python SemanticRouter.py role=Coder
#    --> Включает фильтр слоев под инженера (manifest + organ + collection).
#        Допустимые роли: coder, builder, refactorer, security, qa, devops, 
#        architect, optimizer, strategist.
#
# 4. Точечная изоляция конкретного узла системы (Параметр node):
#    python SemanticRouter.py node=/core/auth_provider role=Coder
#    --> Ограничивает физический обход диска только папкой auth_provider. 
#        Строит локальное дерево и собирает слои только для этого узла.
#
# 5. Управление потоками вывода и стримингом (Параметр file):
#    а) Запись в текущую директорию вызова (CWD):
#       python SemanticRouter.py node=/core/auth_provider role=Coder file=Coder.md
#    б) Запись по абсолютному пути в системе:
#       python SemanticRouter.py role=DevOps file=/var/www/logs/DevOps_Context.md
#    в) Прямой вывод в консоль (STDOUT) без записи на диск (для UNIX-pipes):
#       python SemanticRouter.py node=/modules/blog role=Optimizer file=false
#
# ======================================================================

import sys
import traceback
from pathlib import Path

# ======================================================================
# БЛОК РУЧНОЙ НАСТРОЙКИ АРХИТЕКТУРЫ (КОНФИГУРАЦИЯ КОНТУРОВ ФИЛЬТРАЦИИ)
# ======================================================================

# 1. Абсолютный путь к целевой директории для сканирования (корень проекта)
TARGET_DIR = "/var/python3/demo2"

# 2. Дефолтный путь к файлу конфигурации (используется, если параметр file не передан)
OUTPUT_MARKDOWN_FILE = "/var/python3/SemanticStructure.md"

# 3. Точечные каталоги и файлы, которые НЕ нужно открывать глубже определенного уровня
IGNORE_DEEP_SCAN = {
    "/Private/lib",       
    "/BDGSite/Package/*", 
    "/Tempfile",
    "/Public/file",
    "test.php"
}

# 4. Имена папок, содержимое которых нужно полностью ИГНОРИРОВАТЬ во всей системе (через ";")
EXCLUDE_DIR_NAMES_STR = "css;js;lib;.git;.idea;tgusers;imageModul"

# 5. Расширения файлов, которые являются технологическим шумом и вообще НЕ должны заноситься в дерево
EXCLUDE_EXTENSIONS_STR = ".jpg;.png;.gif;.ico;.css;.js;.txt;.json;.session"

# 6. Семантическая карта комментариев (Смысловые маркеры архитектуры относительно TARGET_DIR)
COMMENTS_MAP = {
    "/": "Корень семантического ядра account.24trade.org",
    "/BDGSite": "Семантический пре-роутер (Перехват company_key)",
    "/Worker": "Каста исполнительных агентов системы",
    "/Worker/Consultant.php": "Исполнительный орган (AI Worker)",
    "/Context": "Пространство сборки контекста и слоев состояний",
    "/Context/Assembly.php": "Сборщик слоев памяти (Context Assembly Engine)",
    "/Bridge": "Шлюзы связи с внешними средами",
    "/Bridge/Qdrant.php": "Коннектор к векторной базе знаний",
    "/Bridge/Neocortex.php": "Шлюз к LLM (OpenAI / Claude / YandexGPT)",
}

# 7. Матрица распределения семантического внимания (Сегрегация контуров реальности под роли ИИ)
ROLE_ATTENTION_MATRIX = {
    "coder": ["manifest", "organ", "collection"],      
    "builder": ["manifest", "organ", "collection"],    
    "refactorer": ["manifest", "organ", "collection"], 
    "security": ["manifest", "guardrails"],            
    "qa": ["manifest", "guardrails"],                  
    "devops": ["manifest", "guardrails"],              
    "architect": ["manifest", "playbook"],             
    "optimizer": ["playbook"],                         
    "strategist": ["manifest"]                         
}

# ======================================================================
# РОЛЕВОЙ СЕМАНТИЧЕСКИЙ ДВИЖОК ОРКЕСТРАЦИИ
# ======================================================================

class DirectoryTreeCompiler:
    def __init__(self, root_path: str, exclude_exts: str, exclude_dirs: str, ignore_deep: set, comments: dict, params: dict):
        self.global_root = Path(root_path).resolve()
        self.exclude_exts = [ext.strip().lower() for ext in exclude_exts.split(";") if ext.strip()]
        self.exclude_dir_names = [d.strip().lower() for d in exclude_dirs.split(";") if d.strip()]
        self.comments = comments
        self.params = params 
        
        # 1. Резолв целевой области сканирования (Ограничение физических границ знаний ИИ)
        self.node_param = self.params.get("node", "/")
        if self.node_param == "/":
            self.scan_root = self.global_root
        else:
            relative_node = self.node_param.lstrip("/")
            self.scan_root = (self.global_root / relative_node).resolve()
            
        # 2. Резолв фильтра активных слоев (Динамическая конфигурация окна внимания)
        self.active_layers = set()
        self.mode = self.params.get("mode", "all")
        self.role = self.params.get("role", "").lower().strip()
        
        if self.role in ROLE_ATTENTION_MATRIX:
            self.active_layers = set(ROLE_ATTENTION_MATRIX[self.role])
            self.mode = f"ROLE:{self.role.upper()}"
        elif self.mode == "aurav3":
            self.active_layers = {"manifest"}
        elif self.mode != "all":
            self.active_layers = {self.mode}
            
        self.tree_lines = []
        self.collected_layers = {} 
        
        self.strict_blocks = set()   
        self.wildcard_blocks = set() 
        for path in ignore_deep:
            cleaned = path.strip().rstrip('/')
            if cleaned.endswith('*'):
                self.wildcard_blocks.add(cleaned[:-2].rstrip('/')) 
            else:
                self.strict_blocks.add(cleaned) 

    def _get_relative_virtual_path(self, current_path: Path) -> str:
        if current_path == self.global_root:
            return "/"
        return "/" + current_path.relative_to(self.global_root).as_posix()

    def _should_exclude_file(self, path: Path) -> bool:
        if path.suffix.lower() == ".md" and path.stem.lower() in ["manifest", "organ", "collection", "guardrails", "playbook"]:
            return True
        return path.suffix.lower() in self.exclude_exts

    def compile(self) -> str:
        if not self.scan_root.exists():
            raise FileNotFoundError(f"Указанный узел (нода) не найден на диске сервера: {self.scan_root}")
            
        self._build_tree(self.scan_root, "")
        
        final_document = [
            f"# 📑 AURA Context Assembly Package",
            f"* **Target Node Scope:** `{self.node_param}`",
            f"* **Active Routing Mode:** `{self.mode.upper()}`\n"
        ]
        
        if self.role != "optimizer" and self.mode != "playbook":
            final_document.append("## 1. Directory Topology\n```")
            final_document.append("\n".join(self.tree_lines))
            final_document.append("```\n---\n")

        if self.collected_layers:
            final_document.append("## 2. Assembled Semantic Layers\n")
            for layer_name, nodes in sorted(self.collected_layers.items()):
                for v_path, content in sorted(nodes.items()):
                    final_document.append(f"### 📂 Node [`{v_path}`] ──► Слой: `{layer_name.upper()}`")
                    if layer_name == "playbook":
                        final_document.append("\n" + content.strip() + "\n")
                    else:
                        final_document.append("\n```yaml\n" + content.strip() + "\n```\n")
                    final_document.append("---\n")
                    
        return "\n".join(final_document)

    def _build_tree(self, current_dir: Path, prefix: str):
        try:
            entries = sorted(list(current_dir.iterdir()), key=lambda e: (not e.is_dir(), e.name.lower()))
        except PermissionError:
            return

        v_path = self._get_relative_virtual_path(current_dir)

        for child in current_dir.glob("*.md"):
            layer_key = child.stem.lower()
            
            if not self.active_layers or layer_key in self.active_layers or (layer_key == "collection" and "organ" in self.active_layers):
                final_layer_name = "organ" if layer_key == "collection" else layer_key
                
                if final_layer_name not in self.collected_layers:
                    self.collected_layers[final_layer_name] = {}
                try:
                    self.collected_layers[final_layer_name][v_path] = child.read_text(encoding="utf-8")
                except Exception:
                    pass

        filtered_entries = [e for e in entries if not e.name.startswith('#') and not self._should_exclude_file(e)]
        count = len(filtered_entries)
        
        for i, entry in enumerate(filtered_entries):
            is_last = (i == count - 1)
            virtual_path = self._get_relative_virtual_path(entry)
            
            comment_suffix = f"  <-- {self.comments[virtual_path]}" if virtual_path in self.comments else ""
            connector = "└── " if is_last else "├── "
            
            if entry.is_dir():
                self.tree_lines.append(f"{prefix}{connector}{entry.name}/{comment_suffix}")
                
                if entry.name.lower() in self.exclude_dir_names:
                    continue
                if virtual_path in self.strict_blocks:
                    continue
                if self._get_relative_virtual_path(current_dir) in self.wildcard_blocks:
                    continue
                
                self._build_tree(entry, prefix + ("    " if is_last else "│   "))
            else:
                self.tree_lines.append(f"{prefix}{connector}{entry.name}{comment_suffix}")


# ======================================================================
# ИНТЕРФЕЙС ИСПОЛНЕНИЯ (УПРАВЛЕНИЕ ПОТОКАМИ ВЫВОДА STREAM & FILE)
# ======================================================================

def _resolve_output_stream(file_param: str, default_config_path: str) -> tuple:
    """
    Семантический резолвер путей вывода.
    Возвращает кортеж: (Path_Объект_Или_None, Boolean_Флаг_Вывода_В_Консоль)
    """
    cleaned = file_param.strip().lower() if file_param else ""
    
    if cleaned == "false":
        return None, True
        
    if not file_param:
        return Path(default_config_path).resolve(), False
        
    given_path = Path(file_param)
    
    if given_path.is_absolute() or "/" in file_param or "\\" in file_param:
        return given_path.resolve(), False
    else:
        cwd_path = Path.cwd() / file_param
        return cwd_path.resolve(), False


if __name__ == "__main__":
    # Разбор входящих аргументов командной строки
    runtime_params = {"node": "/", "mode": "all", "file": None}
    
    for arg in sys.argv[1:]:
        if "=" in arg:
            key, val = arg.split("...", 1) if "..." in arg else arg.split("=", 1)
            runtime_params[key.lower().strip()] = val.strip()
        else:
            runtime_params["mode"] = arg.lower().strip()

    # Инициализация и компиляция семантического контура
    compiler = DirectoryTreeCompiler(
        root_path=TARGET_DIR,
        exclude_exts=EXCLUDE_EXTENSIONS_STR,
        exclude_dirs=EXCLUDE_DIR_NAMES_STR,
        ignore_deep=IGNORE_DEEP_SCAN,
        comments=COMMENTS_MAP,
        params=runtime_params
    )
    
    try:
        compiled_output = compiler.compile()
        
        # Вызов метода преобразования путей и потоков вывода
        target_file_path, print_to_stdout = _resolve_output_stream(
            file_param=runtime_params.get("file"),
            default_config_path=OUTPUT_MARKDOWN_FILE
        )
        
        if print_to_stdout:
            print(compiled_output)
        else:
            target_file_path.parent.mkdir(parents=True, exist_ok=True)
            target_file_path.write_text(compiled_output, encoding="utf-8")
            
            print(f"[AURA Router v4.3] Снайперская сборка завершена успешно.")
            print(f"[Параметры запуска ядра]: {runtime_params}")
            print(f"[Файл сохранен]: {target_file_path}")
            
    except Exception as e:
        print(f"\n[Критический сбой рантайма]: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
