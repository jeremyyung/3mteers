all: db api gui
db:
	docker build -f ./docker-images/3m-mysql/dkrfile_sql -t 3m-mysql:1.0 .
api:
	docker build -f ./docker-images/3m-api/dkrfile_api -t 3m-api:1.0 .
gui:
	docker build -f ./docker-images/3m-gui/dkrfile_gui -t 3m-gui:1.0 .

