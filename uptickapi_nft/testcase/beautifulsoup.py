from bs4 import BeautifulSoup

# 打开测试报告的HTML文件
with open(r'/Users/starrymedia/PycharmProjects/upticknetwork/uptickapi_nft/reports/upticknftapireport2023-10-31.html', 'r') as file:
    html_content = file.read()

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')

# 查找所有的失败测试用例
failed_testcases = soup.find_all(class_='text-danger')
errored_testcases = soup.find_all(class_='text-warning')
# 遍历每个失败的测试用例，提取相关数据
for testcase in failed_testcases or errored_testcases:
    # 获取测试用例名称
    testcase_name = testcase.select().text

    # 获取失败消息
    failure_message = testcase.find(class_='test_log').text

    # 打印测试用例名称和失败消息
    print(f'Test Case: {testcase_name}')
    print(f'Failure Message: {failure_message}')
    print('---')
