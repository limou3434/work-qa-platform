#!/bin/sh
set -e

mysql -h work-mysql -u root -pQwe54188_ --skip-ssl <<'EOF'
CREATE DATABASE IF NOT EXISTS work_qa_platform
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'wqp'@'%' IDENTIFIED BY 'Qwe54188_';

GRANT ALL PRIVILEGES ON work_qa_platform.* TO 'wqp'@'%';
FLUSH PRIVILEGES;
EOF

# 只在 migrations 不存在时 init（只会成功一次）
if [ ! -d "migrations" ]; then
  echo "Init migrations..."
  flask db init
fi

echo "Running db upgrade..."
flask db upgrade || true
# upgrade 失败不阻止服务启动（非常关键）

echo "Starting gunicorn..."
exec gunicorn -w 4 -b 0.0.0.0:8000 app:app
