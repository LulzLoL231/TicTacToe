# -*- coding: utf-8 -*-
#
#  "Tic Tac Toe" Game
#
#  Created by LulzLoL231 on 2/24/20.
#
from random import choice
from os import system
from platform import system as OperationSystem
from time import sleep

class Vars(object):
    '''Variables class for Tic Tac Toe game\n'''
    game_rules = '-= RULES  =-\n1. The game is played on a grid that\'s 3 squares by 3 squares.\n2. You choice your sign (X or O), and put them in empty squares.\n3. The first player to get 3 of her signs in a row (up, down, across, or diagonally) is the winner.\n4. When all 9 squares are full, the game is over. If no player has 3 signs in a row, the game ends in a tie.'
    game_help = 'Use numbers (from 1 to 9) to put your signs.\nUse "exit" for stop game & take draw.\n"rules" for Rules & "help" for Help.\nGood luck & Have fun! ^^'
    game_welcome = 'Welcome to "Tic Tac Toe" game!'
    game_pc_move = 'Now PC move!'
    game_player_move = 'Now is YOUR move!'
    game_grid_print_template = '''
       |   |
     {} | {} | {}
       |   |
    -----------
       |   |
     {} | {} | {}
       |   |
    -----------
       |   |
     {} | {} | {}
       |   |\n'''
    game_grid_template = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    game_grid_template_wo_digit = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    game_player_sign_is = 'Your sign is "{}"'


class Utils(object):
    '''Utilites class for Tic Tac Toe game.\n'''
    def GetRandomSign():
        '''Return random sign for game.'''
        return choice(['X', 'O'])
    
    def ClearConsole():
        '''Clear console stdin using "clear" for Unix-like system, and "cls" for Windows system. Or pass if can\'t recognize os.'''
        if (OperationSystem() == 'Darwin') or (OperationSystem() == 'Linux'):
            system('clear')
        elif OperationSystem() == 'Windows':
            system('cls')
        else:
            pass


class GameSession(object):
    '''Game Session class for Tic Tac Toe game.\n'''
    def __init__(self):
        '''Class init function'''
        self.play = False
        self.pc_score = 0
        self.player_score = 0
        self.draws = 0
        self.pc_sign = None
        self.player_sign = None
        self.grid = Vars.game_grid_template.copy()
        self.last_move = None
        self.digit_grid = True
    
    def DisableNumbersInGrid(self):
        '''Remove numbers from grid template.'''
        for i in self.grid:
            if self.grid[i] == Vars.game_grid_template[i]:
                self.grid[i] = ' '
            else:
                continue
        self.digit_grid = False
        return True
    
    def EnableNumbersInGrid(self):
        '''Restore numbers in grid template.'''
        for i in self.grid:
            if self.grid[i] == ' ':
                self.grid[i] = Vars.game_grid_template[i]
            else:
                continue
        self.digit_grid = True
        return True
    
    def GetAvailableGridPlaces(self):
        '''Return Available places in grid as a list.'''
        list = []
        for i in self.grid:
            place = self.grid[i]
            if place in ['X', 'O']:
                continue
            else:
                list.append(i)
        return list

    def PcRandomMove(self):
        '''Return grid_place for PC move.'''
        if self.pc_sign:
            if self.InPlay():
                return choice(self.GetAvailableGridPlaces())
            raise Exception('Game is not in "play" state!')
        raise Exception('"pc_sign" is not installed!')

    def InstallSigns(self, player_sign, pc_sign):
        '''Set players signs.'''
        self.player_sign = player_sign
        self.pc_sign = pc_sign
        return True
    
    def InstallWhoNextMove(self):
        '''Randomly choice who make next move.'''
        self.last_move = choice(['pc', 'player'])
        return True
    
    def InPlay(self):
        '''Return "play" state'''
        return self.play
    
    def IsPlayerMove(self):
        '''Return True if now is Player move.'''
        if self.last_move == 'player':
            return False
        else:
            return True
    
    def GetGrid(self):
        '''Return grid in template, ready for pretty print.'''
        return Vars.game_grid_print_template.format(self.grid[1], self.grid[2], self.grid[3], self.grid[4], self.grid[5], self.grid[6], self.grid[7], self.grid[8], self.grid[9])
    
    def GetScore(self):
        '''Return current game score as string.'''
        return f'{str(self.player_score)}:{str(self.pc_score)}:{str(self.draws)}'
    
    def MakeMove(self, grid_place, sign):
        '''Make move in game.'''
        if str(grid_place).isdigit():
            if int(grid_place) in range(1, 10):
                if sign.upper() in ['X', 'O']:
                    if self.InPlay():
                        self.grid[int(grid_place)] = sign
                        return True
                    raise Exception('Game is not in "play" state!')
                raise Exception('"sign" is not in signs list!')
            raise Exception('"grid_place" is not in range!')
        raise Exception('"grid_place" must be digit!')
    
    def ResetGrid(self):
        '''Reset grid to default state.'''
        if self.digit_grid:
            self.grid = Vars.game_grid_template.copy()
        else:
            self.grid = Vars.game_grid_template_wo_digit.copy()
        return True
    
    def GridIsFull(self):
        '''Return True if grid has not have free space.'''
        if self.GetAvailableGridPlaces() == []:
            return True
        return False
    
    def WhoWin(self):
        '''Return Players name if one of them won, "draw" if nobody win, but grid don\'t have free space, and None if grid is have free space.'''
        for sign in ['X', 'O']:
            stat = ((self.grid[1] == sign and self.grid[2] == sign and self.grid[3] == sign) or (self.grid[4] == sign and self.grid[5] == sign and self.grid[6] == sign) or (self.grid[7] == sign and self.grid[8] == sign and self.grid[9] == sign) or (self.grid[1] == sign and self.grid[4] == sign and self.grid[7] == sign) or (self.grid[2] == sign and self.grid[5] == sign and self.grid[8] == sign) or (self.grid[3] == sign and self.grid[6] == sign and self.grid[9] == sign) or (self.grid[1] == sign and self.grid[5] == sign and self.grid[9] == sign) or (self.grid[3] == sign and self.grid[5] == sign and self.grid[7] == sign))
            if stat is True:
                if self.pc_sign == sign:
                    return 'pc'
                elif self.player_sign == sign:
                    return 'player'
                else:
                    raise Exception('PC or Player sign is not installed!')
            else:
                continue
        if self.GridIsFull():
            return 'draw'
        return None
    
    def WhoWinByScore(self):
        '''Return Players name if one of them won, "draw" if nobody win, and None if PC and Player have 0 score, and 0 draws.'''
        if (((self.pc_score == 0) and (self.player_score == 0)) and (self.draws == 0)):
            return None
        else:
            if self.pc_score > self.player_score:
                return 'pc'
            elif self.pc_score < self.player_score:
                return 'player'
            else:
                return 'draw'
    
    def ResetMoves(self):
        '''Set last_move to None.'''
        self.last_move = None
        return True

def Game():
    '''Main function in Tic Tac Toe game.\n'''
    try:
        print()
        print(Vars.game_welcome)
        print()
        session = GameSession()
        player_sign = str(input('[?] Enter what a sign you want (X or O): '))

        if player_sign.upper() in ['X', 'O']:
            if player_sign.upper() == 'X':
                pc_sign = 'O'
            else:
                pc_sign = 'X'
        else:
            print('[!] Wrong choice! Using random for choice...')
            player_sign = Utils.GetRandomSign()
            if player_sign.upper() == 'X':
                pc_sign = 'O'
            else:
                pc_sign = 'X'

        session.InstallSigns(player_sign, pc_sign)
        session.InstallWhoNextMove()
        session.play = True
        print(f'Player sign is "{player_sign}"')
        sleep(2)
        
        while session.play:
            Utils.ClearConsole()
            print('\n-= SCORE =-')
            print('   ' + session.GetScore())
            print(session.GetGrid())
            win = session.WhoWin()
            if win:
                if win == 'player':
                    print('\nPlayer win!')
                    session.player_score += 1
                elif win == 'pc':
                    print('\n PC win!')
                    session.pc_score += 1
                else:
                    print('\nIt\'s a draw!')
                    session.draws += 1
                session.ResetGrid()
                session.ResetMoves()
                session.InstallWhoNextMove()
                sleep(2)
                continue
            else:
                if session.IsPlayerMove():
                    print(Vars.game_player_move)
                    print()
                    print(Vars.game_help)
                    print()
                    cmd = str(input('>>> '))
                    if cmd.isdigit():
                        if int(cmd) in range(1, 10):
                            if int(cmd) in session.GetAvailableGridPlaces():
                                session.MakeMove(cmd, session.player_sign)
                                session.last_move = 'player'
                                continue
                            else:
                                print('\nThis place is engaged! Please choice other.')
                                sleep(2)
                                continue
                        else:
                            print('\n[!] Please use numbers in grid for making move!')
                            sleep(2)
                            continue
                    else:
                        if cmd == 'help':
                            print(Vars.game_help)
                            print()
                            input('Press ENTER button for continue.')
                            continue
                        elif cmd == '':
                            print(Vars.game_help)
                            print()
                            sleep(2)
                            continue
                        elif cmd == 'digit':
                            if session.digit_grid is True:
                                print('Disabling numbers in grid...')
                                session.DisableNumbersInGrid()
                            else:
                                print('Enabling numbers in grid...')
                                session.EnableNumbersInGrid()
                            sleep(2)
                            continue
                        elif cmd == 'rules':
                            print(Vars.game_rules)
                            print()
                            input('Press ENTER button for continue.')
                            continue
                        elif cmd == 'exit':
                            q = str(input('[?] You are sure (Yes/No): ')).lower()
                            if q.startswith('y'):
                                print('Okay!')
                                sleep(1)
                                session.play = False
                                break
                            else:
                                print('Continue!')
                                sleep(1)
                                continue
                        elif cmd == 'cmd':
                            print('\n-= CMDs =-\n"help" – Print help.\n"rules" – Print rules.\n"exit" – For exit from game and take draw.\n"digit" – For disable print numbers in grid.\n"debug" – Print debug info.\n"cmd" – Print this message.\n')
                            input('Press ENTER button for continue.')
                            continue
                        elif cmd == 'debug':
                            print('\n-= DEBUG =-')
                            print(f'\nplay: {str(session.play)}\nplayer_sign: {session.player_sign}\npc_sign: {session.pc_sign}\nlast_move: {str(session.last_move)}\nscore: {session.GetScore()}\ngrid: {str(session.grid)}\ndigit_grid: {str(session.digit_grid)}\n')
                            input('Press ENTER button for continue.')
                            continue
                        else:
                            print('\n[!] Unrecognized command!')
                            sleep(2)
                            continue
                else:
                    print(Vars.game_pc_move)
                    session.MakeMove(session.PcRandomMove(), session.pc_sign)
                    session.last_move = 'pc'
                    sleep(2)
                    continue

        Utils.ClearConsole()
        print('-= SCORE =-')
        print('   ' + session.GetScore())
        win = session.WhoWinByScore()

        if win:
            if win == 'player':
                print(f'\nYou did it! You won PC with scope: {str(session.player_score)}:{str(session.pc_score)}. Draws: {str(session.draws)}')
            elif win == 'pc':
                print(f'\nSo sad! You lose to PC with scope: {str(session.pc_score)}:{str(session.player_score)}. Draws: {str(session.draws)}')
            else:
                print(f'It\'s a draw... Score: {session.GetScore()}')
        else:
            print('You don\'t play!')
        
        print('It was be a nice game, bye & have a nice day! ^^')
        if __name__ == '__main__':
            exit()

    except KeyboardInterrupt:
        print('\n[!] Emergency exit!')
        sleep(1)
        if __name__ == '__main__':
            exit()
    except Exception as e:
        print('Houston we have a problem!')
        raise e

if __name__ == '__main__':
    Game()
