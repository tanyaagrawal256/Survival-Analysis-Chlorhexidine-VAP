**Survival-Analysis-Chlorhexidine-VAP**

***Survival analysis of 0.12% vs 0.20% chlorhexidine in preventing ventilator-associated pneumonia (VAP)***

This repository contains a complete capstone project evaluating whether 0.20% chlorhexidine is more effective than 0.12% chlorhexidine in preventing ventilator-associated pneumonia (VAP) among mechanically ventilated ICU patients.
The project applies standard survival analysis methods including:

*Kaplan–Meier curves

*Log-rank hypothesis testing

*Cox proportional hazards modeling

📌 **Project Summary**

This analysis uses patient-level ICU data from a 10-day chlorhexidine oral-care trial.
The goals were to:

*Compare VAP-free survival between 0.12% and 0.20% CHX groups

*Estimate whether the hazard (risk) of VAP differs between concentrations

*Evaluate the role of age and APACHE II score as risk factors

🛑 **Key Finding**

Although 0.20% chlorhexidine showed a numerical trend toward better VAP-free survival,
➡️ None of the differences reached statistical significance.

📊 **Methods Overview**

**1. Data Preparation**

*Event = 1 if VAP occurred

*Censoring = 0 if patient did not develop VAP during follow-up

*Duration = last clinical day recorded (Day 1–10)

*Treatment coding

0 → CHX 0.12%

1 → CHX 0.20%

Python scripts in src/ perform:

*Cleaning

*Survival variable creation

*Group encoding

**2. Kaplan–Meier Survival Analysis**

*KM curves generated for both CHX concentrations

*Slight numerical advantage for 0.20%

*Confidence intervals overlapped → no significant difference

### 3. Log-Rank Test

| Statistic | Value |
|----------|--------|
| χ²       | **1.56** |
| p-value  | **0.21** |

➡️ **No statistically significant difference in survival curves.**

---

### 4. Cox Proportional Hazards Model

| Predictor                | Hazard Ratio (HR) | Interpretation                     | p-value |
|--------------------------|-------------------|-------------------------------------|---------|
| **CHX 0.20% vs 0.12%**   | **0.45**           | 55% ↓ hazard (not significant)      | 0.48    |
| **Age**                  | 0.97               | No meaningful effect                | 0.19    |
| **APACHE II Score**      | 0.95               | No meaningful effect                | 0.36    |


➡️ No predictors were statistically significant.

## 📈 Results Summary

### **Kaplan–Meier Curves**
- 0.20% chlorhexidine shows **slightly better VAP-free survival**
- Differences are **not statistically significant**

### **Log-Rank Test**
- **p = 0.21**
- ➡️ Insufficient evidence of a difference between survival curves

### **Cox Proportional Hazards Model**
- **HR = 0.45**, but with wide confidence intervals  
- ➡️ Not statistically significant (p = 0.48)

### **Power Note**
- Only **6 VAP events** recorded  
- ➡️ Statistical power is limited

---

## 🧠 Conclusion

Over a 10-day ICU follow-up period:

- **0.20% chlorhexidine** showed a mild numerical improvement  
- **No statistical evidence** supports its superiority over **0.12%**  
- **Age** and **APACHE II score** were **not significant predictors**  
- Both concentrations appear to perform similarly  
- Larger sample sizes would be required to detect meaningful differences

---

## 📂 Repository Structure

Survival-Analysis-Chlorhexidine-VAP/
├── data/                       # Raw dataset (Excel)
│   └── Data form Chlorhexidine Trial.xlsx
├── notebooks/                  # Jupyter/Colab notebook
│   └── Survival_capstone.ipynb
├── results/                    # Output plots & result files
│   └── analysis_result_plots.pdf
├── src/                        # Modular Python scripts
│   ├── data_preprocessing.py
│   ├── eda.py
│   ├── km_analysis.py
│   ├── logrank_test.py
│   └── cox_model.py
└── README.md

**▶️ How to Run the Analysis (Colab/Jupyter)**
1. Clone the repository
git clone https://github.com/tanyaagrawal256/Survival-Analysis-Chlorhexidine-VAP.git
cd Survival-Analysis-Chlorhexidine-VAP

2. Import modules in your notebook
from data_preprocessing import load_and_prepare_data
from km_analysis import km_overall, km_by_trial_arm
from logrank_test import logrank_by_trial_arm
from cox_model import fit_cox_model, plot_cox_forest

3. Run the workflow
df = load_and_prepare_data()

km_overall(df)
km_by_trial_arm(df)

logrank_by_trial_arm(df)

cph = fit_cox_model(df)
plot_cox_forest(cph)

**📜 License**

This project is for academic and educational purposes.

**🙌 Acknowledgements**

Developed as part of a survival analysis capstone on chlorhexidine use in ICU VAP prevention.
