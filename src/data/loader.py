from pathlib import Path
import pandas as pd


class DataLoader:
    """Loads datasets used throughout the project."""

    def __init__(self, data_dir: Path = Path("data/raw")):
        self.data_dir = data_dir

    def load_results(self) -> pd.DataFrame:
        """
        Load international football match results.

        Returns
        -------
        pd.DataFrame
            Raw match dataset.
        """
        file_path = self.data_dir / "results.csv"

        if not file_path.exists():
            raise FileNotFoundError(f"Dataset not found: {file_path}")

        return pd.read_csv(file_path)