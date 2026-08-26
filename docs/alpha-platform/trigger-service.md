# Features

<https://documentation.neutrinos.com/articles/#!alpha-platform/trigger-service>

The Alpha Module Trigger Service is a comprehensive trigger management system that handles various types of triggers including API calls, reels integration, CMS operations, DMS operations, dialogs, custom code execution, and page navigation. It provides a unified interface for managing complex workflow triggers in Alpha applications.

### Features

- API Triggers: Execute HTTP requests with authentication and error handling
- Reels Integration: Connect with Reels services using client credentials
- CMS Operations: Trigger CMS service functions
- DMS Operations: Trigger DMS service functions with validation tokens
- Case Service: Execute case service operations
- Custom Code Execution: Run custom JavaScript code with plugin dependencies
- Dialog Management: Trigger dialog operations
- Page Navigation: Handle navigation triggers
- Pagination Support: Built-in pagination handling for data operations
- Session Management: Access user and case instance data
- Error Handling: Comprehensive error handling with custom code execution

### Installation

This module is automatically available via the global ap object when using Alpha UI Base.

### Usage

Basic Trigger Execution

```javascript
// Execute a trigger actionconst result = await ap.trigger(action, params, triggerResult, emitLoaderEvent);// Example: API triggerconst apiAction = {  type: 'api',  config: {    url: 'https://api.example.com/data',    method: 'POST',    body: [{ key: 'name', value: 'John Doe' }]  }};const result = await ap.trigger(apiAction, { eventDetail: {} });
```

API Triggers

```javascript
// Simple API callconst apiConfig = {  type: 'api',  config: {    url: 'https://api.example.com/users',    method: 'GET',    headers: [      { key: 'Authorization', value: 'Bearer token' }    ]  }};const response = await ap.trigger(apiConfig, { eventDetail: {} });console.log(response.data);
```

Reels Integration

```javascript
// Reels service triggerconst reelsConfig = {  type: 'reels',  config: {    url: 'https://reels.example.com/data',    method: 'POST',    body: [      { key: 'query', value: 'search term' }    ]  }};const reelsResult = await ap.trigger(reelsConfig, { eventDetail: {} });
```

CMS Operations

```javascript
// CMS service triggerconst cmsConfig = {  type: 'cms',  config: {    module: 'content',    functionName: 'getArticles',    body: [      { key: 'category', value: 'technology' }    ]  }};const cmsResult = await ap.trigger(cmsConfig, { eventDetail: {} });
```

DMS Operations

```javascript
// DMS service triggerconst dmsConfig = {  type: 'dms',  config: {    module: 'documents',    functionName: 'uploadFile',    validator_token: 'token123',    body: [      { key: 'file', value: fileData }    ]  }};const dmsResult = await ap.trigger(dmsConfig, { eventDetail: {} });
```

Case Service Operations

```javascript
// Case service triggerconst caseConfig = {  type: 'case',  config: {    module: 'workflow',    functionName: 'startProcess',    body: [      { key: 'processId', value: 'proc_123' }    ]  }};const caseResult = await ap.trigger(caseConfig, { eventDetail: {} });
```

Custom Code Execution

```javascript
// Custom code triggerconst customCodeConfig = {  type: 'custom-code',  config: {    code: `      // Custom JavaScript code      const user = ap.user.get();      console.log('Current user:', user);            // Access trigger parameters      console.log('Params:', params);      console.log('Trigger result:', triggerResult);    `  }};await ap.trigger(customCodeConfig, { eventDetail: {} });
```

Dialog Operations

```javascript
// Dialog triggerconst dialogConfig = {  type: 'dialog',  config: {    dialogId: 'user-form',    options: {      title: 'User Information',      width: '500px'    }  }};const dialogResult = await ap.trigger(dialogConfig, { eventDetail: {} });
```

Page Navigation

```javascript
// Navigation triggerconst navigateConfig = {  type: 'navigate-to-page',  config: {    pageId: 'dashboard',    params: {      userId: '123',      tab: 'overview'    }  }};await ap.trigger(navigateConfig, { eventDetail: {} });
```
