import os

import dotenv

path_env = os.getenv('DOTENV') or os.path.join(os.getcwd(), '.env')
if os.path.exists(path_env):
    dotenv.load_dotenv(path_env)

DB_NAME = os.getenv('DBNAME')
DB_PASSWORD = os.getenv('DBPASSWORD')
DB_USER = os.getenv('DBUSER')
DB_HOST = os.getenv('DBHOST')
