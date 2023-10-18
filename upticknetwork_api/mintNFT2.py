from web3 import Web3
import json

# web3连接节点
web3 = Web3(Web3.HTTPProvider('https://json-rpc.uptick.network/'))

contract_address = '0xddb74a14ecced953c2f2937ca5800de1dc23712d'
# 将地址转换为 checksum 格式
checksum_address = Web3.to_checksum_address(contract_address)

# 打印 checksum 格式的地址
print("Checksum Address:", checksum_address)

private_key = '193a382c2df43babd9bc6f2f1aae507d2ffe62cf8991c78c1580ac545a1c18ca'

# ABI文件路径
abi_file_path = '/Users/starrymedia/Downloads/Uptick1155.json'

# 加载合约ABI
with open(abi_file_path, 'r') as abi_file:
    abi = json.load(abi_file)['abi']

# 创建合约实例
contract = web3.eth.contract(address=checksum_address, abi=abi)
print(contract)

# 创建一个账户对象
account = web3.eth.account.from_key(private_key)

# 设置默认的交易发送者
web3.eth.default_account = account.address
# 创建NFT
def create_nft(toAddress,tokenId,baseurl,royaltyPercentage,amountValue):
    nonce = web3.eth.get_transaction_count(web3.eth.default_account)
    transaction = contract.functions.createNFT(toAddress,tokenId,baseurl,royaltyPercentage,amountValue).buildTransaction({
        'from': web3.eth.default_account,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    })
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
    #发送交易
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # 等待交易被确认
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_receipt













# # 增发NFT
# def mint_nft(token_id, amount):
#     nonce = web3.eth.getTransactionCount(web3.eth.defaultAccount)
#     transaction = contract.functions.mintNFT(token_id, amount).buildTransaction({
#         'from': web3.eth.defaultAccount,
#         'nonce': nonce,
#         'gas': 2000000,
#         'gasPrice': web3.toWei('50', 'gwei')
#     })
#     signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
#     tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
#     tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
#     return tx_receipt

# 使用示例
if __name__ == "__main__":
    # 创建NFT
    toAddress="0xe6391ac3d333aedbbd8b398e524509d705f3e23e"
    tokenId="999999"
    baseurl=""
    royaltyPercentage="5"
    amountValue="2"
    create_nft(toAddress,tokenId,baseurl,royaltyPercentage,amountValue)

    # # 增发NFT
    # mint_token_id = 1
    # mint_amount = 10
    # mint_nft(mint_token_id, mint_amount)

