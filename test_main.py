# Databricks notebook source
# DBTITLE 1, Nutter test fixtures
from runtime.nutterfixture import NutterFixture
class CovidData(NutterFixture):
    
    def before_all(self):
        dbutils.notebook.run('main', 3600)
    
    def assertion_is_not_empty(self):
        tbl = spark.sql("SELECT COUNT(*) AS total_record FROM covid.covid_data")
        first_row = tbl.first()
        assert (first_row[0] >= 1)

    # def assertion_your_assertion(self):
    #     # your code
    #     assert (your_assertion_condition)
# COMMAND ----------
# DBTITLE 1, Execute the tests and print the results
result = CovidData().execute_tests()
print(result.to_string())
# COMMAND ----------
result.exit(dbutils)    