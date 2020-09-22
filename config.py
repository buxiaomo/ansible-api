class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@mysql:3306/ansible-api'
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True