# ♟️ Chess RL Game (Python + HTML/CSS)

A full-stack chess game built using **Python (Flask)** and **HTML/CSS/JavaScript**, where a user can play chess against an **AI powered by Reinforcement Learning (Q-Learning)**.

---

## 🚀 Features

- 🎮 Playable Chess Game (User vs AI)
- 🤖 AI opponent using Reinforcement Learning
- 🌐 Frontend built with HTML, CSS, JavaScript
- ⚡ Backend powered by Flask
- 🔄 Reset Game functionality
- 🧠 Q-Table learning and saving (`q_table.pkl`)
- 🎨 Modern UI with interactive board

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Flask-CORS**
- **python-chess**
- **HTML5**
- **CSS3**
- **JavaScript (Fetch API)**

---

## 📁 Project Structure
chess-rl-project/
│
├── backend/
│ ├── app.py
│ ├── rl_agent.py
│ └── q_table.pkl
│
├── frontend/
│ └── index.html

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository


git clone https://github.com/pundlachandu1703/rl_chess_project

cd chess-rl-project


---

### 2️⃣ Install dependencies


pip install flask flask-cors python-chess


---

### 3️⃣ Run the backend server


cd backend
python app.py


You should see:


Running on http://127.0.0.1:5000/


---

### 4️⃣ Open the frontend

Go to:


frontend/index.html


👉 Open it in your browser

---

## 🎮 How to Play

1. Click on a chess piece  
2. Click destination square  
3. AI will automatically respond  
4. Use **Reset Button** to restart the game  

---

## 🧠 Reinforcement Learning (Q-Learning)

- The AI uses a **Q-table** to store learned moves
- Board states are stored using **FEN notation**
- Moves are updated using the Q-learning formula
- Data is saved in:


q_table.pkl


---

## 🔧 API Endpoints

| Endpoint | Method | Description |
|---------|--------|------------|
| `/` | GET | Server status |
| `/move` | POST | Send player move |
| `/reset` | GET | Reset the board |

---

## ⚠️ Important Notes

- Do NOT open `/move` in browser (POST only)
- Backend must be running before opening frontend
- CORS is enabled to allow frontend communication

---

## 🔥 Future Improvements

- Drag & Drop chess pieces
- Highlight legal moves
- Strong AI (Minimax / Alpha-Beta)
- Multiplayer support
- Deploy to cloud (Heroku / Render)

---

## 👨‍💻 Author

Developed by **Chandu**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
