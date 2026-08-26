# Features

<https://documentation.neutrinos.com/articles/#!pulse-publication/change-tracker-plugins-gcc>

The Alpha Module Change Tracker is a lightweight and efficient change tracking service that monitors and tracks changes across different components and types in Alpha applications. It provides a simple yet powerful way to track the dirty state of various application components, enabling efficient rendering updates and change detection.

### Features

- Change Tracking: Track changes across different component types
- Dirty State Management: Mark components as dirty or clean
- Type-based Tracking: Organize tracking by component types
- Memory Efficient: Uses Map-based storage for optimal performance
- Simple API: Clean and intuitive interface for change management
- TypeScript Support: Full TypeScript definitions for type safety
- Lightweight: Minimal overhead with maximum functionality
- Integration Ready: Seamlessly integrates with Alpha ecosystem

### Installation

This module is automatically available via the global ap object when using Alpha UI Base.

### Usage

#### Basic Change Tracking

```javascript
// Access change tracker via ap.tracker
const tracker = ap.tracker;

// Mark a component type as dirty
tracker.markAsDirty('user-form');
tracker.markAsDirty('data-table');
tracker.markAsDirty('navigation');

// Check if a component type is dirty
if (tracker.isDirty('user-form')) {
  console.log('User form has unsaved changes');
}

// Mark a component type as clean
tracker.markAsClean('user-form');
```

#### Component State Management

```javascript
// Track form changes
function handleFormChange() {
  // Mark form as dirty when user makes changes
  ap.tracker.markAsDirty('user-profile-form');
  
  // Update form data
  updateFormData();
}

function handleFormSubmit() {
  try {
    // Submit form data
    await submitForm();
    
    // Mark form as clean after successful submission
    ap.tracker.markAsClean('user-profile-form');
    
    console.log('Form submitted successfully');
  } catch (error) {
    console.error('Form submission failed:', error);
    // Keep form as dirty if submission fails
  }
}

// Check form state before navigation
function checkFormState() {
  if (ap.tracker.isDirty('user-profile-form')) {
    return confirm('You have unsaved changes. Are you sure you want to leave?');
  }
  return true;
}
```
