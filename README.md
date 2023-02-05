## Simple Python AQA Framework
### Overview:
- Playwright for UI Testing
- requests library for API testing
- Good structure :slightly_smiling_face:
- Logs

### Requirements:
- python 3+

### Install:
```
pip3 install -r requirements.txt
playwright install  
```

### Running:
To run all tests use following command:
```
pytest tests
```

To run only API tests use following command:
```
pytest tests/api_tests
```

To run only UI tests use following command:
```
pytest tests/ui_tests
```
### Configuration:
In config.json you can see configuration of test:
- ``urls`` using for web/api urls
- ``url`` base url of website
- ``browser`` using to define browser, you can use ``webkit``, ``chrome``, ``firefox``, ``msedge``
- ``headless`` using to enable headless mode of browser
- ``logging`` using to enable logging
- ``timeout`` using to set timeout in ms
### Feature plans:
- Docker support
- Parallelization
- Beautiful HTML report for PMs :rofl: