import pandas as pd
from datetime import datetime

# Electronics Store Data (Sampled)
data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005],
    'ProductName': ['Laptop', 'Smartphone', 'Headphones', 'Smartwatch', 'Bluetooth Speaker'],
    'Price(USD)': [899, 699, 99, 249, 79],
    'Quantity': [1, 2, 1, 1, 3],
    'DiscountApplied': [True, False, True, True, False]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert price from USD to CAD
usd_to_cad_rate = 1.25  # Assuming conversion rate is 1 USD = 1.25 CAD
df['Price(CAD)'] = df['Price(USD)'] * usd_to_cad_rate

# Convert boolean to string "yes" or "no"
df['DiscountApplied'] = df['DiscountApplied'].map({True: 'Yes', False: 'No'})

# Get current date for CSV filename
current_date = datetime.now().strftime('%Y-%m-%d')

# Save DataFrame to CSV with current date as filename
output_filename = f"ecommerce_data_{current_date}.csv"
df.to_csv(output_filename, index=False)

print(f"CSV file '{output_filename}' has been created with transformed data.")