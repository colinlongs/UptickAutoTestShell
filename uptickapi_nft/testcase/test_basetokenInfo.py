import unittest
from  unittestreport import ddt,list_data
from uptickapi_nft.testcase import excelutils
import requests

ex= excelutils.HandleExcel(r"/Users/starrymedia/PycharmProjects/upticknetwork/uptickapi_nft/testcase/api_testcase.xlsx","商品基础信息")
cases=ex.read_data()

@ddt
class TestgetbasetokenInfo(unittest.TestCase):
    @list_data(cases)
    def test_getbasetokenInfo(self,item):
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
                self.assertEqual(expect["name"],result["data"]["name"])
                self.assertEqual(expect["metadataUrl"], result["data"]["metadataUrl"])
        except AssertionError as e:
            raise e
