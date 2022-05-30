# Crizon
My Playground

# Setup

# Install Python
1. Install latest python version from official site. (Python 3.10.4 at the time of writing)
2. Check if python is installed by running 
    ~py --version
3. If py is not recognised, make sure variables are set as expected.
4. Uninstall any older version of Python.

# Install Pip environment
1. Allows you to create isolated python runtime with isolated dependencies.
~pip3 install django

# Install Django in virtual environment
1. Navigate to your project directory.
2. Create virtual environment 
~py -m venv.venv 
3. Install Django
~pipenv install django
4. Activate virtual environment by running following on root directory
~.venv/Scripts/activate

# Local Server
1. Run following command on root directory
~python manage.py runserver
2. You can configure this on Pycharm Server configurations
3. Hit http://127.0.0.1:8000/playground/health/ to check health of your server.


# Setup after Git
py -m venv .venv
.venv/Scripts/activate
pipenv install --dev