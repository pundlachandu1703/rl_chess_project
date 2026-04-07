import random
import pickle
import os

Q_FILE = "q_table.pkl"

# Learning parameters
alpha = 0.1   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.2 # exploration

# Load Q-table
if os.path.exists(Q_FILE):
    with open(Q_FILE, "rb") as f:
        Q = pickle.load(f)
else:
    Q = {}


# -------------------------
# Get board state
# -------------------------
def get_state(board):
    return board.fen()


# -------------------------
# Choose action (AI move)
# -------------------------
def choose_action(board):
    state = get_state(board)

    if state not in Q:
        Q[state] = {}

    legal_moves = list(board.legal_moves)

    # Exploration
    if random.random() < epsilon:
        return random.choice(legal_moves)

    # Exploitation (best move)
    best_move = None
    best_value = -9999

    for move in legal_moves:
        move_str = str(move)
        value = Q[state].get(move_str, 0)

        if value > best_value:
            best_value = value
            best_move = move

    return best_move if best_move else random.choice(legal_moves)


# -------------------------
# Update Q-table (learning)
# -------------------------
def update_q_table(prev_state, move, reward, next_state):
    if prev_state not in Q:
        Q[prev_state] = {}

    if move not in Q[prev_state]:
        Q[prev_state][move] = 0

    # Get max future reward
    future_rewards = Q.get(next_state, {})
    max_future = max(future_rewards.values()) if future_rewards else 0

    # Q-learning formula
    Q[prev_state][move] += alpha * (
        reward + gamma * max_future - Q[prev_state][move]
    )


# -------------------------
# Save Q-table
# -------------------------
def save_q_table():
    with open(Q_FILE, "wb") as f:
        pickle.dump(Q, f)