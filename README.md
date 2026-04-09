# Todo App Telegram Bot <sup>v1.0.0</sup>

---

Asynchronous task manager. [Use Telegram bot](https://t.me/smarttodoappbot). 

---

> TODO app (task management app) is a simple app that allows users to create, edit, delete and track their tasks.

This bot can be deployed even on a phone using [Termux](https://github.com/termux).

---

## ⚠️ Disclaimer

**By using this software, you agree to the full disclaimer terms.**

**Summary:** Software provided "AS IS" without warranty. You assume all risks.

**Full legal disclaimer:** See [DISCLAIMER.md](DISCLAIMER.md)

---

## Other to-do list apps:

- [Desktop ToDo app](https://github.com/smartlegionlab/smart-todo-app-desktop)
- [Cli ToDo app](https://github.com/smartlegionlab/todo-app-cli)
- [Web ToDo app](https://github.com/smartlegionlab/todo-app-django)

---

## What's new:

- Architectural code refactoring.
- The code has been rewritten using the MVC (Model-View-Controller) architecture.
- Bugs fixed.
- The user interface has been simplified and improved.
- The structure and readability of the code has been improved, making it easier to maintain and extend functionality. (SOLID, DRY, MVC).

---

## In the next updates:

- Adding comments to tasks.
- Adding subtasks to tasks.

---

## Help:

- Clone the repository.
- Create a bot and get a token using: [@BotFather](https://t.me/BotFather).

### MariaDb:

- `sudo mysql -u root -p`
- `CREATE USER 'USER_NAME'@'localhost' IDENTIFIED BY 'PASSWORD';`
- `CREATE DATABASE database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;`
- `GRANT ALL PRIVILEGES ON database_name.* TO 'USER_NAME'@'localhost';`
- `FLUSH PRIVILEGES;`


### Create a `.env` file in the project folder:

```.env
API_TOKEN="<token>"
DB_USER="<db_user>"
DB_NAME="<db_name>"
DB_PASSWORD="<password>"
DB_HOST="<host>"
```

### Use:

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python bot.py`

---

### Termux:

- Install Termux
- Run Termux app
- `termux-wake-lock`
- `pkg update`
- `pkg upgrade`
- `pkg install termux-tools`
- `pkg install python`
- `pkg install python-pip`
- `pkg install python-pip`
- `pkg install git`
- `pkg install vim`
- `pkg install mariadb`


- The problem with installing aiogram is solved by installing rust: `pkg install rust`


- `mysql_install_db`
- `mysqld_safe &`
- `mysql -u root -p`
- `ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_password';`
- `CREATE USER 'USER_NAME'@'localhost' IDENTIFIED BY 'PASSWORD';`
- `CREATE DATABASE database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;`
- `GRANT ALL PRIVILEGES ON database_name.* TO 'USER_NAME'@'localhost';`
- `FLUSH PRIVILEGES;`
- Clone repo.
- Create a `.env` file in the project folder:


```.env
API_TOKEN="<token>"
DB_USER="<db_user>"
DB_NAME="<db_name>"
DB_PASSWORD="<password>"
DB_HOST="<host>"
```

### Use:

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python bot.py`

---

## License

BSD 3-Clause License - Copyright (©) 2026, [Alexander Suvorov](https://github.com/smartlegionlab)