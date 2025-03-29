# config.py
import secrets
class Config:
    # This line of code is setting the SQLALCHEMY_DATABASE_URI configuration variable to a specific
    # database URI. In this case, it is specifying a MySQL database connection using the PyMySQL
    # driver, with the username 'root', an empty password, connecting to the localhost on port 3306,
    # and using the database named 'login'. This URI will be used by the application to connect to the
    # specified database.
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/tiendamotos'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///flaskdb.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_urlsafe(24)
    WEASYPRINT_DLL_DIRECTORIES="C:\Program Files (x86)\GTK2-Runtime\bin"
    #pip install --no-index --find-links=librerias -r requirements.txt