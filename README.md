# Survival-Analysis-Chlorhexidine-VAP
Capstone project comparing 0.12% vs 0.20% chlorhexidine using survival analysis (KM, Log-rank, Cox PH).
🧪 Survival Analysis of Chlorhexidine Concentrations in Preventing Ventilator-Associated Pneumonia

This repository contains a complete survival analysis project evaluating whether 0.20% chlorhexidine is more effective than 0.12% chlorhexidine in preventing ventilator-associated pneumonia (VAP) among mechanically ventilated ICU patients.
The project applies standard statistical survival methods including Kaplan–Meier, Log-rank testing, and Cox proportional hazards regression.

📌 Project Summary

This project uses patient-level ICU data from a chlorhexidine mouthwash trial (10-day follow-up).
The key goals were to:

Compare VAP-free survival between 0.12% and 0.20% chlorhexidine groups

Estimate whether the hazard (risk) of developing VAP differs between groups

Identify whether age or APACHE II score predict VAP development

🛑 Key Result:
Although 0.20% chlorhexidine showed a trend toward better VAP-free survival, none of the differences between groups were statistically significant.


📊 Methods
1. Data Preparation

Event defined as 1 if VAP occurred

Censoring (0) if no VAP during 10-day follow-up

Duration = last follow-up day with available clinical data

Treatment encoded as:

0 → CHX 0.12%

1 → CHX 0.20%

2. Kaplan–Meier Survival Analysis

VAP-free survival curves generated for both treatment groups

Visual comparison showed a mild advantage for 0.20% CHX

Confidence intervals overlapped

3. Log-Rank Test

χ² = 1.56

p = 0.21
➡️ No statistically significant difference in survival curves

4. Cox Proportional Hazards Model
Predictor	HR	Interpretation	p-value
CHX 0.20% vs 0.12%	0.45	55% ↓ hazard, but not significant	0.48
Age	0.97	No effect	0.19
APACHE II Score	0.95	No effect	0.36

➡️ No statistically significant predictors of VAP in the model.

📈 Results Summary

KM curves: 0.20% CHX showed a slight advantage but nonsignificant

Log-rank p = 0.21 → no evidence of difference

Cox model: HR = 0.45 but wide CI and p = 0.48

Only 6 events in dataset → low statistical power

🧠 Conclusion

The study found no statistically significant difference in VAP-free survival between 0.12% and 0.20% chlorhexidine mouthwash over a 10-day ICU follow-up.
While 0.20% CHX showed better numerical performance, the evidence is insufficient to confirm clinical superiority.
