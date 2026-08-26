# Package Information

<https://documentation.neutrinos.com/articles/#!alpha-platform/http-plugins>

A comprehensive HTTP client module for Alpha UI Base that provides enhanced request/response handling with built-in hooks, error handling, and file upload support

### Package Information

- Name: alpha-module-http
- Version: 1.0.0
- Description: Provides HTTP request methods with advanced features
- Exposed Name: http

### Features

- Enhanced HTTP Client: Built on top of ky for modern HTTP requests
- Request/Response Hooks: Customizable before/after request handling
- File Upload Support: Specialized handling for file uploads
- Automatic Response Parsing: Smart content-type detection and parsing
- Request Tracking: Unique request IDs for debugging and monitoring
- Loader Events: Built-in loading state management
- Error Handling: Comprehensive error handling with custom events
- Session Management: Automatic unauthorized session handling

### API Reference

#### Main Function

http(url, options, isFile, emmitLoaderEvent): The main HTTP function that handles all types of requests.

Parameters:

- url (string | object): The target URL or environment configuration
- options (object): Request configuration options
- isFile (boolean, optional): Whether this is a file upload request (default: false)
- emmitLoaderEvent (boolean, optional): Whether to emit loader events (default: true)

Returns: Promise

#### Options Object

```javascript
interface HttpOptions {  path: string;                    // API endpoint path  parseResponseBody?: boolean;     // Whether to parse response body  url?: string;                    // Target URL (auto-set for non-file requests)  [key: string]: any;             // Additional request options}
```

### Usage Examples

#### Basic HTTP Request

```javascript
// Simple POST requestconst response = await ap.http('https://api.example.com', {  path: '/users',  method: 'POST',  body: { name: 'John', email: 'john@example.com' }});
```
