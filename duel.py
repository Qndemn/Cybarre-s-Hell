import utils
import hosts
import random
import time
import sys
import script

RESET = "\033[0m"

dummy_hp = 150
dummy_balance = 40
dummy_def = 15
dummy_sta = 20

eclipse_hp = 250
eclipse_balance = 50
eclipse_def = 15
eclipse_sta = 20
eclipse_chance = 0
eclipse_parry = False
single_suit = ""
deaths = 0

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

def win():
  global dummy_hp, dummy_def, dummy_balance, dummy_sta, eclipse_hp, eclipse_def, eclipse_balance, eclipse_sta, height, single_suit, eclipse_chance, eclipse_parry, deaths
  utils.fast_print("weee x999 screen clear time")
  print("\n"*999)
  utils.slow_print("They Kneel, And Offer Their Sword.")
  utils.slow_print(f"They Bested You {deaths} Times.")
  print("\n"*999)
  utils.slow_print("I would add a new host, but to quote my fav COURS dev 'I'm lazy'")
  time.sleep(2)
  utils.fast_print("Why are you still here")
  sys.exit()

def reset():
  global dummy_hp, dummy_def, dummy_balance, dummy_sta, eclipse_hp, eclipse_def, eclipse_balance, eclipse_sta, height, single_suit, eclipse_chance, eclipse_parry, deaths
  print("Yeah this is going to clear the terminal for sure")
  deaths += 1
  print("\n"*999)
  utils.slow_print(f"Don't Give Up.")
  utils.slow_print(f"Wake Up, Reset, And Try Again.")
  time.sleep(1)
  print("\n"*999)
  utils.slow_print("R e a d y ?")
  input("Reset (press enter)")
  dummy_hp = 150
  dummy_balance = 40
  dummy_def = 15
  dummy_sta = 20
  eclipse_hp = 250
  eclipse_balance = 50
  eclipse_def = 15
  eclipse_sta = 20
  eclipse_chance = 0
  eclipse_parry = False
  single_suit = ""

def process_eclipse_attack():
    global dummy_hp, dummy_def, dummy_balance, dummy_sta
    global eclipse_hp, eclipse_def, eclipse_balance, eclipse_sta

    # -----------------------------
    # 1. Aequinoctium chooses stance + attack
    # -----------------------------
    stance = random.choice(["1", "2", "3"])  # High, Mid, Low

    attack_names = {
        ("1","1"): "Swan Dive",
        ("1","2"): "Grève du croissant",
        ("1","3"): "Cybarre's Smite",

        ("2","1"): "Suit-piercer",
        ("2","2"): "Aiguille",
        ("2","3"): "Asterion's Strike",

        ("3","1"): "Rising Gale",
        ("3","2"): "Coupeur",
        ("3","3"): "Atlas's Surrender",
    }

    attack = random.choice(["1", "2", "3"])
    attack_name = attack_names[(stance, attack)]

    # -----------------------------
    # 2. Announce the attack
    # -----------------------------
    stance_name = { "1":"HIGH", "2":"MIDDLE", "3":"LOW" }[stance]
    utils.fast_print(f"\nAequinoctium enters {stance_name} stance.")
    utils.fast_print(f"Aequinoctium uses {attack_name}!")

    # -----------------------------
    # 3. Symbol sets
    # -----------------------------
    symbol_sets = {
        ("1", "1"): [")", "}", "]", ">", "/"],
        ("1", "2"): ["(", ")", "()", "{}", "[]"],
        ("1", "3"): ["vV", "VV", "><", "\\/", "/\\", "||"],

        ("2", "1"): ["/", "\\", "|", "||", "//", "\\\\"],
        ("2", "2"): ["->", "-->", ">", ">>"],
        ("2", "3"): ["====", "===", "==", "=>", "==>"],

        ("3", "1"): ["/", "//", "/>"],
        ("3", "2"): ["()", "[]", "][", "><", "/\\", "\\/"],
        ("3", "3"): ["#", "@", "&", "%", "$"],
    }

    # -----------------------------
    # 4. Base thresholds
    # -----------------------------
    base_thresholds = {
        ("1", "1"): 1.0,
        ("1", "2"): 0.9,
        ("1", "3"): 0.75,

        ("2", "1"): 1.15,
        ("2", "2"): 1.25,
        ("2", "3"): 1.1,

        ("3", "1"): 1.35,
        ("3", "2"): 1.45,
        ("3", "3"): 1.5,
    }

    base = base_thresholds[(stance, attack)]
    max_sta = 20

    # -----------------------------
    # 5. Determine number of hits
    # -----------------------------
    hit_counts = {
        ("1","1"): 1,
        ("1","2"): 3,
        ("1","3"): 1,

        ("2","1"): 6,
        ("2","2"): 1,
        ("2","3"): 1,

        ("3","1"): 1,
        ("3","2"): 16,
        ("3","3"): 11,  # 10 small + 1 final
    }

    hits = hit_counts[(stance, attack)]

    # -----------------------------
    # 6. Multi‑hit parry loop
    # -----------------------------
    total_damage = 0
    parry_success = False

    for hit in range(1, hits+1):

        prompt = random.choice(symbol_sets[(stance, attack)])

        # STA‑scaled threshold
        threshold = base * (dummy_sta / max_sta)
        if len(prompt) > 1:
            threshold += 0.15 * len(prompt)

        # Hit label
        if hits == 1:
            label = "[FINAL STRIKE]"
        else:
            label = f"[STRIKE {hit}/{hits}]"

        utils.fast_print(f"\n{label}  PARRY: {prompt}")
        start = time.time()
        player_input = input("> ")
        reaction = time.time() - start

        parry_success = (player_input == prompt and reaction < threshold)

        if parry_success:
            utils.fast_print("Parry Successful!")
        else:
            utils.fast_print("Parry Failed!")

        # -----------------------------
        # 7. Apply mirrored effects PER HIT
        # -----------------------------

        # ---------------- HIGH STANCE ----------------
        if stance == "1" and attack == "1":  # Swan Dive
            dmg = random.randint(60, 80)
            if parry_success:
                dmg = int(dmg * 0.2)
                dummy_sta -= 6
                dummy_balance -= 1
            else:
                dummy_balance -= 3
            dmg -= dummy_def
            if dmg < 0: dmg = 0
            total_damage += dmg

        elif stance == "1" and attack == "2":  # Croissant
            dmg = random.randint(12, 21)
            if parry_success:
                dmg = int(dmg * 0.1)
                dummy_sta -= 3
                dummy_balance -= 1
            else:
                dummy_balance -= 2
            dmg -= dummy_def
            if dmg < 0: dmg = 0
            total_damage += dmg

        elif stance == "1" and attack == "3":  # Smite
            if hit == 1:  # only once
                dmg = random.randint(70, 90)
                eclipse_sta -= 10
                eclipse_balance -= 6
                if parry_success:
                    dmg = int(dmg * 0.35)
                    dummy_sta -= 7
                    dummy_balance -= 8
                else:
                    dummy_balance -= 8
                dmg -= dummy_def
                if dmg < 0: dmg = 0
                total_damage += dmg

        # ---------------- MIDDLE STANCE ----------------
        elif stance == "2" and attack == "1":  # Suit-piercer
            dmg = random.randint(8, 16)
            if parry_success:
                dmg = 0
                dummy_sta -= 1
                dummy_balance -= 1
            else:
                dummy_balance -= 1
            dmg -= dummy_def
            if dmg < 0: dmg = 0
            total_damage += dmg

        elif stance == "2" and attack == "2":  # Aiguille
            if hit == 1:
                dmg = random.randint(5, 20)
                if parry_success:
                    dmg = 0
                    dummy_sta -= 2
                    dummy_balance -= 5
                else:
                    dummy_balance -= 4
                dmg -= dummy_def
                if dmg < 0: dmg = 0
                total_damage += dmg

        elif stance == "2" and attack == "3":  # Asterion
            if hit == 1:
                dmg = random.randint(40, 50)
                eclipse_sta -= 6
                eclipse_balance -= 3
                if parry_success:
                    dmg = int(dmg * 0.15)
                    dummy_sta -= 3
                    dummy_balance -= 5
                else:
                    dummy_balance -= 10
                dmg -= dummy_def
                if dmg < 0: dmg = 0
                total_damage += dmg

        # ---------------- LOW STANCE ----------------
        elif stance == "3" and attack == "1":  # Rising Gale
            if hit == 1:
                dmg = random.randint(30, 45)
                if parry_success:
                    dmg = int(dmg * 0.15)
                    dummy_sta -= 3
                    dummy_balance -= 3
                else:
                    dummy_balance -= 3
                dmg -= dummy_def
                if dmg < 0: dmg = 0
                total_damage += dmg

        elif stance == "3" and attack == "2":  # Coupeur
            dmg = random.randint(1, 2)
            if parry_success:
                dmg = 0
                dummy_sta -= 1
                dummy_balance -= 1
            else:
                dummy_balance -= 1
            dmg -= dummy_def
            if dmg < 0: dmg = 0
            total_damage += dmg

        elif stance == "3" and attack == "3":  # Atlas’s Surrender
            if hit <= 10:
                if random.random() < 0.5:
                    dummy_hp -= 5
                    eclipse_def -= 3
                else:
                    dummy_sta -= 3
                    eclipse_sta -= 3
                    dummy_balance -= 1
            else:
                if random.random() < 0.5:
                    dummy_hp -= 25
                    eclipse_def -= 15
                else:
                    dummy_sta -= 9
                    eclipse_sta -= 9
                    dummy_balance -= 3

    # -----------------------------
    # 8. Apply total damage
    # -----------------------------
    dummy_hp -= total_damage
    if total_damage > 0:
        utils.fast_print(f"\nYou took {total_damage} damage!")

def process_dummy_choice():
  global dummy_hp, dummy_def, dummy_balance, dummy_sta, eclipse_hp, eclipse_def, eclipse_balance, eclipse_sta, height, single_suit, eclipse_chance, eclipse_parry, damage
  eclipse_parry = False
  print("\n\n")
  utils.fast_print("Height:")
  utils.fast_print("\n1. High")
  utils.fast_print("2. Middle")
  utils.fast_print("3. Low")
  height = input("\n(enter a number)\n")
  if height == "1":
    utils.fast_print("\n\nHigh Attacks:")
    utils.fast_print("1. Swan Dive")
    utils.fast_print("2. Grève du croissant")
    utils.fast_print("3. Cybarre's Smite")
    number = input("\n(enter a number)\n")
  elif height == "2":
    utils.fast_print("\n\nMiddle Attacks:")
    utils.fast_print(f"1. {single_suit}piercer")
    utils.fast_print("2. Aiguille")
    utils.fast_print("3. Asterion's Strike")
    number = input("\n(enter a number)\n")
  elif height == "3":
    utils.fast_print("\n\nLow Attacks:")
    utils.fast_print("1. Rising Gale")
    utils.fast_print("2. Coupeur")
    utils.fast_print("3. Atlas's Surrender")
    number = input("\n(enter a number)\n")
  if number == "1":
    if height == "1":
      utils.fast_print("\n\n)\n )\n  )\n   )\n    )\n     )\n      )\n       )\n        )\n\n")
      damage = random.randint(60, 80)
      eclipse_chance = eclipse_sta / 20 # Ex. 5 STA = 0.25% Parry Chance
      if random.random() < eclipse_chance:
        damage *= 0.2
        utils.fast_print("They Parried The Attack!")
        eclipse_parry = True
        eclipse_sta -= 6
        if eclipse_sta < 0:
          eclipse_sta = 0
          eclipse_balance -= 1
        eclipse_balance -= 1
      damage -= eclipse_def
      if damage < 0:
        damage = 0
      eclipse_hp -= damage
      if not eclipse_parry:
        eclipse_balance -= 3
        utils.fast_print(f"You Struck For {damage}!")
    elif height == "2":
      for _ in range(6):
        option = ["\\", "/"]
        chosen = random.choice(option)
        utils.fast_print(f"{chosen}")
        damage = 0
        damage += random.randint(8, 16)
        eclipse_chance = eclipse_sta / 15
        if random.random() < eclipse_chance:
          damage *= 0
          utils.fast_print("They Parried The Attack!")
          eclipse_parry = True
          eclipse_sta -= 1
          if eclipse_sta < 0:
            eclipse_sta = 0
            eclipse_balance -= 1
        damage -= eclipse_def
        if damage < 0:
          damage = 0
        eclipse_hp -= damage
        if not eclipse_parry:
          eclipse_balance -= 1
          utils.fast_print(f"You Struck For {damage}!")
    elif height == "3":
      print("        /")
      print("      /")
      print("    /")
      print("  /")
      print("/")
      damage = random.randint(30, 45)
      eclipse_chance = eclipse_sta / 25
      if random.random() < eclipse_chance:
        damage *= 0.15
        damage = int(damage)
        utils.fast_print("They Parried The Attack!")
        eclipse_parry = True
        eclipse_sta -= 3
        if eclipse_sta < 0:
          eclipse_sta = 0
          eclipse_balance -= 3
        eclipse_balance -= 2
      damage -= eclipse_def
      if damage < 0:
        damage = 0
      eclipse_hp -= damage
      if not eclipse_parry:
        eclipse_balance -= 3
        utils.fast_print(f"You Struck For {damage}!")
  elif number == "2":
    if height == "1":
      for _ in range(3):
        print("\n\n")
        print("__")
        print("  \\")
        print("    \\")
        print("     |")
        print("    /")
        print("__/")
        damage = random.randint(12, 21)
        eclipse_chance = eclipse_sta / 10
        if random.random() < eclipse_chance:
          damage *= 0.1
          damage = int(damage)
          utils.fast_print("They Parried The Attack!")
          eclipse_parry = True
          eclipse_sta -= 3
          if eclipse_sta < 0:
            eclipse_sta = 0
            eclipse_balance -= 1
        damage -= eclipse_def
        if damage < 0:
          damage = 0
        eclipse_hp -= damage
        if not eclipse_parry:
          eclipse_balance -= 2
          utils.fast_print(f"You Struck For {damage}!")
    elif height == "2":
      utils.fast_print("\n\n------------------------------>\n\n", delay=0.01)
      damage = random.randint(5, 20)
      eclipse_chance = eclipse_sta / 25
      if random.random() < eclipse_chance:
        damage *= 0
        damage = int(damage)
        utils.fast_print("They Parried The Attack!")
        eclipse_parry = True
        eclipse_sta -= 2
        if eclipse_sta < 0:
          eclipse_sta = 0
          eclipse_balance -= 5
      damage -= eclipse_def
      if damage < 0:
        damage = 0
      eclipse_hp -= damage
      if not eclipse_parry:
        eclipse_balance -= 4
        utils.fast_print(f"You Struck For {damage}!")
    elif height == "3":
      print("\n\n")
      for rounds in range(16):
        slashes = [")", "(", "()", "[]", "]", "[", "\\", "/"]
        slash = random.choice(slashes)
        damage = random.randint(1, 2)
        utils.fast_print(f"{slash}")
        eclipse_chance = eclipse_sta / 50
        if random.random() < eclipse_chance:
          damage *= 0
          damage = int(damage)
          utils.fast_print("They Parried The Attack!")
          eclipse_parry = True
          eclipse_sta -= 1
          if eclipse_sta < 0:
            eclipse_sta = 0
            eclipse_balance -= 1
        damage -= eclipse_def
        if damage < 0:
          damage = 0
        eclipse_hp -= damage
        if not eclipse_parry:
          eclipse_balance -= 1
  elif number == "3":
    if height == "1":
      utils.fast_print("⤈"*100, delay=0.01)
      damage = random.randint(70, 90)
      dummy_sta -= 10
      dummy_balance -= 6
      eclipse_chance = eclipse_sta / 30
      if random.random() < eclipse_chance:
        damage *= 0.35
        damage = int(damage)
        utils.fast_print("They Parried The Attack!")
        eclipse_parry = True
        eclipse_sta -= 7
        if eclipse_sta < 0:
          eclipse_sta = 0
          eclipse_balance -= 8
      damage -= eclipse_def
      if damage < 0:
        damage = 0
      eclipse_hp -= damage
      if not eclipse_parry:
        eclipse_balance -= 8
        utils.fast_print(f"You Struck For {damage}!")
    elif height == "2":
      print("===============================================================>")
      print("===============================================================>")
      print("===============================================================>")
      damage = random.randint(40, 50)
      dummy_sta -= 6
      dummy_balance -= 3
      eclipse_chance = eclipse_sta / 60
      if random.random() < eclipse_chance:
        damage *= 0.15
        damage = int(damage)
        utils.fast_print("They Parried The Attack!")
        eclipse_parry = True
        eclipse_sta -= 3
        if eclipse_sta < 0:
          eclipse_sta = 0
          eclipse_balance -= 5
      damage -= eclipse_def
      if damage < 0:
        damage = 0
      eclipse_hp -= damage
      if not eclipse_parry:
        eclipse_balance -= 10
        utils.fast_print(f"You Struck For {damage}!")
    elif height == "3":
      utils.fast_print("♜", delay=0.3)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      utils.fast_print(" ♜", delay=0.25)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      utils.fast_print("  ♜", delay=0.2)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      utils.fast_print("   ♜", delay=0.15)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      utils.fast_print("    ♜", delay=0.1)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      utils.fast_print("     ♜", delay=0.08)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      utils.fast_print("      ♜", delay=0.05)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      utils.fast_print("       ♜", delay=0.03)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      utils.fast_print("        ♜", delay=0.01)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      utils.fast_print("         ♜", delay=0.01)
      if random.random() < 0.5:
        eclipse_hp -= 5
        dummy_def -= 3
      else:
        eclipse_sta -= 3
        dummy_sta -= 3
        eclipse_balance -= 1
      print()
      time.sleep(0.25)
      print("\n"*30)
      print("          ♢")
      if random.random() < 0.5:
        eclipse_hp -= 25
        dummy_def -= 15
      else:
        eclipse_sta -= 9
        dummy_sta -= 9
        eclipse_balance -= 3
      print()
      time.sleep(0.25)
      print("\n"*30)
      
def duel():
  global dummy_hp, dummy_def, dummy_balance, dummy_sta, eclipse_hp, eclipse_def, eclipse_balance, eclipse_sta, height, single_suit, eclipse_chance, eclipse_parry, damage
  if hosts.host == "Goober":
    utils.slow_print(f"<<| ... what even ARE you...? *poke poke* uh... grab... grab the sword...? |>>")
  elif hosts.host == "Argo":
    utils.slow_print("<<| Your knowledge will not help you here. Pick up your blade, and return to the beginning. |>>")
  elif hosts.host == "Ego":
    utils.slow_print("<<| We are nobles, you and I. Your pursuit of knowledge is at its end, cleanse your mind of the burden of your knowledge, and face me once again. |>>")
  elif hosts.host == "Artifex":
    utils.slow_print("<<| So many emotions in one contained place. Interesting, and I'm genuinely sad to say that you must return. Your story was so far from over... and yet. Pick up your sword and fight. |>>")
  elif hosts.host == "Sans":
    utils.slow_print("*no")
    time.sleep(1)
    sys.exit()
  elif hosts.host == "Blu":
    print(RESET)
    utils.slow_print("<<| Do away with that technology, and fight me like a noble. |>>")
  utils.slow_print("Stripped Of All Pleasantries, Return To Square One, And Face Us In Your Original Form", delay=0.15)
  utils.fast_print("""
     _
    (_)
    |_|
    |_|
    |_|
    |_|
    |_|
o=========o
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    \ /
  """)
  time.sleep(2)
  print("\n"*60)
  suit = random.choice(suits)
  if suit == "Hearts":
    single_suit = "Heart"
  if suit == "Spades":
    single_suit = "Spade"
  if suit == "Clubs":
    single_suit = "Club"
  if suit == "Diamonds":
    single_suit = "Diamond"
  while True:
    if dummy_hp <= 0 or dummy_balance <= 0:
      reset()
      continue
    if eclipse_hp <= 0 or eclipse_balance <= 0:
      win()
    dummy_balance += dummy_sta / 2
    eclipse_balance += eclipse_sta / 2
    dummy_sta += utils.sta_gain
    eclipse_sta += utils.sta_gain
    eclipse_parry = False
    damage = 0
    dummy_balance = min(dummy_balance, 60)
    eclipse_balance = min(eclipse_balance, 70)
    dummy_sta = max(0, dummy_sta)
    utils.fast_print(f"--==== Aequinoctium Stats ====--\n\nHP: {int(eclipse_hp)}")
    utils.fast_print(f"DEF: {int(eclipse_def)}")
    utils.fast_print(f"STA: {int(eclipse_sta)}")
    utils.fast_print(f"Balance: {int(eclipse_balance)}")
    time.sleep(0.5)
    utils.fast_print(f"\n\n--==== Dummy of {suit} Stats ====--\n\nHP: {int(dummy_hp)}")
    utils.fast_print(f"DEF: {int(dummy_def)}")
    utils.fast_print(f"STA: {int(dummy_sta)}")
    utils.fast_print(f"Balance: {int(dummy_balance)}")
    time.sleep(0.5)
    process_dummy_choice()
    if eclipse_hp <= 0 or eclipse_balance <= 0:
      print("\n"*999)
      utils.slow_print("<<| I Assume You Will Not Return. I Assume I Will Be Forgotten. No. I KNOW. You Won't Come Back. None Of You Will, Ungrateful Brats That You Are. I Give You JOY. I Give You LAUGHTER. And What Do I Get In Return? I Don't Ask For Much... But You Matter More, Right? Have Fun With Your... F...friends..s...s, G, L, I, W...whi...whichev- |>>")
      time.sleep(1)
      utils.fast_print("ℚ Oh, how the mighty have fallen. Well... 'mighty' might be an overstatement. Guten Joben, friend...en? I don't speak german")
      time.sleep(2)
      win()
    process_eclipse_attack()
    if dummy_hp <= 0 or dummy_balance <= 0:
      reset()
      continue