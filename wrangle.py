import pandas as pd
import numpy as numpy

from sklearn.model_selection import train_test_split
import sklearn.preprocessing

############################# Acquire Movies Data ############################# 

def get_movies_data():
    '''
    This function will pull the dataset from the provided .csv file 
    and will write it to a pandas dataframe. 
    
    To reproduce the results, you will need the movies_metadata.csv file in your working directory.
    '''
    df = pd.read_csv('movies_metadata.csv')
    
    return df




############################# Prepare Movies Data ############################# 

# defines function to clean movies data and return as a cleaned pandas DataFrame
def clean_movies(df):
    '''
    clean_movies will take one argument df, a pandas dataframe and will:
    set id as new index,
    drop unnecessary columns and columns with too many null values,
    grab the features needed to address initial hypotheses,
    fill in values with very little nulls,
    fix errors in order to change popularity and budget dtypes,
    convert data types to integers
   
    return: a single pandas dataframe with the above operations performed
    '''
  
    #set id as index
    df = df.set_index("id")

    #removing unnecessary columns and cols with too many nulls and features not needed for project
    df = df.drop(['belongs_to_collection', 
                'homepage', 
                'overview', 
                'poster_path', 
                'imdb_id', 
                'original_title', 
                'adult', 
                'original_language', 
                'production_companies', 
                'production_countries', 
                'runtime',
                'spoken_languages', 
                'tagline',
                'video',
                'release_date',
                'title',
                'genres',
                'status'], axis=1)


    #fill in values w/ very little nulls
    df = df.fillna(0)

    #replacing due to getting an error from converting popularity and budget cols to float
    df.replace('Beware Of Frost Bites',0, inplace = True)
    df.replace('/ff9qCepilowshEtG2GYWwzt2bs4.jpg',0, inplace = True)
    df.replace('/zV8bHuSL6WXoD6FWogP9j4x80bL.jpg',0, inplace = True)
    df.replace('/zaSf5OG7V8X8gqFvly88zDdRm46.jpg',0, inplace = True)

    #convert dtypes to integers
    df.popularity = df.popularity.astype('float64')
    df.revenue = df.revenue.astype('float64')
    df.budget = df.budget.astype('float64')


    return df



# splits a dataframe into train, validate, test 
def split(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames.
    return train, validate, test DataFrames.
    '''
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123)
    return train, validate, test





# defines MinMaxScaler() and returns scaled data
def Min_Max_Scaler(X_train, X_validate, X_test):
    """
    Takes in X_train, X_validate and X_test dfs with numeric values only
    makes, fits, and uses/transforms the data,
    
    Returns X_train_scaled, X_validate_scaled, X_test_scaled dfs 
    """

    #make and fit
    scaler = sklearn.preprocessing.MinMaxScaler().fit(X_train)

    #use and turn numpy arrays into dataframes
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), index = X_train.index, columns = X_train.columns)
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate), index = X_validate.index, columns = X_validate.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), index = X_test.index, columns = X_test.columns)
    
    return X_train_scaled, X_validate_scaled, X_test_scaled