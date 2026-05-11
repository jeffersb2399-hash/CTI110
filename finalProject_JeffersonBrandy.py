#Brandy Jefferson
#10 May 2026
#Final Project 
#Text-Based Adventure Game

"""
╔══════════════════════════════════════════════════════════╗
║          🗡️  SHADOW QUEST: THE LOST RELIC  🗡️            ║
║         A Text-Based Python Adventure Game               ║
╚══════════════════════════════════════════════════════════╝
"""

import random
import time

# ─────────────────────────────────────────────
#  CHARACTER & INVENTORY SETUP
# ─────────────────────────────────────────────

def create_character(name):
    """Create and return the main character dictionary."""
    character = {
        "name": name,
        "class": "Shadow Hunter",
        "level": 1,
        "vitality": 100,
        "max_vitality": 100,
        "power": 15,
        "defense": 10,
        "gold": 50,
        "xp": 0,
        "xp_to_level": 100,
        "location": "Village of Ashveil",
        "status": "Focused 💚",
        "quests_completed": 0,
        "alive": True
    }
    return character


def create_inventory():
    """Create and return the character's starting inventory dictionary."""
    inventory = {
        "Elixir 🧪": 2,
        "Rusty Sword ⚔️": 1,
        "Leather Armor 🛡️": 1,
        "Torch 🔦": 1,
        "Bread 🍞": 3
    }
    return inventory


# ─────────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────────

def slow_print(text, delay=0.03):
    """Print text character by character for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def print_divider():
    print("\n" + "═" * 55 + "\n")


def show_stats(character):
    """Display the character's current stats."""
    print_divider()
    print(f"  👤 {character['name']} | {character['class']}  |  Level {character['level']}")
    print(f"  💜 Vitality: {character['vitality']}/{character['max_vitality']}   ⚔️  Power: {character['power']}   🛡️  DEF: {character['defense']}")
    print(f"  💰 Gold: {character['gold']}   ⭐ XP: {character['xp']}/{character['xp_to_level']}")
    print(f"  📍 Location: {character['location']}   Status: {character['status']}")
    print_divider()


def show_inventory(inventory):
    """Display the character's inventory."""
    print("\n  🎒 YOUR INVENTORY:")
    print("  " + "─" * 30)
    if not inventory:
        print("  (empty)")
    else:
        for item, qty in inventory.items():
            print(f"    {item} x{qty}")
    print()


# ─────────────────────────────────────────────
#  UTILITY FUNCTIONS
# ─────────────────────────────────────────────

def gain_xp(character, amount):
    """Award XP and handle leveling up."""
    character["xp"] += amount
    slow_print(f"\n  ✨ You gained {amount} XP!")
    if character["xp"] >= character["xp_to_level"]:
        level_up(character)


def level_up(character):
    """Level up the character and improve stats."""
    character["level"] += 1
    character["xp"] = character["xp"] - character["xp_to_level"]
    character["xp_to_level"] = int(character["xp_to_level"] * 1.5)
    character["max_vitality"] += 20
    character["vitality"] = character["max_vitality"]
    character["power"] += 5
    character["defense"] += 3
    character["status"] = "Empowered 💛"
    time.sleep(0.5)
    print()
    slow_print("  ⭐ ⭐ ⭐  LEVEL UP!  ⭐ ⭐ ⭐")
    slow_print(f"  You are now Level {character['level']}!")
    slow_print(f"  Max Vitality ↑  |  Power ↑  |  Defense ↑")


def use_elixir(character, inventory):
    """Use an Elixir if available."""
    elixir_key = "Elixir 🧪"
    if inventory.get(elixir_key, 0) > 0:
        restore = random.randint(25, 45)
        character["vitality"] = min(character["vitality"] + restore, character["max_vitality"])
        inventory[elixir_key] -= 1
        if inventory[elixir_key] == 0:
            del inventory[elixir_key]
        slow_print(f"\n  🧪 You drink an Elixir and restore {restore} Vitality!")
        slow_print(f"  💜 Vitality is now {character['vitality']}/{character['max_vitality']}")
        return True
    else:
        slow_print("\n  ❌ You have no Elixirs!")
        return False


def check_alive(character):
    """Check if character is still alive."""
    if character["vitality"] <= 0:
        character["vitality"] = 0
        character["alive"] = False
        character["status"] = "Fallen 💀"
    return character["alive"]


# ─────────────────────────────────────────────
#  COMBAT SYSTEM
# ─────────────────────────────────────────────

def combat(character, inventory, enemy_name, enemy_vit, enemy_pwr, enemy_xp, enemy_gold, enemy_drop=None):
    """
    Run a turn-based combat encounter.
    Returns True if player wins, False if player loses.
    """
    print_divider()
    slow_print(f"  ⚠️  A wild {enemy_name} appears!")
    time.sleep(0.5)
    slow_print(f"  {enemy_name}  |  Vitality: {enemy_vit}  |  Power: {enemy_pwr}")
    print_divider()

    current_enemy_vit = enemy_vit

    while current_enemy_vit > 0 and character["alive"]:
        print(f"\n  Your Vitality: {character['vitality']}/{character['max_vitality']}   |   {enemy_name} Vitality: {current_enemy_vit}")
        print("\n  What will you do?")
        print("    [1] ⚔️  Attack")
        print("    [2] 🧪  Use Elixir")
        print("    [3] 🏃 Flee")

        choice = input("\n  > ").strip()

        if choice == "1":
            # Player attacks
            crit = random.random() < 0.15  # 15% crit chance
            player_dmg = random.randint(character["power"] - 3, character["power"] + 5)
            if crit:
                player_dmg = int(player_dmg * 1.8)
                slow_print(f"\n  💥 CRITICAL HIT! You dealt {player_dmg} damage!")
            else:
                slow_print(f"\n  ⚔️  You attack for {player_dmg} damage!")
            current_enemy_vit -= player_dmg

            if current_enemy_vit <= 0:
                break

            # Enemy attacks back
            enemy_dmg = max(1, random.randint(enemy_pwr - 3, enemy_pwr + 2) - character["defense"] // 3)
            character["vitality"] -= enemy_dmg
            slow_print(f"  💢 {enemy_name} hits you for {enemy_dmg} damage!")

            if character["vitality"] <= 25:
                character["status"] = "Injured 🟡"
            if character["vitality"] <= 0:
                check_alive(character)

        elif choice == "2":
            use_elixir(character, inventory)
            # Enemy still attacks
            enemy_dmg = max(1, random.randint(enemy_pwr - 3, enemy_pwr + 2) - character["defense"] // 3)
            character["vitality"] -= enemy_dmg
            slow_print(f"  💢 {enemy_name} hits you for {enemy_dmg} damage!")
            if character["vitality"] <= 0:
                check_alive(character)

        elif choice == "3":
            flee_chance = random.random()
            if flee_chance > 0.4:
                slow_print(f"\n  🏃 You successfully flee from {enemy_name}!")
                return False
            else:
                slow_print(f"\n  ❌ You couldn't escape! {enemy_name} blocks your path!")
                enemy_dmg = max(1, random.randint(enemy_pwr - 2, enemy_pwr + 4) - character["defense"] // 3)
                character["vitality"] -= enemy_dmg
                slow_print(f"  💢 {enemy_name} hits you for {enemy_dmg} damage!")
                if character["vitality"] <= 0:
                    check_alive(character)
        else:
            slow_print("  ❓ Invalid choice. You hesitate — the enemy attacks!")
            enemy_dmg = max(1, random.randint(enemy_pwr, enemy_pwr + 5) - character["defense"] // 3)
            character["vitality"] -= enemy_dmg
            slow_print(f"  💢 {enemy_name} hits you for {enemy_dmg} damage!")
            if character["vitality"] <= 0:
                check_alive(character)

    # ── Outcome ──
    if not character["alive"]:
        return False

    # Victory
    time.sleep(0.4)
    slow_print(f"\n  🏆 You defeated the {enemy_name}!")
    character["gold"] += enemy_gold
    slow_print(f"  💰 You looted {enemy_gold} gold!")
    gain_xp(character, enemy_xp)

    # Loot drop
    if enemy_drop and random.random() < 0.5:
        item, qty = enemy_drop
        inventory[item] = inventory.get(item, 0) + qty
        slow_print(f"  🎁 You found: {item} x{qty}!")

    if character["vitality"] > 0 and character["status"] != "Empowered 💛":
        character["status"] = "Focused 💚"

    character["quests_completed"] += 1
    return True


# ─────────────────────────────────────────────
#  LOCATIONS / EVENTS
# ─────────────────────────────────────────────

def visit_village(character, inventory):
    """Visit the Village of Ashveil — rest, shop, or get a quest."""
    character["location"] = "Village of Ashveil 🏘️"
    print_divider()
    slow_print("  🏘️  VILLAGE OF ASHVEIL")
    slow_print("  Lanterns flicker. The smell of bread drifts from the inn.")
    print()
    print("    [1] 🛏️  Rest at the Inn (costs 10 gold, full heal)")
    print("    [2] 🛒  Visit the Shop")
    print("    [3] 📋  Accept a Bounty Quest")
    print("    [4] 🗺️  Leave the Village")

    choice = input("\n  > ").strip()

    if choice == "1":
        if character["gold"] >= 10:
            character["gold"] -= 10
            character["vitality"] = character["max_vitality"]
            character["status"] = "Rested 💚"
            slow_print("\n  🛏️  You sleep soundly. Vitality fully restored!")
        else:
            slow_print("\n  ❌ Not enough gold to rest.")

    elif choice == "2":
        visit_shop(character, inventory)

    elif choice == "3":
        bounty_quest(character, inventory)

    elif choice == "4":
        slow_print("\n  🗺️  You head out into the wilderness...")
    else:
        slow_print("  ❓ The innkeeper eyes you suspiciously. Nothing happens.")


def visit_shop(character, inventory):
    """Simple shop system."""
    print_divider()
    slow_print("  🛒  MERCHANT'S STALL")
    slow_print(f"  Your gold: 💰 {character['gold']}")
    print()
    shop_items = {
        "1": ("Elixir 🧪", 20),
        "2": ("Iron Sword ⚔️", 60),
        "3": ("Chain Mail 🛡️", 80),
        "4": ("Smoke Bomb 💨", 30),
    }
    for key, (item, price) in shop_items.items():
        print(f"    [{key}] {item}  — {price} gold")
    print("    [5] Leave Shop")

    choice = input("\n  > ").strip()
    if choice in shop_items:
        item, price = shop_items[choice]
        if character["gold"] >= price:
            character["gold"] -= price
            inventory[item] = inventory.get(item, 0) + 1
            slow_print(f"\n  ✅ Purchased {item}!")
            # Upgrade stats if weapon/armor bought
            if "Iron Sword" in item:
                character["power"] += 8
                slow_print("  ⚔️  Your power increased!")
            if "Chain Mail" in item:
                character["defense"] += 7
                slow_print("  🛡️  Your defense increased!")
        else:
            slow_print("\n  ❌ Not enough gold.")
    elif choice == "5":
        slow_print("\n  You leave the shop.")
    else:
        slow_print("\n  ❓ The merchant shrugs.")


def bounty_quest(character, inventory):
    """A random bounty encounter in the wilds."""
    slow_print("\n  📋 The village elder hands you a bounty notice...")
    time.sleep(0.5)

    quests = [
        {
            "desc": "🐺 A pack of wolves terrorizes the forest road.",
            "enemy": "Wolf Pack 🐺", "vit": random.randint(35, 50),
            "pwr": 12, "xp": 40, "gold": random.randint(20, 35),
            "drop": ("Wolf Pelt 🐺", 1)
        },
        {
            "desc": "💀 Skeletons have risen from the old graveyard.",
            "enemy": "Skeleton Warrior 💀", "vit": random.randint(45, 60),
            "pwr": 14, "xp": 55, "gold": random.randint(25, 40),
            "drop": ("Bone Shard 💀", 2)
        },
        {
            "desc": "🕷️ A giant spider blocks the mountain pass.",
            "enemy": "Giant Spider 🕷️", "vit": random.randint(40, 55),
            "pwr": 13, "xp": 50, "gold": random.randint(20, 30),
            "drop": ("Spider Silk 🕸️", 1)
        },
    ]

    quest = random.choice(quests)
    slow_print(f"\n  Quest: {quest['desc']}")
    input("\n  Press ENTER to head out...")

    character["location"] = "The Wilds 🌲"
    won = combat(
        character, inventory,
        quest["enemy"], quest["vit"], quest["pwr"],
        quest["xp"], quest["gold"], quest["drop"]
    )

    if won:
        reward_gold = random.randint(15, 30)
        character["gold"] += reward_gold
        slow_print(f"\n  📋 Quest Complete! The village rewards you {reward_gold} gold!")
        character["quests_completed"] += 1


def explore_dungeon(character, inventory):
    """Multi-room dungeon crawl with escalating enemies."""
    character["location"] = "The Shadow Dungeon 🏰"
    print_divider()
    slow_print("  🏰  THE SHADOW DUNGEON")
    slow_print("  Cold air rushes from the iron gate. Shadows writhe within.")
    time.sleep(0.5)

    dungeon_enemies = [
        {"enemy": "Dungeon Rat 🐀",    "vit": 20, "pwr": 8,  "xp": 20, "gold": 10, "drop": ("Rat Tail 🐀", 1)},
        {"enemy": "Dark Goblin 👺",    "vit": 40, "pwr": 13, "xp": 40, "gold": 20, "drop": ("Goblin Dagger 🗡️", 1)},
        {"enemy": "Stone Golem 🪨",    "vit": 70, "pwr": 18, "xp": 70, "gold": 35, "drop": ("Magic Ore 💎", 1)},
        {"enemy": "Shadow Wraith 👻",  "vit": 85, "pwr": 22, "xp": 90, "gold": 50, "drop": ("Wraith Essence ✨", 1)},
    ]

    slow_print("\n  You descend into darkness... 🔦")
    time.sleep(0.8)

    rooms_cleared = 0
    for i, enc in enumerate(dungeon_enemies):
        if not character["alive"]:
            break
        input(f"\n  [ Room {i+1} ] Press ENTER to continue... ")
        won = combat(
            character, inventory,
            enc["enemy"], enc["vit"], enc["pwr"],
            enc["xp"], enc["gold"], enc["drop"]
        )
        if won:
            rooms_cleared += 1
            if i < len(dungeon_enemies) - 1:
                slow_print(f"\n  You press deeper into the dungeon... ({rooms_cleared} rooms cleared)")
        else:
            if not character["alive"]:
                break
            slow_print("\n  You retreat from the dungeon, bruised but alive.")
            break

    if rooms_cleared == len(dungeon_enemies):
        print_divider()
        slow_print("  🏆 🏆 🏆  DUNGEON CLEARED!  🏆 🏆 🏆")
        slow_print("  You find the Lost Relic gleaming on the altar!")
        inventory["Lost Relic 🔮"] = inventory.get("Lost Relic 🔮", 0) + 1
        character["gold"] += 150
        gain_xp(character, 200)
        character["status"] = "Legendary 🌟"
        slow_print("  💰 +150 Gold  |  ✨ +200 XP  |  🔮 Lost Relic acquired!")


def random_event(character, inventory):
    """A random world event — could be good or bad."""
    events = [
        lambda: _event_treasure(character, inventory),
        lambda: _event_trap(character),
        lambda: _event_merchant(character, inventory),
        lambda: _event_ambush(character, inventory),
        lambda: _event_blessing(character),
    ]
    event = random.choice(events)
    event()


def _event_treasure(character, inventory):
    slow_print("\n  💎 You spot a glimmering chest off the trail!")
    gold = random.randint(20, 60)
    character["gold"] += gold
    inventory["Elixir 🧪"] = inventory.get("Elixir 🧪", 0) + 1
    slow_print(f"  You found {gold} gold and an Elixir!")


def _event_trap(character):
    dmg = random.randint(10, 25)
    character["vitality"] = max(1, character["vitality"] - dmg)
    slow_print(f"\n  💣 SNAP! You trigger a hidden trap! -{dmg} Vitality!")
    if character["vitality"] <= 25:
        character["status"] = "Injured 🟡"


def _event_merchant(character, inventory):
    slow_print("\n  🧙 A wandering mage offers you a deal...")
    if character["gold"] >= 30:
        character["gold"] -= 30
        inventory["Mystery Potion 💜"] = inventory.get("Mystery Potion 💜", 0) + 1
        slow_print("  You paid 30 gold for a Mystery Potion 💜.")
    else:
        slow_print("  You can't afford the mage's wares. They vanish in smoke.")


def _event_ambush(character, inventory):
    slow_print("\n  ⚠️  Bandits leap from the shadows!")
    combat(character, inventory, "Bandit 🗡️",
           random.randint(30, 45), 11, 35, random.randint(15, 30),
           ("Stolen Coin Pouch 💰", 1))


def _event_blessing(character):
    restore = random.randint(15, 30)
    character["vitality"] = min(character["vitality"] + restore, character["max_vitality"])
    slow_print(f"\n  🌟 A beam of golden light touches you. +{restore} Vitality restored!")
    character["status"] = "Blessed 💛"


# ─────────────────────────────────────────────
#  GAME OVER / WIN SCREENS
# ─────────────────────────────────────────────

def game_over(character):
    print_divider()
    slow_print("  💀  GAME OVER  💀", delay=0.06)
    slow_print(f"\n  {character['name']} has fallen in battle.")
    slow_print(f"  Level reached: {character['level']}  |  Quests completed: {character['quests_completed']}")
    slow_print(f"  Gold carried: 💰 {character['gold']}")
    print_divider()


def victory_screen(character):
    print_divider()
    slow_print("  🌟  VICTORY!  🌟", delay=0.06)
    slow_print(f"\n  {character['name']} has retrieved the Lost Relic!")
    slow_print(f"  Final Level: {character['level']}  |  Quests: {character['quests_completed']}")
    slow_print(f"  Gold: 💰 {character['gold']}  |  Status: {character['status']}")
    print_divider()


# ─────────────────────────────────────────────
#  INTRO
# ─────────────────────────────────────────────

def show_intro():
    print("\n" + "═" * 55)
    slow_print("  🗡️   SHADOW QUEST: THE LOST RELIC   🗡️", delay=0.05)
    print("═" * 55)
    time.sleep(0.3)
    slow_print("\n  Long ago, the Lost Relic kept darkness at bay.")
    slow_print("  It was stolen and locked deep within the Shadow Dungeon.")
    slow_print("  You are Ashveil's last hope. 🌑")
    time.sleep(0.5)


# ─────────────────────────────────────────────
#  MAIN GAME LOOP
# ─────────────────────────────────────────────

def main():
    """Main function — entry point for Shadow Quest."""
    show_intro()

    name = input("\n  Enter your hero's name: ").strip()
    if not name:
        name = "Hero"

    character = create_character(name)
    inventory = create_inventory()

    slow_print(f"\n  Welcome, {character['name']} the {character['class']}! ⚔️")
    slow_print("  Your quest begins in the Village of Ashveil.")
    time.sleep(0.5)

    # ── Main Game Loop ──
    while character["alive"]:

        # Win condition — player has the Lost Relic
        if "Lost Relic 🔮" in inventory:
            victory_screen(character)
            break

        show_stats(character)
        print("  🗺️  WORLD MAP — What will you do?")
        print()
        print("    [1] 🏘️  Visit the Village of Ashveil")
        print("    [2] 🏰  Enter the Shadow Dungeon")
        print("    [3] 🎲  Explore the Wilds (random event)")
        print("    [4] 🎒  Check Inventory")
        print("    [5] 🚪  Quit Game")
        print()

        choice = input("  > ").strip()

        if choice == "1":
            visit_village(character, inventory)

        elif choice == "2":
            if character["level"] < 2:
                slow_print("\n  ⚠️  The dungeon gate is sealed. You must be Level 2 to enter!")
                slow_print("  Complete bounty quests and explore the wilds to level up first.")
            else:
                explore_dungeon(character, inventory)

        elif choice == "3":
            slow_print("\n  🌲 You venture into the wilds...")
            time.sleep(0.6)
            random_event(character, inventory)

        elif choice == "4":
            show_inventory(inventory)
            use_pot = input("  Use an Elixir? (y/n): ").strip().lower()
            if use_pot == "y":
                use_elixir(character, inventory)

        elif choice == "5":
            slow_print(f"\n  Farewell, {character['name']}. May the shadows spare you. 🌑")
            break

        else:
            slow_print("\n  ❓ Unknown command.")

        # Check death after any action
        if not check_alive(character):
            game_over(character)
            break

        time.sleep(0.3)

    slow_print("\n  Thanks for playing Shadow Quest! 🗡️\n")


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    main()
