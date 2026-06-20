class AlphaBetaAgent:
    def __init__(self, depth=4):
        self.depth = depth

    def evaluate(self, game, player):
        # Using the same robust evaluation logic
        opp = -player
        size = game.size
        corners = [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]
        
        my_pieces, opp_pieces = 0, 0
        my_corners, opp_corners = 0, 0

        for r in range(size):
            for c in range(size):
                cell = game.board[r][c]
                if cell == player:
                    my_pieces += 1
                    if (r, c) in corners:
                        my_corners += 1
                elif cell == opp:
                    opp_pieces += 1
                    if (r, c) in corners:
                        opp_corners += 1

        my_moves = len(game.get_valid_moves(player))
        opp_moves = len(game.get_valid_moves(opp))

        corner_weight = 30
        mobility_weight = 5
        piece_weight = 1

        score = (my_corners - opp_corners) * corner_weight + \
                (my_moves - opp_moves) * mobility_weight + \
                (my_pieces - opp_pieces) * piece_weight

        return score

    def alphabeta(self, game, depth, alpha, beta, maximizing, root_player):
        if depth == 0 or game.game_over():
            return self.evaluate(game, root_player), None

        current_player = root_player if maximizing else -root_player
        moves = game.get_valid_moves(current_player)

        if not moves:
            eval_score, _ = self.alphabeta(game, depth - 1, alpha, beta, not maximizing, root_player)
            return eval_score, None

        best_move = None
        if maximizing:
            max_eval = float('-inf')
            for move in moves:
                g = game.copy()
                g.make_move(current_player, *move)
                eval_score, _ = self.alphabeta(g, depth - 1, alpha, beta, False, root_player)
                
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break # Beta cutoff
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in moves:
                g = game.copy()
                g.make_move(current_player, *move)
                eval_score, _ = self.alphabeta(g, depth - 1, alpha, beta, True, root_player)
                
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break # Alpha cutoff
            return min_eval, best_move

    def choose_move(self, game, player):
        _, move = self.alphabeta(
            game, self.depth, float('-inf'), float('inf'), True, player
        )
        return move