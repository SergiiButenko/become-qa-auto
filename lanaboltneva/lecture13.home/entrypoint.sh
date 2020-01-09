# run app in container and put it on background
python3 simple-app.py &
# set timeout 5 seconds before tests run
sleep 5
# run tests for app and put results in xml file path in container: output/test_results.xml
pytest test_home10.py -v --junitxml="output/test_results.xml"
