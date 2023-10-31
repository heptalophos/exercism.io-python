def tally(rows):
    standings = {}
    table = [f"{'Team':<30} | {'MP':>2} | {'W':>2} | {'D':>2} | {'L':>2} | {'P':>2}"]
    for row in rows:
        home, away, outcome = row.split(";")
        for team in [home, away]:
            if team not in standings: 
                standings[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
            standings[team]["MP"] += 1
        if outcome == "win":
            standings[home]["W"] += 1
            standings[away]["L"] += 1
            standings[home]["P"] += 3
        if outcome == "draw":
            standings[home]["D"] += 1
            standings[away]["D"] += 1
            standings[home]["P"] += 1
            standings[away]["P"] += 1
        if outcome == "loss":
            standings[home]["L"] += 1
            standings[away]["W"] += 1
            standings[away]["P"] += 3
    for team in sorted(sorted(standings.keys()), key= lambda x: 0 - standings[x]["P"]):
        t = standings[team]
        team_rank = f"{team:31}| {t['MP']:2} | {t['W']:2} | {t['D']:2} | {t['L']:2} | {t['P']:2}"
        table.append(team_rank)
    return table 
