# Todo app Telegram bot

---

Asynchronous task manager. Telegram bot. [Python](https://python.org) + [Aiogram](https://github.com/aiogram/aiogram/tree/dev-3.x).

---

> TODO app (task management app) is a simple app that allows users to create, edit, delete and track their tasks.

This bot can be deployed even on a phone using [Termux](https://github.com/termux).

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

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
