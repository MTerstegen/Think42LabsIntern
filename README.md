# Project Tasks
Task: 1) Predicting student marks. 2) Predicting movie success

Predicting movie success:
1. I got a database of 85 movies(2016) from a public database. This database(movies.csv) contains data about budget,gross revenue,rating, imdb score, imdb votes etc.
2. I added a few features to the dataframe by doing a sentiment analysis of Youtube trailers for these movies.(no. of views,likes,dislikes,comments,etc.) using the code in MovieTrailerData.py. The columns were then added to movies.csv and the updated database was saved in updated_movies.csv
3. I then fitted a linear regression model to predict the gross revenue using all the other features. This was done in MovieModel.py.

Predicting Student Marks:
1. I fitted a linear regression model to predict student marks using all the other features in student-performance.csv. This was done in PredictingStudentMarks.py.
