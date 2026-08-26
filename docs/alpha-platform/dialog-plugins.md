# Package Information

<https://documentation.neutrinos.com/articles/#!alpha-platform/dialog-plugins>

A comprehensive dialog system for Alpha UI Base that provides modal dialogs, page rendering, and dynamic content management with support for global pages, project-specific content, and multi-language support.

### Package Information

- Name: alpha-module-dialog
- Version: 1.0.3
- Description: Display a dialog box with dynamic content rendering
- Exposed Name: dialog

### Features

- Dynamic Dialog Creation: Create dialogs with dynamic content from Alpha pages
- Global Page Support: Support for both project-specific and global pages
- Multi-language Support: Built-in internationalization capabilities
- Flexible Sizing: Configurable height and width (percentage-based)
- Header Customization: Optional dialog headers with trimming
- Multiple Dialog Management: Support for multiple concurrent dialogs

### API Reference

#### Core Methods

1. open(config): Opens a new dialog with the specified configuration.
    Parameters:
    Copy CodeJavaScriptinterface DialogConfig {
    page: {
    pageId: string;
    type: string;
    };
    height?: string; // Height as percentage (default: '50%')
    width?: string; // Width as percentage (default: '50%')
    header?: string; // Optional dialog header
    url?: string; // Custom URL for page fetching
    pageType?: string; // Page type (page, dialog, global)
   }
    Returns: Promise
    Throws: Error if the required configuration is missing.
2. close(dialogId): close(dialogId)
    Parameters:
    Returns: void
  - Closes a specific dialog by ID.
3. closeAll(): Closes all open dialogs.
    Returns: void

### Usage Examples

#### Basic Dialog

```javascript
// Open a simple dialogawait ap.dialog.open({  page: {    pageId: 'user-form',    type: 'page'  },  height: '60%',  width: '70%',  header: 'User Information'});
```

#### Global Page Dialog

```javascript
// Open a dialog with global page contentawait ap.dialog.open({  page: {    pageId: 'help-content',    type: 'global'  },  height: '80%',  width: '90%',  header: 'Help & Documentation'});
```

#### Custom Configuration

```javascript
// Open dialog with custom configurationawait ap.dialog.open({  page: {    pageId: 'custom-dialog',    type: 'dialog'  },  height: '40%',  width: '50%',  header: 'Custom Dialog',  url: '/custom/pages/fetch'});
```

#### Dialog Management

```javascript
// Close specific dialogap.dialog.close('dialog-123');// Close all dialogsap.dialog.closeAll();
```

### Page Types

1. Task Page (type: 'page')
  - Scope: Task-specific pages
  - Content: Task-specific pages
2. Dialog Pages (type: 'dialog')
  - Scope: Page type popup
  - Content: Modal-specific content and forms
  - Use Cases: Confirmation dialogs, quick forms
3. Global Pages (type: 'global')
  - Scope: Global pages
  - Content: Help, documentation, system pages
