import pandas as pd
from palmerpenguins import load_penguins
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import click


@click.command()
@click.option('--data_path', required=True)

def main( data_path ):
        
        data = pd.read_csv(data_path)

        features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
        X = data[features]
        y = data['species']

        # -------------------------------
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.25, random_state=123, stratify=y
        )

        # -------------------------------
        pipeline = Pipeline([
            ('scaler', StandardScaler()),  # optional but good for KNN
            ('knn', KNeighborsClassifier(n_neighbors=5))
        ])

        # -------------------------------
        pipeline.fit(X_train, y_train)


        y_pred = pipeline.predict(X_test)
        print(classification_report(y_test, y_pred))

        joblib.dump(pipeline, "results/penguin_model.pkl")

        # Save predictions to CSV
        predictions_df = X_test.copy()
        predictions_df["true_species"] = y_test.values
        predictions_df["predicted_species"] = y_pred
        predictions_df.to_csv("results/predictions.csv", index=False)

        # Save classification report as a text file
        report = classification_report(y_test, y_pred)
        with open("results/classification_report.txt", "w") as f:
            f.write(report)

if __name__ == "__main__":
    main()
