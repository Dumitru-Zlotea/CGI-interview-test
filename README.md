# CGI-interview-test

Set up a virtual environment:
`python -m venv venv`
`.\venv\Scripts\activate`

Add dependencies:
`python -m pip install Flask-2.2.2`
`python -m pip install "connexion[swagger-ui]==2.14.1"`

Run the server with `python app.py`

Postman url: `http://127.0.0.1:5000/counters/`

Run tests: `python -m unittest tests\test_file.py`
