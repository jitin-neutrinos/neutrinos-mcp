# Features

<https://documentation.neutrinos.com/articles/#!pulse-publication/cms-service-plugins-gcc>

The Alpha Module CMS Service is a comprehensive Content Management System service that provides powerful capabilities for managing content, schemas, and dynamic content rendering in Alpha applications. It offers a complete solution for content lifecycle management with support for content creation, updates, schema management, and Handlebars templating.

### Features

- Content Management: Create, read, update, and delete content
- Schema Management: Fetch and manage content schemas
- Dynamic Content: Handlebars templating for dynamic content rendering
- Content Fetching: Retrieve content by ID or fetch all content
- HTTP Integration: Seamless integration with HTTP services
- TypeScript Support: Full TypeScript definitions for type safety
- Error Handling: Comprehensive error handling and response management
- Flexible API: RESTful API design for easy integration
- Content Lifecycle: Complete content management workflow
- Performance Optimized: Efficient content retrieval and caching

### Installation

This module is automatically available via the global ap object when using Alpha UI Base.

### Usage

#### Basic CMS Service Access

```javascript
// Access CMS service via ap.cmsService
const cmsService = ap.cmsService;

// Access different service modules
const schemaService = cmsService.schema;
const contentService = cmsService.content;
```

#### Content Operations

#### Create Content

```javascript
// Create new content
const createArgs = {
  title: 'Welcome to Alpha',
  description: 'Introduction to Alpha platform',
  content: 'This is the main content of the page',
  type: 'page',
  status: 'published',
  metadata: {
    author: 'John Doe',
    category: 'introduction',
    tags: ['alpha', 'platform', 'welcome']
  }
};

try {
  const result = await cmsService.content.createContent(createArgs);
  console.log('Content created successfully:', result);
} catch (error) {
  console.error('Content creation failed:', error);
}
```

#### Fetch Content by ID

```javascript
// Fetch specific content by ID
const fetchArgs = {
  contentId: 'content-123',
  includeMetadata: true,
  includeSchema: true
};

const content = await cmsService.content.fetchContentByID(fetchArgs);
console.log('Content details:', content);
```

#### Fetch All Content

```javascript
// Fetch all content with pagination and filtering
const fetchAllArgs = {
  type: 'page',
  status: 'published',
  pageSize: 20,
  pageNumber: 0,
  sortBy: 'createdAt',
  sortOrder: 'desc',
  filters: {
    category: 'introduction',
    author: 'John Doe'
  }
};

const allContent = await cmsService.content.fetchAllContent(fetchAllArgs);
console.log('Total content items:', allContent.total);
console.log('Content items:', allContent.items);
```

#### Update Content

```javascript
// Update existing content
const updateArgs = {
  contentId: 'content-123',
  title: 'Updated Welcome to Alpha',
  description: 'Updated introduction to Alpha platform',
  content: 'This is the updated main content of the page',
  metadata: {
    author: 'John Doe',
    category: 'introduction',
    tags: ['alpha', 'platform', 'welcome', 'updated'],
    lastModified: new Date().toISOString()
  }
};

const updatedContent = await cmsService.content.updateContent(updateArgs);
console.log('Content updated successfully:', updatedContent);
```

#### Remove Content

```javascript
// Remove content
const removeArgs = {
  contentId: 'content-123',
  permanent: false, // Set to true for permanent deletion
  reason: 'Content no longer relevant'
};

const removeResult = await cmsService.content.removeContent(removeArgs);
console.log('Content removed:', removeResult);
```

#### Handlebars Templating

```javascript
// Process content with Handlebars templates
const handlebarsArgs = {
  template: 'Hello {{name}}, welcome to {{platform}}!',
  data: {
    name: 'John Doe',
    platform: 'Alpha'
  },
  options: {
    allowProtoPropertiesByDefault: true,
    allowCallsToHelperMissing: true
  }
};

const processedContent = await cmsService.content.handlebars(handlebarsArgs);
console.log('Processed content:', processedContent);
// Output: "Hello John Doe, welcome to Alpha!"
```

#### Schema Operations

#### Fetch Schema

```javascript
// Fetch specific schema
const schemaArgs = {
  schemaId: 'schema-123',
  includeFields: true,
  includeValidation: true
};

const schema = await cmsService.schema.fetchSchema(schemaArgs);
console.log('Schema details:', schema);
```

#### Fetch All Schemas

```javascript
// Fetch all schemas
const allSchemasArgs = {
  type: 'content',
  active: true,
  pageSize: 50,
  pageNumber: 0
};

const allSchemas = await cmsService.schema.fetchAllSchema(allSchemasArgs);
console.log('Total schemas:', allSchemas.total);
console.log('Schemas:', allSchemas.items);
```
