#!/usr/bin/env python3
"""Fetch and display top 5 cryptocurrency prices from CoinGecko API."""

import json
import urllib.request


def fetch_prices():
    url = (
        "https://api.coingecko.com/api/v3/coins/markets"
        "?vs_currency=usd&order=market_cap_desc&per_page=5&page=1"
        "&sparkline=false&price_change_percentage=24h"
    )
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())


def format_price(value):
    if value >= 1:
        return f"${value:,.2f}"
    return f"${value:.6f}"


def main():
    print("\nFetching top 5 cryptocurrencies by market cap...\n")
    coins = fetch_prices()

    header = f"{'#':<4} {'Name':<15} {'Symbol':<8} {'Price (USD)':<16} {'24h Change':<12} {'Market Cap'}"
    print(header)
    print("-" * len(header))

    for i, coin in enumerate(coins, 1):
        change = coin.get("price_change_percentage_24h") or 0
        sign = "+" if change >= 0 else ""
        arrow = "\u25b2" if change >= 0 else "\u25bc"

        print(
            f"{i:<4} "
            f"{coin['name']:<15} "
            f"{coin['symbol'].upper():<8} "
            f"{format_price(coin['current_price']):<16} "
            f"{arrow} {sign}{change:.2f}%{'':.<4} "
            f"${coin['market_cap']:,.0f}"
        )

    print()


if __name__ == "__main__":
    main()
