from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import joblib
import click


@click.command()
@click.option('--data_path', required=True)
@click.option('--model_path', help="Path to saved model")

def main(data_path,model_path):

    data = pd.read_csv(data_path)
    pipeline = joblib.load(model_path)
    
        # Prepare features and labels
    features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
    X = data[features]
    y = data['species']

    y_pred = pipeline.predict(X)

    # Combine predictions and save if needed
    predictions = X.copy()
    predictions['true_species'] = y.values
    predictions['predicted_species'] = y_pred
    predictions.to_csv("results/predictions_with_labels.csv", index=False)

    # Plot confusion matrix
    cm = confusion_matrix(y, y_pred, labels=pipeline.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=pipeline.classes_)
    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix")
    plt.savefig("results/confusion_matrix.png", dpi=300, bbox_inches='tight')
    plt.close()

    print(" Confusion matrix saved to results/confusion_matrix.png")

if __name__ == "__main__":
    main()