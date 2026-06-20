"""
University: University of Isfahan
Faculty: Mathematics and Statistics
Department: Computer Science
Course: Artificial Intelligence
Professor: Dr. Faria Nasiri Mofakham
TAs: MehrAzin Marzough, Mohammad Karimi, Anahita Honarmandian
Project: Adversarial Search in Othello (Minimax and Alpha-Beta Pruning)
"""

from agents.random_agent import RandomAgent
from agents.greedy_agent import GreedyAgent
from agents.minimax_agent import MinimaxAgent
from agents.alphabeta_agent import AlphaBetaAgent
from tournament import play_game

def run_tournament(agent1, agent1_name, agent2, agent2_name, num_games=20):
    wins = 0
    draws = 0
    
    for i in range(num_games):
        if i % 2 == 0:
            score = play_game(agent1, agent2) # agent1 is Black
            if score[0] > score[1]: wins += 1
            elif score[0] == score[1]: draws += 1
        else:
            score = play_game(agent2, agent1) # agent1 is White
            if score[1] > score[0]: wins += 1
            elif score[1] == score[0]: draws += 1
            
    win_rate = (wins / num_games) * 100
    print(f"{agent1_name} vs {agent2_name} | Games: {num_games} | Wins: {wins} | Win Rate: {win_rate}%")

if __name__ == "__main__":
    print("Running Tournaments...\n")
    
    ab_agent = AlphaBetaAgent(depth=4)
    minimax_agent = MinimaxAgent(depth=4)
    greedy_agent = GreedyAgent()
    random_agent = RandomAgent()

    run_tournament(ab_agent, "Alpha-Beta(4)", random_agent, "Random", 20)
    run_tournament(ab_agent, "Alpha-Beta(4)", greedy_agent, "Greedy", 20)
    run_tournament(minimax_agent, "Minimax(4)", random_agent, "Random", 20)
    run_tournament(minimax_agent, "Minimax(4)", greedy_agent, "Greedy", 20)