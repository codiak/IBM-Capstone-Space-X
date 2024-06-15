# IBM-Capstone-Space-X


## Project Summary

This project uses publicly available SpaceX launch data to explore and model the probability of successful launch and reuse of a booster. Data transformation, interactive visualizations, and multiple model types were all used in development. Targeted application for the models was the cost estimation fora given launch.​

The resulting models, especially SVM and KNN, proved to be sufficiently accurate for the targeted estimation use case (83.3% accuracy). The interactive map and plots could also be used to help guide decisions for launch customers.​

## Background

The increasing demand for cost-effective space launches has positioned SpaceX as the leading private space launch company, primarily due to its focus on booster reusability. The launch data used in this project spans from 2010 to 2020. The goal is to tackle the challenge of estimating launch costs for customers, focusing on predicting booster retrieval and reuse. Comprehensive data transformations and interactive visualizations—such as pie charts, scatterplots, and maps—provide valuable insights.​

Problems addressed and potential applications include:​

* Estimating launch costs for customers.​

* Predicting booster retrieval and reuse.​

* Offering insights through interactive visualizations.​

* Useful for SpaceX, payload organizations, and environmental groups.​

## Methodology

* Data Collection​

  * Sourced from SpaceX API and Wikipedia (2010-2020).​

* Data Wrangling​

  * Aggregated data into CSV; loaded into Pandas dataframe.​

* Transformations​

  * Categorical data mapped to binary/numeric values.​

* EDA​

  * Conducted using SQL and visual tools.​

* Visualizations​

  * Created with Folium and Plotly Dash (pie charts, scatterplots, interactive maps).​

* Predictive Models​

  * Built and tuned SVM and KNN models.​

* Evaluation​

  * Focused on accuracy and minimizing false positives.​

​
