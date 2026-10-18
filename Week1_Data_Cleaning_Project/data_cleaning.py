import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project folders
ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "outputs"
OUT_DIR.mkdir(exist_ok=True)

# Titanic dataset
DATA_SOURCE = DATA_DIR / "titanic.csv"


def main():

    # -------------------------------
    # 1. Load dataset
    # -------------------------------
    df = pd.read_csv(DATA_SOURCE)

    print("========== INITIAL DATASET ==========")
    print("Dataset Shape:", df.shape)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nDataset Information:")
    df.info()

    print("\nStatistical Summary:")
    print(df.describe())

    # -------------------------------
    # 2. Missing values BEFORE cleaning
    # -------------------------------
    print("\n========== MISSING VALUES BEFORE ==========")
    print(df.isnull().sum())

    print("\nMissing Value Percentage:")
    print((df.isnull().sum() / len(df) * 100).round(2))

    # -------------------------------
    # 3. Duplicate check
    # -------------------------------
    print("\n========== DUPLICATE CHECK ==========")
    print("Duplicate rows:", df.duplicated().sum())

    # -------------------------------
    # 4. Check categorical values
    # -------------------------------
    print("\n========== CATEGORICAL CHECK ==========")
    print("Sex:", df["Sex"].unique())
    print("Embarked:", df["Embarked"].unique())
    print("Pclass:", df["Pclass"].unique())
    print("Survived:", df["Survived"].unique())

    # -------------------------------
    # 5. Handle missing values
    # -------------------------------

    # Fill Age with median
    df["Age"] = df["Age"].fillna(df["Age"].median())

    # Fill Embarked with mode
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Cabin has too many missing values, so remove it
    df = df.drop(columns=["Cabin"])

    # -------------------------------
    # 6. Outlier analysis using IQR
    # -------------------------------
    print("\n========== OUTLIER ANALYSIS ==========")

    for column in ["Age", "Fare", "SibSp", "Parch"]:

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[
            (df[column] < lower_bound) |
            (df[column] > upper_bound)
        ]

        print(column, "potential outliers:", len(outliers))

    # -------------------------------
    # 7. Boxplot - Age
    # -------------------------------
    plt.figure(figsize=(8, 5))
    plt.boxplot(df["Age"].dropna())
    plt.title("Age Outlier Detection")
    plt.ylabel("Age")
    plt.show()

    # -------------------------------
    # 8. Boxplot - Fare
    # -------------------------------
    plt.figure(figsize=(8, 5))
    plt.boxplot(df["Fare"].dropna())
    plt.title("Fare Outlier Detection")
    plt.ylabel("Fare")
    plt.show()

    # -------------------------------
    # 9. Encode categorical columns
    # -------------------------------
    df = pd.get_dummies(
        df,
        columns=["Sex", "Embarked"],
        drop_first=True
    )

    # -------------------------------
    # 10. Final dataset information
    # -------------------------------
    print("\n========== FINAL CLEANED DATASET ==========")

    print("Final Dataset Shape:", df.shape)

    print("\nRemaining Missing Values:")
    print(df.isnull().sum())

    print("\nFinal Dataset - First 5 Rows:")
    print(df.head())

    # -------------------------------
    # 11. Save cleaned dataset
    # -------------------------------
    output_file = OUT_DIR / "titanic_cleaned.csv"

    df.to_csv(output_file, index=False)

    print("\nCleaned dataset saved successfully!")
    print("Saved at:", output_file)


if __name__ == "__main__":
    main()