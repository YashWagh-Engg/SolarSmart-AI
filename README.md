# 🌞 SolarSmart AI  
**AI-Powered Energy Optimization for Rooftop Solar Users**

SolarSmart AI is a data-driven web application that helps rooftop solar users maximize their solar energy utilization by recommending the best time to run heavy household appliances based on solar generation and home electricity consumption patterns.

## 📌 Problem Statement

Rooftop solar systems usually generate maximum power during midday, while household electricity consumption often peaks in the morning and evening. 
This mismatch leads to underutilization of solar energy and increased dependence on the power grid. Most users do not have clear, data-driven guidance on when to shift flexible loads (like washing machines, water pumps, or EV charging) to make the best use of their solar power.


## 💡 Solution

SolarSmart AI analyzes:
- 🌞 Solar generation data  
- 🏠 Household electricity consumption data  

It learns hourly patterns from both and computes an **opportunity score** to identify time windows where solar generation is high and home usage is low.
Based on this, it recommends the best hours to operate heavy appliances, helping users save money and reduce grid dependence.


## 🚀 Key Features

- 📂 Upload solar & home consumption CSV files  
- 📊 Visualize hourly solar generation and usage patterns  
- ⚡ Compute opportunity score for each hour  
- 🕒 Recommend best time slots for heavy appliances  
- 🌐 Interactive web interface using Streamlit  
- 🧠 Modular backend design for easy extension  


## 🏗️ Project Architecture

SolarSmartAI/
│
├── src/
│ ├── data_processing.py # Data loading & cleaning
│ ├── patterns.py # Hourly pattern analysis
│ ├── recommendations.py # Opportunity score & decisions
│ ├── main.py # Backend pipeline runner
│ └── app.py # Streamlit web app
│
├── .gitignore
└── README.md


## 🔄 System Flow

1. User uploads solar and home consumption CSV files.  
2. Data is cleaned and aggregated into hourly values.  
3. Hourly patterns are learned for both datasets.  
4. Data is normalized and an **opportunity score** is computed.  
5. Best hours are recommended to shift heavy loads.  
6. Results are displayed through an interactive web UI.

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Visualization:** Streamlit  
- **Environment:** VS Code, Windows  
- **Version Control:** Git & GitHub  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YashWagh-Engg/SolarSmart-AI.git
cd SolarSmart-AI
2️⃣ (Optional) Create virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install pandas scikit-learn streamlit
▶️ How to Run the Application
From the project root:

bash
Copy code
streamlit run src/app.py
Then open your browser at:

arduino
Copy code
http://localhost:8501
📥 How to Use
Launch the app.

Upload:

🌞 Solar generation CSV file

🏠 Household consumption CSV file

Click Run Analysis.

View:

Hourly patterns

Opportunity score chart

Top recommended hours to run heavy appliances

📂 Datasets
Due to GitHub file size limits, large CSV datasets are not included in this repository.

You can download similar datasets from:

Individual Household Electric Power Consumption Dataset:
https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption

After downloading, place the CSV files inside a local Data/ folder before running the app.

📊 Results & Impact
Helps users identify best times to use heavy appliances

Improves solar self-consumption

Reduces electricity bills and grid dependence

Increases return on investment of solar systems

Promotes sustainable energy usage

🔮 Future Scope
🔋 Battery storage optimization
📅 Day-ahead solar forecasting
📈 Cost-based optimization using tariffs
🧠 Advanced ML/DL model
☁️ Cloud deployment
📱 Mobile-friendly U
🏘️ Multi-household support

👨‍🎓 Project By
Yash Wagh
Project: SolarSmart AI – Intelligent Energy Optimization System


⚡ Why Timing of Electricity Usage Matters
Many people assume that installing rooftop solar means electricity is “free” and usage timing no longer matters. In reality, this is not true.
Solar panels generate electricity mainly during midday, while household consumption often peaks in the morning and evening. This creates a mismatch between generation and usage.
In most billing systems (such as net metering):
Excess solar energy exported to the grid is compensated at a lower rate.
Electricity imported from the grid during non-solar hours is charged at a higher rate.
Some exported units may expire or not be fully adjusted.
Fixed charges and minimum billing still apply.
As a result, users may still receive electricity bills even after installing solar panels.
The key to maximizing savings is self-consumption — using solar energy directly at the time it is generated rather than exporting it and buying back later.
SolarSmart AI addresses this problem by:
Identifying hours when solar generation is high.
Detecting hours when household usage is low.
Recommending the best time windows to shift flexible loads.
By shifting appliance usage to these periods, users can:
Increase solar self-consumption.
Reduce grid imports during peak hours.
Improve return on investment of solar panels.

Achieve more sustainable and efficient energy usage.

Note: In some cases, users may receive government subsidies for rooftop solar installation and may even observe zero monthly electricity bills due to favorable net metering policies. While this represents a best-case scenario, long-term benefits still depend on how efficiently solar energy is utilized.
SolarSmart AI adds value by maximizing self-consumption, improving ROI even for subsidized systems, and future-proofing users against possible tariff or policy changes.

Improve return on investment of solar panels.

Achieve more sustainable and efficient energy usage.

Note: In some cases, users may receive government subsidies for rooftop solar installation and may even observe zero monthly electricity bills due to favorable net metering policies.
While this represents a best-case scenario, long-term benefits still depend on how efficiently solar energy is utilized.
SolarSmart AI adds value by maximizing self-consumption, improving ROI even for subsidized systems, and future-proofing users against possible tariff or policy changes.


📜 License
