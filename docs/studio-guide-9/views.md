# Example

<https://documentation.neutrinos.com/articles/#!studio-guide-9/views>

On Neutrinos Studio, you can reuse the user interface of a page on another page in the form of [views](/smart/project-concepts/view). A view represents the content that is displayed to the user.

For example, let us assume that you have created an app with a view that includes a set of address fields. If you want to create a second view that needs the same address fields, you can reuse the first view on the second page. In both cases, the app is using an instance of the view.

You can edit the properties of each instance independently. For example, changing the label of one view instance does not change the label of the other. Both view instances use a reference to point to the view definition. This means that if the view definition changes, you can see the change reflected in the instances of the view as well.

### 

### Example

Consider an app with 2 pages **weathersearch** and **weathercard**.

To create a view of **weathercard** on the **weathersearch** page, perform the following steps:

- Open the **weathersearch **page.
- Navigate to the **Views** section.
- Drag and drop the **weathercard** view to the **weathersearch **page container. You will see that the Studio creates an instance of the **weathercard **page on the **weathersearch **page.

![Weathercard View](/resources/Storage/studio-guide-9/weathercard%20view2019-07-09_12h28_59.png)

![Weather card view](/resources/Storage/studio-guide-9/2019-07-09_12h32_46.png)

### Considerations when using Views

- Cyclic dependency is checked. That is, if you create a view of page **weathercard** on the **weathersearch **page, you cannot create a view of the **weathersearch** page on the **weathercard** page. This creates nested dependency. Therefore, Neutrinos Studio does not allow such dependency and throws an error message if such dependencies are encountered.

![Cyclic dependancy](/resources/Storage/studio-guide-9/Cyclic%20dependancy2019-07-09_12h35_44.png)

- You cannot drag and drop components into a view, or delete components from a view. Modifications, if any, has to be made to its original page.

### Pass data between views

Any data to be passed between views is added to the **Input** and **Output** properties of the [On Init](/smart/project-page-services-designer-guide/on-init-node) node that is present on a page flow. After adding the properties, the input and output properties of the child view are displayed in the **Advanced Properties** section of the parent view's Attributes window.

#### Sharing data from Parent to Child view

Data from the parent view is shared with the child view by declaring page input variables in the **On Init** node of the child view.

#### Example

Consider an app with 2 pages **weathersearch** and **weathercard **where you need to get the `cityName` property value of **weathercard** from **weathersearch**.

The **weathersearch** page provides an input field where you input the name of the city for which you want to check the weather. The **weathercard** page displays the weather of the city entered in the **weathersearch** page. This can be achieved by making use of views. Define a page input variable `cityName` in the flow of the **weathercard **page.

![city name declared as a page input variable](/resources/Storage/studio-guide-9/cityName_oninit.png)

Navigate to the attribute's window of the **weathercard** page and bind the input variable to the property of the **weathersearch** page. For example, here, we are binding  cityName to the `searchString` property of the **weathersearch** page.

![Bind child property and parent property](/resources/Storage/studio-guide-9/cityname_searchString.png)

#### Share data from Child to Parent view

Data from the child view is shared with the parent view by declaring page output variables in the **On Init **node of the child page.

The parent can listen to the event by using event binding. This approach is ideal when you want to share data changes that occur on actions like button clicks, form entries, and other user events.

To create an output

 property in the **weathercard **view, you define the page output variable in the
** On Init** node of the
 **weathercard **page.

![page output variables](/resources/Storage/studio-guide-9/page_output_var.png)

After defining the variable, navigate to the attribute's window of the **weathercard** page and bind the output variable to:

- a property of the **weathersearch** page
- or a client or page flow.

For example, here we have bound the output property to a page flow called **updateLog**. See [Bind Page Flows to a Component's Attribute](/articles/studio-guide-9/bind-page-flows-to-components) to learn how to use the flow picker to bind a page flow to a component's attribute.

![binding output variable to a page flow](/resources/Storage/studio-guide-9/log_output.png)
