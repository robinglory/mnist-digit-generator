import pandas as pd

# Load your dataset
df = pd.read_csv(r"C:\Users\ASUS\Desktop\Problem 2\synthetic_wtp_laptop_data.csv")

# Base model specs and selling price
base_specs = {
    'Memory': 16,
    'Storage': 512,
    'CPU_class': 1,
    'Screen_size': 14.0,
    'Year': 2025,
    'Price': 111000
}

# Upgrade costs
upgrade_costs = {
    'Memory_32GB': 7000,
    'Storage_1024GB': 5000,
    'CPU_Class_2': 15000,
    'Screen_Size_16inch': 3000
}

# Estimate price difference function
def estimate_price_increase(df, base_specs, upgrade_name):
    if upgrade_name == 'Memory_32GB':
        base = df[
            (df['Memory'] == 16) &
            (df['Storage'] == 512) &
            (df['CPU_class'] == 1) &
            (df['Screen_size'] == 14.0)
        ]
        upgraded = df[
            (df['Memory'] == 32) &
            (df['Storage'] == 512) &
            (df['CPU_class'] == 1) &
            (df['Screen_size'] == 14.0)
        ]

    elif upgrade_name == 'Storage_1024GB':
        base = df[
            (df['Memory'] == 16) &
            (df['Storage'] == 512) &
            (df['CPU_class'] == 1) &
            (df['Screen_size'] == 14.0)
        ]
        upgraded = df[
            (df['Memory'] == 16) &
            (df['Storage'] == 1024) &
            (df['CPU_class'] == 1) &
            (df['Screen_size'] == 14.0)
        ]

    elif upgrade_name == 'CPU_Class_2':
        base = df[
            (df['Memory'] == 16) &
            (df['Storage'] == 512) &
            (df['CPU_class'] == 1) &
            (df['Screen_size'] == 14.0)
        ]
        upgraded = df[
            (df['Memory'] == 16) &
            (df['Storage'] == 512) &
            (df['CPU_class'] == 2) &
            (df['Screen_size'] == 14.0)
        ]

    elif upgrade_name == 'Screen_Size_16inch':
        base = df[
            (df['Memory'] == 16) &
            (df['Storage'] == 512) &
            (df['CPU_class'] == 1) &
            (df['Screen_size'] == 14.0)
        ]
        upgraded = df[
            (df['Memory'] == 16) &
            (df['Storage'] == 512) &
            (df['CPU_class'] == 1) &
            (df['Screen_size'] >= 15.5)  # Approx match for 16 inch
        ]

    else:
        return 0

    base_price = base['price'].mean()
    upgraded_price = upgraded['price'].mean()

    if pd.isna(base_price) or pd.isna(upgraded_price):
        return 0

    return upgraded_price - base_price


# Calculate gross profits
gross_profits = {}
for upgrade, cost in upgrade_costs.items():
    price_diff = estimate_price_increase(df, base_specs, upgrade)
    gross_profit = price_diff - cost
    gross_profits[upgrade] = gross_profit
    print(f"{upgrade}: Price Increase = {price_diff:.0f}, Cost = {cost}, Gross Profit = {gross_profit:.0f}")

# Rank upgrades
sorted_upgrades = sorted(gross_profits.items(), key=lambda x: x[1], reverse=True)

print("\nTop 2 Upgrade Options:")
for upgrade, profit in sorted_upgrades[:2]:
    print(f"{upgrade} with estimated gross profit of {profit:.0f} yen")
