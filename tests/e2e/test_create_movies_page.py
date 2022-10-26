from flask.testing import FlaskClient
#Completed to the best of my knowledge: Marcel Newman
def test_home_page(test_app: FlaskClient):
    response = test_app.post('/movie',data={"movie_title":"Jump In",
    "movie_director":"Tu Sans","movie_rating":2})
    response_data = response.data
    assert response.status_code == 200
    assert response_data["movie_title"] == "Jump In"