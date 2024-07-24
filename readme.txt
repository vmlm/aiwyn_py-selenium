## Installation and Execution
Follow these steps to run the tests:
1. Install Python >~3.12

2. From a terminal window, go to the root of the project and run the corresponding configuration script:
    * Windows:  setup.bat
    * Linux/MacOS: setup.sh

3. Run Behave in the same terminal, by writing "behave" and pressing enter.

Behave will run all tests specified in the features folder and produce the following:
a. A folder containing any screenshots taken during the tests.
b. A log of all the actions taken on the target website.

## Implementation
I've chosen to implement the tests as BDD feature scripts, relying on Python and the Behave BDD framework for the implementation. Using BDD feature scripts has two main advantages:
    1) It communicates, in natural language, what each test is meant to achieve. This comes in handy when communicating tests to non-technical stakeholders.
    2) It provides a framework in which test programmers (myself, other testers or developers in test) can quickly add more test specifications (as feature files) and testing logic (as step scripts).

Some more implementation details:
* I've defined separate scripts to manage the selenium webdriver and logger configuration, just to keep it separate and make it easier to call.
* The logger is set up in the environment.py script, before testing begins.
* The driver is set up the first time the target website is accessed in a given scenario. This allows me to specify different browser drivers and configurations for each scenario.
* The homepage URL is defined once, in environment.py

## Project Structure
The project is structured as follows:
aiwyn_py-selenium (root)
|-- features: contains gherkin feature files
|       |-- steps: contains python feature step implementations
|-- scripts: contains all auxiliary scripts.

After running the tests, the following additional directories are created:
aiwyn_py-selenium (root)
|-- results: contains test run reports
|       |-- {test timestamp}: a single test run report
|       |       |-- screenshots: screenshots generated during the test
|       |       |-- actions.log: A log of all action taken during the test.