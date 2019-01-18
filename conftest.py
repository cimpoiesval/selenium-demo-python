
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser can be: chrome or firefox"
    )
