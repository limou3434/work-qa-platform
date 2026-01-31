# work-qa-platform

## 项目介绍
一个基于 `flask` 的简单问答平台

## 软件特点
- 用户认证：用户可以注册、登录和退出
- 问答功能：用户可以提问、回答以及其他用户的问题
- 邮件支持：集成邮件服务，用于用户通知等
- 数据库集成：使用 `ORM` 模型进行数据操作
- 蓝图支持：模块化应用设计，易于扩展和维护

## 安装教程
``` ssh
# 创建虚拟环境
conda create -n myenv python=3.10
conda activate myenv

# 克隆远端仓库
git clone https://gitee.com/limou3434/work-qa-platform.git
rm -rf migrations # 删除重新生成

# 安装相关的第三方库
pip install -r requirements.txt

# 进入 MySQL 创建一个数据库
mysql -h 127.0.0.1 -u root -pQwe54188_ <<'EOF'
-- 项目数据库
DROP DATABASE IF EXISTS `work_qa_platform`;
CREATE DATABASE `work_qa_platform`
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- 项目用户
DROP USER IF EXISTS 'wqp'@'%';
CREATE USER 'wqp'@'%' IDENTIFIED BY 'Qwe54188_';
GRANT ALL PRIVILEGES ON `work_qa_platform`.* TO 'wqp'@'%';
FLUSH PRIVILEGES;
EOF

# 使用脚本生成需要的数据表
flask db init # 就会生成相关的 migrations 配置文件夹, 这一步只需要执行一次
flask db migrate # 识别 ORM 模型改动, 生成迁移脚本, migrations 文件夹内开始有内容, 这一命令可以重复执行
flask db upgrade # 运行迁移脚本, 同步到数据库中, 此时数据库就会出现新的表

# 设置环境变量
EMAIL_USER_NAME=xxxxxx@qq.com
EMAIL_PASSWORD=xxxxxxx

# 开发环境
python app.py

# 生产环境
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app --daemon

# 后续使用浏览器访问即可
```

## 技术选型

- `Python` 编程语言
- `Flask Web` 框架
- `SQLAlchemy ORM` 数据库工具
- `Gunicorn WSGI HTTP`服务器

## 参与贡献

limou3434
