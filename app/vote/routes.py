from os import environ
from flask import render_template, redirect, request, url_for

from app.vote import blueprint
from app.vote.modules.services import VoteServices

@blueprint.route('/live')
def index():
	# fetch all necessary information to make request
	username = environ.get("USERNAME")
	password = environ.get("PASSWORD")
	election_id = request.args.get('election_id')

	# fetch all candidates information from main back-end
	status, response = VoteServices(username, password).get_candidates(election_id)
	if status is not True:
		return response["message"]

	candidates = response['data']

	return render_template('index.html', candidates=candidates)
