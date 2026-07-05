from src.data.cleaner import DataCleaner


def main():
    cleaner = DataCleaner()

    df = cleaner.clean()

    print("\nFirst five rows:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)


if __name__ == "__main__":
    main()