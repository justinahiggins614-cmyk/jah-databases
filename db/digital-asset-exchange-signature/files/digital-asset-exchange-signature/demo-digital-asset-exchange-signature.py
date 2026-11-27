"""Demo program for the Digital Asset Exchange Database (digital-asset-exchange-signature).
Fictional-only: all assets, prices, and trades are invented for teaching.
Run: python3 demo-digital-asset-exchange.py
"""
bids = [11, 10, 9]
asks = [13, 14, 15]
best_bid, best_ask = max(bids), min(asks)
print(f"Best bid {best_bid} credits; best ask {best_ask} credits; spread {best_ask - best_bid} credits")
buy, sell, price = 5, 5, 13
traded = min(buy, sell)
print(f"Buy {buy} at {price} meets sell {sell} at {price}: trade {traded} Aurora Tokens for {traded * price} credits")
value = traded * price
fee = value * 0.002
print(f"Trade value {value} credits; taker fee {fee} credits; buyer pays {value + fee} credits")
