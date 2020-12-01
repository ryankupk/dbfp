from flask import Flask, render_template, request, jsonify, make_response
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
            cursor.execute("SELECT COUNT(*) FROM Pokemon")
            curNumber = cursor.fetchall()
            cursor.execute("SELECT COUNT(*) FROM PokemonFavorite")
            favNumber = cursor.fetchall()
            cursor.execute("""SELECT Pokemon.number, Pokemon.name, Location.name, Generation.name FROM Pokemon 
                                JOIN Location ON Pokemon.location = Location.ID 
                                JOIN Generation ON Pokemon.generation = Generation.ID""")
            curPokes = cursor.fetchall()
            cursor.execute("""SELECT PokemonFavorite.number, PokemonFavorite.name, Location.name, Generation.name FROM PokemonFavorite 
                                JOIN Location ON PokemonFavorite.location = Location.ID 
                                JOIN Generation ON PokemonFavorite.generation = Generation.ID""")
            favList = cursor.fetchall()
            return render_template('index.html', curNumber=curNumber, favNumber=favNumber, curList=curPokes, favList=favList)

        @app.route("/favorite", methods=[ "POST" ])
        def favorite():
            req = request.get_json()
            pokemon = jsonify(req)

            res = make_response({}, 200)
            cursor.execute("CALL FavoritePokemon(" + req["number"] +  ")")

            return res

        @app.route("/unfavorite", methods=[ "POST" ])
        def unfavorite():
            req = request.get_json()
            pokemon = jsonify(req)

            res = make_response({}, 200)
            cursor.execute("CALL UnfavoritePokemon(" + req["number"] +  ")")

            return res


            

        if __name__ == "__main__":
            app.run(debug=True)
