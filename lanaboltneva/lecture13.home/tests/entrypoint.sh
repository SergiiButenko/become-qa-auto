# run tests for app and put results in xml file path in container: output/test_results.xml
pytest test_home10.py -v --junitxml="/app/output/test_results.xml"
