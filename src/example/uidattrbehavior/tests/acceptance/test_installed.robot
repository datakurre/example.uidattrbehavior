# bin/robot-server exampleuidattrbehavior.testing.UIDATTRBEHAVIOR_ROBOT_TESTING
# bin/robot src/example/uidattrbehavior/tests/acceptance/test_installed.robot

*** Settings ***

Resource  uidattrbehavior.robot

Test Setup  Open test browser
Test Teardown  Close all browsers

*** Test Cases ***

Plone is installed
    Go to  ${PLONE_URL}
    Page should contain  Powered by Plone
