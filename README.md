# PredictingHRData


Comparative Analysis of Machine Learning Models for Heart Rate Prediction Across Multiple Data Sheets
Abstract:
This section aims to critically evaluate and compare the performance of five machine learning models—Linear Regression, Random Forest, Gradient Boosting, ARIMA, and LSTM—across multiple data sheets for predicting heart rate. The performance metrics under consideration include Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-Squared (R2).

Introduction:
Given the application's medical nature, high accuracy and reliability are paramount. Hence, multiple models were trained on each sheet, and their performance was evaluated using three metrics: MAE for understanding the average error magnitude, MSE for penalizing larger errors more significantly, and R2 for assessing how well the model explains the variance in the target variable. 



Methods:
The models were trained and evaluated on a set of data sheets labeled from id003 to id032, resulting in a total of 30 different scenarios. Cross-validation techniques were used to ensure a fair comparison.

Metrics Explained:
Model: The machine learning or statistical model used for prediction. Different models have different strengths and weaknesses, and their performance can vary depending on the nature of the data.

MAE (Mean Absolute Error): Represents the average of the absolute differences between the observed actual outcomes and the predictions made by the model. The smaller the MAE, the better the model has performed. A MAE of 0 would mean the model made no errors, which is unlikely in real-world scenarios.

MSE (Mean Squared Error): Similar to MAE but squares the differences before averaging them. MSE gives a relatively high weight to large errors. A smaller MSE indicates a better fit of the model to the data.

R2 (R-squared or Coefficient of Determination): Represents the proportion of the variance in the dependent variable that is predictable from the independent variables. R2 ranges from 0 to 1, where a higher value generally indicates a better fit of the model. Negative values suggest that the model is worse than a horizontal line. 

Results:
Overall Trends:
Random Forest: This model consistently demonstrated lower MAE and MSE values across the majority of data sheets. It also often exhibited a positive R2 score, suggesting a good fit to the data.

ARIMA: The model showed moderate performance but was typically outperformed by Random Forest in terms of all three metrics.

Linear Regression and Gradient Boosting: These models showed inconsistent performance across sheets, making them less reliable for universal application.

LSTM: This model underperformed consistently, with exceptionally high MAE and MSE and negative R2 values, making it unsuitable for this application.

Notable Anomalies:
Sheet id008: Linear Regression showed an exceptionally high MAE and MSE, which might suggest the presence of outliers or non-linearity in the dataset.

Sheets id029 and id030: These sheets also showed high MAE and MSE for Linear Regression, indicating potential issues with the model's assumptions or the data quality.

Discussion:
Robustness: Random Forest emerged as the most robust model, showing strong performance across varying data conditions. It's advisable for any generalized application within this domain.

Inconsistency: Linear Regression and Gradient Boosting were inconsistent, thereby requiring specific tuning or feature engineering for each sheet, which may not be practical for real-world applications.

Unsuitability of LSTM: Given its poor performance, the LSTM model appears unsuitable for this task, possibly due to the non-sequential nature of the data or insufficient data points for effective training.

Conclusion:
The Random Forest model consistently outperforms other tested models across different datasets and should be considered as the primary model for heart rate prediction in similar medical applications. Further investigation is warranted for sheets where anomalies were detected.

Future Work:
Investigate the reason behind the poor performance of Linear Regression on specific sheets.
Fine-tuning the hyperparameters of Random Forest for further performance improvement.



In Addition, I did a complete analysis by concatenating all the participant data. Please see Jupyter Notebook titled, "MLModels.py" for my analysis
