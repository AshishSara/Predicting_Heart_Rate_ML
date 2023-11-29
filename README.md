# PredictingHRData

MLModels is a textbook example of EDA, Feature Engineering, Feature Analysis, and thorough testing of theoretically appropriate machine learning models and their subsequent results. 

Below is a visualization of our feature analysis and subsequent cumulative importance graph to determine and confirm the most important features for our target variable, heart rate prediction. 

<img width="769" alt="Screenshot 2023-11-28 at 7 16 18 PM" src="https://github.com/AshishSara/PredictingHRData/assets/79825659/c3dfee52-5996-44bc-9579-e6db15537ae6">
<img width="784" alt="Screenshot 2023-11-28 at 7 16 50 PM" src="https://github.com/AshishSara/PredictingHRData/assets/79825659/5617ba13-091f-469a-b580-5ec8f0cef2a5">



Below are the results of the base models minus LSTMS and GRUs as I found these to be more complex and ultimately resulted in poor metrics so they were voided from the graph below. 


![image](https://github.com/AshishSara/PredictingHRData/assets/79825659/f6ae7efc-8c66-4018-9b3f-1de438083130)
<img width="804" alt="Screenshot 2023-11-28 at 7 14 46 PM" src="https://github.com/AshishSara/PredictingHRData/assets/79825659/27901916-62fc-4d83-b2d7-cf9fa08e2026">


Below is a more clear and thorough representation of all model performances


Results for Linear Regression:
  MAE: 8.545521803893369
  MSE: 133.38288402675323
  RMSE: 11.549150792450206
  R²: 0.11786161645326065

Results for Ridge Regression:
  MAE: 8.510334911862682
  MSE: 133.10060612197665
  RMSE: 11.536923598688546
  R²: 0.119728483978637

Results for Lasso Regression:
  MAE: 8.83734968577659
  MSE: 143.2286570338927
  RMSE: 11.9678175551724
  R²: 0.052745808314458964

Results for Support Vector Regression:
  MAE: 8.258296571139596
  MSE: 134.60705507666881
  RMSE: 11.602028058777863
  R²: 0.10976546319464142

Results for Decision Tree:
  MAE: 8.892119618696187
  MSE: 159.76751813268754
  RMSE: 12.639917647385506
  R²: -0.05663527383749578

Results for Gradient Boosting:
  MAE: 7.756464375218266
  MSE: 112.18908372179023
  RMSE: 10.591934843162047
  R²: 0.2580285117685738

Results for Random Forest:
  MAE: 6.933641168511686
  MSE: 92.06532002537315
  RMSE: 9.595067484148986
  R²: 0.39111863429488913

Results for Extra Trees:
  MAE: 7.243742675276752
  MSE: 96.87575632509481
  RMSE: 9.842548263793011
  R²: 0.35930442865258294

Results for XGBoost:
  MAE: 7.309931323193389
  MSE: 94.79489504641387
  RMSE: 9.736266997490048
  R²: 0.37306637133476717

Results for Neural Network:
  MAE: 8.6921139807303
  MSE: 137.11080159938007
  RMSE: 11.70943216383186
  R²: 0.09320673509042476

Results for K-Nearest Neighbors:
  MAE: 8.461800369003688
  MSE: 134.27476761317342
  RMSE: 11.587698978363798
  R²: 0.11196307294089547

Results for Support Vector Regression (RBF Kernel):
  MAE: 8.258296571139596
  MSE: 134.60705507666881
  RMSE: 11.602028058777863
  R²: 0.10976546319464142

Results for AdaBoost Regressor:
  MAE: 10.815846875466317
  MSE: 171.1284532797725
  RMSE: 13.081607442503865
  R²: -0.13177172810863524

Results for Bagging Regressor:
  MAE: 6.922520009225093
  MSE: 91.90240257831637
  RMSE: 9.58657407932137
  R²: 0.3921961018758826

Results for PLS Regression:
  MAE: 8.72590512124079
  MSE: 138.75811158664473
  RMSE: 11.779563302034788
  R²: 0.0823121185886958

Results for Elastic Net Regression:
  MAE: 8.820062829628574
  MSE: 141.9012053326641
  RMSE: 11.912229234390349
  R²: 0.06152501643027153

Results for Stacking Regressor:
  MAE: 6.894038777682657
  MSE: 89.77053826040829
  RMSE: 9.474731566667643
  R²: 0.4062953572418351

Results for CatBoost Regressor:
  MAE: 7.715465342226439
  MSE: 112.429797822202
  RMSE: 10.603291838962182
  R²: 0.2564365297913992

Results for Bayesian Ridge Regression:
  MAE: 8.593828946369145
  MSE: 136.8689317861013
  RMSE: 11.699099614333631
  R²: 0.09480636046718349

Results for LSTM:
  MAE: 8.45500888679007
  MSE: 129.03631117019808
  RMSE: 11.359415089263974
  R²: 0.14660802407240214

Results for GRU:
  MAE: 8.259443475533235
  MSE: 126.61759330766657
  RMSE: 11.252448325038714
  R²: 0.16260440832423162

Evaluation of Stacked Regressor with Best Parameters after GridSearchCV:
  MAE: 6.93404648163292
  MSE: 90.22908851397294
  RMSE: 9.498899331710644
  R²: 0.4032626984235317


**Best Model**
Stacking Regressor:
  MAE: 6.894038777682657
  MSE: 89.77053826040829
  RMSE: 9.474731566667643
  R²: 0.4062953572418351
