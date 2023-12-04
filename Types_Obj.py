# object_id 1
# name 2
# stackable 3
# tool 4
# blast_resistance 5
# flammable 6
# rarity 7
# restore 8
# durability 9
# damage 10
# effect 11
# renewable 12

#Complete
class Mine_Object:
    path_to_icon = 'icons/Question.png'
    def __init__(self, object_id:int, name:str, stackable:int):
        self.object_id = object_id
        self.name = name
        self.stackable = stackable
    
    def __str__(self) -> str:
        return f'''\t\tObject
Object ID:  {self.object_id}
Name:  {self.name}
Stackable:  {self.stackable}'''

#Complete
class Armor(Mine_Object):
    path_to_icon = 'icons/Armor.png'
    def __init__(self, object_id:int, name:str, stackable:int,
                 rarity:str, durability:int):
        super().__init__(object_id, name, stackable)
        self.rarity = rarity
        self.durability = durability

    def __str__(self) -> str:
        return f'''\t\tArmor
Object ID:  {self.object_id}
Name:  {self.name}
Stackable:  {self.stackable}
Rarity:  {self.rarity}
Durability:  {self.durability}'''

#Complete
class Block(Mine_Object):
    path_to_icon = 'icons/Block.png'
    def __init__(self, object_id:int, name:str, stackable:int, tool:str, blast_resistance:int|float, flammable:bool):
        super().__init__(object_id, name, stackable)
        self.tool = tool
        self.blast_resistance = blast_resistance
        self.flammable = flammable

    def __str__(self) -> str:
        return f'''\t\tBlock
Object ID:  {self.object_id}
Name:  {self.name}
Stackable:  {self.stackable}
Tool:  {self.tool}
Blast Resistance:  {self.blast_resistance}
Flammable:  {self.flammable}'''

#Complete
class Food(Mine_Object):
    path_to_icon = 'icons/Food.png'
    def __init__(self, object_id:int, name:str, stackable:int, renewable:bool, restore:int|float):
        super().__init__(object_id, name, stackable)
        self.renewable = renewable
        self.restore = restore

    def __str__(self) -> str:
        return f'''\t\tFood
Object ID:  {self.object_id}
Name:  {self.name}
Stackable:  {self.stackable}
Renewable:  {self.renewable}
Restore:  {self.restore}'''

#Complete
class Potion(Mine_Object):
    path_to_icon = 'icons/Potion.png'
    def __init__(self, object_id:int, name:str, stackable:int, rarity:str, effect:bool):
        super().__init__(object_id, name, stackable)
        self.rarity = rarity
        self.effect = effect

    def __str__(self) -> str:
        return f'''\t\tPotion
Object ID:  {self.object_id}
Name:  {self.name}
Stackable:  {self.stackable}
Rarity:  {self.rarity}
Effect:  {self.effect}'''

#Complete
class Tool(Mine_Object):
    path_to_icon = 'icons/Tool.png'
    def __init__(self, object_id:int, name:str, stackable:int, rarity:str, durability:int, damage:int|float):
        super().__init__(object_id, name, stackable)
        self.rarity = rarity
        self.durability = durability
        self.damage = damage

    def __str__(self) -> str:
        return f'''\t\tTool
Object ID:  {self.object_id}
Name:  {self.name}
Stackable:  {self.stackable}
Rarity:  {self.rarity}
Durability:  {self.durability}
Damage:  {self.damage}'''

#Complete    
class All_Props(Mine_Object):
    path_to_icon = 'icons/All_prop.png'
    def __init__(self, object_id: int, name: str, stackable: int, tool: str, blast_resistance: int|float, flammable: bool, rarity: str, restore: int|float, durability: int, damage: int|float, effect: bool, renewable: bool):
        super().__init__(object_id, name, stackable)
        self.tool = tool
        self.blast_resistance =blast_resistance
        self.flammable = flammable
        self.rarity = rarity
        self.restore = restore
        self.durability = durability
        self.damage = damage
        self.effect = effect
        self.renewable = renewable

    def __str__(self) -> str:
        return f'''\t\tAll  Properties  Object
Object ID:  {self.object_id}
Name:  {self.name}
Stackable:  {self.stackable}
Tool:  {self.tool}
Blast Resistance:  {self.blast_resistance}
Flammable:  {self.flammable}
Rarity:  {self.rarity}
Restore:  {self.restore}
Durability:  {self.durability}
Damage:  {self.damage}
Effect:  {self.effect}
Renewable:  {self.renewable}'''
