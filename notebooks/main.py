# Databricks notebook source
# DBTITLE 1,Read Bing_covid-19_data.csv in a pandas dataframe
import pandas as pd
pdf = pd.read_csv('https://pandemicdatalake.blob.core.windows.net/public/curated/covid-19/bing_covid-19_data/latest/bing_covid-19_data.csv', low_memory=False)
# COMMAND ----------
# DBTITLE 1,From pandas dataframe create a spark dataframe
sdf = spark.createDataFrame(pdf)
# COMMAND ----------
# DBTITLE 1,Limit the selection to only 100 rows for simplicity
sdf = sdf.limit(100)
# COMMAND ----------
# DBTITLE 1,Crate schema if it doesn't exists
spark.sql("CREATE SCHEMA IF NOT EXISTS covid")
# COMMAND ----------
# DBTITLE 1,Write data frame into a delta table
sdf.write.mode("overwrite").saveAsTable("covid.covid_data")
# added a comment to test cicd