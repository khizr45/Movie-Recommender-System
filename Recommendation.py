import pickle
from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

with open('cosine_similarities.pickle', 'rb') as f:
     cosine_similarities_pickle = pickle.load(f)

with open('MOVIES-TITLE.pickle', 'rb') as f:
     movies_series = pickle.load(f)

movies = movies_series.tolist()
cosine_similarities = cosine_similarities_pickle.tolist()

@app.route('/api/recommendMovies', methods=['POST'])
def RecommendMovies():
    watchedMovies = request.get_json().get('watchedMovies',[])
    if len(watchedMovies) == 0:
        return jsonify([])
    recommended_movies = []
    recommended_cosine = []
    tempWatched = watchedMovies

    for movie in watchedMovies:
        index = movies.index(movie)
        tempMovies = movies
        cos_movie = cosine_similarities[index]

        sorted_indices = sorted(range(len(cos_movie)), key=lambda i: cos_movie[i],reverse=True)
        cos_movie = [cos_movie[i] for i in sorted_indices]
        tempMovies = [tempMovies[i] for i in sorted_indices]

        count = 1
        while count != 5:
            if tempMovies[count] not in recommended_movies:
                recommended_movies.append(tempMovies[count])
                recommended_cosine.append(cos_movie[count])
                count += 1

    sorted_indices = sorted(range(len(recommended_cosine)), key=lambda i: recommended_cosine[i],reverse=True)
    recommended_cosine = [recommended_cosine[i] for i in sorted_indices]
    recommended_movies = [recommended_movies[i] for i in sorted_indices]

    returnRecommended = []
    for i in range(len(recommended_movies)):
        if recommended_movies[i] not in watchedMovies:
            returnRecommended.append(recommended_movies[i])


    return jsonify({"recommended movies": returnRecommended})


if __name__ == '__main__':
    app.run(debug=True)