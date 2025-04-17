import pandas as pd
from palmerpenguins import load_penguins

def main():
    data = load_penguins()

# Initial cleaning: Remove missing values
    data = data.dropna()

    data.to_csv("results/clean_penguins.csv", index=False)


if __name__ == "__main__":
    main()
    