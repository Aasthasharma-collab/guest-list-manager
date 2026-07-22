def proccessing_leaderboard(scores):
    
    sorted_score = sorted(scores, reverse=True)
    print(f"sorted score(decending): {sorted_score}")
    
    top_3_scores = sorted_score[:3]
    print(f"top 3 scores: {top_3_scores}")

    milestone=[score for score in scores if score >=100]
    print(f"milestone(100+): {milestone}")

def score_statics(score_list):
    if not score_list:
        return

    highest_score = max(score_list)
    average_score = sum(score_list) / len(score_list)
    lowest_score = min(score_list)

    print(f"highest score are: {highest_score}")
    print(f"average score are: {average_score}")
    print(f"lowest score are: {lowest_score}")
print()
team_a_score=[200, 219, 300, 298, 167, 315, 198]
team_b_score=(199, 225, 154, 369, 149, 259, 121)
print("-----proccessing team a score----".title())
proccessing_leaderboard(team_a_score)
score_statics(team_a_score)

print()
print("-----processing team b score-----".title())
proccessing_leaderboard(team_b_score)
score_statics(team_b_score)

print()