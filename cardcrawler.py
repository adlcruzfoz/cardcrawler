from random import sample, choice

suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
deck = []
counter = []


suit_mapping = {
    "Clubs" : "enemy",
    "Spades" : "enemy",
    "Hearts" : "healing",
    "Diamonds" : "weapon"
    }

player = {"hp" : 20, "max_hp" : 20,
          "weapon_level" : 0, "previous_weapon_use" : 0,
          "level" : 0, "escapes" : 0, "last_escaped" : False,
          "kills" : 0, "lv_kills" : 0, "total_healed" : 0, "equips" : 0}

name_list = {
    "weapon": {
        "low": {
            "adjectives": ["Rusty", "Chipped", "Dull", "Bent", "Notched", 
                          "Tarnished", "Worn", "Jagged", "Splintered", "Brittle",
                          "Crude", "Faded", "Rough", "Weak", "Dirty",
                          "Loose", "Flimsy", "Tattered", "Battered", "Cracked"],
            
            "nouns": ["Dagger", "Shortsword", "Club", "Hatchet", "Mace",
                     "Spear", "Sickle", "Cleaver", "Staff", "Hammer",
                     "Pick", "Axe", "Blade", "Bow",
                     "Sling", "Pike", "Shiv", "Flail"]
        },
        
        "high": {
            "adjectives": ["Tempered", "Heroic", "Grand", "Reinforced", "Balanced",
                          "Engraved", "Polished", "Spiked", "Weighted", "Laminated",
                          "Chilled", "Blessed", "Runed", "Sturdy", "Burning",
                          "Glowing", "Two-Handed", "Piercing", "Steel"],
            
            "nouns": ["Longsword", "Waraxe", "Claymore", "Morningstar", "Sword",
                      "Katana", "Zweihander", "Greataxe", "Gladius", "Maul",
                     "Battlestaff", "Lance", "Scimitar", "Arbalest", "Crossbow",
                     "Warhammer", "Trident", "Chainwhip", "Javelin", "Blade",
                     "Greatsword", "Executioner", "Fist"]
        }
    },
    
    "healing": {
        "low": {
            "adjectives": ["Rotten", "Weak", "Muddy", "Flaky", "Thin",
                          "Stale", "Bitter", "Lumpy", "Foul", "Old",
                          "Mildewed", "Pale", "Sour", "Rancid", "Salty",
                          "Diluted", "Moldy", "Smelly"],
            
            "nouns": ["Herb", "Berry", "Bread", "Moss", "Salve",
                     "Poultice", "Root", "Paste", "Tonic", "Apple",
                     "Leaf", "Drink", "Ointment", "Balm", "Brew",
                     "Syrup", "Essence", "Extract", "Concoction", "Remedy",
                     "Ale", "Grog", "Vial", "Ampoule"]
        },
        
        "high": {
            "adjectives": ["Clear", "Soothing", "Herbal", "Sparkling", "Robust",
                          "Fortified", "Blessed", "Filtered", "Crystal", "Vigorous",
                          "Invigorating", "Tasty", "Distilled", "Oak-aged",
                          "Golden", "Zesty", "Mystic", "Enchanted", "Alchemist's"],
            
            "nouns": ["Elixir", "Medicine", "Tincture", "Infusion", "Resin",
                     "Nectar", "Distillate", "Potion", "Essence", "Concoction",
                     "Restorative", "Stimulant", "Cream", "Ambrosia", "Potion"]
        }
    },
    
    "enemy": {
        "low": {
            "adjectives": ["Scrawny", "Rotten", "Sickly", "Foul",
                          "Bumbling", "Filthy", "Wretched", "Hungry", "Ragged",
                          "Diseased", "Clumsy", "Weak", "Broken",
                          "Twisted", "Blind", "Lame", "Feral"],
            
            "nouns": ["Rat", "Goblin", "Spider", "Thief", "Wraith",
                      "Ghost", "Snatcher", "Leper", "Vermin", "Zombie",
                      "Slime", "Skeleton", "Soul", "Snapper", "Mongrel",
                      "Imp", "Husk", "Knight", "Hound", "Toad"]
        },
        
        "high": {
            "adjectives": ["Savage", "Vicious", "Bloodied", "Ironclad", "Venomous",
                          "Crazed", "Warped", "Cunning", "Brutish", "Hulking",
                          "Two-headed", "Possessed", "Flaming", "Great", "Wandering",
                          "Barbaric", "Relentless", "Corrupted", "Blighted", "Spectral"],
            
            "nouns": ["Ogre", "Troll", "Knight", "Centaur", "Harpy", "Creature",
                      "Death Knight", "Ghoul", "Specter", "Minotaur", "Cyclops",
                      "Basilisk", "Banshee", "Warlock", "Berserker", "Chimera",
                      "Lich", "Dragon", "Revenant", "Wyvern", "Hobgoblin"]
        },
        
        "boss": {
            "nouns": ["Behemoth", "Archfiend", "Eldritch Horror", "Kraken",
                     "Leviathan", "Juggernaut", "Archlich", "Void Wraith",
                     "Fateweaver", "Worldender", "Demon", "Oblivion Knight",
                     "Harbinger of Doom", "Abyssal Wanderer", "Tyrant",
                     "Grim Reaper", "Lord of the Shadows"]
        }
    },
}

def generate_name(cat, value):
    if cat == "enemy":
        if value > 10:
            tier = "boss"
        elif value > 5:
            tier = "high"
        else:
            tier = "low"

    else:
        if value > 8:
            tier = "high"
        else:
            tier = "low"    

    if tier == "boss":
        return choice(name_list[cat][tier]["nouns"])
    else:
        return " ".join([choice(name_list[cat][tier]["adjectives"]), choice(name_list[cat][tier]["nouns"])])

for suit in suits:
    for rank in ranks:
        if suit in ["Hearts", "Diamonds"] and isinstance(rank, str):
            continue
        
        if isinstance(rank, str):
            match rank:
                case "Jack":
                    value = 11
                case "Queen":
                    value = 12
                case "King":
                    value = 13
                case "Ace":
                    value = 14
        else:
            value = rank
        
        cat = suit_mapping.get(suit)
        
        name = generate_name(cat, value)
                        
        deck.append({
            "rank" : rank,
            "suit" : suit,
            "value" : value,
            "cat" : cat,
            "name" : f"{name} (lv. {value} {cat}, the {rank} of {suit})",
            "short_name" : name
            })

def equip(target, room):
    player["weapon_level"] = target["value"]
    player["weapon"] = target
  
    if target in room:
        room.remove(target)
    player["equips"] += 1
    
    print(f"\nYou equip a level {target['value']} {target['short_name']}!\n")

def attack(target, room):
    enemy_hp = target["value"]
    enemy_name = target["short_name"]
    weapon_value = player["weapon_level"]
    previous_weapon_use = player["previous_weapon_use"]
    
    if weapon_value == 0 or enemy_hp > previous_weapon_use > 0:
        # Barehanded
        player["hp"] -= enemy_hp
        print(f"\nYou fight the {enemy_name} barehanded and take {enemy_hp} damage!\n")
        
    else:
        # Weapon attack
        damage = max(0, enemy_hp - weapon_value)
        player["hp"] -= damage
        print(f"\nYou defeat the {enemy_name} with your {player['weapon']['short_name']} and take {damage} damage!\n")
        
        # Update weapon
        player["previous_weapon_use"] = max(previous_weapon_use, enemy_hp)
        print(f"\nYour weapon has damaged!\nIt can only be used on monsters up to level {player['previous_weapon_use']} now.\n")
        
        
    # Remove the monster from the room
    if target in room:
        room.remove(target)
    
    # Increase kill statistics
    player["kills"] += 1
    player["lv_kills"] += enemy_hp
    

"""



"""



def heal(target, room):
    level = target["value"]
    healer = target["short_name"]
    
    healing = min(level, player["max_hp"] - player["hp"])
    
    if healing > 0:
        print(f"\nYou consume the {healer} and restore {healing} HP!\n")
        player["hp"] += healing
        player["total_healed"] += healing
        
        if target in room:
            room.remove(target)
        
    else:
        print(f"\nYou are already at max HP! The {healer} has no effect.\n")



def die():
    print("\nYou're too weak to keep on fighting. The dungeon has defeated you.\n")
    
    level = player["level"]
    kills = player["kills"]
    lv_kills = player["lv_kills"]
    total_healed = player["total_healed"]
    equips = player["equips"]
    
    print("\nStats:"
          f"\nLevel: {level} (number of rooms completed)"
          f"\nKills: {kills}"
          f"\nLevels killed: {lv_kills} (enemy levels slain)"
          f"\nTotal HP healed: {total_healed}"
          f"\nWeapons equipped: {equips}")
    
    
    
def no_enemies(room):
    monsters = [entity for entity in room if entity["cat"] == "enemy"]
    return len(monsters) == 0
   
 

def generate_room(deck):
    entities = sample(deck, 4)
    return entities


room = generate_room(deck)

def interact(room): 
    interactions = 0  # Track interactions per room
    while True:
        if player["hp"] <= 0:
            die()
            break
        
        print("o----------------------------------------------------------------------------------------o")
        
        print("\nYou look around the room and see:\n")
        for idx, entity in enumerate(room, start=1):  # Numbered entities
            print(f"{idx}. {entity['name']}")

        print(f"\nPlayer HP: {player['hp']}"
              f"\nWeapon level: {player['weapon_level']}")
        
        if not room:
            print("\nThe room is empty! You move on to the next room...\n")
            player["level"] += 1
            player["last_escaped"] = False
            room[:] = generate_room(deck)
            interactions = 0  # Reset interactions for new room
            continue
        
        if no_enemies(room):
            print("\nThere are no enemies in this room. You may proceed safely.")
        
        choice = input("\nChoose an entity to interact with (1-4) or 'w' to move on: ")
        
        if choice.lower() == 'w':
            if no_enemies(room) and player["last_escaped"] == False:
                print("\nYou decide to move on to the next room.\n")
                player["level"] += 1
                player["last_escaped"] = False
                room[:] = generate_room(deck)  # Full reshuffle
                
            else:
                print("\nYou ran away, but you won't be able to run from the next room.\n")
                player["escapes"] += 1
                player["last_escaped"] = True
                room[:] = generate_room(deck)  # Full reshuffle
                
            interactions = 0  # Reset interactions
            counter
            
            continue
        
        elif choice.lower() == "kill":
            print("\nYou successfully kill yourself.\n")
            die()
        
        elif choice.lower() == "help" or choice.lower() == "h":
            print(                  
                "\nGAMEPLAY"
                "\nOn your first and every turn, cards will be randomly generated until there are four of them. These four cards make up a Room."
                
                "\n\nYou must face 3 of the four cards in every Room, one by one."
                
                "\n\nYou can avoid from a Room if you wish, reshuffling all four cards."
                "\nYou may avoid as many Rooms as you want, you can't avoid two Rooms in a row."
                
                "\n\nIf there are no enemies left, it doesn't count as avoiding."
                
                "\nThe game only ends if your Health reaches 0."
                
                
                "\n\nWEAPONS"
                "\nChoosing a weapon will replace your previous weapon (or equip it, if you have none)."
                
                
                "\n\nHEALING"
                "\nUsing a healing item simply adds your the item's level to your HP."
                "\nYour health may not exceed 20."
                "\nYou cannot use healing items at 20 HP."
                
                
                "\n\nCOMBAT"
                "\nIf you have no equipped Weapon or the Enemy's level is higher than your Weapon's, you will fight barehanded."
                "\nThis will defeat the Enemy, but you will lose Health equal to the Enemy's level."
                
                "\n\nIf you have an effective Weapon, you will defeat the Enemy and lose Health equal to the level difference."
                "\n\tFor example, if you attack a level 7 Enemy with a Level 4 Weapon, you'd take 3 HP of damage (7-4 = 3)."
                "\n\tHowever, attacking a level 3 Enemy with a level 4 Weapon wouldn't make you lose any HP (3-4 < 0)"
                
                "\n\nOnce a Weapon is used on an Enemy, it can only be used to attack Enemies of equal or lower level."
                "\n\tFor example, if you use a level 5 Weapon to slay a level 6 Enemy, it wouldn't be able to attack level 7, 8, 9... Enemies."
                "\n\tHowever, it would still be able to attack Enemies of level 6 and under."
            )
            
        elif choice.isdigit() and 1 <= int(choice) <= len(room):
            target = room[int(choice) - 1]
            
            if target['cat'] == "enemy":
                attack(target, room)
            elif target['cat'] == "healing":
                heal(target, room)
            elif target['cat'] == "weapon":
                equip(target, room)
            
            interactions += 1  # Increment interaction count
            
        else:
            print("\nInvalid choice. Please select 'w' or a number between 1 and 4.\n")
            continue
        
        # If the player has interacted 3 times, carry one entity over
        if interactions >= 3:
            print("\nYou've completed three actions. Moving to the next room...\n")
            player["level"] += 1
            player["last_escaped"] = False
            remaining_entity = room[0] if room else None  # Preserve one entity
            room[:] = generate_room(deck)[:3]  # Get 3 new entities
            if remaining_entity:
                room.append(remaining_entity)  # Carry over the last entity
            interactions = 0  # Reset interaction count for next room

    

interact(room)