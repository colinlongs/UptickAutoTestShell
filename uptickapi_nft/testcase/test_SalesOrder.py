import unittest
from  unittestreport import ddt,list_data
from uptickapi_nft.testcase import excelutils
import requests

ex= excelutils.HandleExcel(r"/Users/starrymedia/PycharmProjects/upticknetwork/uptickapi_nft/testcase/api_testcase.xlsx","销售订单")
cases=ex.read_data()

@ddt
class Testsaleorder(unittest.TestCase):
    @list_data(cases)
    def test_saleorder(self,item):
        parms= eval(item["data"])
        url= item["url"]
        method = item["method"].lower()
        response = requests.request(method, url, data=parms)
        result = response.json()

        expect = eval(item["expect"])

        try:

            self.assertEqual(expect["code"], result["code"])
            self.assertEqual(expect["msg"], result["msg"])
            if expect["code"] in result:
                self.assertEqual(expect["totalRow"],result["data"]["totalRow"])
        except AssertionError as e:
            raise e