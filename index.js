async function getRecommendedMovies(watchedMovies){
    const response = await fetch('http://localhost:5000/api/recommendMovies', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ watchedMovies }),
    });
    const data = await response.json();
    console.log(data)
}

let Nasir_watched = ['The Godfather','Pulp Fiction']
getRecommendedMovies(Nasir_watched)