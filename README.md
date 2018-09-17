# Table Tennis Ladder

### Created by
Mike Silverstone

James Sheard

## Why did we make this?

Used to track your table tennis rankings within Infinity Works. Also, it's one of the grad projects!

## How to install

Download Python 2.7

make build

## How to use

Python command:
python main.py

Example use:
python main.py -w Dan -l Ben -lb sky_bet

|Arguements|Longer Arg|What it does|
|-|-|-|
|-w <name> -l <name>|--win <name> --lose <name>|Sets who won and lost the game. Both variables needed|
|-gl|--getladder|Get's the current state of the ladder|
|-h|--help|Help file in CLI|
|-lb|--leaderboard|Selects which leaderboard to save to|
  
## Testing
We have some unit tests written. This will test if logic works.

### How to run
|Command|Description|
|-|-|
|make build|
|make test|
