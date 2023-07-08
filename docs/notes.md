# Random Notes

The virtual environment

One time for all virtual environments, if it's not already installed.
``pip install virtualenv``

Create the virtual environment one time after the development environment has been cloned or downloaded. Objects that can be re-created are not checked into the source repository.
``virtualenv -p python3 .``
Restore the state of the development environment after it has been cloned or downloaded.
``pip install -r requirements.txt``

Activate virtual environment for development session.
``. bin/activate``
Deactivate the virtual enviroment when finished development.
``deactivate``

Run the application
``flask --app src/child --debug run``
or
```bash
export FLASK_APP=src/child
export FLASK_DEBUG=1
flask run
```
Access it from the web page
``firefox localhost:5000``

Save the state of the development environment. This should be done before committing changes if a library has been added or removed using pip.
``pip freeze > requirements.txt``



