import time
import random
import sys
import utils

RESET = "\033[0m"
BRIGHT_RED = "\x1b[91m"
BRIGHT_CYAN = "\033[96m"

def process_goober():
  utils.fast_print("\n1. Circle (3 STA Cost)\n2. Salvo! (STA Regain)\n3. Drunk Fish (6 STA Cost)\n")
  utils.fast_print("(Enter A Number!)")
  number = input("")
  if number == "1" and utils.sta >= 3:
    salvo = ["⇟", " ⇟", "  ⇟", "    ⇟", "     ⇟", "⇟   ⇟", " ⇟  ⇟ ⇟", "⇟  ⇟   ⇟"]
    utils.sta -= 3
    if utils.cross_the_line:
      for _ in range(111):
        time.sleep(0.005)
        if random.random() > 0.5:
          print()
        tcl = random.choice(salvo)
        print(f"{RESET}{tcl}")
        utils.damage = random.uniform(0.05, 0.075)
        if utils.jarrets_shard:
          utils.damage *= 1.5
        if utils.damage - utils.enemy_de <= 0:
          utils.enemy_de -= utils.damage
        else:
          utils.damage -= utils.enemy_de
        if utils.enemy_de < 0:
          utils.enemy_de = 0
          utils.enemy_hp -= utils.damage
      print(BRIGHT_RED)
    for _ in range(666):
      time.sleep(0.005)
      if random.random() > 0.5:
        print()
      tcl = random.choice(salvo)
      print(f"{RESET}{tcl}")
      utils.damage = random.uniform(0.05, 0.075)
      if utils.jarrets_shard:
        utils.damage *= 1.5
      if utils.i_will_not_be_moved:
        utils.damage *= 1.5
      if utils.damage - utils.enemy_de <= 0:
        utils.enemy_de -= utils.damage
      else:
        utils.damage -= utils.enemy_de
      if utils.enemy_de < 0:
        utils.enemy_de = 0
      utils.enemy_hp -= utils.damage
    print(BRIGHT_RED)
  elif number == "2":
    print(BRIGHT_CYAN)
    utils.fast_print("very refresh much good lot liking")
    if utils.cornucopia:
      utils.sta += 5
      utils.de += 5
      utils.hp += 10
    if utils.tsunami:
      utils.enemy_hp -= 30
      if utils.i_will_not_be_moved:
        utils.enemy_hp -= 15
      utils.enemy_sta += 6
    utils.sta += 6
    utils.de += 5
    utils.hp += 15
    print(BRIGHT_RED)
  elif number == "3" and utils.sta >= 6:
    utils.sta -= 6
    if utils.manias_lies:
      for rounds in range(50):
        time.sleep(0.05)
        shots = ["tequila", "rum", "margarita"]
        shot = random.choice(shots)
        if shot == "tequila":
          if utils.extra_ammo:
            print("BAM")
            utils.enemy_de -= 1
          print("BAM")
          utils.enemy_de -= 1
        elif shot == "rum":
          if utils.salt_the_rim:
            print("CLEAVE")
            utils.enemy_sta -= 1
          print("CLEAVE")
          utils.enemy_sta -= 1
        elif shot == "margarita":
          if utils.double_struck:
            print("GASH")
            utils.enemy_hp -= 1
            if utils.i_will_not_be_moved:
              utils.enemy_hp -= 0.5
          print("GASH")
          utils.enemy_hp -= 1
          if utils.i_will_not_be_moved:
              utils.enemy_hp -= 0.5
        if utils.enemy_sta < 0:
          utils.enemy_sta = 0
        if utils.enemy_de < 0:
          utils.enemy_de = 0
    for rounds in range(50):
      time.sleep(0.05)
      shots = ["tequila", "rum", "margarita"]
      shot = random.choice(shots)
      if shot == "tequila":
        if utils.extra_ammo:
          print("BAM")
          utils.enemy_de -= 1
        print("BAM")
        utils.enemy_de -= 1
      elif shot == "rum":
        if utils.salt_the_rim:
          print("CLEAVE")
          utils.enemy_sta -= 1
        print("CLEAVE")
        utils.enemy_sta -= 1
      elif shot == "margarita":
        if utils.double_struck:
          print("GASH")
          utils.enemy_hp -= 1
        print("GASH")
        utils.enemy_hp -= 1
      if utils.enemy_sta < 0:
        utils.enemy_sta = 0
      if utils.enemy_de < 0:
        utils.enemy_de = 0
  elif number == "3" and utils.sta < 6:
    print("Not Enough STA! This Attack Needs 6 STA!")
  elif number == "1" and utils.sta < 3:
    print("Not Enough STA! This Attack Needs 3 STA!")
  if number == "2" and utils.sta >= 999:
    utils.fast_print("... I have so many questions, starting with: do you have a job...? that's what I thought. for your sake and mine, go get therapy and/or a job, because this is too much f*cking STA man it's like that guy from MFN when he's hopped up on chocolate bars")