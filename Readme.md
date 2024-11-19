// create venv

python3 -m venv venv

// active venv for ubuntu

source venv/bin/activate

// move to root project

cd djproject

// freeze lib

pip freeze > requirements.txt

// install lib

pip install -r requirements.txt

// run docker compose

docker-compose up --build
