# Installation

<https://documentation.neutrinos.com/articles/#!pulse-publication/renderer-instance-gcc>

The Alpha Module Renderer Instance is a library to get a renderer instance of any page.

### Installation

This module is automatically available via the global ap object when using Alpha UI Base.

### Usage

#### Basic Renderer Instance access

```javascript
// Get a renderer instance for a page
const rendererElement = await ap.renderer.get(
  'user-profile',     // pageId
  'form',            // pageType
  false,             // readonly
  ['custom-class']   // additional CSS classes
);

// Append to DOM
document.body.appendChild(rendererElement);
```
