import random

hp = 20
global stamina
stamina = 5
quiver = 10
mana = 3

plyrInv = ['rusty sword', 'twig bow', 'staff of conjuration']
#combat stats
no_dmg = 0
str_dmg = 2
dex_dmg = 1
mag_dmg = 3
crit_dmg = 2

def attack_sword(stamina, str_dmg):
    on_target = random.randrange(10)
    #print(on_target)
    use_stamina(stamina)
    if stamina >= 1:   
        print('Sching!')     
        if on_target % 2 ==0:
            print(f'Hit for {str_dmg} damage!')
            return str_dmg
        elif on_target == 5:
            str_dmg = str_dmg * crit_dmg
            print(f'Critical hit for {str_dmg} damage!')
            return str_dmg
        else:
            print('Miss!')
            return no_dmg
    else:
        return no_dmg

def attack_arrow(stamina, dex_dmg):
    on_target = random.randrange(10)
    #print(on_target)
    use_stamina(stamina)
    if stamina >= 1:   
        print('Ready, aim, fire!')     
        
        if on_target % 2 ==0:
            print(f'Hit for {dex_dmg} damage!')
            return dex_dmg
        elif on_target == 5:
            dex_dmg = dex_dmg * crit_dmg
            print(f'Headshot for {dex_dmg} damage!')
            return dex_dmg
        else:
            print('Miss!')
            return no_dmg
    else:
        return no_dmg


def attack_spell(stamina, mag_dmg):   
    on_target = random.randrange(10)
    #print(on_target)
    use_stamina(stamina)
    if stamina >= 1:   
        print('Fffwwwooosh!')     
        
        if on_target % 2 ==0:
            print(f'Cast fireball for {mag_dmg} damage!')
            return mag_dmg
        elif on_target == 5:
            mag_dmg = mag_dmg * crit_dmg
            print(f'Cast ice storm for {mag_dmg} damage!')
            return mag_dmg
        else:
            print('Miss!')
            return no_dmg
    else:
        return no_dmg
    

def use_stamina(stamina):
    if stamina >= 1:  
        stamina -= 1
        #print('stamina remaining: ',stamina)
        return stamina
    if stamina <= 0:
        print('Out of resources - use another command!')
        return stamina
    

def enemy_attack(enmy_name,enmy_atk,enmy_wpn):
    on_target = random.randrange(10)
    print(f'The {enmy_name} attacks you with its {enmy_wpn}!')     
    if on_target % 2 ==0:
            print(f'Hit for {enmy_atk} damage!')
            return enmy_atk
    else:
            print('Miss!')
            return no_dmg



def battle_commands():
    
    print('Type sword, arrow, or magic to defeat your opponent.')
    inp = input('')

    if inp ==('sword'):
        damage = attack_sword(stamina, str_dmg)
    elif inp ==('arrow'):
        damage = attack_arrow(stamina, dex_dmg)
    elif inp ==('magic'):
        damage = attack_spell(stamina, mag_dmg)

    else:
        print('invalid action')
        damage = no_dmg

    return damage



def battle(enmy_name, enmy_hp, enmy_atk,enmy_wpn, loot):
    print(f'An {enmy_name} appears! Prepare for battle.')
    while enmy_hp >= 1:
        damage = battle_commands()
        if damage >= 1:
            enmy_hp = enmy_hp - damage
            print(f'{enmy_name} takes {damage} points of damage')
                

        if damage <= 0:
            print(f'{enmy_name} is unharmed')

    if enmy_hp <= 0:
        print(f'{enmy_name} is destroyed. Found {loot}')
        if loot =='nothing':
            return
        else:
            plyrInv.append(loot)


def exploration(location):
    #variables for unlock final encounter
    global progress
    progress = 0
    print(progress)

    if progress <=3:
        print(f'You find yourself lost {location}. Which direction do you wish to explore? Type North,East,South,West')
        print('Type inv to check what items you are carrying')
        # these parameters are for the following - paste them back if you get them working 
        # treasure=false, item, item_location
        #
        #if treasure == True:
        #    print(f'There is a {item} {item_location}. Type pick to add it to your inventory')
        #    inp=input('')
        #    if inp =='pick':
        #        print(f'Picked up {item}')

        inp=input('')
        if inp =='North':
            print('Go North')
            progress = encounter('knee deep in a foggy,fowl-smelling swamp', 'you hear a blood-curdling roar approaching!', 'Orge', 10, 2, 'Giant Club', 'A rotten piece of meat, covered in flies', progress)
        if inp =='East':
            print('Go East')
            progress = encounter('on a squally beach, with the tide fast approaching', 'you see something lurking beneath the waves!', 'Mudcrab', 5, 1,'Sharp Pincers', 'nothing', progress)
        if inp =='South':
            print('Go South')
            progress = encounter('climbing a rocky mountainside as gale force winds chill your bones', ' you feel the earth rumbling as something is digging out of the ground!', 'Moleman', 7, 1, 'Shovel Claws', 'Crystillium ore', progress)
        if inp =='West':
            print('Go West')
            progress = encounter('creeping slowly through a dimly lit cave', ' you can hear something leathery above you', 'Batman', 12,2, 'Sonar blast', 'Guano', progress)
        #if inp =='inv':
        #    print(plyrInv)
    elif progress >= 4:
        print('You find yourself in front of a crumbling, ancient castle, as storm clouds gather. Prepare for the final battle!')
        encounter('standing on the drawbridge of the derelcit castle', 'when the beast swoops down from the ramparts!' 'Cockatrice', 20, 3, 'Razor-sharp talons', 'A princess of average beauty',progress)
        finish()

def encounter(location, enmy_intro, enmy_name, enmy_hp, enmy_atk, enmy_wpn, loot, progress):
    print(f'You are {location}, {enmy_intro}')
    battle(enmy_name,enmy_hp,enmy_atk, enmy_wpn, loot)
    exploration(location)
    print(plyrInv)
    return progress + 1

def finish():
    print('Well done, you have completed the quest')
    exit()



# here lies the gameplay loop
exploration('in a dense, dark forest')


