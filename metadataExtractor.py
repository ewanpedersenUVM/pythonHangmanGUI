import tinytag as tt
import eyed3

# extracts album art and other mp3 metadata
def getMetadata(filename):
    # get metadata
    metadata = tt.TinyTag.get(filename)
    # get album art
    albumArt = metadata.get_image()
    # get album name
    album = metadata.album
    # get artist name
    artist = metadata.artist
    # get song title
    title = metadata.title
    # get song length in seconds
    length = metadata.duration