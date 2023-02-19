class CricketMatch:
    def __init__(self):
        self.runs = 0
        self.wickets = 0
        self.overs = 0
        self.is_inning_over = False
        self.batsman_runs = {}
        self.bowler_wickets = {}
    
    def score_runs(self, runs, batsman):
        self.runs += runs
        if batsman in self.batsman_runs:
            self.batsman_runs[batsman] += runs
        else:
            self.batsman_runs[batsman] = runs
    
    def take_wicket(self, bowler):
        self.wickets += 1
        if bowler in self.bowler_wickets:
            self.bowler_wickets[bowler] += 1
        else:
            self.bowler_wickets[bowler] = 1
    
    def play_over(self):
        self.overs += 1
        if self.overs == 20 or self.wickets == 10:
            self.is_inning_over = True
    
    def display_score(self):
        print("Score: {}/{} in {} overs".format(self.runs, self.wickets, self.overs))
        print("Batsman Runs: ", self.batsman_runs)
        print("Bowler Wickets: ", self.bowler_wickets)

# Create an instance of the CricketMatch class
match = CricketMatch()

# Play the match
batsman = "Batsman1"
bowler = "Bowler1"
while not match.is_inning_over:
    match.score_runs(5, batsman)
    match.take_wicket(bowler)
    match.play_over()
    match.display_score()

print("Inning Over!")
