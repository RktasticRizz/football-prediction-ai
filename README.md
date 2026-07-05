# ⚽ Football Prediction AI

Predict international football matches using **Elo Ratings**, **Machine Learning**, **Poisson Goal Simulation**, and **Monte Carlo Tournament Simulation**.

---

## 🚀 Live Demo

Coming Soon

---

## 📸 Screenshots

### 🏠 Home Dashboard

(Add Screenshot)

---

### ⚽ Match Predictor

(Add Screenshot)

---

### 📊 Team Analysis

(Add Screenshot)

---

### ⚔️ Head-to-Head

(Add Screenshot)

---

### 🏆 Elo Rankings

(Add Screenshot)

---

### 🌍 Tournament Simulator

(Add Screenshot)

---

## ✨ Features

- ⚡ Elo Rating System
- 🤖 Machine Learning Goal Prediction
- ⚽ Poisson Goal Simulation
- 📊 Team Performance Analytics
- ⚔️ Head-to-Head Comparison
- 🏆 Live Elo Rankings
- 🌍 Tournament Simulator
- 🎲 Monte Carlo Tournament Simulation
- 📈 Model Performance Dashboard

---

## 📂 Dataset

Historical international football matches

- 📅 1872 – Present
- ⚽ 49,000+ Matches
- 🌍 200+ National Teams

---

## 🧠 Methodology

### 1. Elo Rating

Each international match updates the rating of both teams.

Higher-rated teams have a greater probability of winning future matches.

---

### 2. Goal Prediction

A machine learning model predicts:

- Home Goals
- Away Goals

using features such as

- Home Elo
- Away Elo
- Elo Difference
- Neutral Venue

---

### 3. Probability Simulation

Expected goals are converted into match probabilities using the Poisson Distribution.

Outputs include

- Home Win %
- Draw %
- Away Win %
- Most Likely Scorelines

---

### 4. Tournament Simulation

Knockout tournaments are simulated using the prediction engine.

The project also supports Monte Carlo simulation to estimate championship probabilities.

---

## 📊 Project Structure

```text
football-prediction/

├── app/
│   ├── Home.py
│   └── pages/
│
├── src/
│   ├── models/
│   ├── services/
│   ├── simulation/
│   └── features/
│
├── data/
├── outputs/
├── tests/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/football-prediction.git
```

Enter the directory

```bash
cd football-prediction
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
streamlit run app/Home.py
```

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Joblib
- SciPy

---

## 📈 Future Improvements

- Player-level statistics
- FIFA Rankings integration
- XG (Expected Goals)
- Injury analysis
- Live Match Prediction API
- World Cup Group Stage Simulation

---

## 👨‍💻 Author

**Rudraksh Prajapati**

Ahmedabad University

---

## 📄 License

MIT License