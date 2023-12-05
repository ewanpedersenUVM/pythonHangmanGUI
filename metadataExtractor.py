import os
import sys
import eyed3

# function to extract a specific metadata from a file given an argument

def extractMetadata(file, metadata):
    audiofile = eyed3.load(file)
    if metadata == "title":
        return audiofile.tag.title
    elif metadata == "artist":
        return audiofile.tag.artist
    elif metadata == "album":
        return audiofile.tag.album
    elif metadata == "genre":
        return audiofile.tag.genre
    elif metadata == "year":
        return audiofile.tag.recording_date
    elif metadata == "track":
        return audiofile.tag.track_num
    elif metadata == "albumArt":
        return audiofile.tag.images[0].image_data
    else:
        return "Invalid metadata"