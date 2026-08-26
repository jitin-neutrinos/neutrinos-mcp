# Handle Errors

<https://documentation.neutrinos.com/articles/#!studio-guide-7/configure-error-hint>

## 

Here's how you can handle errors and hints in your application.

### Handle Errors

#### Global Error Handling using Angular

Angular provides a hook for centralized exception handling with ErrorHandler. The default implementation of ErrorHandler prints error messages to the console. We can modify this behavior by creating a class that implements the ErrorHandler:

```javascript
import { ErrorHandler } from '@angular/core';@Injectable()export class GlobalErrorHandler implements ErrorHandler {    handleError(error) {    // your custom error handling logic      }}
```

We can then provide it in our root module to change the default behavior in our application. Instead of using the default ErrorHandler class, you can use your own class like this:Copy CodeJavaScript@NgModule({
 providers: [{provide: ErrorHandler, useClass: GlobalErrorHandler}]
})
Now you will only have a single place to change the code for error handling.
Error Handling in ComponentsNeutrinos Studio allows you to handle errors when you use the Input, Select, and Date Picker components. To configure errors:Drag and drop an Input, Select, or Date Picker component to your app page.Double-click the component to open its attributes window.Click the** Errors **button to configure error messages.Enter a valid error condition and its associated message. Set the message alignment to **start** or** end**.Click **+Add **to add the configured error.Click** Save** to save the error, or click **+ Add** to configure another error.Example: To display an error message if the user enters the current date less than today's date:![Configuring error message](/resources/Storage/studio-guide-7/error_date.png)TS implementation:Copy CodeJavaScriptexport class DatepickerOverviewExample {
 selectedDate;
 currentDate = new Date().getTime();
 isValid() {
 console.log(new Date(this.selectedDate).getTime() > this.currentDate);
 return new Date(this.selectedDate).getTime() > this.currentDate
 }
}
Configure HintsHints are used to give specific information about some data, action, or page in an application. Once added, they appear as a snack bar in your application. To configure hints:Drag and drop an Input, Select, or Date Picker component to your app page.Double-click the component to open its attributes window.Click the** Hints **button to configure hints.Enter a valid hint condition and its associated message. Set the message alignment to **start** or** end**.Click **+ Add** to add the hint.**Save** to save the hint, or click **+ Add** to configure another hint.Example:![Configure Hints](/resources/Storage/studio-guide-7/hint.png)
