import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/goodbye', methods=['GET'])
def get_goodbye():
    return render_template('goodbye.html', goodbye='Bye!')

@app.route('/singlealbum/<id>', methods=['GET'])
def get_one_album(id):
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    artist_repo = ArtistRepository(connection)
    album_in_route = repo.find(id)
    artist_in_route = artist_repo.find(album_in_route.artist_id)
    return render_template('single_album.html', album_in_html=album_in_route, artist=artist_in_route)

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repo = AlbumRepository(connection)
    albums_in_route = repo.all()
    return render_template('albums.html', albums_in_html=albums_in_route)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist_in_route = repo.all()
    return render_template('artist.html', artist_in_html=artist_in_route)

# @app.route('/albums', methods=['GET'])
# def get_all_album_names():
#     connection = get_flask_database_connection(app)
#     repo = AlbumRepository(connection)
#     Albums = repo.all()
#     return ", ".join([Album.title for Album in Albums])

@app.route('/albums/new', methods=['GET'])
def new_album():
    return render_template('create_album.html')
@app.route('/artists/new', methods=['GET'])
def new_artist():
    return render_template('create_artist.html')
###NOT DONE YET
# @app.route('/books', methods=['POST'])
# def create_artists():
#         # Set up the database connection and repository
#         connection = get_flask_database_connection(app)
#         repository = AlbumRepository(connection)

#         # Get the fields from the request form
#         title = request.form['title']
#         author_name = request.form['artist_id']
#         artist_name = request.form['name']
#         artist_id = None
#         # for artist in artist_repo:
#         #         if artist.name == artist_name
#         #             artist_id = artist.id
#         # Create a book object
#         book = Album(None, title, author_name, artist_id)
#         id=artist_id
#         # artist = Artist(id, name, genre)

#         # Check for validity and if not valid, show the form again with errors
#         if not book.is_valid():
#             return render_template('books/new.html', book=book, errors=book.generate_errors()), 400

#         # Save the book to the database
#         book = repository.create(book)

#we need to call artist create if artist does not exist
#we need use to input title, release_year, and artist name
@app.route('/albums', methods=['POST'])
def add_album():
    title = request.form['title']
    release_year = int(request.form['release_year'])
    artist_name = request.form['name']

    sub_connection = get_flask_database_connection(app)
    repo = AlbumRepository(sub_connection)
    artist_repo = ArtistRepository(sub_connection)

    artist_id = None
    for artist in artist_repo.all():
        if artist_name == artist.name:
            artist_id = artist.id
            repo.create(Album(None, title, release_year, artist_id))
            return "Album added"

    
    # if artist_name not in artists(database):
    #     return  
    #     artist_repo.create(None,artist_name,genre)
    
    # albums = repo.all()
    
    # return redirect(f"/singlealbum/{album.id}")
    # response = ""
    # for album in albums:
    #     response += f"{album}\n"
    # return response


@app.route('/artists', methods=['GET'])
def get_all_artists_names():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artists = repo.all()
    return ", ".join([artist.name for artist in artists])
    
@app.route('/artists', methods=['POST'])
def post_add_new_artist():
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    repo.create(Artist(None, name, genre))
    return 'Artist added'

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
