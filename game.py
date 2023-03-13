"""a functional module for main.py"""

class Room:
    """
    a class for presenting Room
    >>> room_1 = Room(1)
    >>> room_1.name
    1
    """
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, description):
        """a method for setting description"""
        self.description = description

    def set_character(self, character):
        """a method for setting character"""
        self.character = character

    def set_item(self, item):
        """a method for setting item"""
        self.item = item

    def get_item(self):
        """a method for getting item"""
        return self.item

    def link_room(self, room_to_link, direction):
        """a method for linking room"""
        self.linked_rooms[direction] = room_to_link

    def get_character(self):
        """a method for getting character"""
        return self.character

    def get_details(self):
        """a method for getting details"""
        print(f"{self.name}\n--------------------")
        print(self.description)
        linked_rooms_reversed = dict(reversed(list(self.linked_rooms.items())))
        for direction in linked_rooms_reversed:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}")
        if self.character:
            print(f"{self.character.name} is here!")

    def move(self, command):
        """a method for moving"""
        return self.linked_rooms[command]

class Enemy:
    """a class for representing Enemy"""
    winnings = 0
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        """a method for setting conversation"""
        self.conversation = conversation

    def set_weakness(self, weakness):
        """a method for setting weakness"""
        self.weakness = weakness

    def get_details(self):
        """a method for getting details"""
        print(self.name)
        print(self.description)
        print(f"Likes to talk about: {self.conversation}")
        print(f"Weakness: {self.weakness}")

    def describe(self):
        """a method for describing"""
        print (self.description)

    def talk(self):
        """a method for talking"""
        print (f"[{self.name} says]: {self.conversation}")

    def fight(self, fight_with):
        """a method for fighting"""
        if self.name == 'zombie' and fight_with == 'cheese' or \
        self.name == 'Tabitha' and fight_with == 'book':
            print(f'You fend {self.name} off with the book')
            return True
        print(f'{self.name} crushes you, puny adventurer!')
        return False

    def get_defeated(self):
        """a method for getting defended"""
        Enemy.winnings += 1
        return Enemy.winnings

class Item():
    """a class representing Item"""
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        """a method for setting description"""
        self.description = description

    def get_details(self):
        """a method for getting description"""
        print(self.name)
        print(self.description)

    def get_name(self):
        """a method for getting name"""
        return self.name

    def describe(self):
        """a method for returning description"""
        print(f"The [{self.name}] is here - {self.description}")
