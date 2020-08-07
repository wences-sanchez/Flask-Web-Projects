from flask import Flask

first_app = Flask(__name__)

@first_app.route('/')
def index():
	return 'Good morning, Sir Wences'

if __name__ == '__main__':
	first_app.run()
