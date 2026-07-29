import time
import sys
import random
import utils

mech_mode = False
ch = 0
stun_chance = 0.5
stun = False
blu_dodge = False

def process_blu():
  global mech_mode, ch, stun_chance, stun, blu_dodge, blu_saved
  blu_saved = utils.de
  if blu_dodge:
    utils.de += 50
    utils.fast_print("ROLL ACTIVE! >:)")
  else:
    utils.de = blu_saved
  if stun:
    stun = False
    utils.enemy_hp -= 15
    utils.enemy_sta = 0
  if ch > 100:
    ch = 100
  if ch <= 0 and mech_mode:
    utils.fast_print("!! BATTERY CRITICAL - EXITING MECH MODE !!")
    mech_mode = False
  if ch > 0 and mech_mode:
    if not utils.aspect_of_beast:
      utils.fast_print("!! LOSING POWER !!")
      ch -= 5
    if utils.aspect_of_smileez:
      ch -= 5 * 0.25
  utils.fast_print(f"BATTERY: {ch}% / 100% !! MAX NEEDED FOR MECH MODE !!")
  if not mech_mode:
    utils.fast_print("1. Stun Grenade")
    utils.fast_print("2. Roll")
    utils.fast_print("3. Laser Round")
    utils.fast_print("4. Mech Mode")
  if mech_mode:
    utils.fast_print("1. Stun Volley")
    utils.fast_print("2. Rocket")
    utils.fast_print("3. Beam Cascade")
    utils.fast_print("4. Normal Mode")
  choice = input("\nChoose: ")
  if choice == "1":
    if not mech_mode and utils.sta >= 3:
      utils.sta -= 3
      if utils.aspect_of_dark:
        utils.sta += 3 * 0.25
      utils.fast_print("You Throw A Stun Grenade!")
      if random.random() < stun_chance:
        print("""
               ᛋᛋᛋᛋᛋᛋᛋᛋ
          ᛋᛋᛋᛋᛋᛋ      ᛋᛋᛋᛋᛋᛋ
       ᛋᛋᛋᛋ                ᛋᛋᛋᛋ
     ᛋᛋᛋ                      ᛋᛋᛋ
    ᛋᛋ                          ᛋᛋ
    ᛋᛋ        ! STUNNED !       ᛋᛋ
     ᛋᛋᛋ                      ᛋᛋᛋ
       ᛋᛋᛋᛋ                ᛋᛋᛋᛋ
          ᛋᛋᛋᛋᛋᛋ      ᛋᛋᛋᛋᛋᛋ
               ᛋᛋᛋᛋᛋᛋᛋᛋ

        """)
        stun = True
        ch += 15
        if utils.aspect_of_smileez:
          ch += 15 * 0.5
        utils.enemy_sta -= 6
        utils.enemy_de -= 3
      else:
        print("☁ !Dud! ☁")
    if mech_mode and ch >= 6:
      ch -= 6
      if utils.aspect_of_smileez:
        ch -= 6 * 0.25
      for rounds in range(15):
        time.sleep(0.1)
        if random.random() > 0.5:
          print()
          if random.random() > 0.5:
            print()
        if random.random() < stun_chance:
          stun = True
          print("ᛋ")
          utils.enemy_sta -= 3
          utils.enemy_de -= 1
        else:
          print("☁")
  elif choice == "2":
    if not mech_mode:
      utils.sta += 4
      if utils.aspect_of_dark:
        utils.sta += 4 * 0.25
      blu_dodge = True
      utils.hp += 15
      utils.fast_print("You rolled!")
      if utils.aspect_of_light:
        utils.hp += 15
    if mech_mode:
      rocket_round = 101
      for _ in range(100):
        time.sleep(0.1)
        rocket_round -= 1
        ch -= 1
        if utils.aspect_of_smileez:
          ch -= 1 * 0.25
        print(rocket_round)
        if random.random() > rocket_round / 100:
          damage = rocket_round
          damage -= utils.enemy_de
          if damage < 0:
            damage = 0
          utils.enemy_hp -= damage
          print("!!! BOOM !!!")
          break
  elif choice == "3":
    if not mech_mode and utils.sta >= 1:
      utils.sta -= 1
      if utils.aspect_of_dark:
        utils.sta += 1 * 0.25
      ch += 20
      if utils.aspect_of_smileez:
          ch += 20 * 0.5
      damage = random.uniform(10, 30)
      if utils.aspect_of_starz:
        damage += 10
      damage -= utils.enemy_de
      if damage < 0:
        damage = 0
      print(damage)
      utils.enemy_hp -= damage
    if mech_mode and ch >= 3:
      ch -= 3
      if utils.aspect_of_smileez:
          ch -= 3 * 0.25
      lasers = ["|", " |", "  |", "    |", "     |"]
      for rounds in range(30):
        time.sleep(0.1)
        laser = random.choice(lasers)
        print(laser)
        damage = random.uniform(1, 3)
        if utils.aspect_of_comet:
          damage = random.uniform(3, 7)
        utils.enemy_hp -= damage
  elif choice == "4":
    if utils.aspect_of_light:
        utils.hp += 15
    if not mech_mode and ch == 100:
      utils.fast_print("MECH TIME, BABY >:D!!")
      utils.de += 30
      mech_mode = True
    elif mech_mode:
      utils.fast_print("back to boring old normal mode :(")
      mech_mode = False
      if ch >= 25:
        utils.fast_print("!!! BATTERY REFUND !!!")
        ch += 15
  else:
    utils.fast_print("WE NEDD TO FGIHT THEM NTO DO WAHETEVR YUOR DIONG >:(")
  blu_dodge = False