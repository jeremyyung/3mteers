all: hello bye
db:
	docker build -f ./docker-images/3m-mysql/dkrfile_sql -t 3m-mysql:1.0 .
api:
	docker build -f ./docker-images/3m-api/dkrfile_api -t 3m-api:1.0 .	

