import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import click
from palmerpenguins import load_penguins

@click.command()
@click.argument('data_path')

def main(data_path):

    data = pd.read_csv(data_path)

    summary = data[['bill_length_mm', 'bill_depth_mm']].agg({
      'bill_length_mm': 'mean',
     'bill_depth_mm': 'mean'
    })

    print(summary)

    sns.set_theme(style="whitegrid")
    sns.boxplot(data=data, x="species", y="bill_length_mm")

    plt.savefig("results/bill_length_boxplot.png", dpi=300)

if __name__ == "__main__":
    main()
