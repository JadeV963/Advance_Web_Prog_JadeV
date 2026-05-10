class Playlist:
    def __init__(self, name, song_count):
        self.name = name
        self.song_count = song_count

    def add_song(self, new_song):
        self.song_count += 1
        print(f"the song added is {new_song}")

    def remove_song(self):
        self.song_count -= 1
        print(f"1 song was deleted successfully")

    def show_info(self):
        print(f"the name of the playlist is {self.name}, and it has {self.song_count} songs")


playlist1 = Playlist("Beat it", 10)
playlist1.add_song("BAD")
playlist1.remove_song()
playlist2 = Playlist("The best of Mike", 20)
playlist2.show_info()

class ShoppingCart:
    def __init__(self, owner, item_count):
        self.owner = owner
        self.item_count = item_count

    def add_item(self, new_item):
        self.item_count += 1
        print(f"you added an item which is {new_item}")
        
    def remove_item(self):
        if self.item_count > 0:
            self.item_count-=1

        else: 
            print("there is no item in the cart")
    
    def show_cart(self):
        print(f"Owner: {self.owner}, Items: {self.item_count}")

shoppingCart1 = ShoppingCart("Ian", 10)
shoppingCart1.add_item("table")
shoppingCart1.remove_item()
shoppingCart1.remove_item()
shoppingCart1.remove_item()
shoppingCart1.show_cart()
   

class UserAccount:
    def __init__(self, username, login_count, active = False): 
        self.username = username
        self.login_count = login_count
        self.active = active
    
    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
    
    def login(self):
      self.activate()
      self.login_count += 1

    def show_status(self):
        if self.active:
            print(f"vous êtes connecté")
        else:
            print(f"vous n'êtes pas connecté")

userAccount1 = UserAccount("John", 0)
userAccount2 = UserAccount("Sarah", 5)

userAccount1.show_status()
userAccount2.show_status()

userAccount1.activate()
userAccount1.show_status()

userAccount2.login()
userAccount2.show_status()
