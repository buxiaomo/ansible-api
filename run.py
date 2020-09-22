import click
from app import create_app
from app.models.models import *
from flask_script import Manager

app = create_app()
manager = Manager(app)


@manager.command
def initdb():
    db.drop_all()
    db.create_all()
    click.echo('初始化数据库')


@manager.command
def insert():
    playbook = PlayBookModel(name='test')
    db.session.add(playbook)
    db.session.commit()
    click.echo('添加一个类别')


if __name__ == '__main__':
    manager.run()
