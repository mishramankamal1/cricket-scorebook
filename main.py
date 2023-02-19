import random
import time
max_overs = range(0,50)
total_balls = 0
batsman_one_score = 0
batsman_two_score = 0
runs_given_by_bowler = 0

def change_strike(batsman_on_strike: str, other_batsman: str) -> None:
    print(f"{batsman_on_strike} is on strike. Changing strike to {other_batsman}.")
    return other_batsman, batsman_on_strike

def maintain_strike(batsman_on_strike: str, other_batsman: str) -> None:
    print(f"{batsman_on_strike} is on strike. Maintaining strike to {batsman_on_strike}.")
    return batsman_on_strike, other_batsman


def start_over(bowler, batsman_one,batsman_two, batsman_one_score, batsman_two_score, runs_given_by_bowler):
    balls = range(1,7)
    runs = range(0,7)
    for ball in balls:
        time.sleep(1)
        run = random.choice(runs)
        if run == 5:
            run = random.choice(runs)
        if run in [1,3,5]:
            print(f"Ball: {ball}, runs scored by {batsman_one} :{run}")
            on_strike, off_strike = change_strike(batsman_one,batsman_two)
        else:
            on_strike, off_strike=maintain_strike(batsman_one,batsman_two)
            print(f"Ball: {ball}, runs scored by {batsman_one} :{run}")
        
    return batsman_one_score, batsman_two_score

batsman_one = "V.Kohli"
batsman_two = "H.Pandiya"
bowler = "H.Rauf"
on_strike = None
off_strike = None


for over in max_overs:
    if not on_strike:
        on_strike=batsman_one
    if not off_strike:
        off_strike = batsman_two
    time.sleep(2)
    total_balls = total_balls + 6
    print(f"------------------- Overs:{over} -------------------")
    runs_scored_by_batsman=start_over(bowler,on_strike,off_strike, batsman_one_score,batsman_two_score,runs_given_by_bowler)
    print(runs_scored_by_batsman)
