# this.page.system.httpLoaderService

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/this-page-system-httploaderservice>

This service listens to HTTP requests and indicates its progress.

**Methods:**[isHTTPRequestInProgress()](/smart/project-service-designer-user-s-guide/system-httploaderservice/a/isHTTPRequestInProgress)[alertError()](/smart/project-service-designer-user-s-guide/system-httploaderservice/a/alertError)**Variable:**_isHTTPRequestInProgress$:This is an observable variable. You subscribe to this variable to listen to the start and end of the HTTP request-response cycle. It emits True when the HTTP request is sent and emits False when it returns a response.**Syntax:**Copy CodeJavaScript_isHTTPRequestInProgress$ → <Observable any>;isHTTPRequestInProgress()This method is used to trigger the _isHTTPRequestInProgress$ variable's values.
**Return type: **void**Syntax:**Copy CodeJavaScriptisHTTPRequestInProgress(bool: any) → {}alertError(error)This method shows a snack bar with an appropriate error message based on the error object that you input.PropertiesDescriptionerrorAn HTTP error object.**Return type: **void**Syntax:**Copy CodeJavaScriptalertError(error: any) → {}
