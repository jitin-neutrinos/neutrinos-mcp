# Call an AuthGuard Services to Protect Application Routes

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/call-a-legacy-auth-guard-service-in-the-routes-editor>

AuthGuard is a service that is defined by the user to tell the router whether or not it should allow navigation to a requested route. It is useful when you need authentication and authorization-based control over the application pages. AuthGuard on Neutrinos implements the Angular interface CanActivate, to decide whether the user has access/permission to view a specific page/route in the application or not.

| ![Information](/resources/Storage/how-to-articles-8/info.png) | You create an AuthGuard service on Neutrinos Studio to authenticate users' access to application pages. To authorize the user on the login page, that is, to authorize a user to access the application, you configure an Identity Server for your app and use the default [NeutrinosAuthGuard](/smart/project-sample-how-to-guide/use-ids) Service. |
| --- | --- |

**Step 1: Create the service**

To define the AuthGuard service, you create a [legacy service](/smart/project-sample-how-to-guide/create-legacy-services) on the Studio Application Page. Perform the following steps:

1. On the side menu on the Studio Application page, select **Services > Legacy > Add New**. Add a service name of your choice.
2. Open the service, import the required dependencies, and define the canActivate() method. This method should return a boolean indicating whether or not navigation to a route should be allowed. The template of the canActivate() looks like this: Copy CodeJavaScriptimport { Injectable } from'@angular/core';
   import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from'@angular/router';
   import {Observable} from'rxjs';
   @Injectable({ providedIn: 'root' })
   export class AuthenticationGuardimplementsCanActivate
    {
   canActivate():boolean
    {
    // Write the business logic based on your app requirement.
    return true;
    }
    }
3. Save the changes.

**Step 2: Call the Service in the Routes editor**

After defining the service, you should call the service on the desired route. Perform the following steps:

1. Open the **Routes** editor by selecting **Routes** on the side menu of the Studio Application page.
2. Apply the AuthGuard to the routes you wish to protect. Enter the name of the AuthGuard service in the canActivate field and suffix it with the keyword 'Service'. For example, if the name of the service is **capabilityguard**, enter **capabilityguardService** in the canActivate field.
3. Similarly, apply the AuthGuard service to other routes you wish to protect based on the same business logic. The service will run any time someone tries to access the route. If the user is authenticated, they get to the route. If not, they are redirected away from the route.
