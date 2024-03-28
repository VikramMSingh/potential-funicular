def make_album(album_name, artist, num_songs=None):
    """Return a dictionary of information about an album"""
    album={'title':album_name, 'singer':artist}
    if num_songs:
        album['num_songs'] = num_songs
    
    return album

album_detail = make_album('Vik','Vikram Singh', 12)

print(f"The details of the {album_detail['title']} sung by {album_detail['singer']} contains {album_detail['num_songs']} songs")


