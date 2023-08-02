from utils import load_data_from_csv_files
from utils import preprocess_data

def main():
    # List of file paths for CSV files
    file_paths = ['contract.csv', 'internet.csv', 'personal.csv', 'phone.csv']

    # Call the load_data_from_csv_files function from the utils file
    data = load_data_from_csv_files(file_paths)

    # Do further processing or analysis with the data
    print(data.head())
    print(data.info())
    print(data.shape)

    data = preprocess_data(data)
    print(data.info())

if __name__ == "__main__":
    main()
