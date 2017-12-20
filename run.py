# Run a test server.
from flask_blog import app
app.run(host='0.0.0.0', port=8090, debug=True)