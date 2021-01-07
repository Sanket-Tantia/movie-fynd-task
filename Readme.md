HOW TO CLONE AND USE THE DJANGO APP
Step1: Create a virtualenv and activate it
Step2: Clone the repo using: git clone https://github.com/Sanket-Tantia/movie-fynd-task.git
Step3: Install the dependencies using command: pip install -r requirements.txt
Step4: Run the migrations and migrate using two commands: python manage.py makemigrations & python manage.py migrate
Step5: Load all the movies into database using custom command: python manage.py loadmovie
Step6: Start the localhost server: python manage.py runserver


Now the application is ready. To test the APIs, we can do it using POSTMAN:

To search for movies:
Movies can be searched using different parameters: name, director_name, genre_name, imdb_score, popularity

Get all movies: 
REQUEST TYPE: GET
URL: https://go-fynd-imdb.herokuapp.com/movie

Filter result or search by parameters:
REQUEST TYPE: GET
URL: https://go-fynd-imdb.herokuapp.com/movie?search={value}

e.g 
Search a particular movie by name
REQUEST TYPE: GET
URL: https://go-fynd-imdb.herokuapp.com/api/movie?search=vertigo

Search a particular movie by director name
REQUEST TYPE: GET
URL: https://go-fynd-imdb.herokuapp.com/api/movie?search=Alfred Hitchcock


Search a particular movie by genre
REQUEST TYPE: GET
URL: https://go-fynd-imdb.herokuapp.com/api/movie?search=Adventure

All search parameters are case insensitive


Admin Create A Movie:
Assuming the new data (json object) will follow the same pattern as the json object shared in json format.
REQUEST TYPE: POST
URL: https://go-fynd-imdb.herokuapp.com/movie
JSON BODY:
{
    "name": "The Office",
    "99popularity": 86.0,
    "imdb_score": 8.6,
    "director": {
        "name": "Sanket Tantia"
    },
    "genre": [
        {
            "name": "Comedy"
        }
    ]
}
HEADER: {
    Authorization: Token dc52f377ac61c3665888c4eac371ea3f99a6def0
}


Admin Update A Movie:
Assuming the update data (json object) will follow the same pattern as the json object shared in json format.
REQUEST TYPE: PUT
URL: https://go-fynd-imdb.herokuapp.com/movie
JSON BODY:
{
    "name": "The Office",
    "99popularity": 45.0,
    "imdb_score": 9.6,
    "director": {
        "name": "Sanket Tantia"
    },
    "genre": [
        {
            "name": "Sad"
        }
    ]
}
HEADER: {
    Authorization: Token dc52f377ac61c3665888c4eac371ea3f99a6def0
}



Admin Delete A Movie:
REQUEST TYPE: DELETE
URL: https://go-fynd-imdb.herokuapp.com/movie
JSON BODY:
{
    "name": "The Office"
}
HEADER: {
    Authorization: Token dc52f377ac61c3665888c4eac371ea3f99a6def0
}
