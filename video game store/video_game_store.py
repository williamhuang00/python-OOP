'''
item:
- id
- title
- base_price
- get_price()

video_game(item):
- genre(s)

shirt(item):
- size

console(item):
- storage (GB)

video_game_store:
- handles operations regarding store
- add to inventory
- add to cart
- remove from cart
- checkout

using a get_price abstract method in the abstract class for item allows 
child classes to implement their own custom pricing logic unique to them

list representation for cart items would preserve the order in which items were added to the cart.
may be useful for printing a receipt
'''
from abc import ABC, abstractmethod
from enum import Enum

class Item(ABC):
    def __init__(self, id, title, base_price) -> None:
        self.id = id
        self.title = title
        self.base_price = base_price
    
    @abstractmethod
    def get_price(self) -> float:
        #let children implement their own pricing, enforce contract
        pass
    
    def __str__(self) -> str:
        return f"id - {self.id}, title - {self.title}, base price - {self.base_price}"
    #If __str__ is not defined, the print() function and str() call __repr__ instead.

class Genre(Enum):
    # dev-code-reference -> actual value
    SHOOTER = "Shooter"
    STRATEGY = "Strategy"
    RPG = "RPG"
    PLATFORMER = "Platformer"

class VideoGame(Item):
    def __init__(self,id, title, base_price, genres) -> None:
        super().__init__(id, title, base_price)
        self.genres = genres
    
    def __str__(self) -> None:
        base_info = super().__str__() #() after super and the magic method

        return f"{base_info}, genres - {self.genres}"

class Size(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

class Shirt(Item):
    def __init__(self, id, title, base_price, size):
        super().__init__(id, title, base_price)
        self.size = size
    



game1 = VideoGame(0, 'sonic', 9.99, [Genre.PLATFORMER, Genre.STRATEGY])
shirt1 = Shirt(1, 'lego t shirt', 35.40, Size.MEDIUM)
print(game1)
print(shirt1)


