# Features

<https://documentation.neutrinos.com/articles/#!alpha-platform/reels-datasource>

The Alpha Module Reels Datasource is a specialized data source handler for integrating with Reels services in Alpha applications. It provides a comprehensive solution for making authenticated API calls to Reels services with support for dynamic body construction, session data integration, pagination, and environment-based configuration.

### Features

- Reels Service Integration: Seamless integration with Reels services using client credentials
- Dynamic Body Construction: Intelligent body parameter construction from various data sources
- Session Data Integration: Access to user session and case instance data
- Environment Configuration: Environment variable-based configuration management
- Pagination Support: Built-in pagination handling for data operations
- Type Conversion: Automatic type conversion for request parameters

### Usage

#### Basic Reels Datasource Call

```javascript
// Basic reels datasource callconst config = {  url: 'https://reels.example.com/api/data',  method: 'POST',  body: [    { key: 'query', value: 'search term' },    { key: 'limit', value: 10, type: 'number' }  ]};ap.reelsDs.reels(config, {}, (result) => {  if (result.error) {    console.error('Error:', result.error);  } else {    console.log('Data:', result.data);    console.log('Status:', result.status);  }});
```

#### With Pagination

```javascript
// Reels call with paginationconst paginationData = {  pageNumber: 1,  pageSize: 20,  pageNumberKey: 'page',  pageSizeKey: 'size',  paramType: 'queryParams' // or 'body'};const config = {  url: 'https://reels.example.com/api/users',  method: 'GET',  queryParams: [    { key: 'status', value: 'active' }  ]};ap.reelsDs.reels(config, paginationData, (result) => {  if (result.error) {    console.error('Error:', result.error);  } else {    console.log('Users:', result.data);    console.log('Total pages:', Math.ceil(result.data.total / paginationData.pageSize));  }});
```
