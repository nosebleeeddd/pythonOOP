
class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: int,
                 value: int
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

pocket_knife = Weapon(name="pocket knife",
                      weapon_type="sharp",
                      damage=4,
                      value=10)

glock_pistol = Weapon(name="Glock-19",
                      weapon_type="ranged",
                      damage=10,
                      value=30)

fists = Weapon(name="Fists",
                      weapon_type="blunt",
                      damage=10,
                      value=30)

