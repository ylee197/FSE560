# Project 3 - Movie Recommendation
Based on users' movie rating history, recommending a movie. 
1. Dependency
We need to install surprise and pandas
    - pip install scikit-surprise
    - pip install pandas

1. Two input datasets
* User history dataset - http://files.grouplens.org/datasets/movielens/ml-100k/u.data
    - 100,000 rows x 4 columns
    - features - user_id, item_id rating timestamp
* movie dataset - http://files.grouplens.org/datasets/movielens/ml-100k/u.item
    - 1682 rows x 24 columns
    - features - item_id, title, release_data, video_release_date, IMDb_URL and etc..

2. Model
We used a SVD model - Singular Value Decomposition algorithm model

3. Output
When we enter a user id, it shows top 5 movides with predicted rating.


