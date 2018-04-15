import pandas
import json
import numpy as np
import requests

df = pandas.read_csv('C:\\Users\\Sagar\\Desktop\\Think42Labs\\movies.csv',encoding='latin-1' )            # Use a database of 85 movies from 2016 in movies.csv
movie_name_series = df['name']
google_api_key = 'AIzaSyC1_gsjeg5u4T_sOXQ1ZeGAWeXaBXxu6mU'
tmdb_api_key = '0e3738e4122c18de9bc2edb281a843c1'

df['Trailer_View_Count'] =  pandas.Series(0, index=df.index)                #Add new columns containing information from the Trailer using the Youtube API
df['Trailer_Likes_Count'] =  pandas.Series(0, index=df.index)
df['Trailer_Dislikes_Count'] =  pandas.Series(0, index=df.index)
df['Trailer_Comments_Count'] =  pandas.Series(0, index=df.index)

def TMDB_Call(movie):                                                       #Function to access the The Movie Database(TMDB) to get corresponding trailer id  for each movie
    movie_clean = movie.replace(" ","+")                                    
    tmdb_url = "https://api.themoviedb.org/3/search/movie?query="+movie_clean+"&api_key="+tmdb_api_key
    tmdb_url_obj = requests.get(tmdb_url)
    json_object = tmdb_url_obj.json()                                       #Access the json object for each and every movie on the TMDB database
    if len(json_object['results'])==0:
        return 0
    tmdb_movie_id = json_object['results'][0]['id']                         
    Yurl = 'http://api.themoviedb.org/3/movie/'+str(tmdb_movie_id)+'/videos?api_key='+tmdb_api_key
    Yurl_obj = requests.get(Yurl)
    Yjson_object = Yurl_obj.json()
    if len(Yjson_object['results'])==0 or len(Yjson_object['results'][0])==0 :
        return 0
    youtube_video_id=Yjson_object['results'][0]['key']
    return youtube_video_id

def Youtube_Statistics(id):                                                 #Function to access the trailer statistics given the video id 
    youtube_url = ("https://www.googleapis.com/youtube/v3/videos?part=statistics&key="+google_api_key+"&id="+str(id))
    youtube_response = requests.get(youtube_url)
    returnObj = json.loads(youtube_response.content)

    if 'viewCount' not in returnObj['items'][0]['statistics']:              
        viewCount = 0
    else:
        viewCount = str(returnObj['items'][0]['statistics']['viewCount'])
    if 'likeCount' not in returnObj['items'][0]['statistics']:
        likes = 0
    else:
        likes = str(returnObj['items'][0]['statistics']['likeCount'])
    if 'dislikeCount' not in returnObj['items'][0]['statistics']:
        dislikes = 0
    else:
        dislikes = str(returnObj['items'][0]['statistics']['dislikeCount'])
    if 'commentCount' not in returnObj['items'][0]['statistics']:
        comments = 0
    else:
        comments = str(returnObj['items'][0]['statistics']['commentCount'])
    return viewCount,likes,dislikes,comments

i = 0
for movie_name in movie_name_series:                                        # Iterate over each and every movie in the Pandas Series df['name']
    movie_id = TMDB_Call(movie_name)                                
    if movie_id ==0:
        continue
    a,b,c,d = Youtube_Statistics(movie_id)
    df.loc[i,'Trailer_View_Count'] =  a
    df.loc[i,'Trailer_Likes_Count'] =  b
    df.loc[i,'Trailer_Dislikes_Count'] =  c
    df.loc[i,'Trailer_Comments_Count'] =  d
    i = i +1 

df.to_csv('C:\\Users\\Sagar\\Desktop\\Think42Labs\\updated_movies.csv', sep=',', encoding='latin-1')    # Write the dataframe to the 'updated_movies.csv' file
    

