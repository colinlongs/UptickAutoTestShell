import requests
from web3 import Web3
import json


w3 = Web3(Web3.HTTPProvider('https://json-rpc.uptick.network/'))
# 加载智能合约ABI
with open('/Users/starrymedia/Downloads/Uptick1155.json', 'r') as f:
    contract_abi = [json.load(f)]
print(contract_abi)

contract_address = '0xddb74a14ecced953c2f2937ca5800de1dc23712d'
contract = w3.eth.contract(address=contract_address, abi=contract_abi)
print(contract)
#
def create_nft(toAddress,tokenId,baseurl,royaltyPercentage,amountValue):
    tx_hash = contract.functions.mintNft(toAddress,tokenId,baseurl,royaltyPercentage,amountValue).send()

    print(tx_hash)



create_nft("0xe6391ac3d333aedbbd8b398e524509d705f3e23e","99999999","https://ipfs.upticknft.com/ipfs/QmU8sHEVVQtM4URXTS5Ln8cfjJqDVwcBZsHSpWyNf5FhPj","5","2")


# url = "https://uptick.upticknft.com/uptickapi/nft/mint.do"
# payload = {
#
#     "nftAddress": "0x3bf30697c434df2e0dd3f2666d338ff8bfc9499e",
#     "description": "foxfox",
#     "name": "foxfox",
#     "royaltyPercentage": "5",
#     "owner": "0xe6391ac3d333aedbbd8b398e524509d705f3e23e",
#     "imgUrl": "QmU8sHEVVQtM4URXTS5Ln8cfjJqDVwcBZsHSpWyNf5FhPj",
#     "nftId": "1695786039135337721",
#     "amount": "1",
#     "properties": "[]",
#     "metadataUrl": "Qmf5N4sFeXUSDttiHTdnn9ZHcuPRCA7bFD2AhebA7ySmPq",
#     "licenseCode": "",
#     "assetPublic": "true",
#     "nftType": "ERC1155",
#     "fileType": "",
#     "fileUrl": "",
#     "channel": "Uptick",
#     "adult": "false",
#     "authenticationAddress": "0xe6391ac3d333aedbbd8b398e524509d705f3e23e",
#     "lang": "en"
# }
#
# response =requests.post(url=url,data=payload)
# res=response.json()
#
# if response.status_code == 200:
#     print("请求成功")
#     print(res)
# else:
#     print("请求失败")
#     print(response.status_code)
# tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)