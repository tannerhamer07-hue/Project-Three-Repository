#Leaderboard.py
#Should be the code we need for the leaderboard
leaderboard = {}

def update_leaderboard(player_name, did_win):
    """Add a win to the player's record if they won"""
    if did_win:
        if player_name in leaderboard:
            leaderboard[player_name] += 1
        else:
            leaderboard[player_name] = 1


def show_leaderboard():
    """Print leaderboard sorted by wins"""
    print("\n=== LEADERBOARD ===")
    for name, wins in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {wins} wins")
    print("===================")