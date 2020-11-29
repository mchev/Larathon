from peewee import *
from libraries.env import env

class Model:

    def db():
        try :

            if env('DB_CONNECTION') == 'mysql' :
                db = MySQLDatabase(env('DB_DATABASE'),
                                        user=env('DB_USERNAME'),
                                        password=env('DB_PASSWORD'),
                                        host=env('DB_HOST'),
                                        port=int(env('DB_PORT')))

            elif env('DB_CONNECTION') == 'postgresql' :
                db = PostgresqlDatabase(env('DB_DATABASE'),
                                        user=env('DB_USERNAME'),
                                        password=env('DB_PASSWORD'),
                                        host=env('DB_HOST'),
                                        port=int(env('DB_PORT')))

            elif env('DB_CONNECTION') == 'sqllite' :
                db = SqliteDatabase(env('DB_DATABASE'),
                                        user=env('DB_USERNAME'),
                                        password=env('DB_PASSWORD'),
                                        host=env('DB_HOST'),
                                        port=int(env('DB_PORT')))

            else :
                return print("%s n'est pas une connexion reconnnue." % env('DB_CONNECTION'))

            return db.connect()

        except :            
            print("Connexion impossible à la base %s" % env('DB_DATABASE'))