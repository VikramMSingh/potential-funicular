active = True 
def make_album(album_name, artist_name):
    """Return album details"""
    album_detail = f"{album_name} by {artist_name}"
    return album_detail

while active:
    album_title = input("Enter the name of your album, type 'q' to quit")
   #artist_name = input("Enter the name of the artist, type 'q' to quit")
    if album_title == 'q':
        active = False
        break
    artist_name = input("Enter the name of the artist, type 'q' to quit")
    if artist_name == 'q':
        active = False
        break
    album_detail = make_album(album_title, artist_name)
    print(f"Details of the album are {album_detail}")

    
    
