# Query an Element using its Template Reference

<https://documentation.neutrinos.com/articles/#!how-to-articles-8/query-a-view-or-component-using-its-template-reference>

**Template Reference **is used to access all the properties of an element inside a page. Where an element can be a component or a view.

You create the template reference of an element by creating a custom property of type **Attribute** in the properties window of the element. For example, in the below screenshot, a template reference called name is created for the **Input** component.

To query the template reference of the element and perform some logic based on the result of the query, create [page flows](/smart/project-concepts/page-designer/a/h3_520216706) and use the [View Picker](/smart/project-page-services-designer-guide/view-picker-node) node to get access to the template reference.

For example, in the below page flow, the template reference name of the **Input** component is accessed to validate if the Input field is left empty.

A **Switch** node is used to validate the input field.

If the validation fails, a snack bar message is displayed to the user indicating that the name field is required.
