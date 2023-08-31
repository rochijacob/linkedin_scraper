from linkedin import linkedin

# Define CONSUMER_KEY, CONSUMER_SECRET,
# USER_TOKEN, and USER_SECRET from the credentials
# provided in your LinkedIn application

# Instantiate the developer authentication class

authentication = linkedin.LinkedInDeveloperAuthentication(
                    '77w4cuq1ybug2a',
                    'DTIzUiVc1uT6d51b',
                    'http://localhost:8000',
                    linkedin.PERMISSIONS.enums.values()
                )

# Optionally one can send custom "state" value that will be returned from OAuth server
# It can be used to track your user state or something else (it's up to you)
# Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it

# authorization.state = 'your_encoded_message'

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

application.get_profile()