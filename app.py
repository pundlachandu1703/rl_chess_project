from flask import Flask, request, jsonify
from flask_cors import CORS
import chess

# Import RL functions
from rl_agent import choose_action, update_q_table, save_q_table

app = Flask(__name__)
CORS(app)  # ✅ VERY IMPORTANT (fixes frontend connection issue)

# Initialize board
board = chess.Board()


# -------------------------
# Convert board to array
# -------------------------
def board_to_array(board):
    rows = []
    for rank in range(8, 0, -1):
        row = ""
        for file in range(8):
            square = chess.square(file, rank - 1)
            piece = board.piece_at(square)
            row += piece.symbol() if piece else "."
        rows.append(row)
    return rows


# -------------------------
# Home Route
# -------------------------
@app.route("/")
def home():
    return "Chess RL Backend Running ✅"


# -------------------------
# Reset Game
# -------------------------
@app.route("/reset", methods=["GET"])
def reset():
    global board
    board = chess.Board()
    print("🔄 Game Reset")
    return jsonify({
        "board": board_to_array(board),
        "status": "reset"
    })


# -------------------------
# Move API
# -------------------------
@app.route("/move", methods=["POST", "GET"])
def move():
    global board

    # If opened directly in browser
    if request.method == "GET":
        return "⚠️ Use POST request from frontend"

    try:
        data = request.get_json()

        # Get move from frontend
        from_row = int(data["from"]["row"])
        from_col = int(data["from"]["col"])
        to_row = int(data["to"]["row"])
        to_col = int(data["to"]["col"])

        from_sq = chess.square(from_col, 7 - from_row)
        to_sq = chess.square(to_col, 7 - to_row)

        move = chess.Move(from_sq, to_sq)

        # Save previous state
        prev_state = board.fen()

        # -------------------------
        # Player Move
        # -------------------------
        if move in board.legal_moves:
            board.push(move)
            print("♙ Player Move:", move)

            # -------------------------
            # AI Move
            # -------------------------
            if not board.is_game_over():
                ai_move = choose_action(board)
                if ai_move:
                    board.push(ai_move)
                    print("🤖 AI Move:", ai_move)

            # -------------------------
            # RL Learning
            # -------------------------
            next_state = board.fen()

            reward = 0
            if board.is_checkmate():
                reward = 1
                print("🏆 Checkmate! AI learned something")

            update_q_table(prev_state, str(move), reward, next_state)
            save_q_table()

        else:
            print("❌ Invalid Move")

        return jsonify({
            "board": board_to_array(board),
            "status": "ok"
        })

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({
            "error": str(e),
            "status": "failed"
        })


# -------------------------
# Run Server
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)