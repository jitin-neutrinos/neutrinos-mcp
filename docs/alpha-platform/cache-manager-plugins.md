# Package Information

<https://documentation.neutrinos.com/articles/#!alpha-platform/cache-manager-plugins>

A comprehensive caching solution for Alpha UI Base that provides both localStorage and sessionStorage management with automatic expiration, namespace support, and advanced caching strategies.

### Package Information

- Name: alpha-module-cache-manager
- Version: 1.0.0
- Description: Provides methods to manage cache with expiration and namespace support
- Main File: index.js
- Exposed Name: cache

### Features

- Dual Storage Support: Both localStorage and sessionStorage management
- Automatic Expiration: TTL (Time To Live) based cache invalidation
- Namespace Management: Organized cache buckets for different applications
- JSON Serialization: Automatic serialization/deserialization of complex data
- Storage Detection: Automatic detection of storage availability
- Quota Management: Handles storage quota exceeded scenarios gracefully
- Performance Optimized: Cached feature detection and minimal overhead
- Cross-browser Compatible: Works across all modern browsers

### API Reference

#### Main Cache Object

The cache manager provides two storage instances:

```javascript
const cache = {  local: localStorageManager,    // Persistent storage  session: sessionStorageManager // Session-based storage};
```

### Core Methods

1. set(key, value, ttl): Stores a value in cache with optional expiration.
    Parameters:
    Returns: boolean - Success status
  - key (string): Cache key
  - value (any): Value to store (automatically serialized
  - ttl (number, optional): Time to live in minutes
2. get(key): Retrieves a value from cache.
    Parameters:
    Returns: any - Stored value or null if expired/not found
  - key (string): Cache key
3. remove(key): Removes a specific key from cache.
    Parameters:
    Returns: boolean - Success status
  - key (string): Cache key to remove
4. flush(): Clears all cached items.
    Returns: boolean - Success status
5. setBucket(bucket): Sets the current cache namespace/bucket.
    Parameters:
    Returns: void
  - bucket (string): Namespace for cache keys
6. resetBucket(): Resets to default bucket (empty string).
    Returns: void

### Usage Examples

#### Basic Caching

```javascript
// Store data in localStorageap.cache.local.set('user-profile', { name: 'John', id: 123 });// Store data in sessionStorageap.cache.session.set('temp-data', { timestamp: Date.now() });// Retrieve dataconst userProfile = ap.cache.local.get('user-profile');const tempData = ap.cache.session.get('temp-data');
```

#### With Expiration

```javascript
// Cache with 30-minute expirationap.cache.local.set('api-response', apiData, 30);// Cache with 2-hour expirationap.cache.local.set('user-preferences', preferences, 120);// Cache with 1-day expirationap.cache.local.set('static-content', content, 1440);
```

#### Namespace Management

```javascript
// Set namespace for current applicationap.cache.local.setBucket('my-app');// All keys will be prefixed with 'my-app-'ap.cache.local.set('user-data', userData);// Actually stored as 'my-app-user-data'// Reset to default namespaceap.cache.local.resetBucket();
```
