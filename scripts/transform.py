import pandas as pd

def transform():
    df = pd.read_csv("data/orders.csv")

    # Filter
    df = df[df["amount"] > 100]

    # Aggregate
    result = df.groupby("customer_id")["amount"].sum().reset_index()

    print("Transformed Data:")
    print(result)

if __name__ == "__main__":
    transform()
