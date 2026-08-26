# Directive

<https://documentation.neutrinos.com/articles/#!concepts-publication/directive>

A directive is a function that executes whenever Neutrinos Studio finds it in the Document Object Model (DOM). It tells the HTML compiler to attach a specified behavior to that DOM element or to transform the DOM element and its children.

You can either use pre-defined directives or define your own directives and attach custom behavior to elements in the DOM. You can configure the metadata to determine how the directive should be processed, instantiated, and used at runtime. When your app is deployed, the HTML compiler traverses the DOM matching directives against the DOM elements.

There are three kinds of directives that you can use:

- **Components** - directives with a template.
- **Structural directives** - directives that change the DOM layout by adding and removing DOM elements
- **Attribute directives** - directives that change the appearance or behavior of a component, or another directive.
