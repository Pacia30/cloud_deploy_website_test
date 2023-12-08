from lib.album import *

def test_album_contructs():
    album = Album(1, "Test Album", 1989, 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 1989
    assert album.artist_id == 1

def test_albums_format_nicely():
    album = Album(1, "Test Album", 1989, 1)
    assert str(album) == "Album(1, Test Album, 1989, 1)"

def test_albums_are_equal():
    album1 = Album(1, "Test Album", 1989, 1)
    album2 = Album(1, "Test Album", 1989, 1)
    assert album1 == album2
