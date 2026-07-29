import time
import random
import sys
import hosts
import utils
import basik
import duel
BRIGHT_CYAN = "\033[96m"
BRIGHT_RED = "\x1b[91m"
def host_choice():
  while hosts.host not in["Ego", "Artifex", "Argo", "Sans", "Goober", "Blu"]:
    utils.fast_print(f"Want to check out a host?\n1. Argo\n2. Ego\n3. Artifex\n4. Blutuber")
    choice = input("(enter 1-4. Otherwise, skip to selection)\n")
    if choice == "1":
      hosts.argo()
    elif choice == "2":
      hosts.ego()
    elif choice == "3":
      hosts.artifex()
    elif choice == "sans":
      utils.hp = 1
      utils.de = 1
      utils.sta = 999999
      utils.is_sans = True
      hosts.sans()
    elif choice == "4":
      print(BRIGHT_CYAN)
      hosts.blu()
    elif choice == "goober":
      hosts.goober()
    print()
    print()
    choice = input("Want To Choose A Host?\n(enter 1-4. Otherwise, return to host viewing)\nChoose: ")
    if choice == "1":
      hosts.host = "Argo"
    elif choice == "2":
      hosts.host = "Ego"
    elif choice == "3":
      hosts.host = "Artifex"
    elif choice == "sans":
      utils.is_sans = True
      hosts.host = "Sans"
    elif choice == "goober":
      print(BRIGHT_RED)
      hosts.host = "Goober"
    elif choice == "4":
      print(BRIGHT_CYAN)
      hosts.host = "Blu"

def start():
  utils.upgrade_flags = set()   # Tracks which upgrades have been taken

  utils.damage = 0
  utils.enemy_damage = 0

  utils.hp = 100
  utils.enemy_hp = 0

  utils.sta = 20
  utils.enemy_sta = 0

  utils.de = 15
  utils.enemy_de = 0

  utils.enemy_attacks = ""

  utils.harpoon_turn = 1
  utils.harpoon_cost = 8

  utils.vanguard_cost = 10
  utils.vanguard_gain = 15

  utils.sta_gain = 3
  utils.enemy_sta_gain = 3

  utils.ego_mult_1 = 0
  utils.ego_mult_2 = 0

  utils.flare_gain = 5
  utils.ego_dodge = False
  utils.artifex_mult = False

# --- UPGRADE FLAGS ---

# Ego
  utils.eclipse = False
  utils.eclipse_de = None
  utils.sugar_tea_and_rum = False
  utils.sajioyero = False
  utils.santo_fricsat = False
  utils.starry_days = False
  utils.starry_turn = None
  utils.sunny_nights = False
  utils.townfolk = False
  utils.deaf_man_music = False
  utils.infernum_and_polaris = False
  utils.onus_dei = False

# Argo
  utils.ad_mare = False
  utils.perdita_animarum = False
  utils.exploratio = False
  utils.ferrum_mens = False
  utils.stellae_et_ultra = False
  utils.omnes_et_plus = False

# Artifex
  utils.jealousy = False
  utils.pride = False
  utils.tisha_and_brusha = False
  utils.joy = False
  utils.hope = False
  utils.nostalgia = False
  utils.anger = False
  utils.fear = False

# Goober
  utils.salt_the_rim = False
  utils.cornucopia = False
  utils.jarrets_shard = False
  utils.cross_the_line = False
  utils.tsunami = False
  utils.double_struck = False
  utils.extra_ammo = False
  utils.manias_lies = False
  utils.i_will_not_be_moved = False

# Blue Potato-Adjacent Plant (Blu-tuber)
  utils.aspect_of_smileez = False
  utils.aspect_of_beast = False
  utils.aspect_of_thicez = False
  utils.aspect_of_comet = False
  utils.aspect_of_stan = False
  utils.aspect_of_light = False
  utils.aspect_of_dark = False
  utils.aspect_of_shapeshifter = False
  utils.aspect_of_starz = False
  utils.aspect_of_pintr = False

  rounds = 0
  host_choice()
  while True:
    rounds += 1
    print(f"ROUND: {rounds}/6")
    time.sleep(1)
    print("\n"*999)
    if rounds == 7:
      duel.duel()
    else:
      basik.enemy_choice()
      basik.kombat()
      time.sleep(2)
      print("\n"*666)
      if rounds in[1, 2, 3]:
        utils.upgrade_choice(hosts.host)