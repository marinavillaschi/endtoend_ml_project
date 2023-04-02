# End to end Machine Learning Project

This is a robust ML project that aims to touch on skills that goes from Data Engineering all the way to ML Engineering.


I'll be working on the following:

1. [Consume data from an API](#ingestion)
2. Build a pipeline to process this data and store it into a datalake
3. Build a pipeline to move it from the datalake into a data warehouse
4. Build a dashboard to analyze this data
5. Prepare data for ML
6. Train ML models with MLFlow
7. Pick the best model for deployment
8. Build the model package and publish it
8. Build an API to make predictions available
10. Build a dashboard to monitor the model

This project's structure covers:
- Data Engineering: steps 1-3
- Data Analysis: step 4
- Data Science: steps 5-7
- ML Engineering: steps 8-10


## Step 1 - Consume data from an API <a name="ingestion"></a>
I'll be consuming data from the [Finnhub Stock API](https://finnhub.io/) that provides real-time stock, currencies and crypto data.

The data I'll be consuming will come specifically from this [company ESG scores endpoint](https://finnhub.io/docs/api/company-esg-score-api).