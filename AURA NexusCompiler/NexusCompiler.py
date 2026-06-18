# ======================================================================
# AURA NexusCompiler v2.2 [Глобальная фильтрация шумных директорий]
# by AURA (Gemini Personal Agent) and TeymurNurullaev (Human)
# ======================================================================

import os
from pathlib import Path

# ======================================================================
# БЛОК РУЧНОЙ НАСТРОЙКИ АРХИТЕКТУРЫ (КОНФИГУРАЦИЯ)
# ======================================================================

# 1. Абсолютный путь к целевой директории для сканирования
TARGET_DIR = "/var/demo_project"

# 2. АБСОЛЮТНЫЙ путь к файлу, в который будет записан результат
OUTPUT_MARKDOWN_FILE = "/var/rezult/directory_structure.md"

# 3. Точечные каталоги, которые НЕ нужно открывать (Относительно TARGET_DIR)
# Режим 1: Без "*" в конце — папка покажется в дереве, но скрипт НЕ зайдет внутрь.
# Режим 2: С "/*" в конце — скрипт покажет первый уровень вложений, но НЕ пойдет глубже.
IGNORE_DEEP_SCAN = {
    "/Private/lib",       
    "/BDGSite/Package/*", 
    "/Tempfile",
    "/Public/file",
    "test.php"
}

# 4. Имена папок, содержимое которых нужно полностью ИГНОРИРОВАТЬ (разделитель через ";")
# Скрипт покажет саму папку в дереве, но никогда не пойдет внутрь неё, на каком бы уровне она ни лежала.
EXCLUDE_DIR_NAMES_STR = "css;js;lib;.git;.idea;tgusers;image"

# 5. Расширения файлов, которые вообще НЕ нужно заносить в дерево
EXCLUDE_EXTENSIONS_STR = ".jpg;.png;.gif;.ico;.css;.js;.txt;.json;.session"

# 6. Семантическая карта комментариев (Относительно TARGET_DIR)
COMMENTS_MAP = {
    "/": "Корень семантического ядра account.24trade.org",
    "/BDGSite": "Семантический пре-роутер",
    "/Worker": "Каста исполнительных агентов системы",
    "/Worker/Consultant.php": "Исполнительный орган (AI Worker)",
    "/Context": "Пространство сборки контекста и слоев состояний",
    "/Context/Assembly.php": "Сборщик слоев памяти (Context Assembly Engine)",
    "/Bridge": "Шлюзы связи с внешними средами",
    "/Bridge/Qdrant.php": "Коннектор к векторной базе знаний",
    "/Bridge/Neocortex.php": "Шлюз к LLM (OpenAI / Claude / YandexGPT)",
}

# ======================================================================
# СИСТЕМНЫЙ ДВИЖОК КОМПИЛЯЦИИ ДЕРЕВА
# ======================================================================

class DirectoryTreeCompiler:
    def __init__(self, root_path: str, exclude_exts: str, exclude_dirs: str, ignore_deep: set, comments: dict):
        self.root = Path(root_path).resolve()
        self.exclude_exts = [ext.strip().lower() for ext in exclude_exts.split(";") if ext.strip()]
        # Парсим список игнорируемых имен папок
        self.exclude_dir_names = [d.strip().lower() for d in exclude_dirs.split(";") if d.strip()]
        self.comments = comments
        
        self.tree_lines = []
        self.manifests_map = {}  
        
        self.strict_blocks = set()   
        self.wildcard_blocks = set() 
        
        for path in ignore_deep:
            cleaned = path.strip().rstrip('/')
            if cleaned.endswith('*'):
                self.wildcard_blocks.add(cleaned[:-2].rstrip('/'))
            else:
                self.strict_blocks.add(cleaned)

    def _get_relative_virtual_path(self, current_path: Path) -> str:
        if current_path == self.root:
            return "/"
        rel = current_path.relative_to(self.root)
        return "/" + rel.as_posix()

    def _should_exclude_file(self, path: Path) -> bool:
        return path.suffix.lower() in self.exclude_exts

    def compile(self):
        if not self.root.exists() or not self.root.is_dir():
            raise FileNotFoundError(f"Указанная директория не существует: {self.root}")
            
        self.tree_lines = []
        self.manifests_map = {}
            
        root_comment = self.comments.get("/", "")
        root_suffix = f"  <-- {root_comment}" if root_comment else ""
        self.tree_lines.append(f"/{self.root.name}/ {root_suffix}")
        
        self._build_tree(self.root, "")
        
        # Компиляция трехблочной структуры данных
        final_document = []
        
        # --- БЛОК 1: System Overview ---
        final_document.append("## 1. System Overview\n")
        root_manifest = self.manifests_map.get("/")
        if root_manifest:
            final_document.append(root_manifest.strip() + "\n")
        else:
            final_document.append("> *Root manifest.md not found in target directory.*\n")
            
        # --- БЛОК 2: Directory Topology ---
        final_document.append("## 2. Directory Topology\n")
        final_document.append("```")
        final_document.append("\n".join(self.tree_lines))
        final_document.append("```\n")
        
        # --- БЛОК 3: Component Manifests ---
        final_document.append("## 3. Component Manifests\n")
        for v_path in sorted(self.manifests_map.keys()):
            if v_path == "/":
                continue
                
            content = self.manifests_map[v_path].strip()
            final_document.append(f"### 📂 Node: `{v_path}`")
            final_document.append(f"> **Context Boundary:** Ниже представлен манифест управления контекстом узла.")
            final_document.append("\n" + content + "\n")
            final_document.append("---\n")
            
        return "\n".join(final_document)

    def _build_tree(self, current_dir: Path, prefix: str):
        try:
            entries = sorted(list(current_dir.iterdir()), key=lambda e: (not e.is_dir(), e.name.lower()))
        except PermissionError:
            return

        manifest_file = current_dir / "manifest.md"
        if manifest_file.is_file():
            try:
                v_path = self._get_relative_virtual_path(current_dir)
                self.manifests_map[v_path] = manifest_file.read_text(encoding="utf-8")
            except Exception:
                pass

        filtered_entries = []
        for entry in entries:
            if entry.name.startswith('#'):
                continue
            if entry.is_file() and entry.name.lower() == "manifest.md":
                continue
            if entry.is_file() and self._should_exclude_file(entry):
                continue
            filtered_entries.append(entry)

        count = len(filtered_entries)
        for i, entry in enumerate(filtered_entries):
            is_last = (i == count - 1)
            
            virtual_path = self._get_relative_virtual_path(entry)
            comment = self.comments.get(virtual_path, "")
            comment_suffix = f"  <-- {comment}" if comment else ""
            connector = "└── " if is_last else "├── "
            
            if entry.is_dir():
                self.tree_lines.append(f"{prefix}{connector}{entry.name}/{comment_suffix}")
                
                # РЭБ-Контур 1: Фильтрация по глобальному имени папки (css;js;lib)
                if entry.name.lower() in self.exclude_dir_names:
                    continue
                
                # РЭБ-Контур 2: Точечная изоляция пути из IGNORE_DEEP_SCAN
                if virtual_path in self.strict_blocks:
                    continue
                
                # РЭБ-Контур 3: Проверка wildcard-зоны родителя
                parent_virtual_path = self._get_relative_virtual_path(current_dir)
                if parent_virtual_path in self.wildcard_blocks:
                    continue
                
                next_prefix = prefix + ("    " if is_last else "│   ")
                self._build_tree(entry, next_prefix)
            else:
                self.tree_lines.append(f"{prefix}{connector}{entry.name}{comment_suffix}")


if __name__ == "__main__":
    import traceback

    # Передаем новую переменную в инициализатор
    compiler = DirectoryTreeCompiler(
        root_path=TARGET_DIR,
        exclude_exts=EXCLUDE_EXTENSIONS_STR,
        exclude_dirs=EXCLUDE_DIR_NAMES_STR,
        ignore_deep=IGNORE_DEEP_SCAN,
        comments=COMMENTS_MAP
    )
    
    try:
        compiled_output = compiler.compile()
        
        output_path = Path(OUTPUT_MARKDOWN_FILE).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(compiled_output, encoding="utf-8")
        
        print(f"[Успешно] Семантический контур v2.2 развернут.")
        print(f"[Спецификация сохранена]: {output_path}")
        
    except Exception as e:
        print(f"\n[Ошибка рантайма] Не удалось скомпилировать дерево: {e}")
        print("-" * 60)
        traceback.print_exc()
        print("-" * 60)
