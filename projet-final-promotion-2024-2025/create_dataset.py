import pandas as pd
import numpy as np

def create_football_dataset(n_samples=1000):
    # Match statistics
    data = {
        # Basic match stats
        "HS": np.random.randint(0, 25, n_samples),  # Home Shots
        "AS": np.random.randint(0, 25, n_samples),  # Away Shots
        "HST": np.random.randint(0, 15, n_samples), # Home Shots on Target
        "AST": np.random.randint(0, 15, n_samples), # Away Shots on Target
        "HF": np.random.randint(5, 25, n_samples),  # Home Fouls
        "AF": np.random.randint(5, 25, n_samples),  # Away Fouls
        "HC": np.random.randint(0, 15, n_samples),  # Home Corners
        "AC": np.random.randint(0, 15, n_samples),  # Away Corners
        "HY": np.random.randint(0, 6, n_samples),   # Home Yellow Cards
        "AY": np.random.randint(0, 6, n_samples),   # Away Yellow Cards
        "HR": np.random.randint(0, 2, n_samples),   # Home Red Cards
        "AR": np.random.randint(0, 2, n_samples),   # Away Red Cards
    }

    # Betting odds columns (all betting odds are typically between 1.1 and 15.0)
    betting_columns = [
        # Standard betting odds
        "B365H", "B365D", "B365A", "BWH", "BWD", "BWA", "BFH", "BFD", "BFA",
        "PSH", "PSD", "PSA", "WHH", "WHD", "WHA", "1XBH", "1XBD", "1XBA",
        "MaxH", "MaxD", "MaxA", "AvgH", "AvgD", "AvgA", "BFEH", "BFED", "BFEA"
    ]
    for col in betting_columns:
        data[col] = np.random.uniform(1.1, 15.0, n_samples)

    # Over/Under betting odds and Asian Handicap
    ou_columns = [
        "B365>2.5", "B365<2.5", "P>2.5", "P<2.5", "Max>2.5", "Max<2.5",
        "Avg>2.5", "Avg<2.5", "BFE>2.5", "BFE<2.5"
    ]
    for col in ou_columns:
        data[col] = np.random.uniform(1.5, 3.5, n_samples)

    # Asian Handicap and other betting markets
    ah_columns = [
        "AHh", "B365AHH", "B365AHA", "PAHH", "PAHA", "MaxAHH", "MaxAHA",
        "AvgAHH", "AvgAHA", "BFEAHH", "BFEAHA", "B365CH", "B365CD", "B365CA",
        "BWCH", "BWCD", "BWCA", "BFCH", "BFCD", "BFCA", "PSCH", "PSCD", "PSCA",
        "WHCH", "WHCD", "WHCA", "1XBCH", "1XBCD", "1XBCA", "MaxCH", "MaxCD",
        "MaxCA", "AvgCH", "AvgCD", "AvgCA", "BFECH", "BFECD", "BFECA",
        "B365C>2.5", "B365C<2.5", "PC>2.5", "PC<2.5", "MaxC>2.5", "MaxC<2.5",
        "AvgC>2.5", "AvgC<2.5", "BFEC>2.5", "BFEC<2.5", "AHCh", "B365CAHH",
        "B365CAHA", "PCAHH", "PCAHA", "MaxCAHH", "MaxCAHA", "AvgCAHH", "AvgCAHA",
        "BFECAHH", "BFECAHA"
    ]
    for col in ah_columns:
        data[col] = np.random.uniform(1.5, 4.0, n_samples)

    # Generate realistic match outcomes
    # Higher probability of home wins (45%), then draws (30%), then away wins (25%)
    data["FTR"] = np.random.choice(['H', 'D', 'A'], n_samples, p=[0.45, 0.30, 0.25])

    # Create DataFrame
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    # Path to save the CSV file
    csv_file_path = "/Users/ecembayindir/Desktop/SORBONNE/Classes/Neo4j_Cloud_2/Neo4j Project/neo4j-cours/processed_data.csv"

    # Create dataset with 1000 samples
    df = create_football_dataset(1000)

    # Save to CSV
    df.to_csv(csv_file_path, index=False)

    # Print info about the created dataset
    print(f"Created dataset with {len(df)} rows at: {csv_file_path}")
    print("\nFirst few rows:")
    print(df.head())
    print("\nColumn names:")
    print(df.columns.tolist())