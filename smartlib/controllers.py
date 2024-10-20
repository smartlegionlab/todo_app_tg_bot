# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------


class TaskController:
    def __init__(self, db):
        self.db = db

    def create_user(self, full_name):
        user = self.db.add_user(full_name)
        return user

    def get_user(self, user_id):
        user = self.db.get_user(user_id)
        return user

    def get_all_users(self):
        users = self.db.get_all_users()
        return users

    def update_user(self, user_id, full_name):
        user = self.db.update_user(user_id, full_name)
        return user

    def delete_user(self, user_id):
        user = self.db.delete_user(user_id)
        return user

    def create_task(self, user_id, name):
        task = self.db.add_task(user_id, name)
        return task

    def get_task(self, task_id):
        task = self.db.get_task(task_id)
        return task

    def get_all_tasks(self, user_id):
        tasks = self.db.get_all_tasks(user_id)
        return tasks

    def update_task(self, task_id, name=None, completed=None):
        task = self.db.update_task(task_id, name, completed)
        return task

    def delete_task(self, task_id):
        task = self.db.delete_task(task_id)
        return task
