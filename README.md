# ⚽ Football Prediction AI

Predict international football matches using **Elo Ratings**, **Machine Learning**, **Poisson Goal Simulation**, and **Monte Carlo Tournament Simulation**.

---

## 🚀 Live Demo

Coming Soon

---

## 📸 Screenshots

### 🏠 Home Dashboard

<img width="1470" height="956" alt="Screenshot 2026-07-05 at 1 03 40 PM" src="https://github.com/user-attachments/assets/4fa622eb-90ef-4ab5-83b4-775e787531f2" />

---

### ⚽ Match Predictor

<img width="1470" height="956" alt="Screenshot 2026-07-05 at 1 04 35 PM" src="https://github.com/user-attachments/assets/dfae2d00-ef29-498a-9495-6172d9ce1839" />


---

### 📊 Team Analysis

<img width="1470" height="956" alt="Screenshot 2026-07-05 at 1 04 40 PM" src="https://github.com/user-attachments/assets/89ce3f92-5bf5-4386-b520-812710b3d6ea" />



---

### ⚔️ Head-to-Head

<img width="1470" height="956" alt="Screenshot 2026-07-05 at 1 04 50 PM" src="https://github.com/user-attachments/assets/ab3a3f57-a474-4ea1-a181-d7bd180f05a4" />

---

### 🏆 Elo Rankings

<img width="1470" height="956" alt="Screenshot 2026-07-05 at 1 05 03 PM" src="https://github.com/user-attachments/assets/b6c2fd80-2d3d-4d88-a62c-9e1cfd381a53" />


---

### 🌍 Tournament Simulator

<img width="1470" height="956" alt="Screenshot 2026-07-05 at 1 08 45 PM" src="https://github.com/user-attachments/assets/ac3d7369-c1b1-40b8-83c5-e8641c3a178a" />

<img width="1470" height="956" alt="Screenshot 2026-07-05 at 1 09 11 PM" src="https://github.com/user-attachments/assets/26b6d934-5820-4cb3-a9c1-fefad5fdaee6" />



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
