init:
	virtualenv -p python3 venv

install:
	pip install -r requirements.txt

build-docker:
	docker build -t rodrigobrito/backtrader .

run:
	docker run -ti -v`pwd`:/app -d -e ENVIRONMENT=production rodrigobrito/backtrader
