from .main import lambda_handler

def test_authorizer_should_pass_with_correct_secret():

    event = {
        "headers": {
            "secret": "Jpx6GfKbCl2XsJR4I5l7VWO5hEZNVbJ5MFbf9K1SnVqjvDfnIaK4"
        }
    }
    response = lambda_handler(event, None)

    assert response == {
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "allow",
                    "Resource": "*"
                }
            ],
        },
    }

def test_authorizer_should_fail_with_invalid_secret():

    event = {
        "headers": {
            "secret": "INVALID-SECRET"
        }
    }
    response = lambda_handler(event, None)

    assert response == {
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": "deny",
                    "Resource": "*"
                }
            ],
        },
    }
