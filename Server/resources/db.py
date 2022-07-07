from flaskext.mysql import MySQL

mysql = MySQL()

def initialize_db(app):

    app.config["MYSQL_DATABASE_HOST"] = "localhost"
    app.config["MYSQL_DATABASE_USER"] = "root"
    app.config["MYSQL_DATABASE_PASSWORD"] = "rootroot"
    app.config["MYSQL_DATABASE_DB"] = "olx"

    mysql.init_app(app)
