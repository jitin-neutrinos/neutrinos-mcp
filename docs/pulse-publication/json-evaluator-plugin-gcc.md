# Package Information

<https://documentation.neutrinos.com/articles/#!pulse-publication/json-evaluator-plugin-gcc>

A JSON evaluation and manipulation utility for Alpha UI Base that provides advanced JSON path expressions, dynamic value extraction, and object property manipulation using JSONata expressions and Lodash utilities.

### Package Information

- Name: alpha-module-json-evaluator
- Version: 1.0.0
- Description: Provides a JSON evaluator with advanced path expressions
- Exposed Name: jval

### Features

- JSONata Integration: Advanced JSON query language support
- Dynamic Path Evaluation: Complex JSON path expressions and transformations
- Asynchronous Operations: Promise-based value extraction for complex queries
- Synchronous Fallback: Fast synchronous operations for simple paths
- Path Cleaning: Automatic cleanup of mapping path strings
- Lodash Integration: Efficient object manipulation using Lodash utilities
- Error Handling: Graceful error handling with fallback values
- Flexible Path Formats: Support for various path notation styles

### API Reference

#### Main Class: Jval

#### Core Methods

1. get(object, path): Asynchronously gets the value at the specified path using JSONata expressions.
    Parameters:
    Returns: Promise <*> - Resolves to the value at the specified path
    Example:
    Copy CodeJavaScriptconst result = await ap.jval.get(data, 'users[age > 25].name');
  - object (Object): The object to extract values from
  - path (string): JSONata path expression
2. get_sync(object, path): Synchronously gets the value at the specified path using Lodash get.
    Parameters:
    Returns: * - The value at the specified path
    Example:
    Copy CodeJavaScriptconst result = ap.jval.get_sync(data, 'users.0.name');
  - object (Object): The object to extract values from
  - path (string): Simple dot notation path
3. set(object, path, value): Sets the value at the specified path in the object.
    Parameters:
    Returns: Object - The updated object
    Example:
   Copy CodeJavaScriptconst updated = ap.jval.set(data, 'users.0.status', 'active');
  - object (Object): The object to modify
  - path (string): Path where to set the value
  - value (*): Value to set

### Usage Examples

#### Basic Value Extraction

```javascript
const data = {
  users: [
    { name: 'John', age: 30, city: 'New York' },
    { name: 'Jane', age: 25, city: 'Los Angeles' }
  ]
};

// Extract specific values
const userName = await ap.jval.get(data, 'users[0].name');        // 'John'
const userAge = await ap.jval.get(data, 'users[1].age');         // 25
const allNames = await ap.jval.get(data, 'users.name');          // ['John', 'Jane']
```
