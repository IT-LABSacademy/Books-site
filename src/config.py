
from environs import Env
import os


env = Env()
env.read_env()

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.str("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
MYURL = env.str("MYURL")

DBNAME=env.str("DBNAME")
DBUSER=env.str("DBUSER")
DBPASSWORD=env.str("DBPASSWORD")
