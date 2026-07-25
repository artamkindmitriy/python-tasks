data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}

print("Ключи:", list(data.keys()))
print("Значения:", list(data.values()))

data["ETH"]["total_diff"] = 100

data["tokens"][0]["fst_token_info"]["name"] = "doge"

total_out_sum = sum(token.pop("total_out", 0) for token in data["tokens"])
data["ETH"]["totalOut"] = total_out_sum

token_info = data["tokens"][1]["sec_token_info"]
if "price" in token_info:
    token_info["total_price"] = token_info.pop("price")

print("\nОбновленные данные:")
import json
print(json.dumps(data, indent=2, ensure_ascii=False))