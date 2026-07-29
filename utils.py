import time
import sys
import hosts
import random
import blu

is_sans = False

# --- PLAYER STATE ---
upgrade_flags = set()   # Tracks which upgrades have been taken

damage = 0
enemy_damage = 0

hp = 100
enemy_hp = 0

sta = 20
enemy_sta = 0

de = 15
enemy_de = 0

enemy_attacks = ""

harpoon_turn = 1
harpoon_cost = 8

vanguard_cost = 10
vanguard_gain = 15

sta_gain = 3
enemy_sta_gain = 3

ego_mult_1 = 0
ego_mult_2 = 0

flare_gain = 5
ego_dodge = False
artifex_mult = False

# --- UPGRADE FLAGS ---

# Ego
eclipse = False
eclipse_de = None
sugar_tea_and_rum = False
sajioyero = False
santo_fricsat = False
starry_days = False
starry_turn = None
sunny_nights = False
townfolk = False
deaf_man_music = False
infernum_and_polaris = False
onus_dei = False

# Argo
ad_mare = False
perdita_animarum = False
exploratio = False
ferrum_mens = False
stellae_et_ultra = False
omnes_et_plus = False

# Artifex
jealousy = False
pride = False
tisha_and_brusha = False
joy = False
hope = False
nostalgia = False
anger = False
fear = False

# Goober
salt_the_rim = False
cornucopia = False
jarrets_shard = False
cross_the_line = False
tsunami = False
double_struck = False
extra_ammo = False
manias_lies = False
i_will_not_be_moved = False

# Blu
aspect_of_smileez = False
aspect_of_beast = False
aspect_of_thicez = False
aspect_of_comet = False
aspect_of_stan = False
aspect_of_light = False
aspect_of_dark = False
aspect_of_shapeshifter = False
aspect_of_starz = False
aspect_of_pintr = False


def slow_print(text, delay=0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in ".!?":
            time.sleep(delay * 6)
        elif char in ",;:":
            time.sleep(delay * 3)
        else:
            time.sleep(delay)
    print()


def fast_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def upgrade_choice(host_name: str):
    """
    Show upgrade choices for the current host, apply the selected upgrade,
    and return the selected upgrade string (or None if skipped).
    """
    global de, hp, sta, sta_gain, flare_gain, vanguard_gain
    global eclipse, eclipse_de
    global sugar_tea_and_rum, sajioyero, santo_fricsat
    global starry_days, sunny_nights, townfolk, deaf_man_music
    global infernum_and_polaris, onus_dei
    global ad_mare, perdita_animarum, exploratio, ferrum_mens
    global stellae_et_ultra, omnes_et_plus
    global jealousy, pride, tisha_and_brusha, joy, hope
    global nostalgia, anger, fear
    global salt_the_rim, i_will_not_be_moved, cornucopia, jarrets_shard, extra_ammo, tsunami, double_struck, cross_the_line, manias_lies

    # Use the passed host_name if given, otherwise fall back to hosts.host
    if not host_name:
        host_name = getattr(hosts, "host", "").lower()
    else:
        host_name = host_name.lower()

    HOST_UPGRADES = {
        "argo": hosts.argo_upgrades,
        "ego": hosts.ego_upgrades,
        "artifex": hosts.artifex_upgrades,
        "blu": hosts.blu_upgrades,
        "goober": hosts.goober_upgrades,
        "sans": hosts.sans_upgrades
    }

    if host_name not in HOST_UPGRADES:
        raise ValueError(f"No upgrade list found for host '{host_name}'")

    # Filter out upgrades already taken
    available = [u for u in HOST_UPGRADES[host_name] if u not in upgrade_flags]

    if not available:
        fast_print("\nNo more upgrades available for this host.")
        return None

    num_to_show = min(3, len(available))
    chosen = random.sample(available, num_to_show)
    chosen.append("Skip")

    fast_print("\nChoose an upgrade:")
    for i, up in enumerate(chosen, 1):
        # Display only the part before any quotes, if present
        name = up.split('"')[0].strip()
        fast_print(f"{i}. {name}")

    while True:
        choice = input("\nEnter number: ").strip()
        if not choice.isdigit():
            fast_print("Please enter a valid number.")
            continue

        choice = int(choice)
        if not (1 <= choice <= len(chosen)):
            fast_print("Invalid choice.")
            continue

        selected = chosen[choice - 1]

        if selected == "Skip":
            fast_print("You skipped the upgrade.")
            return None

        # Mark upgrade as taken
        upgrade_flags.add(selected)

        name = selected.split('"')[0].strip()
        fast_print(f"You selected: {name}")

        # --- EGO UPGRADES ---
        if ("خسوف" in selected) or ("Eclipse" in selected):
            eclipse = True
            de += 15
            hp -= 10
            # Keep defense as int
            de = int(round(de))
            hp = int(round(hp))
            eclipse_de = de

        elif "Sugar, Tea, and Rum" in selected:
            sugar_tea_and_rum = True
            sta += 5
            hp += 10
            de += 3
            sta = int(round(sta))
            hp = int(round(hp))
            de = int(round(de))

        elif "Sajioyero" in selected:
            sajioyero = True

        elif "Santo Fricsat" in selected:
            santo_fricsat = True

        elif "Starry Days" in selected:
            starry_days = True

        elif "Sunny Nights" in selected:
            sunny_nights = True
            # Hard reset stats as designed
            de = 20
            hp = 100
            sta = 15

        elif "Townfolk" in selected:
            townfolk = True

        elif "Deaf Man Music" in selected:
            deaf_man_music = True

        elif "Infernum and Polaris" in selected:
            infernum_and_polaris = True
            sta_gain = 5

        elif "Onus Dei" in selected:
            onus_dei = True
            sta_gain = 1

        # --- ARGO UPGRADES ---
        elif "Ad Mare" in selected:
            ad_mare = True
            sta_gain -= 1
            de += 5
            de = int(round(de))

        elif "Perdita Animarum" in selected:
            perdita_animarum = True
            de -= 3
            sta_gain += 1
            de = int(round(de))

        elif "Exploratio" in selected:
            exploratio = True
            flare_gain = 4

        elif "Ferrum Mens" in selected:
            ferrum_mens = True
            de += 10
            vanguard_gain -= 7
            de = int(round(de))

        elif "Stellae Et Ultra" in selected:
            stellae_et_ultra = True
            flare_gain += 2

        elif "Omnes Et Plus" in selected:
            omnes_et_plus = True
            flare_gain += 5

        # --- ARTIFEX UPGRADES ---
        elif "Jealousy" in selected:
            jealousy = True

        elif "Pride" in selected:
            pride = True
            # Apply multiplicative effects but keep ints
            de = int(round(de * 0.75))
            hp = int(round(hp * 1.1))

        elif "Tisha and Brusha" in selected:
            tisha_and_brusha = True

        elif "Joy" in selected:
            joy = True

        elif "Hope" in selected:
            hope = True

        elif "Nostalgia" in selected:
            nostalgia = True

        elif "Anger" in selected:
            anger = True

        elif "Fear" in selected:
            fear = True
            # This effect triggers immediately on pick if condition met
            if hp < 25:
                sta += 20
                sta = int(round(sta))
        # Goober
        elif "'something funny'" in selected:
          salt_the_rim = True
        elif "Extra Ammo" in selected:
          extra_ammo = True
        elif "Wait why do none of the monkes in gorilla tag have legs? are they okay?" in selected:
          cornucopia = True
        elif "watch the world burn :D " in selected:
          jarrets_shard = True
        elif "TSUNDRENAMI" in selected:
          tsunami = True
        elif "Mo circles, mo problems" in selected:
          cross_the_line = True
        elif "Starstruck" in selected:
          double_struck = True
        elif "Ichor Overflow" in selected:
          manias_lies = True
        elif "I will not be moved" in selected:
          hp -= 30
          de += 15
          i_will_not_be_moved = True
        # Blu
        elif "Aspect Of Smileez" in selected:
          aspect_of_smileez = True
        elif "Aspect Of Beast" in selected:
          aspect_of_beast = True
        elif "Aspect Of Thicez" in selected:
          blu.stun_chance *= 1.25
          aspect_of_thicez = True
        elif "Aspect Of Comet" in selected:
          aspect_of_comet = True
        elif "Aspect Of Stan" in selected:
          utils.hp += 1
          aspect_of_stan = True
        elif "Aspect Of Light" in selected:
          aspect_of_light = True
        elif "Aspect Of Dark":
          aspect_of_dark = True
        elif "Aspect Of SH4P35H1FT3R":
          aspect_of_shapeshifter = True
        elif "Aspect Of Starz":
          aspect_of_starz = True
        elif "Aspect Of Pintr":
          aspect_of_pintr = True
        return selected

        fast_print("Invalid choice.")