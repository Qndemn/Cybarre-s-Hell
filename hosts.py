import utils
import time
import random

host = ""

# ANSI COLORS
RESET = "\033[0m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# BRIGHT COLORS
BRIGHT_BLACK = "\033[90m"
BRIGHT_RED = "\x1b[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"

def blu():
  utils.fast_print("---- Blu Attacks ----")
  utils.fast_print("NORMAL MODE:")
  utils.fast_print("1. Stun Grenade (50% chance of stunning enemies, deals no damage. 3 STA cost. Regain 15 BATTERY On Hit)")
  utils.fast_print("2. Roll (+4 STA, activate DODGE, heal 15 HP)")
  utils.fast_print("3. Laser Round (1 STA Cost, basic attack. Regain 20 BATTERY)")
  utils.fast_print("4. Mech Mode, Drains 5 BATTERY Every Active Turn")
  utils.fast_print("MECH MODE:")
  utils.fast_print("1. Stun Volley (No STA Cost, costs 6 BATTERY)")
  utils.fast_print("2. Rocket (No STA Cost, Costs 1 BATTERY per round in the air)")
  utils.fast_print("3. Beam Cascade (No STA Cost, 3 BATTERY Cost. Deals damage to enemies.)")
  utils.fast_print("4. Normal Mode, Refund BATTERY If Battery Over 25.")

def goober():
  utils.fast_print(f"{BRIGHT_RED}---- Goober Attacks ----")
  utils.fast_print("1. Circle (Rain hellfire down upon those who wish to obstruct you! It used to have a better name! now it doesn't! haha, serious players, take that!)")
  utils.fast_print("2. Salvo! (Get A Few Buffs, Including Healing. Why Did I Name It Salvo? Because It Sounds-)")
  utils.fast_print(f"3. Drunk Fish (Ok, I'll explain... So, my uncle Larry, he's a fish, right? And he-)")
  print("\n"*999)

def ego():
  utils.fast_print("---- EGO ATTACKS ----")
  utils.fast_print("$ Gamble Gamble $ oh wait that's not his lore uh... here:\n# And Yet More Is In His Grasp #")
  utils.fast_print("1. Godspeed (Activate DODGE, + 3 STA, x2 DM For Two Turns)")
  utils.fast_print("2. Onus (Decrease STA Gain To 1, x2 DM For Two Turns)")
  utils.fast_print("3. Oblivio (25-50 DM, 3 STA Cost)")

def artifex():
  utils.fast_print("---- ARTIFEX ATTACKS ----")
  utils.fast_print("/ Good for strategy :D \\")
  utils.fast_print("1. Lancea Artifex (1-60 DM, 3 STA Cost)")
  utils.fast_print("2. Delere (All Attacks +15 For One Turn, 6 STA Cost)")
  utils.fast_print("3. Sciagraphia (5-10 DM, STA + 5, DEF + 1 Permanently)")

def argo():
  utils.fast_print("---- ARGO ATTACKS ----")
  utils.fast_print(f"{BRIGHT_RED}! NOT FOR NEW PLAYERS !{RESET}")
  utils.fast_print("1. Harpoon (60-80 DM, 8 STA Cost On First Hit, Second Use (Flurry) 5 STA Cost, 25 Rounds of 1-3 DM)")
  utils.fast_print("2. Flare (20-35 DM, + 5 STA, DEF - 3 Permanently.)")
  utils.fast_print("3. Vanguard (10 STA Cost, DEF + 15 Permanently.)\n(Each Consecutive Use Adds 3 To DEF Gain And 5 To STA Cost. Each Attack Used Decreases The Cost Of Vanguard By 1.)")

def sans():
  utils.fast_print("*...")

argo_upgrades = [
  "Ad Mare 'Stranded at sea, and yet we march onward.'\nSTA Gain - 1, DEF + 5",
  "Perdita Animarum 'My crew, now lost. And yet we march onward.'\nDEF - 3, STA Gain + 1",
  "Exploratio 'We learn and persevere. And so we march onward.'\nHarpoon First Hit does 15 more damage, but flare only gives 4 STA",
  "Ferrum Mens 'Only those with an iron will to live will survive. And yet we march onward.'\n DEF + 10, Vanguard gives back 7 less DEF",
  "Stellae Et Ultra 'The final frontier. But still there is more. And yet we march onward.'\n Flare grants + 2 more STA, Harpoon deals 20 less DM",
  "Omnes Et Plus 'Your Will To Live Outweighs Your Will To Explore, courage and determination are your guides thru this hell. March onward.'\nFlare deals - 10 DM but gains + 5 STA"
]

ego_upgrades = [
  "Sugar, Tea & Rum 'The essentials to life'\nHP + 10, STA + 5, DEF + 3",
  "Sajioyero 'The voyager's final destination'\nSTA Gain recovers HP according to current STA divided by 4 every turn.",
  "Santo Fricsat 'What was lost is never found again.'\nLose 10 HP every turn, but you gain 25% lifesteal.",
  "Starry Days 'Passing Fad'\n+150% DM for first attack, -15% DM for every following attack.",
  "Sunny Nights 'Beauty we have lost'\nDEF set to 20, HP set to 100, and STA set to 15.",
  "Townfolk 'The revelry and joy of times now pass'd.'\nOnus sets STA gain to 3 rather than 1.",
  "Deaf Man's Music 'The true beauty of reality's fragility.'\nAll attacks have 5% lifesteal, 5% STA regain, and 5% DEF regain according to DM dealt.",
  "Infernum & Polaris 'Miriat & Eden, hand in hand until the end.'\nOblivio will always hit for 40 DM. STA Gain can never go over or under 5.",
  "خسوف «چیزهای زیادی برای دیدن هست، کارهای زیادی برای انجام دادن هست، و برای تو و من وقت خیلی کم است.»\nDEF set to current location permanently. DEF + 15, HP - 10.",
  "Onus Dei 'Those in charge have too much power both for their benefit and that of their people.'\nSTA Gain set to 1, DM x1.25"
]

artifex_upgrades = [
  "Jealousy 'W e  h a v e  o v e r c o m e  y o u'\nWhenever an enemy deals more damage than you on a turn, they receive 50% of that damage back. This only works if you choose to attack on that turn.",
  "Pride\nDM x1.1, DEF x0.75, HP x1.1",
  "Tisha & Brusha 'Together Until The End...?'\nAll damage dealt is halved and one half dealt back to you, but the same for the opponent.",
  "Joy 'Naught but in passing'\nDelere Gives 5 Less DM Buff, but x1.1 DM",
  "Hope 'I knew they wouldn't return, yet still I carried the flame'\nDEF Takes 25% Of Damage Dealt, DM x1.5",
  "Nostalgia 'I yearn for futures we could have had'\nLancea Artifex Hits Twice, But Max Damage Is Capped At 45.",
  "Anger 'Y o u  h a v e  n o  p l a c e  h e r e'\nGain 10 HP Every Turn, but take 35% Of Damage Dealt.",
  "Fear 'Loss of what?'\nNothing To Lose, Something To Gain. If HP < 25, STA + 20"
]

blu_upgrades = [
  "Aspect Of Smileez: Gain x1.5 CH On Normal Mode, But Spend x1.25 CH On Mech Mode.",
  "Aspect Of Beast: On Mech Mode, CH Is No Longer Drained By One Per Round.",
  "Aspect Of Thicez: Stun Grenade +25% Chance Of Stunning Enemies.",
  "Aspect Of Comet: Beam Cascade DM Range Set To 3-7 Per Hit Rather Than 1-4.",
  "Aspect Of Stan: You Take x999 Damage, But HP + 1.",
  "Aspect Of Light: Heal +15 HP On Every Turn On Which You Don't Attack.",
  "Aspect Of Dark: Refund 25% Of STA Spent On Each Attack.",
  "Aspect Of SH4P35H1FT3R: At The Start Of Each Round, Starting STA Set To Enemy STA.",
  "Aspect Of Starz: Laser Round Gets +10 DM On Hit.",
  "Aspect Of Pintr: Fananphobia: Does nothing to affect gameplay. You're scared of fans now."
]

goober_upgrades = [
  "'something funny': CLEAVE Hits Twice.",
  "Wait why do none of the monkes in gorilla tag have legs? are they okay?: All Stat Buffs + On Salvo!",
  "watch the world burn :D : Circle Deals 50% More DM",
  "Mo circles, mo problems: Circle Lasts Longer",
  "TSUNDRENAMI : 'don't ask what that means' Salvo! Deals 30 DM To Enemies, But Also Increases Their STA By 6",
  "Starstruck: 'ow that star hit me' GASH Hits Twice",
  "Extra Ammo: 'ℚ Hey, that's the average American!' BAM Hits Twice",
  "Ichor Overflow: 'this one's kinda cringey ngl' Drunk Fish Lasts Longer",
  "I will not be moved: 'Can't hold me back' DM x50%, HP - 30, DEF + 15"
]

sans_upgrades = ["*i'm too tired", "*sorry, i don't want to", "*not really feeling up to it right now", "*nah", "*what about 'no'", "*still no upgrades, pal", "*hey, don't look at me! look at whatever idiot is making this game!", "*mmm... no"]