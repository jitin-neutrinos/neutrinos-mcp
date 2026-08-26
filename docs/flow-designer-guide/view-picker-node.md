# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/view-picker-node>

The **View Picker **node gets single or multiple references to elements rendered inside the page. The elements can be [views](/smart/project-concepts/page/a/h4__1350344570) and components. The reference can be of type template, class, or directive.

Any view that you want to query on a page can be accessed using bh.pageViews.<view>.

### Node Properties

1. **Name:** The name of the node on the canvas. This is only used to uniquely identify the node on the editor. It does not provide any behavioral difference on the end app.
2. **Function Name:** This is a read-only field. The function name is generated based on the name that you entered in the **Name** field. It is used to identify the node while debugging.
3. **Views:** The view that is to be picked. The first field is where you specify the selector. The selector can be of type template, class, or directive. The second field is where you specify the directive/component that you want to query. See the [Angular blog](https://blog.knoldus.com/different-types-of-component-selectors-in-angular/) to learn more about selectors.
  - If you want to query a view or a component using its template reference, select the ref option and enter the template reference name. To create a template reference, create a [custom property](/smart/project-concepts/component/a/h4_1169636058) of type **Attribute** in the View or component's properties window by prefixing it with #. You can then use the template reference (without the #) in the **View Picker** node to query that reference in a page flow.
  - If you want to query a view or a component using its associated component class or directive class, select the token option and enter the class or directive name.

**Match All**: If the toggle is set to false (default), the **View Picker** node obtains a single reference of the template or class. If the toggle is set to true, the **View Picker **node gets all the elements matching the given selector.

### Example 1

**Query an Element using its Template Reference**

**Template Reference **is used to access all the properties of an element (component or view) inside a page.

You create the template reference of an element by creating a custom property of type **Attribute** in the properties window of the element. For example, in the below screenshot, a template reference called name is created for the **Input** component.

After the reference is created, to query the template reference and perform some logic based on the result of the query, create [page flows](/smart/project-concepts/page-designer/a/h3_520216706), and use the [View Picker](/articles/flow-designer-guide/view-picker-node) node to get access to the template reference.

For example, in the below page flow, the template reference name of the **Input** component is accessed to validate if the Input field is left empty.

A S**witch** node is used to validate the input field.

If the validation fails, a snack bar message is displayed to the user indicating that the name field is required.

![Snack bar message to the user](/resources/Storage/flow-designer-guide/project-how-to-articles/how-2021-08-03-3.png)

---

### Example 2

**Query a****n Element using its Class or Directive Reference**

You can also use the class or directive reference of an element to access the methods of that element and perform some action on it.

For example, the methods of the** Sidenav** component are listed [here](https://material.angular.io/components/sidenav/api#MatDrawer). To access these methods and perform actions on the Sidenav component, you access the class instance using the** View Picker** node and then call the method on that instance.

Accessing the component class instance of **Sidenav**:

![Accessing sidenav class](/resources/Storage/flow-designer-guide/page-service-designer-preface-2021-08-03.png)

Using the class instance reference to toggle the Sidenav:

![Calling the Sidenav class](/resources/Storage/flow-designer-guide/page-service-designer-preface-2021-08-03-1.png)
