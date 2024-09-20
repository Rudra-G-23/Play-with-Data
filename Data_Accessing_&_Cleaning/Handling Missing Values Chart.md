### Handling Missing Values in a Real Dataset

1. **Visualize Missing Values:**

   First, we identify missing values visually using the `missingno` library:

   ```python
   # Import necessary library to visualize missing values
   import missingno as mnso 

   # Visualize missing values
   mnso.matrix(df)
   ```

2. **Calculate Missing Value Percentage:**

   After identifying missing value columns, calculate the percentage of missing values in each column to get a better understanding:

   ```python
   import pandas as pd

   # Function to calculate missing value percentage for each column
   def missing_value_percentage(df):
       # Calculate the percentage of missing values for each column
       missing_percentage = df.isnull().sum() / len(df) * 100
       return missing_percentage

   print(missing_value_percentage(df))
   ```

3. **Handling Missing Values - Decision Tree:**

   Once we have identified the missing values, we can handle them using the following decision tree:

   ```
                               Handle Missing Values
                                    │
             ┌──────────────────────┴──────────────────┐
             │                                         │
          Remove                                   Input/Output
                                                       │
                                                 ┌─────┴───────┐
                                                 │             │
                                          Univariate      Multivariate
                                                  │              │
                                         ┌────────┴───────┐      └─────────┬─────────┐
                                         │                │                │         │
                                  Numerical         Categorical          KNN       MICE
   ```

---

### Options for Handling Missing Data:

1. **Remove Missing Values:**

   If we want to remove rows or columns with missing values completely:

   ```python
   # Remove rows with any missing values
   df_cleaned = df.dropna()
   ```

2. **Impute Missing Values:**

   This is known as **Complete Case Analysis (CCA)**, where we assume that the data is **Missing Completely at Random (MCAR)**.

   - **Univariate Imputation** (One column has missing values):
     
     If the percentage of missing values (MCAR) is less than 5%, we can proceed with imputation.

   #### 2.1 **Numerical Data Imputation:**
   
   - **Mean/Median Imputation:**
   
     Replace missing numerical values with the mean or median of the column:
   
     ```python
     # Mean imputation
     df['column_name'].fillna(df['column_name'].mean(), inplace=True)
   
     # Median imputation
     df['column_name'].fillna(df['column_name'].median(), inplace=True)
     ```

   - **Arbitrary Value Imputation:**
   
     When data is **not randomly missing**, you can replace missing values with a constant, like -999 or another arbitrary value:
   
     ```python
     # Replace with an arbitrary value (e.g., -999)
     df['column_name'].fillna(-999, inplace=True)
     ```

   - **End of Distribution Imputation:**
   
     Replace missing values with a value at the end of the distribution (e.g., mean + 3*std):
   
     ```python
     # Replace with end of distribution
     end_value = df['column_name'].mean() + 3 * df['column_name'].std()
     df['column_name'].fillna(end_value, inplace=True)
     ```

   #### 2.2 **Categorical Data Imputation:**
   
   For categorical columns, ensure that the ratios before and after imputation remain close.

   - **Mode Imputation (Most Frequent Value):**
   
     Replace missing values with the most frequent value (mode):
   
     ```python
     df['categorical_column'].fillna(df['categorical_column'].mode()[0], inplace=True)
     ```

   - **Forward/Backward Fill:**
   
     Fill missing values with the next or previous value:
   
     ```python
     # Forward fill
     df['categorical_column'].ffill(inplace=True)
   
     # Backward fill
     df['categorical_column'].bfill(inplace=True)
     ```

   - **Random Imputation:**
   
     Replace missing values with randomly selected values from the existing non-missing values:
   
     ```python
     import numpy as np
     df['categorical_column'].fillna(np.random.choice(df['categorical_column'].dropna()), inplace=True)
     ```

   - **Missing Value Indicator:**
   
     Create a new column indicating whether the value was missing:
   
     ```python
     df['missing_indicator'] = df['categorical_column'].isnull().astype(int)
     ```

---

### 3. **Multivariate Imputation:**

   When multiple columns have missing values, you can use multivariate methods like **KNN** or **MICE**.

   #### 3.1 **KNN (K-Nearest Neighbors) Imputation:**

   The KNN algorithm identifies the "neighbors" based on other variables and imputes missing values accordingly. Formula for distance between neighbors is typically **Euclidean Distance**:

   ```python
   from sklearn.impute import KNNImputer

   # Initialize the KNN Imputer with k=5
   knn_imputer = KNNImputer(n_neighbors=5)

   # Apply KNN Imputation
   df_knn_imputed = pd.DataFrame(knn_imputer.fit_transform(df), columns=df.columns)
   ```

   #### 3.2 **MICE (Multiple Imputation by Chained Equations):**

   MICE handles missing data by performing multiple imputations in an iterative manner. The assumption is that the data is **Missing at Random (MAR)**.

   ```python
   from sklearn.experimental import enable_iterative_imputer
   from sklearn.impute import IterativeImputer

   # Initialize the MICE Imputer
   mice_imputer = IterativeImputer()

   # Apply MICE Imputation
   df_mice_imputed = pd.DataFrame(mice_imputer.fit_transform(df), columns=df.columns)
   ```

---

### Additional Notes:

- Before and after imputing, it is a good practice to visualize the distribution of the data again (especially for numerical data) to ensure the imputation method maintains the overall data characteristics.

