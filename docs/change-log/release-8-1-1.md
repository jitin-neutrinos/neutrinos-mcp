# Release 8.1.1

<https://documentation.neutrinos.com/articles/#!change-log/release-8-1-1>

**8.1.1**

**Date: 2022-02-02**

**Features**

- Updated flex layout dependency in seed app.

**Bug Fixes**

- Cmd ![](/resources/Storage/change-log/get-started-2022-02-03.png) +A does not work in mac for input/text fields of the attributes window.
- Deleting a legacy page and creating a new page with the same name breaks the view.
- Application was breaking for certain service names.
- HTTP Request with bearer token authentication fails due to incorrect variable password being used instead of token.
- **[IDS](/smart/project-concepts/identity-server) Mobile - **Not redirecting back to the application after login. To fix this issue, we have added Content-Security-Policy (CSP) headers in the in Login Callback API and Logout Callback API of [IDS](/articles/concepts-publication/identity-server) Server flows.
- Removed fxHide property from the default property for Row and Column UI Components as similar functionality can be achieved by using fxShow (existing default property).
- Http request in the [Client Services Designer](/articles/concepts-publication/client-services-designer) (CSD) throws async error for observer property is toggled on.
