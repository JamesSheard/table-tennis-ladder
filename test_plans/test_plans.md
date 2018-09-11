# Test Plans

###Scenarios:

Showing league table
- When requested with `--getladder` or `-gl`, the league table will show.
    - *Steps*
        - `python main.py --getladder`
        - OR
        - `python main.py -gl`
    - *Outcomes*
        - Ladder is displayed in terminal.

Showing help
- When requested with `--help` or `-h`, the help will show.
    - *Steps*
        - `python main.py --help`
        - OR 
        - `python main.py -h`
    - *Outcomes*
        - The help file is displayed in the terminal.

- When the main program is run with no parameters, the help will show.
    - *Steps*
        - `python main.py`
    - *Outcomes*
        - The help file is displayed in the terminal.

Interactive Mode:
- When requested with `--interactive` or `-i`, interactive mode will be enabled.
    - *Steps*
        - `python main.py --interactive`
        OR 
        - `python main.py -i`
    - *Outcomes*
        - Interactive mode is enabled. The user is prompted to either
            - `Show Table`
            - `Enter New Score`
        - Upon choosing `Enter New Score` 
            - Defer to `Playing a Game` test plan. 


Playing a game
- Player 1 and 2 both in league. Player 1 is above player 2 in league. Player 1 beats player 2.
    - *Steps*     
        - `python main.py --win Player_1 --lose Player_2`
        - OR
        - `python main.py -w Player_1 -l Player_2`
        
    - *Outcomes*
        - Player positions remain the same.
        - Ladder is written to state file.

- Player 1 and 2 both in league. Player 2 is above player 1 in league. Player 1 beats player 2.
    - *Steps*
        - `python main.py --win Player_1 --lose Player_2`
        - OR
        - `python main.py -w Player_1 -l Player_2`
    - *Outcomes*
        - Player 1 takes Player 2's place in the league table.
        - Player 2 moves down 1 place.
        - All players below Player 2 moves down 1 place.
        - Ladder is written to state file.

- Player 1 is not in league, player 2 is. Player 2 beats player 1. 
    - *steps*
        - `python main.py --win Player_2 --lose Player_1`
        - OR
        - `python main.py -w Player_2 -l Player_1`
    - *Outcomes*
        - Player 1 is appended to the end of the league.
        - Ladder is written to state file.

- Player 2 is not in league, player 1 is. Player 2 beats player 1.
    - *steps*
        - `python main.py --win Player_2 --lose Player_1`
        - OR
        - `python main.py -w Player_2 -l Player_1`
    - *Outcomes*
        - Player 2 is added into the league at Player 1's place.
        - Player 1 moves down 1 place.
        - All players below Player 1 move down 1 place.
        - Ladder is written to state file.
        
- Neither players are in league. Player 1 beats player 2.
    - *Steps*
        - `python main.py --win Player_1 --lose Player_2`
        - OR
        - `python main.py -w Player_1 -l Player_2`
    - *Outcomes*
        - Player 1 and Player 2 is added to the league
        - Player 1 is 1 higher than Player 2
        - Ladder is written to state file.

- Player 1 is in league. Player 2 is input with the same name as player 1.
    - *Steps*
        - `python main.py --win Player_1 --lose Player_1`
        - OR
        - `python main.py -w Player_1 -l Player_1`
    - *Outcomes*
        - Error - The user is warned that they have entered the same name twice.
        - The ladder's state remains the same.

- Either player is entered with invalid characters (punctuation, excluding `_`).
    - *Steps*
        - `python main.py --win Player&1--lose Player<>2`
        - OR
        - `python main.py -w Player&1 -l Player<>2`
    - *Outcomes*
        - Error - The user is warned that they have entered invalid characters.
        - The ladder's state remains the same.
        


