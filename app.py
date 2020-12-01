from flask import Flask, render_template, request
import mysql.connector
import os.path
from db_tunnel import DatabaseTunnel
from flask_cors import CORS

DB_HOST = "cs.westminstercollege.edu"
DB_SSH_PORT = 2322
DB_SSH_USER = "student"
DB_PORT = 3306

# Default connection information (can be overridden with command-line arguments)
DB_SSH_KEYFILE = "id_rsa.cmpt307"
DB_NAME = "rtk0720_final_project"
DB_USER = "token_2f91"
DB_PASSWORD = "tfH8abOjPBRtvaCA"


with \
    DatabaseTunnel(DB_SSH_KEYFILE) as tunnel:
        connection = mysql.connector.connect(host='localhost', port=tunnel.getForwardedPort(), database=DB_NAME, user=DB_USER, password=DB_PASSWORD, use_pure=True, autocommit=True)
        cursor = connection.cursor()
        
        app = Flask(__name__)
        CORS(app)
        @app.route('/')
        def index():
            cursor.execute("SELECT Pokemon.number, Pokemon.name, Location.name, Generation.name FROM Pokemon JOIN Location ON Pokemon.location = Location.ID JOIN Generation ON Pokemon.generation = Generation.ID")
            return render_template('index.html', userDetails=cursor)

        @app.route("/favorite", methods=[ "POST" ])
        def favorite(yeet):
            pokemon = request.form
            number = pokemon["number"]

            cursor.execute("CALL addToFavorite(" + number + ")")


            

        if __name__ == "__main__":
            app.run(debug=True)
