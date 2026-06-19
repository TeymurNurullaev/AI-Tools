#!/bin/bash

# ======================================================================
# AURA Test Environment Generator v1.0
# Создает изолированную тестовую структуру для проверки SemanticRouter.py
# ======================================================================

# Папка полигона (создается в текущей директории)
TEST_ROOT="/var/python3/demo2"

echo "[Инициализация] Создаем тестовую экосистему в: $TEST_ROOT"

# 1. Создание структуры папок
mkdir -p "$TEST_ROOT/core/auth_provider"
mkdir -p "$TEST_ROOT/core/database_proxy"
mkdir -p "$TEST_ROOT/modules/blog"
mkdir -p "$TEST_ROOT/modules/billing"
mkdir -p "$TEST_ROOT/public/css"
mkdir -p "$TEST_ROOT/public/js"
mkdir -p "$TEST_ROOT/private/lib"

# 2. Генерация файлов для /core/auth_provider (Mission-Critical Узел, все 4 слоя)
cat << 'EOF' > "$TEST_ROOT/core/auth_provider/manifest.md"
identity:
  node: "/core/auth_provider"
  type: "system_core"
  subsystem: "Security"
  criticality: "mission_critical"
dependencies:
  upstream: ["/gateway/ingress"]
EOF

cat << 'EOF' > "$TEST_ROOT/core/auth_provider/organ.md"
organ_identity:
  node: "/core/auth_provider"
  engine_pattern: "Stateless_Service"
runtime_interfaces:
  methods:
    - name: "validateSession"
      input_format: "JWT_String"
      output_format: "Boolean"
EOF

cat << 'EOF' > "$TEST_ROOT/core/auth_provider/guardrails.md"
security_policies:
  access_level: "isolated"
data_sensitivity:
  contains_credentials: true
  public_exposure_allowed: false
EOF

cat << 'EOF' > "$TEST_ROOT/core/auth_provider/playbook.md"
# playbook.md - Auth Provider Experience
* **2026-04-11:** Исправлена утечка памяти в валидаторе JWT. Введен TTL кэша 60 секунд.
* **Антипаттерн:** Запрещено писать сырые токены в лог-файлы рантайма.
EOF

# Имитируем рабочий код в этой папке
echo "<?php class AuthProvider {} ?>" > "$TEST_ROOT/core/auth_provider/auth.php"


# 3. Генерация файлов для /modules/blog (Стандартный рабочий модуль, 2 слоя)
cat << 'EOF' > "$TEST_ROOT/modules/blog/manifest.md"
identity:
  node: "/modules/blog"
  type: "execution_agent"
  subsystem: "Content"
  criticality: "medium"
EOF

cat << 'EOF' > "$TEST_ROOT/modules/blog/organ.md"
organ_identity:
  node: "/modules/blog"
  type_vc_flag: true
argument_routing_matrix:
  source: "$this->ArgMod()"
EOF

# Имитируем рабочий код, шаблоны и скрытый шум
echo "<?php class BlogModul {} ?>" > "$TEST_ROOT/modules/blog/blog.Modul.php"
echo "<h1>Blog List</h1>" > "$TEST_ROOT/modules/blog/bloglist.tpl"


# 4. Генерация файлов для /public/css и /private/lib (Шумные зоны для проверки РЭБ-фильтрации)
echo "body { color: #333; }" > "$TEST_ROOT/public/css/main.css"
echo "console.log('init');" > "$TEST_ROOT/public/js/app.js"
echo "secret_token_session_data" > "$TEST_ROOT/modules/blog/.session"
echo "<?php class ForeignLibrary {} ?>" > "$TEST_ROOT/private/lib/third_party.php"

# 5. Создаем один корневой манифест для общей картины
cat << 'EOF' > "$TEST_ROOT/manifest.md"
identity:
  node: "/"
  type: "root_manifest"
  subsystem: "Ecosystem Root"
EOF

echo "[Успешно] Тестовый полигон развернут в папке './aura_test_repo'."
echo "Перед тестом не забудь изменить TARGET_DIR в скрипте SemanticRouter.py на путь к этой папке!"
