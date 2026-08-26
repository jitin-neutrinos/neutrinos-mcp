# Advanced Component

<https://documentation.neutrinos.com/articles/#!concepts-publication/advanced-component>

### Advanced Component

An advanced component is an extension of the Component.js class. This is, it is an extension of a basic [component](/articles/concepts-publication/component).

An advanced component provides more features such as:

- Support for complex palette components with parent and child relationship
- Sharing of attributes between child and parent component using slots
- Support for sharing values between parent and child components by using methods such as toChildren(), fromParent(), and toParent().

Advanced components are self-sufficient. They act as mini page designers. They are easy to use, as they reduce the overhead of manual configuration, the time taken to design pages.

### Advanced Component Lifecycle

Every advanced component has a lifecycle. It is a sequence of events that an advanced component’s life experiences. These events are called** Lifecycle Hooks**. If necessary, you can use these lifecycle hooks to do something (run some code) whenever one of these events occurs.

- **onInit: function ():** This function is called when an advanced component is dragged and dropped to a page container. It initializes the component on the page and sets its input properties. This function is also called when the component is moved (dropped) to another location on the same page.

- **onDestroy: function ()**: This function is called just before the advanced component is removed/deleted from the page. It is used to clean up any necessary code, unsubscribe observables, and detach event handlers to avoid memory leaks when a component is removed from the page. This function is also called when a component is moved (dragged) from its location on the page.
