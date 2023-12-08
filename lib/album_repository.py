from lib.album import Album


class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM albums;")
        albums_inst = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums_inst.append(item)
        return albums_inst
    
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])

    def create(self, album: Album):
        self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)",
            [album.title, album.release_year, album.artist_id]
            )
        
    def delete(self, albumid_to_delete):
        self._connection.execute(
            "DELETE FROM albums WHERE id = %s", [albumid_to_delete]
            )