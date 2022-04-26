from asyncio import as_completed
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionTests
from searchtests import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)
smoke_test = TestSuite([assertions_test, search_test])

# parametros para generar el reporte
kwargs = {
    "output": "smoke-report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)