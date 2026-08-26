# Package Information

<https://documentation.neutrinos.com/articles/#!alpha-platform/dom-utils-plugin>

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
// Select elements by CSS selectorconst elements = ap.$('.my-class');const button = ap.$('#submit-button');const inputs = ap.$('input[type="text"]');// Select multiple elementsconst allButtons = ap.$('button');const formElements = ap.$('form input, form select, form textarea');
```

Element Creation

```javascript
// Create new elementsconst div = ap.$('<div>');const button = ap.$('<button>', { text: 'Click me', class: 'btn' });const input = ap.$('<input>', { type: 'email', placeholder: 'Enter email' });
```

DOM Manipulation

```javascript
// Append elementsap.$('#container').append('<p>New content</p>');ap.$('#container').prepend('<h1>Title</h1>');// Insert elementsap.$('#target').before('<span>Before</span>');ap.$('#target').after('<span>After</span>');// Replace elementsap.$('#old-element').replaceWith('<div>New element</div>');
```

### Usage Examples

#### Basic Element Operations

```javascript
// Select and modify elementsap.$('.highlight').addClass('active');ap.$('#username').val('john.doe');ap.$('.status').text('Loading...');// Create and append elementsconst newItem = ap.$('<li>', { text: 'New item', class: 'list-item' });ap.$('#todo-list').append(newItem);
```

#### Event Handling

```javascript
// Bind eventsap.$('#submit-btn').on('click', function(e) {  e.preventDefault();  console.log('Button clicked!');});// Multiple eventsap.$('.interactive').on('click mouseenter', function(e) {  console.log('Event:', e.type);});// Event delegationap.$('#parent').on('click', '.child', function(e) {  console.log('Child clicked:', e.target);});// Remove eventsap.$('#button').off('click');
```

#### DOM Traversal

```javascript
// Find parent elementsconst parent = ap.$('#child').parent();const ancestors = ap.$('#child').parents('.ancestor-class');// Find child elementsconst children = ap.$('#parent').children();const specificChildren = ap.$('#parent').find('.child-class');// Find siblingsconst nextSibling = ap.$('#element').next();const prevSibling = ap.$('#element').prev();const allSiblings = ap.$('#element').siblings();
```

#### Attribute and Style Management

```javascript
// Get and set attributesconst href = ap.$('a').attr('href');ap.$('img').attr('src', 'new-image.jpg');// Get and set propertiesconst value = ap.$('input').prop('value');ap.$('input').prop('disabled', true);// CSS propertiesap.$('.box').css('background-color', 'red');ap.$('.box').css({  'width': '200px',  'height': '200px',  'border-radius': '10px'});// Classesap.$('.element').addClass('active');ap.$('.element').removeClass('inactive');ap.$('.element').toggleClass('highlighted');ap.$('.element').hasClass('special');
```
