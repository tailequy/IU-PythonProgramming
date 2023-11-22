#The DataFrame can accept many different kinds of input data such as 1D or 2D NumPy
#arrays, lists, dictionaries, tuples, structured or record ndarray, a series, or another DataFrame.
import numpy as np
import pandas as pd
def main():
    # create a dataframe from a dictionary
    dictionary = {"col 1":[1., 2., 3., 4., 5.],
                  "col 2":[6, 7, 8, 9, 10],
                  "col 3":["uno", "dos", "tres", "cuatro", "cinco"]}
    df_data = pd.DataFrame(data=dictionary)
    print(df_data)
    #The indexes can be defined with text row numbers.
    # create a dataframe from a dictionary with text row numbers indexes
    df_data = pd.DataFrame(data=dictionary, index=["row1", "row2", "row3","row4", "row5"])
    print("A dataframe from a dictionary with text row numbers indexes:")
    print(df_data)
if __name__ == '__main__':
    main()