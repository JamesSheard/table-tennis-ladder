# Table Tennis Ladder

### Created by
Mike Silverstone

James Sheard

## Why did we make this?

Used to track your table tennis rankings within Infinity Works. Also, it's one of the grad projects!

## How to install

Download Python 2.7

pip2 install PrettyTable

## How to use

Python command:
python main.py

Example use:
python main.py --i

|Arguements|Longer Arg|What it does|
|-|-|-|
|-i|--interactive| Runs the user interface|
|-w <name> -l <name>|--win <name> --lose <name>|Sets who won and lost the game. Both variables needed|
|-gl|--getladder|Get's the current state of the ladder|
|-h|--help|Help file in CLI|
  
## Testing
We have some unit tests written. This will test if logic works.

### How to run
|Command|Description|
|-|-|
|python test_ladder.py|Runs the test for the ladder file|
