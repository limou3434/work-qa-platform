# QA-platform

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
# 安装相关的第三方库
pip install flask
pip install subprocess
pip install pymysql
pip install flask-sqlalchemy
pip install Flask-Mail
pip install Flask-Migrate
pip install WTForms
pip install email_validator
pip install gunicorn

# 克隆远端仓库
git clone https://gitee.com/limou3434/qa-platform.git
rm -rf migrations # 删除重新生成

# 进入 MySQL 创建一个数据库
mysql -u <your_name> -p
mysql >: create database qa_platform character set utf8mb4 collate utf8mb4_unicode_ci;
mysql >: exit

# 使用脚本生成需要的数据表
flask db init # 就会生成相关的 migrations 配置文件夹, 这一步只需要执行一次
flask db migrat # 识别 ORM 模型改动, 生成迁移脚本, migrations 文件夹内开始有内容, 这一命令可以重复执行
flask db upgrade # 运行迁移脚本, 同步到数据库中, 此时数据库就会出现新的表

# 部署项目
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:<your_port> app:app --daemon

# 后续使用浏览器访问即可
```

## 技术选型

- `Python` 编程语言
- `Flask Web` 框架
- `SQLAlchemy ORM` 数据库工具
- `Gunicorn WSGI HTTP`服务器

## 参与贡献

limou3434