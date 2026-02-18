# CRYPTEX — Market Intelligence

A live cryptocurrency price dashboard that fetches the top 5 coins by market cap from the [CoinGecko API](https://www.coingecko.com/en/api) and displays them in a dark, editorial-styled web interface.

## Features

- Live top 5 cryptocurrencies by market cap
- Price flash animation on refresh (green = up, red = down)
- 24h change with ▲/▼ indicators
- Auto-refreshes every 60 seconds
- No build tools or dependencies — single HTML file

## Usage

Just open `crypto_dashboard.html` in your browser:

```bash
open crypto_dashboard.html
```

## Python Script

A terminal version is also available (`crypto_prices.py`) using only the Python standard library:

```bash
python3 crypto_prices.py
```

Output:

```
Fetching top 5 cryptocurrencies by market cap...

#    Name            Symbol   Price (USD)      24h Change   Market Cap
----------------------------------------------------------------------
1    Bitcoin         BTC      $68,585.00       ▲ +0.56%.... $1,371,075,542,188
2    Ethereum        ETH      $1,987.84        ▲ +1.94%.... $240,029,734,980
3    Tether          USDT     $0.999641        ▲ +0.01%.... $183,675,502,510
4    XRP             XRP      $1.49            ▲ +2.03%.... $90,502,352,210
5    BNB             BNB      $626.67          ▲ +2.41%.... $85,467,785,161
```

## Data Source

Powered by the free [CoinGecko API](https://www.coingecko.com/en/api) — no API key required.
