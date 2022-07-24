from project.config import config
from project.dao.model.genre import Genres
from project.dao.model.director import Directors
from project.dao.model.movie import Movies
from project.dao.model.user import Users


from project.server import create_app
from setup_db import db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genres,
        "Director": Directors,
        "Movie": Movies,
        "User": Users

    }


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
