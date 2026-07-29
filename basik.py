import utils
import hosts
import random
import time
import sys
import goober
import blu
import script

enemies = [
  "Clockwork Guard",
  "Huángjiā Wèiduì",
  "Demi-deus Avaritiae"
]

enemy = ""
attacks = {}
last_enemy = ""
choice = ""

def enemy_choice():
  global enemy, attacks, last_enemy, enemies
  if last_enemy == "Clockwork Guard":
    enemies = [
      "Huángjiā Wèiduì",
      "Demi-deus Avaritiae"
    ]
  if last_enemy == "Huángjiā Wèiduì":
    enemies = [
      "Clockwork Guard",
      "Demi-deus Avaritiae"
    ]
  if last_enemy == "Demi-deus Avaritiae":
    enemies = [
      "Clockwork Guard",
      "Huángjiā Wèiduì"
    ]
  enemy = random.choice(enemies)
  last_enemy = enemy
  if enemy == "Clockwork Guard":
    utils.enemy_hp = 80
    attacks = {
      "Asterion's Smite": 8,
      "Overclock": 0,
      "Draining Frenzy": 12
    }
    utils.enemy_de = 25
    utils.enemy_sta = 15
    utils.enemy_sta_gain = 4
  elif enemy == "Huángjiā Wèiduì":
    utils.enemy_hp = 100
    attacks = {
      "Fángyù zītài": 0,
      "Bōlí lìchǎng": 5,
      "Lóng shì": 6
    }
    utils.enemy_de = 30
    utils.enemy_sta = 20
    utils.enemy_sta_gain = 3
  elif enemy == "Demi-deus Avaritiae":
    utils.enemy_hp = 125
    utils.enemy_sta = 50
    utils.enemy_de = 0
    utils.enemy_sta_gain = 7
    attacks = {
      "Fames": 0,
      "Mille Dentes": 0, # Technically 0, drains remaining STA (similar to locusts but uses sta instead) cannot be first attack, and neither can Fames.
      "Exuicio Armorum": 5
    }
    if utils.aspect_of_shapeshifter:
      utils.sta = utils.enemy_sta

def process_enemy():
  global enemy, attacks
  if utils.eclipse:
      utils.de = utils.eclipse_de
  print()
  if enemy == "Demi-deus Avaritiae":
    if utils.enemy_sta < 5 or utils.sta > 20 and utils.enemy_hp >= 25:
      attack = "Fames"
    elif utils.enemy_de < 5:
      attack = "Exuicio Armorum"
    else:
      attack = "Mille Dentes"
  elif enemy == "Huángjiā Wèiduì":
    if utils.enemy_sta < 5 or utils.enemy_de <= 0:
      attack = "Fángyù zītài"
    elif utils.hp < 20:
      attack = "Lóng shì"
    elif utils.enemy_sta >= 5:
      attack = "Bōlí lìchǎng"
  elif enemy == "Clockwork Guard":
    if utils.enemy_sta < 8:
      attack = "Overclock"
    elif utils.enemy_sta >= 12:
      attack = "Draining Frenzy"
    else:
      attack = "Asterion's Smite"
  if utils.enemy_hp > 0:
    utils.fast_print(f"They Used {attack}")
    if attack == "Fames":
      subtracted_sta = utils.sta / 2
      utils.enemy_sta += utils.sta / 2
      utils.sta /= 2
      utils.sta = int(utils.sta)
      utils.fast_print("The Energy Seeps From Your Body Into Theirs")
      utils.fast_print(f"(Player STA -{subtracted_sta} - Enemy STA +{subtracted_sta})")
    elif attack == "Mille Dentes":
      utils.enemy_sta = int(utils.enemy_sta)
      for _ in range(utils.enemy_sta):
        if random.random() > 0.5:
          utils.enemy_damage = random.randint(1, 6)
          utils.fast_print("><")
          utils.enemy_damage -= utils.de
          if utils.enemy_damage <= 0:
            utils.de -= 0.5
          if utils.de < 0:
            utils.de = 0
          if utils.eclipse:
            utils.de = utils.eclipse_de
          if utils.ego_dodge:
            utils.enemy_damage /= 2
          if utils.enemy_damage < 0:
            utils.enemy_damage = 0
          utils.hp -= utils.enemy_damage
        else:
          utils.fast_print("> <")
      utils.enemy_sta = 0
    elif attack == "Exuicio Armorum":
      utils.de -= 3
      if utils.de < 0:
        utils.de = 0
      utils.enemy_de += 3
      utils.enemy_sta -= 5
      utils.fast_print("They Steal Some Of That Which Protected You")
    elif attack == "Fángyù zītài":
      utils.fast_print("They Assume A Defensive Stance")
      utils.enemy_de += 3
      utils.enemy_sta += 5
    elif attack == "Bōlí lìchǎng":
      utils.enemy_sta -= 5
      if utils.enemy_hp > 10:
        utils.enemy_hp -= 10
      utils.enemy_damage = random.randint(10, 40)
      utils.enemy_damage -= utils.de
      if utils.enemy_damage < 0:
        utils.enemy_damage = 0
      if utils.ego_dodge:
        utils.enemy_damage /= 2
      utils.hp -= utils.enemy_damage
      utils.fast_print(f"They Dealt {int(utils.enemy_damage)}!")
    elif attack == "Lóng shì":
      utils.enemy_damage = random.randint(1, 93111342342314234523406456345967369734958674567397193274)
      utils.enemy_damage -= utils.de
      if utils.enemy_damage < 0:
        utils.enemy_damage = 0
      utils.enemy_sta -= 8
      utils.hp -= utils.enemy_damage
      utils.fast_print("You Are Weakened, And They Strike You Down.")
      utils.fast_print(f"!{utils.enemy_damage}!")
    elif attack == "Overclock":
      utils.enemy_de -= 5
      if utils.enemy_de < 0:
        utils.enemy_de = 0
      utils.enemy_sta += 6
      utils.fast_print("The Clockwork Guard Heats Itself Up To Keep Up The Pace.")
    elif attack == "Draining Frenzy":
      utils.enemy_sta -= 12
      for _ in range(15):
        utils.enemy_damage = random.randint(1, 10)
        utils.de -= utils.enemy_damage / 5
        if utils.de < 0:
          utils.de = 0
        if utils.eclipse:
          utils.de = utils.eclipse_de
        utils.enemy_damage /= 2
        utils.enemy_damage -= utils.de
        if utils.enemy_damage < 0:
          utils.enemy_damage = 0
        if utils.ego_dodge:
          utils.enemy_damage /= 2
        utils.hp -= utils.enemy_damage
        utils.fast_print(f"They Struck For !{utils.enemy_damage}!")
    elif attack == "Asterion's Smite":
      utils.enemy_sta -= 8
      utils.enemy_damage = random.randint(30, 55)
      utils.enemy_damage -= utils.de
      if utils.enemy_damage < 0:
       utils.enemy_damage = 0
      if utils.ego_dodge:
        utils.enemy_damage /= 2
      # Tisha & Brusha: enemy side
      if utils.tisha_and_brusha and utils.enemy_damage > 0:
        utils.enemy_damage /= 2
        utils.hp -= utils.enemy_damage
        utils.enemy_hp -= utils.enemy_damage
      else:
        utils.hp -= utils.enemy_damage
      utils.fast_print(f"They Struck For !{utils.enemy_damage}!")
      # Jealousy: reflect 50% of enemy damage if they outdamage you and you attacked
      if utils.jealousy:
        if utils.damage > 0 and utils.enemy_damage >= utils.damage:
          utils.enemy_hp -= utils.enemy_damage * 0.5
  if utils.is_sans and utils.sta > 0:
    utils.hp = 1
    utils.de = 1
    utils.sta -= 1000
    utils.slow_print("The enemy misses you")
  if utils.is_sans and utils.sta <= 0:
    utils.fast_print("You Took:")
    utils.fast_print("999999999999999999999999999999999999999999999999999999999999999999999999999999999999"*999)
    time.sleep(3)
    sys.exit()
  if utils.aspect_of_stan:
    utils.fast_print("You Took x999 Damage :D")
    time.sleep(2)
    sys.exit()

def process_player():
  global choice
  utils.fast_print(f"\n\n\n----====== {hosts.host} ATTACKS ======----\n")
  if utils.vanguard_cost < 0:
    utils.vanguard_cost = 0
  if utils.is_sans:
    utils.fast_print("1. Ger Ballster *heh heh. While you've got me here, I gotta play a few jokes. You know me, pal.")
    utils.fast_print("*huh? did you want MORE attacks? Sorry, can't do, pal.")
    utils.fast_print("*actually... here: 3. Sleep *give us all a break, huh?")
    utils.fast_print("*and I'll make you see these exact same messages each time you try to attack, so... good luck.")
  if hosts.host == "Argo":
    if utils.harpoon_turn == 1:
      utils.harpoon_cost = 8
    else:
      utils.harpoon_cost = 5
      utils.harpoon_turn = 2
    utils.fast_print(f"1. Harpoon ({utils.harpoon_cost} STA Cost, Turn {utils.harpoon_turn})")
    utils.fast_print(f"2. Flare (+ {utils.flare_gain} STA)")
    utils.fast_print(f"3. Vanguard ({utils.vanguard_cost} STA Cost, Gain {utils.vanguard_gain} DEF)")
  elif hosts.host == "Ego":
    utils.fast_print("1. Godspeed (+ 3 STA)")
    utils.fast_print("2. Onus (Decrease STA Gain To 1 (Townfolk: 3))")
    utils.fast_print("3. Oblivio (3 STA Cost)")
  elif hosts.host == "Artifex":
    utils.fast_print("1. Lancea Artifex (3 STA Cost)")
    utils.fast_print("2. Delere (6 STA Cost)")
    utils.fast_print("3. Sciagraphia (STA + 5)")
  if hosts.host != "Goober" and hosts.host != "Blu":
    choice = input("\nChoose: ")
  else:
    if hosts.host == "Goober":
      goober.process_goober()
    if hosts.host == "Blu":
      blu.process_blu()
  if choice == "1" and utils.is_sans:
    utils.enemy_hp = 0
    utils.sta -= 1000
  elif choice == "2" and utils.is_sans:
    utils.fast_print("*were you expecting a secret here? There's no second attack, kid.")
  elif choice == "3" and utils.is_sans:
    utils.slow_print("*great. Good night, kid.")
    sys.exit()
  if choice == "1":
    if hosts.host == "Argo" and utils.harpoon_cost <= utils.sta:
      if utils.vanguard_cost >= 0:
        utils.vanguard_cost -= 1
        utils.vanguard_gain = 15
      if utils.harpoon_turn == 1:
        utils.sta -= utils.harpoon_cost
        utils.damage = random.randint(60, 80)
        if utils.starry_days:
          if utils.starry_turn == None or utils.starry_turn == False:
            utils.starry_turn = True
            utils.damage *= 2
          else:
            utils.damage *= 0.85
        if utils.deaf_man_music:
          utils.hp += utils.damage * 0.05
          utils.sta += utils.damage * 0.05
          utils.de += utils.damage * 0.05
        if utils.exploratio:
          utils.damage += 15
        if utils.stellae_et_ultra:
          utils.damage -= 20
        utils.damage -= utils.enemy_de
        if utils.damage < 0:
          utils.damage = 0
        utils.fast_print(f"You Struck For {int(utils.damage)}!")
        time.sleep(0.5)
        utils.enemy_hp -= utils.damage
        if utils.santo_fricsat:
          utils.hp += utils.damage * 0.25
        utils.harpoon_turn = 2
      else:
        utils.sta -= utils.harpoon_cost
        utils.harpoon_turn = 1
        for _ in range(25):
          utils.damage = random.randint(1, 3)
          if utils.starry_days:
            if utils.starry_turn == None or utils.starry_turn == False:
              utils.starry_turn = True
              utils.damage *= 2
            else:
              utils.damage *= 0.85
          if utils.deaf_man_music:
            utils.hp += utils.damage * 0.05
            utils.sta += utils.damage * 0.05
            utils.de += utils.damage * 0.05
          if utils.enemy_de < 0:
            utils.enemy_de = 0
          if utils.damage < 0:
            utils.damage = 0
          utils.enemy_de -= utils.damage / 5
          utils.damage -= utils.enemy_de
          if utils.enemy_de < 0:
            utils.enemy_de = 0
          if utils.damage < 0:
            utils.damage = 0
          time.sleep(0.05)
          print(f"SLASH !{int(utils.damage)}!")
          utils.enemy_hp -= utils.damage
          if utils.santo_fricsat:
            utils.hp += utils.damage * 0.25
    elif hosts.host == "Ego":
      utils.sta += 3
      utils.ego_dodge = True
      utils.ego_mult_1 = 2
      utils.fast_print("-> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> -> ->.", delay=0.01)
      print("\n"*30)
    elif hosts.host == "Artifex":
      utils.damage = random.randint(1, 60)
      if utils.nostalgia:
        utils.damage = random.randint(1, 45)
      if utils.artifex_mult:
        utils.damage += 15
        if utils.joy:
          utils.damage -= 5
        utils.artifex_mult = False
      if utils.starry_days:
        if utils.starry_turn == None or utils.starry_turn == False:
          utils.starry_turn = True
          utils.damage *= 2
        else:
          utils.damage *= 0.85
      if utils.deaf_man_music:
        utils.hp += utils.damage * 0.05
        utils.sta += utils.damage * 0.05
        utils.de += utils.damage * 0.05
      if utils.pride:
        utils.damage *= 1.1
      utils.damage -= utils.enemy_de
      if utils.damage < 0:
        utils.damage = 0
      if utils.joy:
        utils.damage *= 1.1
      if utils.hope:
        utils.damage *= 1.5
        utils.de -= utils.damage * 0.25
        if utils.de < 0:
          utils.de = 0
      # Tisha & Brusha: player side
      if utils.tisha_and_brusha and utils.damage > 0:
        utils.damage /= 2
        utils.hp -= utils.damage
      utils.enemy_hp -= utils.damage
      if utils.santo_fricsat:
        utils.hp += utils.damage * 0.25
      utils.fast_print(f"You Struck For {int(utils.damage)}!")
      if utils.anger:
        utils.hp -= utils.damage * 0.35
      # Nostalgia second hit
      if utils.nostalgia:
        utils.damage = random.randint(1, 45)
        utils.damage -= utils.enemy_de
        if utils.damage < 0:
          utils.damage = 0
        # Tisha & Brusha also applies to second hit
        if utils.tisha_and_brusha and utils.damage > 0:
          utils.damage /= 2
          utils.hp -= utils.damage
        utils.enemy_hp -= utils.damage
        if utils.anger:
          utils.hp -= utils.damage * 0.35
        utils.fast_print(f"You Struck For {int(utils.damage)}!")
  elif choice == "2":
    if hosts.host == "Argo":
      utils.sta += utils.flare_gain
      utils.de -= 3
      if utils.de < 0:
        utils.de = 0
      utils.damage = random.randint(20, 35)
      if utils.starry_days:
        if utils.starry_turn == None or utils.starry_turn == False:
          utils.starry_turn = True
          utils.damage *= 2
        else:
          utils.damage *= 0.85
      if utils.deaf_man_music:
        utils.hp += utils.damage * 0.05
        utils.sta += utils.damage * 0.05
        utils.de += utils.damage * 0.05
      if utils.omnes_et_plus:
        utils.damage -= 10
      utils.damage -= utils.enemy_de
      if utils.vanguard_cost > 0:
        utils.vanguard_cost -= 1
        utils.vanguard_gain = 15
      if utils.damage < 0:
        utils.damage = 0
      if utils.santo_fricsat:
        utils.hp += utils.damage * 0.25
      utils.fast_print(f"!{int(utils.damage)}! |-> ⛨ <-| !{int(utils.damage)}!")
      time.sleep(0.5)
      utils.enemy_hp -= utils.damage
    elif hosts.host == "Ego":
      if utils.townfolk:
        utils.sta_gain = 3
      else:
        utils.sta_gain = 1
      utils.ego_mult_2 = 2
      utils.fast_print("-:↓↓↓:-")
      time.sleep(0.5)
    elif hosts.host == "Artifex" and utils.sta >= 6:
      utils.sta -= 6
      utils.artifex_mult = True
      utils.fast_print("You Feel Empowered.")
      time.sleep(0.5)
  elif choice == "3":
    if hosts.host == "Argo" and utils.sta >= utils.vanguard_cost:
      utils.de += utils.vanguard_gain
      utils.vanguard_cost += 5
      utils.vanguard_gain += 3
      utils.sta -= utils.vanguard_cost
      utils.fast_print("<-==|:|==-|o ⛨ o|-==|:|==->")
    elif hosts.host == "Ego" and utils.sta > 3:
      utils.damage = random.randint(25, 50)
      if utils.starry_days:
        if utils.starry_turn == None or utils.starry_turn == False:
          utils.starry_turn = True
          utils.damage *= 2
        else:
          utils.damage *= 0.85
      if utils.deaf_man_music:
        utils.hp += utils.damage * 0.05
        utils.sta += utils.damage * 0.05
        utils.de += utils.damage * 0.05
      utils.sta -= 3
      utils.fast_print(f"⇍⇍⇍⇍⇎⇏⇏⇏⇏\n!{int(utils.damage)}!")
      if utils.ego_mult_1 > 0:
        utils.damage *= 2
      if utils.ego_mult_2 > 0:
        utils.damage *= 2
      utils.damage -= utils.enemy_de
      if utils.damage < 0:
        utils.damage = 0
      utils.enemy_hp -= utils.damage
      if utils.santo_fricsat:
        utils.hp += utils.damage * 0.25
    elif hosts.host == "Artifex":
      utils.fast_print("You Regain Your Resources.")
      utils.damage = random.randint(5, 10)
      if utils.starry_days:
        if utils.starry_turn == None or utils.starry_turn == False:
          utils.starry_turn = True
          utils.damage *= 2
        else:
          utils.damage *= 0.85
      if utils.deaf_man_music:
        utils.hp += utils.damage * 0.05
        utils.sta += utils.damage * 0.05
        utils.de += utils.damage * 0.05
      if utils.santo_fricsat:
        utils.hp += utils.damage * 0.25
      if utils.artifex_mult:
        utils.damage += 15
        if utils.joy:
          utils.damage -= 5
        utils.artifex_mult = False
      if utils.pride:
        utils.damage *= 1.1
      utils.sta += 5
      utils.de += 1
      if utils.joy:
        utils.damage *= 1.1
      if utils.tisha_and_brusha and utils.damage > 0:
        utils.damage /= 2
        utils.hp -= utils.damage
      if utils.hope:
        utils.damage *= 1.5
        utils.de -= utils.damage * 0.25
        if utils.de < 0:
          utils.de = 0
      if utils.anger:
        utils.hp -= utils.damage * 0.35
      utils.enemy_hp -= utils.damage
    
def kombat():
  global enemy, attacks
  utils.fast_print(f"{enemy} Challenges You.")
  utils.starry_turn = False
  while utils.hp > 0:
    utils.hp + utils.sta / 2
    if utils.fear:
      if utils.hp <= 25:
        utils.sta += 20
    if utils.anger:
      utils.hp += 10
    utils.damage = 0
    utils.enemy_damage = 0
    if utils.santo_fricsat:
      utils.hp -= 10
    if utils.infernum_and_polaris:
      utils.sta_gain = 5
    if utils.onus_dei:
      utils.sta_gain = 1
    if utils.eclipse:
      utils.de = utils.eclipse_de
    utils.damage = 0
    if utils.sta < 0:
      utils.sta = 0
    utils.sta += utils.sta_gain
    if utils.sajioyero:
      utils.hp += utils.sta / 4
    utils.ego_dodge = False
    if utils.ego_mult_1 > 0:
      utils.ego_mult_1 -= 1
    if utils.ego_mult_2 > 0:
      utils.ego_mult_2 -= 1
    if utils.enemy_hp <= 0:
      print("\n"*30)
      utils.fast_print("Victory. You've yet to reach the end, however. March onward.")
      break
    utils.fast_print(f"\n\n\n{enemy} HP: {int(utils.enemy_hp)}")
    time.sleep(0.5)
    utils.fast_print(f"\n\n{hosts.host} HP: {int(utils.hp)}\n{hosts.host} DEF: {int(utils.de)}\n{hosts.host} STA: {int(utils.sta)}")
    time.sleep(0.5)
    process_player()
    process_enemy()
  if utils.hp <= 0:
    utils.fast_print("Death Cannot Stop You... right? guys? we really need the money i beg you keep playingggggg")
    time.sleep(2)
    script.start()