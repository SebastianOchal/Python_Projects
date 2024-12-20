play_list = {}

def Playlist(s_name, s_info):
    play_list[s_name] = s_info

def add_song():
    
    while True:
        print(50 * "=")
        title = input("Song Title:")
        genre = input("Song Genre:")
        artist = input("Song Artist:")

        info = {
            "Song Genre": genre,
            "Song Artist": artist
        }
        Playlist(title, info)
        print(f"Song added: {title} with genre: {genre} and artist: {artist}")

        quit = input("Would you like to add another song \'Yes' or 'No'")
        if quit.lower() == "no":
            start()
            break
def view_playlist():
    
    for song in play_list:
        print(50 * "=")
        print(f"Song Title: {song}")
        print(f"Song Genre: {play_list[song]["Song Genre"]} Song Artist: {play_list[song]["Song Artist"]}")

    quit = input("Would you like to return to menu? \'Yes' or 'No': ")
    if quit.lower() == "yes":
        start()

def update_song():
    while True:
        print(50*"=")
        update = input("What song would you like to update: ")

        for song in play_list:
            if (update.lower() == song.lower()):
                
                new_genre = input("What is the new Genre: ")
                play_list[song]["Song Genre"] = new_genre

                new_artist = input("What is the new Artist: ")
                play_list[song]["Song Artist"] = new_artist

        quit = input("Would you like to update another song \'Yes' or 'No': ")
        if quit.lower() == "no":
            start()
            break


def delete_song():
    while True:
        print(50*"=")
        delete = input("What Song would you like to delete?: ")
        song_exists = False
        
        for song in play_list:
            if (delete.lower == song.lower):
                song_exists = True
                del_song = song
            
        if (song_exists == True):
            play_list.pop(del_song)
            song_exists = False
        else:
            print(f"{delete} does not exist")

        quit = input("Would you like to delete another song \'Yes' or 'No': ")
        if quit.lower() == "no":
            start()
            break

def menu():
    choice = input("What would you like to do?: ")
    chose = choice.lower()
    print(choice)

    match chose:
        case "add":
            add_song()
        case "view":
            view_playlist()
        case "update":
            update_song()
        case "delete":
            delete_song()
        case "exit":
            print("Ok see ya")
        case _:
            print("That was not an option Please choose from the menu")
            menu()

def start():
    options = ["Type \'add': to add a song", "Type \'view': to view your playlist", "Type \'update': to update a song", "Type \'delete': to delete a song", "Type \'exit': to exit"]
    print(50*"=")

    for opt in options:
        print(opt)
    print(50*"=")
    menu()
start()