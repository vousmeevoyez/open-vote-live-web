run:
	gunicorn -b 0.0.0.0:5002 -w 2 manage:app
