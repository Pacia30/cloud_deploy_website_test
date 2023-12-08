from lib.album_repository import *
from lib.album import *

'''
when we call album repository all, 
we get a list of artist objects reflecting the seed data
'''

def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library2.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.all()

    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2)
    ]

def test_find_record(db_connection):
    db_connection.seed("seeds/music_library2.sql")
    repository = AlbumRepository(db_connection)
    album = repository.find(1)
    assert album == Album(1, "Doolittle", 1989, 1)

def test_create_record(db_connection):
    db_connection.seed("seeds/music_library2.sql")
    repository = AlbumRepository(db_connection)
    repository.create(Album(None, "Test Title", 1989, 1))
    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, "Test Title", 1989, 1)
    ]
