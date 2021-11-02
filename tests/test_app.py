from src.app import *


website_path = "https://cs321-project3-website.herokuapp.com/"


def test_index():
	client = app.test_client()
	response = client.get("/index")
	assert response.status_code == 200  # success


def test_add():
	# creating a post request with data as if coming from form
	client = app.test_client()
	url = '/add'
	data = {'note1': 'New Note'}
	response = client.post(url, data=data)
	
	# making sure we got redirected, and the request didn't fail
	assert response.status_code == 302  # redirect

	# making sure the home page now includes the added test data
	response = client.get("/")
	webpage_text = response.get_data()
	assert b'New Note' in response.data



	# url = website_path + '/add'
	# myobj = {'visitor': 'New person'}

	# webpage = requests.post(url, data = myobj)

	# assert "New person" in webpage.text