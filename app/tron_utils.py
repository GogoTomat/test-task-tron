from tronpy import Tron
from tronpy.providers import HTTPProvider


async def get_tron_wallet_info(wallet_address: str):
    client = Tron(HTTPProvider(api_key="YOUR_TRON_KEY"))
    account = client.get_account(wallet_address)

    return {
        "wallet_address": wallet_address,
        "bandwidth": account.get("bandwidth", 0),
        "energy": account.get("energy", 0),
        "trx_balance": account.get("balance", 0),
    }
