"""
This module is use to launch the deployement server.
"""

from web_site.app import app

if __name__ == "__main__":
    app.run(debug=False)