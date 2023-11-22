#Load data from a comma-separated value (CSV) file
import pandas as pd
def main():
    df_input_file = pd.read_csv(filepath_or_buffer="input_file_with_nan.csv")
    print(df_input_file)
if __name__ == '__main__':
    main()