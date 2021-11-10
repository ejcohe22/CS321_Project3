from src.app import *
from src.note import Note


website_path = "https://cs321-project3-website.herokuapp.com/"
def test_index():
	with app.test_client() as test_client:
		response = test_client.get(website_path)
		assert response.status_code == 200  # success


def test_add():
	# creating a post request with data as if coming from form
	with app.test_client() as test_client:
		url = website_path + 'add'
		note = {"Note" : "new_note", "Priority" : "crazy_medium", "Tag" : "new_tag"}

		response = test_client.post(url, data=note, follow_redirects=True)
		#response = test_client.get(website_path)
		# making sure we got redirected, and the request didn't fail
		assert response.status_code ==  200 # redirect
		# making sure the home page now includes the added test data
		assert "new_note" in response.text
		assert "new_tag" in response.text

		



	# url = website_path + '/add'
	# myobj = {'visitor': 'New person'}

	# webpage = requests.post(url, data = myobj)

	# assert "New person" in webpage.text