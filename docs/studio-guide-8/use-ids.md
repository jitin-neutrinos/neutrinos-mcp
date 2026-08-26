# 1. Update the Environment Properties

<https://documentation.neutrinos.com/articles/#!studio-guide-8/use-ids>

After configuring the IDS, you should enable and use the IDS in your application. Perform the following steps:

#### 1. Update the Environment Properties

Navigate to the Environments editor, and change the** isIDSEnabled **property to** true**. This is required for the client module to enable the request to start authentication.

#### 2. Use the Oauth Module

Use the
 methods and properties from the [N](/smart/project-concepts/neutrinos-oauth-module)
[eutrinos OAuth Client](/smart/project-concepts/neutrinos-oauth-module)

 [module](/smart/project-concepts/neutrinos-oauth-module) to interact with your configured IDS. This is how you use them in your application pages:

authState()

To subscribe to the authState() method in the **ngOnInit** lifecycle, enter the following code in the **Script **node of the [On Init flow](/smart/project-page-services-designer-guide/on-init-flow):

```javascript
this.page.authSubscribe = bh.system.oauthService.authState().subscribe(state =>  {    // Perform user friendly action when session becomes invalid    this.page.authState = state;    alert(JSON.stringify(state));    console.log(this.page.authState); })
```

---

login()

To authenticate users while logging into the app, create a page flow and bind it to a component's attribute:

1. Drag and drop a **Start **node and add a name. For example, **login**.
2. Drag and drop a Script node and call the bh.system.oauthService.login();  method to authenticate the user.
3. If you want to redirect the user to a different page post login, use bh.system.oauthService.login('<path_name>'), and replace <path_name> with the name of the path that you have entered for the page on the **Routes** editor.
4. On the Page UI, [bind the page flow to a component's attribute](/articles/studio-guide-8/bind-page-flows-to-components). For example, drag and drop a **Button** and bind the** login** flow to the (click) attribute of the button.

| ![Information](/resources/Storage/studio-guide-8/info.png) | If you do not want to create a login page manually, you can import the [Neutrinos Login Template](/smart/project-components-documentation-copy/neutrinos-login-templates) while creating the app. This template is configured with the Neutrinos oAuth Strategy by default to authenticate your app users. By default, the** webAppMountPoint** property from the Environments Editor is added to the redirect path. It has the default value as **web**. This is required as the Server Services Designer also serves the Client app. If you want to deploy the Client and Server Services separately, then update the **webAppMountPoint** value to '** /**' in the editor. |
| --- | --- |

---

logout()

To log a user out, create a page flow and bind it to a component's attribute:

1. Drag and drop a **Start **node and add a name. For example, **logout**.
2. Drag and drop a **Script** node and call the bh.system.oauthService.logout(); method to log the user out.
3. If you want to redirect the user to a different page post logout, use bh.system.oauthService.logout('<path_name>'), and replace <path_name> with the name of the path that you have entered for the page on the **Routes** editor. For example, to redirect to the login page, use: Copy CodeJavaScriptbh.system.oauthService.logout('login').then((logout) => {
    console.log(logout);
   }).catch(err => {
    console.error(err);
   });
4. On the Page UI, [bind the page flow to a component's attribute](/articles/studio-guide-8/bind-page-flows-to-components). For example, drag and drop a **Button** and bind the** logout** flow to the (click) attribute of the button.

---

authSubscribe

To save and destroy the user subscription, use this.page.authSubscribe and this.page.authSubscribe.unsubscribe() respectively. For example, drag and drop the [On Destroy](/smart/project-page-services-designer-guide/on-destroy-node) node. Connect it to a **Script** node and enter the following code to destroy the user subscription:

```javascript
if (this.page.authSubscribe) {    alert("Subscription Destoyed");    console.log("Unsubscribe executing!");    this.page.authSubscribe.unsubscribe();}
```

---

userInfo

To fetch or display the information of the currently logged-in user, use page.system.oauthService.userInfo.

---

isLoggedIn

To check if the user has logged in to the application, use page.system.oauthService.isLoggedIn.

#### 3. Protect Your Route

In the** Routes** editor, enable the NeutrinosAuthGuardService on the route that is to be authorized before user access. You usually call this service on the **Home** page of the application. Once called, the AuthGuard service takes care of user authentication on that page based on the OAuth methods defined in the application.
