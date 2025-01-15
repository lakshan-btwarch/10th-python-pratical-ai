# Code to compute the net run rate for a tournament
team_name = input("Enter Team Name: ")
matches = int(input("Enter the number of matches played: "))

total_runs_scored = 0
total_overs_faced = 0
total_runs_conceded = 0
total_overs_bowled = 0

for i in range(matches):
    runs_scored = int(input(f"Enter runs scored in match {i + 1}: "))
    overs_faced = float(input(f"Enter overs faced in match {i + 1}: "))
    runs_conceded = int(input(f"Enter runs conceded in match {i + 1}: "))
    overs_bowled = float(input(f"Enter overs bowled in match {i + 1}: "))
    
    total_runs_scored += runs_scored
    total_overs_faced += overs_faced
    total_runs_conceded += runs_conceded
    total_overs_bowled += overs_bowled

net_run_rate = (total_runs_scored / total_overs_faced) - (total_runs_conceded / total_overs_bowled)
print(f"Net Run Rate for {team_name}: {net_run_rate:.2f}")
