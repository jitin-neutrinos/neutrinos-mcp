# Package Information

<https://documentation.neutrinos.com/articles/#!pulse-publication/dom-utils-plugins-gcc>

A comprehensive DOM manipulation utility library for Alpha UI Base that provides jQuery-like functionality with modern JavaScript APIs, element manipulation, event handling, and DOM traversal capabilities.

### Package Information

- Name: alpha-module-dom-utils
- Version: 1.0.1
- Description: DOM manipulation utilities with jQuery-like syntax
- Exposed Name: $

### Features

- jQuery-like Syntax: Familiar API for developers coming from jQuery
- Modern JavaScript: Built with modern ES6+ features and native DOM APIs
- Element Selection: Powerful CSS selector support for element targeting
- DOM Manipulation: Easy element creation, modification, and removal
- Event Handling: Comprehensive event binding and management
- DOM Traversal: Parent, child, and sibling element navigation
- Attribute Management: Easy get/set of element attributes and properties
- Style Manipulation: CSS property management and manipulation

### API Reference

#### Main Function: $

The $ function serves as the main entry point for DOM operations, similar to jQuery.

Element Selection

```javascript
// Select elements by CSS selector
const elements = ap.$('.my-class');
const button = ap.$('#submit-button');
const inputs = ap.$('input[type="text"]');

// Select multiple elements
const allButtons = ap.$('button');
const formElements = ap.$('form input, form select, form textarea');
```

Element Creation

```javascript
// Create new elements
const div = ap.$('<div>');
const button = ap.$('<button>', { text: 'Click me', class: 'btn' });
const input = ap.$('<input>', { type: 'email', placeholder: 'Enter email' });
```

DOM Manipulation

```javascript
// Append elements
ap.$('#container').append('<p>New content</p>');
ap.$('#container').prepend('<h1>Title</h1>');

// Insert elements
ap.$('#target').before('<span>Before</span>');
ap.$('#target').after('<span>After</span>');

// Replace elements
ap.$('#old-element').replaceWith('<div>New element</div>');
```

### Usage Examples

#### Basic Element Operations

```javascript
// Select and modify elements
ap.$('.highlight').addClass('active');
ap.$('#username').val('john.doe');
ap.$('.status').text('Loading...');

// Create and append elements
const newItem = ap.$('<li>', { text: 'New item', class: 'list-item' });
ap.$('#todo-list').append(newItem);
```

#### Event Handling

```javascript
// Bind events
ap.$('#submit-btn').on('click', function(e) {
  e.preventDefault();
  console.log('Button clicked!');
});

// Multiple events
ap.$('.interactive').on('click mouseenter', function(e) {
  console.log('Event:', e.type);
});

// Event delegation
ap.$('#parent').on('click', '.child', function(e) {
  console.log('Child clicked:', e.target);
});

// Remove events
ap.$('#button').off('click');
```

#### DOM Traversal

```javascript
// Find parent elements
const parent = ap.$('#child').parent();
const ancestors = ap.$('#child').parents('.ancestor-class');

// Find child elements
const children = ap.$('#parent').children();
const specificChildren = ap.$('#parent').find('.child-class');

// Find siblings
const nextSibling = ap.$('#element').next();
const prevSibling = ap.$('#element').prev();
const allSiblings = ap.$('#element').siblings();
```

#### Attribute and Style Management

```javascript
// Get and set attributes
const href = ap.$('a').attr('href');
ap.$('img').attr('src', 'new-image.jpg');

// Get and set properties
const value = ap.$('input').prop('value');
ap.$('input').prop('disabled', true);

// CSS properties
ap.$('.box').css('background-color', 'red');
ap.$('.box').css({
  'width': '200px',
  'height': '200px',
  'border-radius': '10px'
});

// Classes
ap.$('.element').addClass('active');
ap.$('.element').removeClass('inactive');
ap.$('.element').toggleClass('highlighted');
ap.$('.element').hasClass('special');
```
