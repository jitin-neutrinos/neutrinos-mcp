# Component

<https://documentation.neutrinos.com/articles/#!concepts-publication/component>

Component


 A component is a JavaScript class that can be imported from the **[@jatahworx/bhive-toolkits](/articles/concepts-publication/bhive-toolkits-package)** npm module (which is the plugins SDK). Extending this class and implementing its methods will help Neutrinos Studio construct the UI for the component, the list of attributes in the attributes window, and the Code generation template.


 Attribute/Property of a Component

 An attribute of a component is a decorator that provides configuration metadata which determines how the component should be processed, instantiated, and used at runtime.


 Attribute Window


 Attributes of the component are configured in the Attributes window. After you drag and drop the component to the [canvas](/articles/concepts-publication/canvas), click the component to open its attributes window to the right.


 The attributes window of a component has 2 sections:

 **Basic properties**These are the most common properties of the component that are readily available for you to configure. For example, the basic properties of a **Router Outlet** component:
 **Custom properties**These are properties that are not available by default. Custom properties are used to store custom data private to the page. They are defined in the Custom Properties section of the component's attributes window. Every component can have any number of custom attributes. Depending on the type of custom attribute you want to add, you can toggle between **Attribute** and **Key&Value **types. By default, **Attribute** is selected.**Attribute - **should only be used to define scalar values like strings, numbers and boolean values. **Key & Value** - can hold values that are objects or arrays.

###
