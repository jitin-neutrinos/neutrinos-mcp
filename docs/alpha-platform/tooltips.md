# Package Information

<https://documentation.neutrinos.com/articles/#!alpha-platform/tooltips>

A tooltip system for Alpha UI Base that provides intelligent positioning, shadow DOM support, and customizable styling with CSS custom properties.

### Package Information

- Name: alpha-module-tootip
- Version: 1.0.0
- Description: Advanced tooltip component with smart positioning
- Exposed Name: attachTootip

### Features

- Smart Positioning: Uses Floating UI for intelligent tooltip placement
- Shadow DOM Support: Works seamlessly with Alpha dialog components📋 API Reference

### Main Function

attachTooltip(elementRef, tooltipText): Attaches a tooltip to the specified HTML element.

Parameters:

- elementRef (HTMLElement): The DOM element to attach the tooltip to
- tooltipText (string): The text content to display in the tooltip

Returns: Error object if validation fails, undefined on success

Throws: Error if elementRef is not an HTMLElement

### Usage Examples

```javascript
// Get the elementconst button = document.querySelector('#my-button');// Attach tooltipap.attachTootip(button, 'Click me to submit the form');
```
