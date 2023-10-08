import pandas as pd

def main():
    removedp()

def removedp():
    input_file = input('Enter Your file location path/to/file.csv: ')
    output_file = input('Enter location to save path/to/file.csv: ')
    factor = input('Enter columns to remove duplicates, separated by commas (e.g., id,place_name): ')
    values = factor.split(',')

    # Trim whitespace from each value and remove leading/trailing spaces
    values = [value.strip() for value in values]

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(input_file)

    # Remove duplicates based on the specified columns
    df.drop_duplicates(subset=values, inplace=True)

    # Save the deduplicated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Duplicates removed and saved to {output_file}")

if __name__ == "__main__":
    main()
