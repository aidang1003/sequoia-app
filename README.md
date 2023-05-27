## Steps to install dependencies in a virtual environment

1.  Clone this repository to local computer

2.  If you already have a ./venv folder skip this step

    Create a new virtual environment

    - Windows: `python -m venv ./venv`
    - Mac: `python3 -m venv ./venv`

3.  Activate the new virtual environment

    - Windows:
      `.\venv\Scripts\activate`
    - Mac:
      `source ./venv/bin/activate`

4.  Install the dependencies

        `pip install -r requirements.txt`

## Best practices to maintain dependencies

- After adding a new python dependency run the freeze script at the .\ProfileUserEngine level to update the requirements.txt

      pip freeze > requirements.txt

- Run python files at the root level to avoid installing multiple `.venv` folders
  Example to run app.py:
  `C:Users\user\Sequoia\ProfileUserEngine> python .\backend\app.py`

## Run the repo

## Test the repo

- Use `**repr**' to return variables for every class - EXTREMELY helpful for testing
