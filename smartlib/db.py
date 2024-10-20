# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from models import User, Task

Base = declarative_base()
load_dotenv()


class TaskDatabase:
    def __init__(self):
        self.engine = self.create_connection()
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    @classmethod
    def create_connection(cls):
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST', 'localhost')
        database = os.getenv('DB_NAME', 'tasks')
        return create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    def get_session(self):
        return self.Session()

    # User methods
    def add_user(self, full_name):
        session = self.get_session()
        new_user = User(full_name=full_name)
        session.add(new_user)
        session.commit()
        session.close()
        return new_user

    def get_user(self, user_id):
        session = self.get_session()
        user = session.query(User).filter(User.id == user_id).first()
        session.close()
        return user

    def get_all_users(self):
        session = self.get_session()
        users = session.query(User).all()
        session.close()
        return users

    def update_user(self, user_id, full_name):
        session = self.get_session()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.full_name = full_name
            session.commit()
        session.close()
        return user

    def delete_user(self, user_id):
        session = self.get_session()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()
        return user

    # Task methods
    def add_task(self, user_id, name):
        session = self.get_session()
        new_task = Task(user_id=user_id, name=name)
        session.add(new_task)
        session.commit()
        session.close()
        return new_task

    def get_task(self, task_id):
        session = self.get_session()
        task = session.query(Task).filter(Task.id == task_id).first()
        session.close()
        return task

    def get_all_tasks(self, user_id):
        session = self.get_session()
        tasks = session.query(Task).filter(Task.user_id == user_id).all()
        session.close()
        return tasks

    def update_task(self, task_id, name=None, completed=None):
        session = self.get_session()
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            if name is not None:
                task.name = name
            if completed is not None:
                task.completed = completed
            session.commit()
        session.close()
        return task

    def delete_task(self, task_id):
        session = self.get_session()
        task = session.query(Task).filter(Task.id == task_id).first()
        if task:
            session.delete(task)
            session.commit()
        session.close()
        return task
