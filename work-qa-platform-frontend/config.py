""" 文件描述
存放关于 Flask 对象的相关配置
"""

import os

SPRING_PROFILES_ACTIVE = os.getenv('SPRING_PROFILES_ACTIVE', 'develop').lower() 

# 数据库配置
""" 创建数据库的脚本
create database work_qa_platform
character set utf8mb4
collate utf8mb4_unicode_ci;
"""

if SPRING_PROFILES_ACTIVE == 'release':
    SERVER_IP = 'work-mysql'
    PASSWORD = os.getenv('WORK_MYSQL_PASSWD', 'Qwe54188_')
else: # develop
    SERVER_IP = '127.0.0.1'
    PASSWORD = 'Qwe54188_'
USERNAME                = 'wqp'
SERVER_PORT             = '3306'
DATABASE_NAME           = 'work_qa_platform'
DB_URI                  = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, SERVER_IP, SERVER_PORT, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
MAIL_SERVER = 'smtp.qq.com'                             # SMTP 服务器地址(这里配置的是 qq 的)
MAIL_USE_SSL = True                                     # 使用 SSL 加密
MAIL_PORT = 465                                         # qq 邮箱服务器公开的端口号
MAIL_USERNAME = os.getenv('EMAIL_USER_NAME')            # 邮箱账户
MAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')             # 授权密码
MAIL_DEFAULT_SENDER = MAIL_USERNAME # 默认发送者

# 会话配置
SECRET_KEY = "limou3434" # 用于加密用户会话信息

if __name__ == '__main__':
    print(SQLALCHEMY_DATABASE_URI)
    print(MAIL_USERNAME)
    print(MAIL_PASSWORD)
