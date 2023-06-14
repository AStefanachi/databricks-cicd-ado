from runtime.nutterfixture import NutterFixture, tag
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