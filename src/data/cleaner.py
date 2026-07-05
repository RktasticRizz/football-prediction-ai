from pathlib import Path
import pandas as pd


class DataCleaner:
    """Cleans and preprocesses the raw football results dataset."""

    def __init__(
        self,
        input_path: Path = Path("data/raw/results.csv"),
        output_path: Path = Path("data/processed/results_clean.csv"),
    ):
        self.input_path = input_path
        self.output_path = output_path

    def clean(self) -> pd.DataFrame:
        """Clean the dataset and save the processed version."""

        df = pd.read_csv(self.input_path)

        # -----------------------
        # Convert date
        # -----------------------
        df["date"] = pd.to_datetime(df["date"])

        # -----------------------
        # Remove duplicate rows
        # -----------------------
        duplicates = df.duplicated().sum()
        print(f"Duplicates removed: {duplicates}")

        df = df.drop_duplicates()

        # -----------------------
        # Remove missing scores
        # -----------------------
        df = df.dropna(subset=["home_score", "away_score"])

        # -----------------------
        # Ensure scores are integers
        # -----------------------
        df["home_score"] = df["home_score"].astype(int)
        df["away_score"] = df["away_score"].astype(int)

        # -----------------------
        # Sort chronologically
        # -----------------------
        df = df.sort_values("date").reset_index(drop=True)

        # -----------------------
        # Save cleaned dataset
        # -----------------------
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(self.output_path, index=False)

        print(f"\nClean dataset saved to:")
        print(self.output_path)

        return df