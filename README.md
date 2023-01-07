# gudlift-registration

Install environment :

    - python -m venv env
    - env/Scripts/activate.ps1
    - pip install -r requirements.txt
    
Run project :
    
    - set FLASK_APP=server.py
    - $env:FLASK_APP = "server.py"
    - flask run
    
Tests :

    - you can run "pytest" to tests all unit, integrity and functional tests 
    
    - generate tests report with coverage :
        run "coverage run -m pytest tests " and then "coverage report" to generate all tests report except performance.
       
    - performance tests with locust :
        run "locust -f tests/tests_performance/locustfile.py" and then use "http://localhost:8089/" url

           
