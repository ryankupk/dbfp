from flask import Flask, render_template
import mysql.connector
import os.path
from db_tunnel import DatabaseTunnel

DB_HOST = "cs.westminstercollege.edu"
DB_SSH_PORT = 2322
DB_SSH_USER = "student"
DB_PORT = 3306

# Default connection information (can be overridden with command-line arguments)
DB_SSH_KEYFILE = "id_rsa.cmpt307"
DB_NAME = "rtk0720_final_project"
DB_USER = "token_2f91"
DB_PASSWORD = "tfH8abOjPBRtvaCA"


try:
    with \
        DatabaseTunnel(DB_SSH_KEYFILE) as tunnel:
            connection = mysql.connector.connect(host='localhost', port=tunnel.getForwardedPort(), database=DB_NAME, user=DB_USER, password=DB_PASSWORD, use_pure=True, autocommit=True)
            cursor = connection.cursor()
            
            # for (pokemon, name, location, generation) in cursor:
            #     print(pokemon, name, location, generation)
            # cursor.close()
except mysql.connector.Error as err:
    print(err)



cursor.execute("SELECT Pokemon.number, Pokemon.name, Location.name, Generation.name FROM Pokemon JOIN Location ON Pokemon.location = Location.ID JOIN Generation ON Pokemon.generation = Generation.ID")

for (pokemon, name, location, generation) in cursor:
    print(pokemon, name, location, generation)
# cursor.close()

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
    # pokemon = [[1, "bulbasaur", "cannot be caught", "kanto"]]
    return render_template('index.html', userDetails=pokemon)

if __name__ == "__main__":
    app.run(debug=True)