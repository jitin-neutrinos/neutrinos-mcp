# Package Information

<https://documentation.neutrinos.com/articles/#!alpha-platform/navigate-plugin>

A lightweight navigation service for Alpha UI Base that provides programmatic page navigation through the Alpha renderer system with event-driven architecture.

### Package Information

- Name: alpha-module-navigate
- Version: 1.0.0
- Description: Navigate plugin for programmatic page navigation
- Exposed Name: navigate

### Features

- Event-Driven Navigation: Uses custom events for seamless integration
- Alpha Renderer Integration: Works with Alpha's page rendering system
- Simple API: Clean and straightforward navigation interface
- Flexible Configuration: Support for both page ID and name-based navigation
- Non-blocking: Asynchronous navigation that doesn't block the UI

### API Reference

#### Main Function

navigate(config): Navigates to a specified page using the Alpha renderer system.

Parameters

- config (object): Navigation configuration object
- pageId (string): The ID of the page to navigate to
- name (string): The name of the page to navigate to

Returns: void




 Events Emitted: alpha-renderer:navigate-to-page

### Usage Examples

#### Basic Navigation

```javascript
// Navigate by page IDap.navigate({ pageId: 'user-profile' });// Navigate by page nameap.navigate({ name: 'dashboard' });
```

#### Navigation with Both Parameters

```javascript
// You can provide both pageId and nameap.navigate({   pageId: 'user-settings',   name: 'User Settings' });
```
