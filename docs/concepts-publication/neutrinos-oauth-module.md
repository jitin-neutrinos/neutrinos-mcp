# OAuth Methods

<https://documentation.neutrinos.com/articles/#!concepts-publication/neutrinos-oauth-module>

The neutrinos-oauth-client module gives you access to all the OAuth methods and properties that you can use from your application to interact with your configured IDS.

#### OAuth Methods

- login(): Performs authentication while logging a user into the app. Based on the IDS strategies enabled, your login page will appear with different login options such as Google sign-in, Azure sign-in, etc.
    For web and mobile applications, post login, the user information is available with the userInfo property. For mobile applications, this method also returns a promise with the user information.

- logout(): Opens the IDS logout page and logs the user out. For mobile applications, this method returns a promise.
- authState(): Emits multiple events when a user session becomes invalid. This method can be used to notify the user about his/her active session and can prompt the user to log back into the app.

#### OAuth Properties

- userInfo: Gives information about the currently logged-in user. This is a read-only property.
- isLoggedIn: Checks if the user has logged in to the application. It returns True if the user has logged in. Else, returns False.
