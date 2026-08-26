# Configure App Navigation (Routes)

<https://documentation.neutrinos.com/articles/#!studio-guide-7/adding-routes>

You configure the app navigation (routes) using the **Routes editor**. On Neutrinos Studio, routes communicate to the application router about which view to display when a user clicks a link or pastes a URL into the browser's address bar. Using the Routes editor in the Studio application page, you can enable navigation from one page to another as you perform various tasks using the application. For every app you create on Neutrinos Studio, two routes are pre-configured for you. The default route for the landing page and a route to handle the unregistered route.In addition to this, when you create an app using a [template](/smart/project-concepts/app-templates), there are additional routes that are preconfigured based on the template that you select.![Routes editor](/resources/Storage/studio-guide-7/routes.png)
The **Routes** editor displays the following attributes:**Path: **The path of an application page that is to be displayed on the Browser's URL. For example, if the browser's URL is www.docs.neutrinos.com, you can set the path of this page to be add-routes. So, the complete URL to display this documentation topic will be www.docs.neutrinos.com/add-routes. The path can also be a wild card where:** matches any URL / loads the root path. **Page:** The application page to be displayed for the path entered in the Path field.**Data: **Additional developer-defined data provided to the page. By default, no additional data is passed to the page. For example, {pagetitle:"PROFILE EDITOR"}. **Path Match: ** Informs a router how to match and map a URL to the path of an actual route. Accepts full and prefix values. By default, the router checks URL elements from the left to see if the URL matches a given path and stops when there is a config match. Importantly there must still be a config match for each segment of the URL. For example, '/team/11/user' matches the prefix 'team/:id' if one of the route's children matches the segment 'user'. That is, the URL '/team/11/user matches the config {path: 'team/:id', children: [{path: ':user', component: User}]} but does not match when there are no children as in {path: 'team/:id', component: Team}`.The path-match strategy 'full' matches against the entire URL. It is important to do this when redirecting empty-path routes. Otherwise, because an empty path is a prefix of any URL, the router would apply the redirect even when navigating to the redirect destination, creating an endless loop.**RedirectTo: **The path of the page to which the user has to be redirected if the path matches. The redirect is absolute if the URL begins with a slash (/), otherwise, the redirect is relative to the path URL. Note that no further redirects are evaluated aft0er an absolute redirect. When no value is entered, the router does not redirect.**Resolve:** Resolves data via API or other sources before loading a route. Use this field to ensure certain data is loaded from an API response before the route is actually activated. For example, consider an application where, in a page, some elements are displayed spontaneously, but other elements are loaded after Observable is subscribed successfully which might take some time to render on UI. Here, Resolvers come to the rescue. They allow applications to retrieve data first from an API response before the component gets loaded, allowing for route navigation. In other words, to prefetch the data for a particular route before the component is loaded. **canActivate: **Uses the canActivate method's return value (a Boolean) to determine if the current user is allowed to activate a child of the route. By default, any user can activate a child. Use this template to define the canActivate method: Copy CodeJavaScriptimport { Injectable } from '@angular/core';
import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import {Observable} from 'rxjs';

@Injectable({ providedIn: 'root' })

export class AuthemticationGuard implements CanActivate {

 canActivate():boolean
 {
 return true;
 }
}See [Angular documentation](https://angular.io/api/router/CanActivate) to learn more. Also, see an [example on GitHub](https://github.com/cornflourblue/angular-8-basic-authentication-example/blob/master/src/app/_helpers/auth.guard.ts).**canDeactivate: **Uses the canDeactivate method's return value (a Boolean) to determine if the current user is allowed to deactivate a route. Use this template to define the canDeactivate method: import { Injectable } from '@angular/core';
import {CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import {Observable} from 'rxjs';

@Injectable({ providedIn: 'root' })

export class AuthemticationGuard implements CanDeactivate {

 canDeactivate():boolean
 {
 return true;
 }
}See [Angular documentation](https://angular.io/api/router/CanDeactivate#description) to learn more. Also, see an [example on GitHub](https://github.com/angular/angular/blob/master/aio/content/examples/router/src/app/can-deactivate.guard.1.ts).

Configuring Routes



 To configure a route, define the path of the route and select a Page. You can also create and configure nested routes, that is, a child route within a route to have a one-page view within another page. To create a child route, click ![Add a child route](/resources/Storage/studio-guide-7/arrow.png) next to the route.
Navigate to [Create Routes](/smart/project-tutorial-leave-management-system/create-routes-and-add-styles) to see an example.
