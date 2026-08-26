# Package Information

<https://documentation.neutrinos.com/articles/#!pulse-publication/toasts-gcc>

A toast notification service for Alpha UI Base that provides conditional toast rendering, internationalization support, and dynamic message generation based on API responses and trigger results.

### Package Information

- Name: alpha-module-toast
- Version: 1.0.2
- Description: Display dynamic toast notifications with conditional logic
- Exposed Name: toast

### Features

- Conditional Toast Rendering: Show toasts based on API status codes and trigger results
- Internationalization: Built-in translation support with Handlebars templating
- Dynamic Message Generation: Toast content adapts based on context and data
- Multiple Toast Types: Support for status-based, dependency-based, and basic toasts

### API Reference

showToast(options): Direct method to show toast messages.

Parameters:

```javascript
interface ToastOptions {
  status: string;      // Toast status (success, error, warning, info)
  title: string;       // Toast title
  message: string;     // Toast message content
  duration?: number;   // Display duration in milliseconds
}
```

### Toast Configuration

#### Toast Types

1. Basic Toast (type: 'basic'): Always shows the toast regardless of context.
    Copy CodeJavaScript{
    type: 'basic',
    message: {
    summary: 'Information',
    detail: 'This is an informational message'
    }
   }

### Internationalization

#### Translation Support

The service automatically handles translations using Handlebars templating

```javascript
// Toast configuration with translation keys
{
  message: {
    summary: '{{lang.toast.success.title}}',
    detail: '{{lang.toast.success.message}}'
  }
}
```

### Usage Examples

#### Basic Usage

```javascript
// Show a simple toast
ap.toast.showToast({
  status: 'success',
  title: 'Success!',
  message: 'Operation completed successfully',
  duration: 5000
});
```
