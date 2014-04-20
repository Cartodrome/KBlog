"""KBlog app

Usage:
  app.py live
  app.py dev
  app.py unit

Options:
  -h --help    Show this screen.

"""
from docopt import docopt
import warnings

from utils import get_logger
from pages import app

log = get_logger("app")

def start_unit_tests():
    warnings.warn("No unit tests")

def start_live_server():
    log.info("Starting live server.")
    app.run()

def start_dev_server():
    log.info("Starting DEV server.")
    app.run(debug=True, use_reloader=True)

if __name__ == "__main__":
    arguments = docopt(__doc__, version="KBlog 0.1")

    if arguments["unit"]:
        start_unit_tests()
    elif arguments["dev"]:
        start_dev_server()
    elif arguments["live"]:
        start_live_server()
    else:
        AssertionError("Webserver failed to start.")