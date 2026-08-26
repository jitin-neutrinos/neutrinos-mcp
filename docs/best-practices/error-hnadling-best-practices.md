# Error Handling Best Practices

<https://documentation.neutrinos.com/articles/#!best-practices/error-hnadling-best-practices>

# Error Handling Best Practices

---

Error handling is a cornerstone of an enterprise application. Follow these best practices while handling errors in your application:

### Error Message

![Error handling](/resources/Storage/best-practices/error-handling.jpg)

Error messages matter and should. Have some meaning to help the user to move along. By showing an error message such as **“An error occurred”**, we are not telling the user what the problem is or how to resolve it.In comparison, if we instead show a message saying **“Sorry, you are offline”,** then the user knows what the error is. This is a bit better but it does not help them to resolve the error.An even better solution would be to tell them to turn on the wifi and give a link to the Wifi settings page. Remember that error handling is not a substitute for bad UX. That is, you should not have any expected errors. If a user can do something that throws an error, then fix it! Don’t let an error through just because you created a nice error message for it.

LoggingIf you don’t log errors, then only the user who runs into them knows about them. Saving the information is necessary to be able to troubleshoot the problem later. So, make sure you log the error messages.Error TrackingError tracking is the process of proactively identifying issues and fixing them as quickly as possible. This makes sure that you identify bugs in your web application before your end-users encounter them, and proactively log and monitor them.Using one of the front-end error tracking solutions such as Bugsnag, Sentry, TrackJs, and Rollbar, you can record and replay user sessions so that you can see for yourself exactly what the user has experienced.
In other words, a proper error tracking solution could alert you when an error occurs and provide insights into how to replicate/resolve the issue.
