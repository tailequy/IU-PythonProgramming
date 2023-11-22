#Pandas can be installed using “pip install pandas” or “conda install pandas”
#Series: one-dimensional labeled array
import numpy as np
import pandas as pd
def main():
    print("pandas version: {}".format(pd.__version__))
    #pandas version: 1.3.5
    # randn(): return a sample (or samples) from the standard normal distribution
    s_data = pd.Series(np.random.randn(5))
    print(s_data)
if __name__ == '__main__':
    main()
