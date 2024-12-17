from flask import Flask
from routes import configure_routes

app = Flask(__name__)

# Register routes
configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
