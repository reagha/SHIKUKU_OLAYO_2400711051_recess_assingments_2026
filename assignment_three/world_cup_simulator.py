import random


def initialize_teams(countries):
    for country in countries:
        country["wins"] = 0
        country["draws"] = 0
        country["losses"] = 0
        country["points"] = 0
        country["consecutive_wins"] = 0


def create_groups(countries):

    slot1, slot2, slot3, slot4 = [], [], [], []

    for country in countries:
        if country["weight"] == 4:
            slot1.append(country)
        elif country["weight"] == 3:
            slot2.append(country)
        elif country["weight"] == 2:
            slot3.append(country)
        else:
            slot4.append(country)

    groups = [[] for _ in range(12)]

    for group in groups:

        team = random.choice(slot1)
        group.append(team)
        slot1.remove(team)

        team = random.choice(slot2)
        group.append(team)
        slot2.remove(team)

        team = random.choice(slot3)
        group.append(team)
        slot3.remove(team)

        team = random.choice(slot4)
        group.append(team)
        slot4.remove(team)

    return groups


def update_weight(team, result):

    if result == "win":
        team["consecutive_wins"] += 1

        if team["consecutive_wins"] == 2:
            team["weight"] += 0.5

    elif result == "draw":
        team["consecutive_wins"] = 0
        team["weight"] += 0.25

    else:
        team["consecutive_wins"] = 0


def play_match(team1, team2, weighted=True):

    if weighted:

        total = team1["weight"] + team2["weight"]

        team1_win = 0.6 * (team1["weight"] / total)
        team2_win = 0.6 * (team2["weight"] / total)

        draw = 0.4

        roll = random.random()

        if roll < draw:
            result = "draw"

        elif roll < draw + team1_win:
            result = "team1"

        else:
            result = "team2"

    else:

        result = random.choice(
            ["team1", "team2", "draw"]
        )

    if result == "team1":

        team1["wins"] += 1
        team2["losses"] += 1

        team1["points"] += 3

        update_weight(team1, "win")
        update_weight(team2, "loss")

        print(f"{team1['name']} beat {team2['name']}")

    elif result == "team2":

        team2["wins"] += 1
        team1["losses"] += 1

        team2["points"] += 3

        update_weight(team2, "win")
        update_weight(team1, "loss")

        print(f"{team2['name']} beat {team1['name']}")

    else:

        team1["draws"] += 1
        team2["draws"] += 1

        team1["points"] += 1
        team2["points"] += 1

        update_weight(team1, "draw")
        update_weight(team2, "draw")

        print(f"{team1['name']} drew with {team2['name']}")


def play_group_stage(group):

    fixtures = [
        (group[0], group[1]),
        (group[2], group[3]),

        (group[0], group[2]),
        (group[1], group[3]),

        (group[0], group[3]),
        (group[1], group[2]),
    ]

    print("\nMATCHES")
    print("-" * 40)

    for match_number, (team1, team2) in enumerate(fixtures):

        if match_number < 4:
            play_match(team1, team2, weighted=True)

        else:
            play_match(team1, team2, weighted=False)


def print_group_table(group):

    standings = sorted(
        group,
        key=lambda x: x["points"],
        reverse=True
    )

    print("\nTABLE")
    print("-" * 60)

    for team in standings:

        print(
            f"{team['name']:20}"
            f" Pts:{team['points']:2}"
            f" W:{team['wins']}"
            f" D:{team['draws']}"
            f" L:{team['losses']}"
            f" Weight:{team['weight']}"
        )

def get_qualified_teams(groups):

    qualified = []
    third_place = []

    for group in groups:

        standings = sorted(
            group,
            key=lambda x: x["points"],
            reverse=True
        )

        # Top 2 qualify automatically
        qualified.append(standings[0])
        qualified.append(standings[1])

        # Save 3rd place team
        third_place.append(standings[2])

    # Best 8 third-place teams
    third_place.sort(
        key=lambda x: x["points"],
        reverse=True
    )

    qualified.extend(third_place[:8])

    return qualified

def create_knockout_pots(groups):

    winners = []
    runners_up = []
    thirds = []

    for group in groups:

        standings = sorted(
            group,
            key=lambda x: x["points"],
            reverse=True
        )

        winners.append(standings[0])
        runners_up.append(standings[1])
        thirds.append(standings[2])

    thirds.sort(
        key=lambda x: x["points"],
        reverse=True
    )

    best_thirds = thirds[:8]

    return {
        "winners": winners,
        "runners_up": runners_up,
        "best_thirds": best_thirds
    }


def create_round_of_32(groups):

    qualified = get_qualified_teams(groups)

    random.shuffle(qualified)

    return [
        (qualified[i], qualified[i + 1])
        for i in range(0, len(qualified), 2)
    ]

def knockout_match(team1, team2):

    roll = random.random()

    if roll < 0.2:
        # draw -> tiebreak

        if team1["weight"] > team2["weight"]:

            winner = random.choices(
                [team1, team2],
                weights=[70, 30]
            )[0]

        elif team2["weight"] > team1["weight"]:

            winner = random.choices(
                [team1, team2],
                weights=[30, 70]
            )[0]

        else:

            winner = random.choice(
                [team1, team2]
            )

    else:

        total = (
            team1["weight"] +
            team2["weight"]
        )

        winner = random.choices(
            [team1, team2],
            weights=[
                team1["weight"],
                team2["weight"]
            ]
        )[0]

    print(
        f"{team1['name']} vs {team2['name']} "
        f"-> {winner['name']} advances"
    )

    return winner

def play_knockout_round(matches):

    winners = []

    for team1, team2 in matches:
        winners.append(
            knockout_match(team1, team2)
        )

    return winners


# -------------------------------------
# MAIN PROGRAM
# -------------------------------------
countries = [
    # Weight 4 (12 teams)
    {"name": "Argentina", "weight": 4},
    {"name": "Brazil", "weight": 4},
    {"name": "France", "weight": 4},
    {"name": "Spain", "weight": 4},
    {"name": "England", "weight": 4},
    {"name": "Germany", "weight": 4},
    {"name": "Portugal", "weight": 4},
    {"name": "Netherlands", "weight": 4},
    {"name": "Belgium", "weight": 4},
    {"name": "Croatia", "weight": 4},
    {"name": "Uruguay", "weight": 4},
    {"name": "Colombia", "weight": 4},

    # Weight 3 (12 teams)
    {"name": "Morocco", "weight": 3},
    {"name": "Switzerland", "weight": 3},
    {"name": "Japan", "weight": 3},
    {"name": "Mexico", "weight": 3},
    {"name": "United States", "weight": 3},
    {"name": "Senegal", "weight": 3},
    {"name": "South Korea", "weight": 3},
    {"name": "Norway", "weight": 3},
    {"name": "Sweden", "weight": 3},
    {"name": "Iran", "weight": 3},
    {"name": "Australia", "weight": 3},
    {"name": "Turkey", "weight": 3},

    # Weight 2 (12 teams)
    {"name": "Egypt", "weight": 2},
    {"name": "Ivory Coast", "weight": 2},
    {"name": "Canada", "weight": 2},
    {"name": "Qatar", "weight": 2},
    {"name": "Bosnia and Herzegovina", "weight": 2},
    {"name": "Czechia", "weight": 2},
    {"name": "South Africa", "weight": 2},
    {"name": "Paraguay", "weight": 2},
    {"name": "Scotland", "weight": 2},
    {"name": "Tunisia", "weight": 2},
    {"name": "Ecuador", "weight": 2},
    {"name": "Algeria", "weight": 2},

    # Weight 1 (12 teams)
    {"name": "Curacao", "weight": 1},
    {"name": "New Zealand", "weight": 1},
    {"name": "Saudi Arabia", "weight": 1},
    {"name": "Cape Verde", "weight": 1},
    {"name": "Iraq", "weight": 1},
    {"name": "Austria", "weight": 1},
    {"name": "Jordan", "weight": 1},
    {"name": "DR Congo", "weight": 1},
    {"name": "Uzbekistan", "weight": 1},
    {"name": "Ghana", "weight": 1},
    {"name": "Panama", "weight": 1},
    {"name": "Haiti", "weight": 1}
]



# Add stats to all teams
initialize_teams(countries)

# Create 12 groups
groups = create_groups(countries)

# Play group stage
for i, group in enumerate(groups):

    print(f"\n{'=' * 60}")
    print(f"GROUP {chr(65 + i)}")
    print(f"{'=' * 60}")

    print("\nTeams:")

    for team in group:
        print(team["name"])

    print("\nPlaying matches...")
    play_group_stage(group)

    print_group_table(group)

# ==================================
# KNOCKOUT STAGE
# ==================================

print("\n")
print("=" * 60)
print("ROUND OF 32")
print("=" * 60)

round32_matches = create_round_of_32(groups)

round32_winners = play_knockout_round(round32_matches)

print("\n")
print("=" * 60)
print("ROUND OF 16")
print("=" * 60)

round16_matches = [
    (round32_winners[i], round32_winners[i + 1])
    for i in range(0, len(round32_winners), 2)
]

round16_winners = play_knockout_round(round16_matches)

print("\n")
print("=" * 60)
print("QUARTER FINALS")
print("=" * 60)

quarter_matches = [
    (round16_winners[i], round16_winners[i + 1])
    for i in range(0, len(round16_winners), 2)
]

quarter_winners = play_knockout_round(quarter_matches)

print("\n")
print("=" * 60)
print("SEMI FINALS")
print("=" * 60)

semi_matches = [
    (quarter_winners[i], quarter_winners[i + 1])
    for i in range(0, len(quarter_winners), 2)
]

semi_winners = play_knockout_round(semi_matches)

print("\n")
print("=" * 60)
print("FINAL")
print("=" * 60)

champion = knockout_match(
    semi_winners[0],
    semi_winners[1]
)

print("\n")
print("=" * 60)
print(f"WORLD CHAMPION: {champion['name']}")
print("=" * 60)


                 


    

                  

      






