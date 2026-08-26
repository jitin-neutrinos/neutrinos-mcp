# Package Information

<https://documentation.neutrinos.com/articles/#!pulse-publication/pages-plugins-gcc>

A page management utility for Alpha UI Base that provides page fetching, dependency resolution, and visibility management for the Alpha ecosystem

### Package Information

- Name: alpha-module-pages
- Version: 1.0.2
- Description: Pages plugin which is used for fetching plugins
- Exposed Name: pages

### Features

- Page Fetching: Fetch pages from Alpha Configuration Service
- Dependency Resolution: Handle page visibility based on model dependencies
- Global Pages: Support for global pages across projects
- Dynamic Visibility: Update page display based on mapping source changes

### API Reference

#### Main Export: pages

The pages object provides functionality for managing pages within the Alpha ecosystem.

#### Core Methods

Page Fetching

```javascript
// Fetch all pages for current project
const allPages = await ap.pages.get();

// Fetch specific page by ID
const specificPage = await ap.pages.get('page-123', 'page');

// Fetch global pages
const globalPages = await ap.pages.getGlobalPages();
```

Page Management

```javascript
// Get current pages list
const currentPages = ap.pages.getPagesList();

// Set pages list (triggers visibility update event)
ap.pages.setPagesList(newPagesArray);

// Cleanup event listeners
ap.pages.cleanup();
```

Dependency Resolution

```javascript
// Manually resolve dependencies (usually automatic)
await ap.pages.resolveDependency();
```

### Usage Examples

Basic Page Operations

```javascript
// Fetch all pages for current project
async function loadProjectPages() {
  try {
    const projectPages = await ap.pages.get();
    console.log('Project pages loaded:', projectPages);
    
    // Set pages in the system
    ap.pages.setPagesList(projectPages);
  } catch (error) {
    console.error('Failed to load project pages:', error);
  }
}

// Fetch global pages
async function loadGlobalPages() {
  try {
    const globalPages = await ap.ap.pages.getGlobalPages();
    console.log('Global pages loaded:', globalPages);
  } catch (error) {
    console.error('Failed to load global pages:', error);
  }
}
```
