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

Nasir_watched = ['The Dark Knight','Inception','Star Wars: Episode V - The Empire Strikes Back']
getRecommendedMovies(Nasir_watched)