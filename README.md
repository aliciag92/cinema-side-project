# Predicting Movie Success
![Movies](https://image.shutterstock.com/image-vector/film-festival-260nw-8170690.jpg)
****

## About the Project

****

### Description and Goals

The motion picture industry is raking in more revenue than ever with its expansive growth. For this project, I was curious to find out two things:
- What are the top features/drivers of movie revenue?
- Could I be able to build a model that helps predict movie revenue?

The dataset I am working with consists of movies released on or before July 2017. Data points include cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts and vote averages.


### Objectives for this project include:
- Identifying the drivers of a movie's success based on its revenue.
- Documenting process and analysis throughout the data science pipeline.
- Demonstrating the information that was discovered.
- Deliverables:
    - README.md file containing overall project information, how to reproduce work, and notes from project planning.
    - [Jupyter Notebook Report](https://github.com/aliciag92/cinema-side-project/blob/main/movie-revenue-report.ipynb) detailing the pipeline process.
    - Python module that automates the data [wrangling](https://github.com/aliciag92/cinema-side-project/blob/main/wrangle.py).

****

### Data Dictionary

Feature      | Description   | Data Type
------------ | ------------- | ------------
budget | The budget of the movie in dollars | float
popularity | The Popularity Score assigned by TMDB | float
revenue | The total revenue of the movie in dollars | float
vote_average | The average rating of the movie | float
vote_count | The number of votes by users, as counted by TMDB | float

**** 

### Initial hypotheses
- Does vote count or vote average affect movie revenue?
- Do higher budget films bring more revenue?
- Do more popular movies bring in more revenue?


****

### Pipeline Process:
To take a peek at my planning process, you can view my Trello board by clicking [here](https://trello.com/b/qwVUJS23/alicias-side-project-prediction-of-movie-revenue-from-tmdb-dataset).

#### Plan
- Understand project description and goals. 
- Form hypotheses and brainstorm ideas.
- Have all necessary imports ready for project.


#### 1. Acquire
- Download dataset from [Kaggle](https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv).
- Move download to desired folder on personal device.
- Define function to get movie data from local csv and return as a pandas DataFrame.
- Read csv in notebook by using wrangle.py script.
- Function to acquire the data are included in [wrangle.py](https://github.com/aliciag92/cinema-side-project/blob/main/wrangle.py).
- Complete initial data summarization and plot distributions of individual variables to get to know data and know what is needed to be prepped/cleaned.

#### 2. Prepare
- Define functions to:
    - clean movie data and return as a cleaned pandas DataFrame.
    - split the dataframe into train, validate, test.
    - scale the data.
- Functions to prepare the data are included in [wrangle.py](https://github.com/aliciag92/cinema-side-project/blob/main/wrangle.py).

#### 3. Explore
- Address questions posed in planning and brainstorming and figure out drivers to predict movie revenue.
- Create visualizations of variables and run statistical tests (as many as needed).
- Summarize key findings and takeaways.

#### 4. Model/Evaluate
- Establish and evaluate a baseline model.
- Generate various regression algorithms with varying hyperparameters (as many as needed) and settle on the best algorithm by plotting residuals and comparing evaluation metrics.
- Choose the best model and test that final model on out-of-sample data.
- Summarize performance, interpret, and document results.

#### 5. Deliver
- - My OLS model specified parameters (normalize=True) and used all features in the data set. It had:
    - an RMSE of \$33,670,874.47 on training data
    - an RMSE of \$31,264,245.48 on validate data
    - r^2 of 0.77 on validate data
    - RMSE of \$29,124,148.98 on test data
    - r^2 of 0.76 on test data. 
- The r^2 value means that 76% of the variance in revenue could be explained by the features in the data set.
- The model outperformed baseline and did better than the other models so it should be used moving forward as it predicts revenue.

****

#### Next Steps
With more time, I would like to:
- prepare data even further by removing outliers, encoding variables, and/or adding new features.
- explore how genre, release date, language, runtime, and tagline also affect movie revenue.
- explore clusters, if any.


****

### Recreating Project
- To reproduce this project, download [wrangle.py](https://github.com/aliciag92/cinema-side-project/blob/main/wrangle.py) and [movie-revenue-report.ipynb](https://github.com/aliciag92/cinema-side-project/blob/main/movie-revenue-report.ipynb) in your working directory and follow the steps from the pipeline process above.
- You can always obtain more features, or remove the ones you do not want, do your own exploring, modeling, and evaluating to deliver any new information.

****