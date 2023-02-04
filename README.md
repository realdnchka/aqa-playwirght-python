## Simple Python AQA Framework
### Overview:
- Playwright for UI Testing
- requests library for API testing
- Good structure :slightly_smiling_face:

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
pytest Tests
```

To run only API tests use following command:
```
pytest Tests/API_Tests
```

To run only UI tests use following command:
```
pytest Tests/UI_Tests
```
### Configuration:
In config.json you can see configuration of test:
- ``urls`` using for web/api urls
- ``url`` base url of website
- ``browser`` using to define browser, you can use ``webkit``, ``chrome``, ``firefox``, ``msedge``
- ``headless`` using to define headless mode of browser

### Feature plans:
- Docker support
- Beautiful HTML report for PMs :rofl: