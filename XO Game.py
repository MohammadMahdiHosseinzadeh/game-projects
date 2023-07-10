# Getting players names
name_player_1 = input('Enter player 1\'s name: ')
name_player_2 = input('Enter player 2\'s name: ')

# Available moves
arr_remaining_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Chosen moves of player 1
arr_player_1 = []
# Chosen moves of player 2
arr_player_2 = []

# Checks if player 1 has chosen his/her move if error occurs so it won't ask for move two times from player 1
is_player_1_chosen = False

# Checks if the game is finished (one of players have won) so it won't show a draw message at the end if one player has won
is_game_finished = False

# This loop will continues until all choices from 1-9 are taken by players and either one player will be the winner or the game will be a draw
while len(arr_remaining_moves) != 0:

    # Checks if this is the last time loop being called (last move)
    if len(arr_remaining_moves) == 1:

        # Takes player 1 move input and shows both users previous movements and all available movements
        move_player_1 = input('\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' +
            str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves) + '\n(' + name_player_1 + ') Choose your move: ')
        
        # Validates player input (if the input is a number or not)
        if move_player_1.isnumeric():
            # Validates player input (if the input is between 1 and 9)
            if int(move_player_1) > 0 and int(move_player_1) < 10:
                # Validates player input (if the input was not chosen before)
                if int(move_player_1) in arr_remaining_moves:
                    # Sets player chosen move into an array so all moves can be tracked
                    arr_player_1.append(int(move_player_1))
                    # Removes this chosen move from all remaining moves so no one can choose it again
                    arr_remaining_moves.remove(int(move_player_1))

                    # Checks if user has won or not (checks numbers in rows, columns and crosses)
                    if (1 in arr_player_1 and 2 in arr_player_1 and 3 in arr_player_1) or (4 in arr_player_1 and 5 in arr_player_1 and 6 in arr_player_1) or (7 in arr_player_1 and 8 in arr_player_1 and 9 in arr_player_1) or (1 in arr_player_1 and 4 in arr_player_1 and 7 in arr_player_1) or (2 in arr_player_1 and 5 in arr_player_1 and 8 in arr_player_1) or (3 in arr_player_1 and 6 in arr_player_1 and 9 in arr_player_1) or (1 in arr_player_1 and 5 in arr_player_1 and 9 in arr_player_1) or (3 in arr_player_1 and 5 in arr_player_1 and 7) in arr_player_1:

                        # Prints each players moves during the match
                        print(name_player_1 + ' Won!\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' +
                            name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves))
                        # Sets this value so the draw message won't show
                        is_game_finished = True
                        # finishes the while loop
                        break

                else:
                    # Prints the error and restarts the while loop
                    print('ERROR1: This move is already taken.')
                    continue
            else:
                # Prints the error and restarts the while loop
                print('ERROR2: Move is not in in range(1-9).')
                continue
        else:
            # Prints the error and restarts the while loop
            print('ERROR3: Input must be numeric.')
            continue
    else:
        if not is_player_1_chosen:
            # Takes player 1 move input and shows both users previous movements and all available movements
            move_player_1 = input('\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' +
                str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves) + '\n(' + name_player_1 + ') Choose your move: ')
            # Validates player input (if the input is a number or not)
            if move_player_1.isnumeric():
                # Validates player input (if the input is between 1 and 9)
                if int(move_player_1) > 0 and int(move_player_1) < 10:
                    # Validates player input (if the input was not chosen before)
                    if int(move_player_1) in arr_remaining_moves:
                        # Sets player chosen move into an array so all moves can be tracked
                        arr_player_1.append(int(move_player_1))
                        # Removes this chosen move frm all remaining moves so no one can choose it again
                        arr_remaining_moves.remove(int(move_player_1))
                        # Sets this value so if any errors occurred during player 2's move choosing this will prevent asking again from player 1
                        is_player_1_chosen = True

                        # Checks if user has won or not (checks numbers in rows, columns and crosses)
                        if (1 in arr_player_1 and 2 in arr_player_1 and 3 in arr_player_1) or (4 in arr_player_1 and 5 in arr_player_1 and 6 in arr_player_1) or (7 in arr_player_1 and 8 in arr_player_1 and 9 in arr_player_1) or (1 in arr_player_1 and 4 in arr_player_1 and 7 in arr_player_1) or (2 in arr_player_1 and 5 in arr_player_1 and 8 in arr_player_1) or (3 in arr_player_1 and 6 in arr_player_1 and 9 in arr_player_1) or (1 in arr_player_1 and 5 in arr_player_1 and 9 in arr_player_1) or (3 in arr_player_1 and 5 in arr_player_1 and 7) in arr_player_1:

                            # Prints each players moves during the match
                            print(name_player_1 + ' Won!\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' +
                                name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves))
                            # Sets this value so the draw message won't show
                            is_game_finished = True
                            # finishes the while loop
                            break

                    else:
                        # Prints the error and restarts the while loop
                        print('ERROR4: This move is already taken.')
                        continue
                else:
                    # Prints the error and restarts the while loop
                    print('ERROR5: Move is not in in range(1-9).')
                    continue
            else:
                # Prints the error and restarts the while loop
                print('ERROR6: Input must be numeric.')
                continue

        # Takes player 2 move input and shows both users previous movements and all available movements
        move_player_2 = input('\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 + '\'s moves: ' + str(
            arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves) + '\n(' + name_player_2 + ') Choose your move: ')
        # Validates player input (if the input is a number or not)
        if move_player_2.isnumeric():
            # Validates player input (if the input is between 1 and 9)
            if int(move_player_2) > 0 and int(move_player_2) < 10:
                # Validates player input (if the input was not chosen before)
                if int(move_player_2) in arr_remaining_moves:
                    # Sets player chosen move into an array so all moves can be tracked
                    arr_player_2.append(int(move_player_2))
                    # Removes this chosen move frm all remaining moves so no one can choose it again
                    arr_remaining_moves.remove(int(move_player_2))
                    # removes the true value so next time player 1 will be asked provide a movement
                    is_player_1_chosen = False

                    # Checks if user has won or not (checks numbers in rows, columns and crosses)
                    if (1 in arr_player_2 and 2 in arr_player_2 and 3 in arr_player_2) or (4 in arr_player_2 and 5 in arr_player_2 and 6 in arr_player_2) or (7 in arr_player_2 and 8 in arr_player_2 and 9 in arr_player_2) or (1 in arr_player_2 and 4 in arr_player_2 and 7 in arr_player_2) or (2 in arr_player_2 and 5 in arr_player_2 and 8 in arr_player_2) or (3 in arr_player_2 and 6 in arr_player_2 and 9 in arr_player_2) or (1 in arr_player_2 and 5 in arr_player_2 and 9 in arr_player_2) or (3 in arr_player_2 and 5 in arr_player_2 and 7) in arr_player_1:
                        # Prints each players moves during the match
                        print(name_player_2 + ' Won!\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' +
                            name_player_2 + '\'s moves: ' + str(arr_player_2) + '\nremaining moves: ' + str(arr_remaining_moves))
                        # Sets this value so the draw message won't show
                        is_game_finished = True
                        # finishes the while loop
                        break

                else:
                    # Prints the error and restarts the while loop
                    print('ERROR7: This move is already taken.')
                    continue
            else:
                # Prints the error and restarts the while loop
                print('ERROR8: Move is not in in range(1-9).')
                continue
        else:
            # Prints the error and restarts the while loop
            print('ERROR9: Input must be numeric.')
            continue

# checks if any player has won the game or not if not shows the draw message and each players moves during the match
if not is_game_finished:
    print('Draw!\n' + name_player_1 + '\'s moves: ' + str(arr_player_1) + '\n' + name_player_2 +
        '\'s moves: ' + str(arr_player_2) + '\remaining moves: ' + str(arr_remaining_moves))