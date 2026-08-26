# Update the Environment Properties

<https://documentation.neutrinos.com/articles/#!app-builder-s-user-guide/use-ids>

### Update the Environment Properties

Once you register the IDS client, navigate to the Environments editor, and change the** isIDSEnabled **property to** true**. This is required for the client module to enable the request to start authentication.

### NeutrinosAuthGuardService

After registering the IDS client, you can enable the NeutrinosAuthGuardService on any page in the **Routes** editor to check if the user has logged in, If not, you can explicitly call the login() method of the neutrinos-oauth-client module in the TS editor of a page to log the user in and create a user session.

### neutrinos-oauth-client Module

The neutrinos-oauth-client module gives you access to all the OAuth methods and properties that you can use from your application. These are the methods and properties using which you can interact with your configured IDS.

### Using the Auth Module

Once you configure IDS, save the configuration. Click **Okay** when you see the following message:

![](/resources/Storage/app-builder-s-user-guide/ODS_warning.png)

Next, create a page in Neutrinos Studio. To do that, click the **Add** option on the Studio Application page and select **Page**. Enter the name of the page in the **Enter a Page Name** dialog window.

Once the page is created, click the** Pages **option and select the page that you created. Click the **TS** icon to open the TypeScript editor of the page.

Import the neutrinos-oauth-client module on the page and inject it into a component. Copy CodeMarkdown//Importing the OAuth Module
import { NeutrinosOAuthClientService } from 'neutrinos-oauth-client';

//Injecting to a component
constructor(private bdms: NDataModelService,
public neutrinosOAuthClientService: NeutrinosOAuthClientService)
{
 super();
 this.mm = new ModelMethods(bdms);
}

Once you import and inject the module, you will have access to all the Neutrinos OAuth methods and properties such as:

### OAuth Methods

- login(): Performs authentication while logging a user into the app. Based on the IDS strategies enabled, your login page will appear with different login options such as Google sign-in, Azure sign-in, etc.
     For web and mobile applications, post login, the user information is available with the userInfo property. For mobile applications, this method also returns a promise with the user information.

- logout(): Opens the IDS logout page and logs the user out. For mobile applications, this method returns a promise.
- authState(): Emits multiple events when a user session becomes invalid. This method can be used to notify the user about his/her active session and can prompt the user to log back into the app.

### OAuth Properties

- userInfo: Gives information about the current logged in user. This is a read-only property.
- isLoggedIn: Checks if the user has logged in to the application. It returns True if the user has logged in. Else, returns False.

#### Examples

In the example below, the login() method opens the IDS login page to authenticate the user:

```markdown
login() {        this.neutrinosOAuthClientService.login().then(loggedin => {            // User logged in        }).catch(loginError => {            // Login error        });    }
```

In the example below, the logout() method opens the IDS logout page and logs the user out:

```markdown
logout() {        this.neutrinosOAuthClientService.logout().then(logoutSuccess => {            // User logged out        }).catch(logoutError => {            // User logout error        });    }
```

Using this example, you can subscribe to the authState() method in the **ngOnInit** lifecycle. You can unsubscribe to the method using the **ngOnDestroy** lifecycle.

```markdown
ngOnInit() {        this.authSubscribe = this.neutrinosOAuthClientService.authState().subscribe(state => {            // Perform user friendly action when session becomes invalid        });    }ngOnDestroy() {        if (this.authSubscribe) {            this.authSubscribe.unsubscribe();        }    }
```

| ![Information](/resources/Storage/app-builder-s-user-guide/info.png) | if you do not want to create a login page manually, you can import the [Neutrinos Login Template](/smart/project-components-documentation-copy/neutrinos-login-templates) while creating the app. This template is configured with the Neutrinos oAuth Strategy by default to authenticate your app users. |
| --- | --- |

### Redirecting Web App Users

**Redirecting app users post successful login:**

To redirect your web application users to a different page post login, perform the following steps:

1. In the TS editor of your page, enter the page name to which you want to redirect the user when you call the login() method. Example: Post login, redirecting the user to the **home** page. Copy CodeJavaScriptlogin() {
    this.neutrinosOAuthClientService.login('home')
    }
    ![Information](/resources/Storage/app-builder-s-user-guide/info.png)
    By default, the** webAppMountPoint** property from the Environments Editor is added to the redirect path. It has the default value as **web**. This is required as the Server Services Designer also serves the Client app. If you want to deploy the Client and Server Services separately, then update the **webAppMountPoint** value to '** /**' in the editor.
2. Configure the **Routes** editor with the page that you have called in the login() method.
    ![Routes editor](/resources/Storage/app-builder-s-user-guide/home_routes.png)

**Redirecting app users post logout:**

| ![Information](/resources/Storage/app-builder-s-user-guide/info.png) | This feature is available from version 7.1.0 of Neutrinos Studio. |
| --- | --- |

To redirect your web application users to a different page post logout, perform the following steps:

1. In the TS editor of your page, enter the page name to which you want to redirect the user when you call the logout() method. Example: redirecting the user to the **login** page post logout. Copy CodeJavaScript logout() {
    this.neutrinosOAuthClientService.logout('login')
    }
2. Configure the **Routes** editor with the page that you have called in the logout() method.
