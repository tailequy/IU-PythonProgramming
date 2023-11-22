'''
Data preprocessing:
• Drop duplicated rows and keep the first.
• Replace empty values with the mean value in columns 1 and 2.
• Replace empty values with the median value in column 3.
• Replace empty values with the “club” string in column 4.
• Replace empty values with the true boolean in column 5.
• Replace empty values with the current date in column 6.
• Replace empty values with the £0.0 in column 7.
• Remove the first character (English pound symbol) in column 8.
• Substitute the abbreviation in column 8.
• Define x column labels.
• Define y column target.
• Save the final file as “output_data.csv”. File location path must be defined.
'''
import pandas as pd
import numpy as np
import config
import sys
import os
import datetime

def main():
    print("using pandas library for data manipulation and cleansing:")
    print()

    project_directory_path = os.path.dirname(sys.argv[0])
    print("project directory path:")
    print(project_directory_path)
    print()

    input_file_path = os.path.join(project_directory_path, config.INPUT_FILE_PATH)
    print("input file path:")
    print(input_file_path)
    print()
    output_file_path = os.path.join(project_directory_path, config.OUTPUT_FILE_PATH)
    print("output file path:")
    print(output_file_path)
    print()
    #Read data and print
    df_input_file = pd.read_csv(filepath_or_buffer=input_file_path, sep=",",encoding="utf-8")
    print("pandas data frame for input file:")
    print(df_input_file)
    print()

    print("number of rows and columns:")
    print(df_input_file.shape)
    print()
    #(8, 8)

    print("file information:")
    df_input_file.info()
    print()
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 8 entries, 0 to 7
    # Data columns (total 8 columns):
    #  ...

    print("summary descriptive stats for numerical columns:")
    print(df_input_file.describe())
    print()
    #             one       two     three
    # count  5.000000  6.000000  6.000000
    # mean   3.800000  2.350000  3.283333
    # ...
    df_result = df_input_file["four"].value_counts()
    print("frequency distribution for categorical column four:")
    print(df_result)
    print()
    # bar      3
    # club     3
    # house    1

    df_result = df_input_file["eight"].value_counts()
    print("frequency distribution for categorical column eight:")
    print(df_result)
    print()
    # ACS    3
    # BMC    2
    # BPS    1
    # CJS    1
    # FM     1
    df_result = df_input_file.apply(lambda x: sum(x.isnull()), axis=0)
    print("missing values (nan) by columns:")
    print(df_result)
    print()
    # one      3
    # two      2
    # three    2
    # four     1
    # five     2
    # six      2
    # seven    2
    # eight    0
    # dtype: int64
    #Return boolean Series denoting duplicate rows.
    df_result = df_input_file.duplicated()
    print("duplicated rows:")
    print(df_result)
    print()
    # 0    False
    # 1    False
    # 2    False
    # 3    False
    # 4    False
    # 5    False
    # 6    False
    # 7     True
    # dtype: bool
    df_input_file = df_input_file.drop_duplicates(keep="first")
    print("drop duplicated rows and keep the first:")
    print(df_input_file)
    print()
    #   one  two  three   four   five       six    seven eight
    # 0  NaN  2.1    3.1    bar   True       NaN  £200.45   BMC
    # 1  NaN  NaN    3.2    NaN  False  1/1/2017  £650.38   ACS
    # 2  3.0  2.3    3.3   club   True  2/1/2017   £85.07   ACS
    # 3  5.0  2.4    NaN    bar    NaN  3/1/2017      NaN   BPS
    # 4  NaN  2.5    3.5    bar  False       NaN  £230.22   BMC
    # 5  6.0  NaN    3.3   club   True  2/1/2017  £650.96   CJS
    # 6  2.0  2.5    NaN  house    NaN  4/1/2017      NaN    FM

    df_input_file = df_input_file.fillna(df_input_file.mean()["one":"two"])
    print("replace nan values with the mean value in columns one and two:")
    print(df_input_file)
    print()
    # one   two  three   four   five       six    seven eight
    # 0  4.0  2.10    3.1    bar   True       NaN  £200.45   BMC
    # 1  4.0  2.36    3.2    NaN  False  1/1/2017  £650.38   ACS
    # 2  3.0  2.30    3.3   club   True  2/1/2017   £85.07   ACS
    # 3  5.0  2.40    NaN    bar    NaN  3/1/2017      NaN   BPS
    # 4  4.0  2.50    3.5    bar  False       NaN  £230.22   BMC
    # 5  6.0  2.36    3.3   club   True  2/1/2017  £650.96   CJS
    # 6  2.0  2.50    NaN  house    NaN  4/1/2017      NaN    FM

    df_input_file = df_input_file.fillna(df_input_file.median()[:"three"])
    print("replace nan values with the median value in column three:")
    print(df_input_file)
    print()
    #    one   two  three   four   five       six    seven eight
    # 0  4.0  2.10    3.1    bar   True       NaN  £200.45   BMC
    # 1  4.0  2.36    3.2    NaN  False  1/1/2017  £650.38   ACS
    # 2  3.0  2.30    3.3   club   True  2/1/2017   £85.07   ACS
    # 3  5.0  2.40    3.3    bar    NaN  3/1/2017      NaN   BPS
    # 4  4.0  2.50    3.5    bar  False       NaN  £230.22   BMC
    # 5  6.0  2.36    3.3   club   True  2/1/2017  £650.96   CJS
    # 6  2.0  2.50    3.3  house    NaN  4/1/2017      NaN    FM

    df_input_file["four"] = df_input_file["four"].fillna("club")
    print("replace nan values with the 'club' string in column four:")
    print(df_input_file)
    print()
    #    one   two  three   four   five       six    seven eight
    # 0  4.0  2.10    3.1    bar   True       NaN  £200.45   BMC
    # 1  4.0  2.36    3.2   club  False  1/1/2017  £650.38   ACS
    # 2  3.0  2.30    3.3   club   True  2/1/2017   £85.07   ACS
    # 3  5.0  2.40    3.3    bar    NaN  3/1/2017      NaN   BPS
    # 4  4.0  2.50    3.5    bar  False       NaN  £230.22   BMC
    # 5  6.0  2.36    3.3   club   True  2/1/2017  £650.96   CJS
    # 6  2.0  2.50    3.3  house    NaN  4/1/2017      NaN    FM

    df_input_file["five"] = df_input_file["five"].fillna(True)
    print("replace nan values with the true boolean in column five:")
    print(df_input_file)
    print()
    #    one   two  three   four   five       six    seven eight
    # 0  4.0  2.10    3.1    bar   True       NaN  £200.45   BMC
    # 1  4.0  2.36    3.2   club  False  1/1/2017  £650.38   ACS
    # 2  3.0  2.30    3.3   club   True  2/1/2017   £85.07   ACS
    # 3  5.0  2.40    3.3    bar   True  3/1/2017      NaN   BPS
    # 4  4.0  2.50    3.5    bar  False       NaN  £230.22   BMC
    # 5  6.0  2.36    3.3   club   True  2/1/2017  £650.96   CJS
    # 6  2.0  2.50    3.3  house   True  4/1/2017      NaN    FM

    now = datetime.datetime.now().strftime("%m/%d/%Y")
    df_input_file["six"] = df_input_file["six"].fillna(str(now))
    df_input_file["six"] = pd.to_datetime(df_input_file["six"])
    print("replace nan values with the current date in column six:")
    print(df_input_file)
    print()
    #    one   two  three   four   five        six    seven eight
    # 0  4.0  2.10    3.1    bar   True 2023-11-15  £200.45   BMC
    # 1  4.0  2.36    3.2   club  False 2017-01-01  £650.38   ACS
    # 2  3.0  2.30    3.3   club   True 2017-02-01   £85.07   ACS
    # 3  5.0  2.40    3.3    bar   True 2017-03-01      NaN   BPS
    # 4  4.0  2.50    3.5    bar  False 2023-11-15  £230.22   BMC
    # 5  6.0  2.36    3.3   club   True 2017-02-01  £650.96   CJS
    # 6  2.0  2.50    3.3  house   True 2017-04-01      NaN    FM

    df_input_file["seven"] = df_input_file["seven"].fillna("£0.0")
    print("replace nan values with the £0.0 in column seven:")
    print(df_input_file)
    print()
    #    one   two  three   four   five        six    seven eight
    # 0  4.0  2.10    3.1    bar   True 2023-11-15  £200.45   BMC
    # 1  4.0  2.36    3.2   club  False 2017-01-01  £650.38   ACS
    # 2  3.0  2.30    3.3   club   True 2017-02-01   £85.07   ACS
    # 3  5.0  2.40    3.3    bar   True 2017-03-01     £0.0   BPS
    # 4  4.0  2.50    3.5    bar  False 2023-11-15  £230.22   BMC
    # 5  6.0  2.36    3.3   club   True 2017-02-01  £650.96   CJS
    # 6  2.0  2.50    3.3  house   True 2017-04-01     £0.0    FM

    df_input_file["seven"] = df_input_file["seven"].map(lambda x: str(x)[1:])
    print("remove the first character (English pound symbol) in column seven:")
    print(df_input_file)
    print()
    #    one   two  three   four   five        six   seven eight
    # 0  4.0  2.10    3.1    bar   True 2023-11-15  200.45   BMC
    # 1  4.0  2.36    3.2   club  False 2017-01-01  650.38   ACS
    # 2  3.0  2.30    3.3   club   True 2017-02-01   85.07   ACS
    # 3  5.0  2.40    3.3    bar   True 2017-03-01     0.0   BPS
    # 4  4.0  2.50    3.5    bar  False 2023-11-15  230.22   BMC
    # 5  6.0  2.36    3.3   club   True 2017-02-01  650.96   CJS
    # 6  2.0  2.50    3.3  house   True 2017-04-01     0.0    FM

    df_input_file["eight"].replace(to_replace=dict(BMC="BioMed Central",
                                                   ACS="American Chemical Society",
                                                   BPS="Biophysical Society",
                                                   CJS="Cadmus Journal Services",
                                                   FM="Frontiers Media"), inplace = True)
    print("substitute the abbreviation in column eight:")
    print(df_input_file)
    print()
    #    one   two  three   four   five        six   seven                      eight
    # 0  4.0  2.10    3.1    bar   True 2023-11-15  200.45             BioMed Central
    # 1  4.0  2.36    3.2   club  False 2017-01-01  650.38  American Chemical Society
    # 2  3.0  2.30    3.3   club   True 2017-02-01   85.07  American Chemical Society
    # 3  5.0  2.40    3.3    bar   True 2017-03-01     0.0        Biophysical Society
    # 4  4.0  2.50    3.5    bar  False 2023-11-15  230.22             BioMed Central
    # 5  6.0  2.36    3.3   club   True 2017-02-01  650.96    Cadmus Journal Services
    # 6  2.0  2.50    3.3  house   True 2017-04-01     0.0            Frontiers Media

    x = df_input_file.drop(labels="eight", axis=1)
    print("x: labels by dropping column eight:")
    print(x)
    print()
    #    one   two  three   four   five        six   seven
    # 0  4.0  2.10    3.1    bar   True 2023-11-15  200.45
    # 1  4.0  2.36    3.2   club  False 2017-01-01  650.38
    # 2  3.0  2.30    3.3   club   True 2017-02-01   85.07
    # 3  5.0  2.40    3.3    bar   True 2017-03-01     0.0
    # 4  4.0  2.50    3.5    bar  False 2023-11-15  230.22
    # 5  6.0  2.36    3.3   club   True 2017-02-01  650.96
    # 6  2.0  2.50    3.3  house   True 2017-04-01     0.0
    x = df_input_file.iloc[:, 0:6].values
    print("x: labels selection by using index location method iloc():")
    print(x)
    print()
    # [[4.0 2.1 3.1 'bar' True Timestamp('2023-11-15 00:00:00')]
    #  [4.0 2.3600000000000003 3.2 'club' False
    #   Timestamp('2017-01-01 00:00:00')]
    #  [3.0 2.3 3.3 'club' True Timestamp('2017-02-01 00:00:00')]
    #  [5.0 2.4 3.3 'bar' True Timestamp('2017-03-01 00:00:00')]
    #  [4.0 2.5 3.5 'bar' False Timestamp('2023-11-15 00:00:00')]
    #  [6.0 2.3600000000000003 3.3 'club' True Timestamp('2017-02-01 00:00:00')]
    #  [2.0 2.5 3.3 'house' True Timestamp('2017-04-01 00:00:00')]]

    y = df_input_file["eight"]
    print("y: target selection by column eight:")
    print(y)
    print()
    # 0               BioMed Central
    # 1    American Chemical Society
    # 2    American Chemical Society
    # 3          Biophysical Society
    # 4               BioMed Central
    # 5      Cadmus Journal Services
    # 6              Frontiers Media
    # Name: eight, dtype: object

    y = df_input_file.iloc[:, 7].values
    print("y: target selection by using index location method iloc():")
    print(y)
    print()
    # ['BioMed Central' 'American Chemical Society' 'American Chemical Society' 'Biophysical Society' 'BioMed Central' 'Cadmus Journal Services'  'Frontiers Media']
    df_input_file.to_csv(output_file_path, encoding="latin1")
    print("the output file has been created successfully:")
    print(output_file_path)
    print()
    # D:/IU University/2023/Programming with Python/Examples/Unit4\output_data.csv
if __name__ == '__main__':
    main()