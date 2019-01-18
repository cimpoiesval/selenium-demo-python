## Preconditions

    1. python (3.6.4 or higher)
    2. pip

## How to run

    1. unzip the drivers/drivers.zip in the same folder
    2. install dependencies: pip install -r requirements.txt
    3. run all tests on the default browser (chrome): pytest
    4. run a specific test file: pytest test_cases.py
    5. run on a specific browser: pytest --browser=firefox
    6. run tests and save results in a html report: pytest --html=report.html