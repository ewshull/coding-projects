import random


def decide_winner(list_of_two_teams):
    print(list_of_two_teams[0], ' versus ', list_of_two_teams[1])

    winning_index = random.randint(0, 1)

    return list_of_two_teams[winning_index]


def assign_teams_from_file(file_name, bracket_quadrant_initials):
    try:
        teams_list = []

        file_to_read = open(file_name, 'r')

        for idx, line in enumerate(file_to_read):
            full_name = '(' + str(idx + 1) + bracket_quadrant_initials + ')' + line.strip()
            teams_list.append(full_name)

        return teams_list
    except IOError:
        print('Something went wrong: File Not Found.')


def build_initial_bracket(teams_list, bracket_quadrant):
    all_teams = []

    print('\nINITIAL BRACKET FOR THE ', bracket_quadrant)

    # team 1 vs team 16
    all_teams.append([teams_list[0], teams_list[15]])
    print(teams_list[0], ' versus ', teams_list[15])

    # team 8 vs team 9
    all_teams.append([teams_list[7], teams_list[8]])
    print(teams_list[7], ' versus ', teams_list[8])

    # team 5 vs team 12
    all_teams.append([teams_list[4], teams_list[11]])
    print(teams_list[4], ' versus ', teams_list[11])

    # team 4 vs team 13
    all_teams.append([teams_list[3], teams_list[12]])
    print(teams_list[3], ' versus ', teams_list[12])

    # team 6 vs team 11
    all_teams.append([teams_list[5], teams_list[10]])
    print(teams_list[5], ' versus ', teams_list[10])

    # team 3 vs team 14
    all_teams.append([teams_list[2], teams_list[13]])
    print(teams_list[2], ' versus ', teams_list[13])

    # team 7 vs team 10
    all_teams.append([teams_list[6], teams_list[9]])
    print(teams_list[6], ' versus ', teams_list[9])

    # team 2 vs team 15
    all_teams.append([teams_list[1], teams_list[14]])
    print(teams_list[1], ' versus ', teams_list[14])

    return all_teams


def build_subsequent_rounds(teams_list):
    next_round_teams = []

    winners_list = []
    for match_up in teams_list:
        winners_list.append(decide_winner(match_up))

    for match_up_index in range(0, len(winners_list), 2):
        next_round_teams.append([winners_list[match_up_index], winners_list[match_up_index + 1]])

    return next_round_teams


def fill_bracket(teams_list, bracket_quadrant):
    initial_list = build_initial_bracket(teams_list, bracket_quadrant)
    second_round = build_subsequent_rounds(initial_list)

    print('\nSECOND ROUND FOR THE ', bracket_quadrant)
    sweet_sixteen = build_subsequent_rounds(second_round)

    print('\nSWEET SIXTEEN FOR THE ', bracket_quadrant)
    elite_eight = build_subsequent_rounds(sweet_sixteen)

    print('\nELITE EIGHT FOR THE ', bracket_quadrant)
    final_four_team = decide_winner(elite_eight[0])

    return final_four_team


# ---- main
# ---------------- SOUTHERN BRACKET ----------------
south_list = assign_teams_from_file('southernBracket.txt', ' S')
south_final_four_team = fill_bracket(south_list, 'SOUTH')

# ---------------- MIDWESTERN BRACKET ----------------
midwest_list = assign_teams_from_file('midwesternBracket.txt', ' MW')
midwest_final_four_team = fill_bracket(midwest_list, 'MIDWEST')

# ---------------- EASTERN BRACKET ----------------
east_list = assign_teams_from_file('easternBracket.txt', ' E')
east_final_four_team = fill_bracket(east_list, 'EAST')

# ---------------- WESTERN BRACKET ----------------
west_list = assign_teams_from_file('westernBracket.txt', ' W')
west_final_four_team = fill_bracket(west_list, 'WEST')

# ---------------- FINAL FOUR ----------------
print('\nFINAL FOUR')
final_four = []

# south versus east
final_four.append([south_final_four_team, east_final_four_team])

# midwest versus west
final_four.append([midwest_final_four_team, west_final_four_team])

championship_teams = build_subsequent_rounds(final_four)

# ---------------- CHAMPIONSHIP ----------------
print('\nCHAMPIONSHIP')

champion = decide_winner(championship_teams[0])

print('\n**THE WINNER IS: ', champion, '**')
