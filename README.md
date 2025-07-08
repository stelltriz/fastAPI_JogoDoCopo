## 🥤 Cup Game API (FastAPI)
Backend API built with FastAPI to support the Cup Game logic.
Handles cup shuffling, answer retrieval, and user guesses.

### 🧰 Technologies Used
- FastAPI
- Python
- Uvicorn

### 🎯 Endpoints
- POST /embaralhar — Shuffles the cups randomly
- GET /resposta — Returns the index of the cup hiding the ball
- POST /chute — Accepts a guess (chute) and returns whether it’s correct, along with confetti trigger
