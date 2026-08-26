# Accessing Environment Properties on the Page UI

<https://documentation.neutrinos.com/articles/#!studio-guide-9/accessing-environment-properties>

After defining the environment properties in the **Environments** editor, you may want to access them across your app.

### Accessing Environment Properties on the Page UI

You can access environment properties on the Page UI by:

- **Method 1: **Binding it directly to a component attribute. This is a preferred method if you do not want to run any logic on the properties. Use {{page.system.environment.properties.<env_property>}} and bind the property to a component.
- **Method 2: **Creating a page flow to bind the environment properties to page or flow variables and then binding that page flow to a component. Prefer using this method if you want to run some logic on the environment properties before displaying them on the UI.
    There are two ways to access the environment properties within a flow:
  - Using the [Environment node](/smart/project-page-services-designer-guide/environments-node).
  - Using the following notation in a node's attribute window:
    - bh.system.environment.properties.<env_property_name>
    - For an attribute that is a typedInput and that has page as one of the types, use system.environment.properties.<env_property_name> as the value.

#### Binding the Environments property to a component

When you create a page on Neutrinos Studio, along with the page variable, a namespace called page.system.environment is also gets created. This namespace can be used to access the properties that you have configured on the **Environments** editor, and bind them to the page UI. See [Properties in Page Designer](/smart/project-page-services-designer-guide/properties-page-designer) to learn about the page properties in more detail.

**Example:**

Create or open a page. On the HTML editor of the page, drag and drop a **Toolbar** component to the canvas.




 Bind the default appName environment property to this toolbar by entering {{page.system.environment.properties.appName}} in the content property of the toolbar.

 ![toolbar properties](/resources/Storage/studio-guide-9/appname_toolbar.png)



 On preview, the app name is displayed on the toolbar:

 ![app name on the toolbar](/resources/Storage/studio-guide-9/appname.png)

#### Binding the Environment properties to a Page Flow

In the above example, you mapped the environment property directly to a component's property. Alternatively, you can design page flows on the [flow designer](/smart/project-concepts/page-designer/a/h3_520216706), and then bind that flow to a component's property.

**Example:**

Let us look at an example of how to bind the environment property to the page flow. Let us create a new environment property called url, call that URL on the page flow, and display the result returned by the URL on the Page UI.

 **Step 1: Configure the property on the Environments editor**

Open the **Environments **Editor.


 Enter the new property name as url and value as https://jsonplaceholder.typicode.com/posts/1. This is a dummy URL that returns a sample user data when it is called. Select** Client **to add this as a client property, and click the **Add** button.



 ![adding an env property](/resources/Storage/studio-guide-9/add_env_prop.png)

**Step 2: Bind the Property to a Page Flow**



 Create/open a page and select the flow designer of the page.


 Let us create a call API flow to call the url that we defined in the Environments editor.


 Drag and drop a** Start** node to the canvas. Name the node as call API.


 Join an HTTP Request node to the Start node. Set the following properties:


 Method: **Get**


 URL: Select page. and enter system.environment.properties.url.


 Return Type: **JSON**


 Result Mapping: Select page. and enter apiRes. The JSON object returned by the API will be saved in this property.




 Save the flow.



 **Step 3: Bind the Page Flow to the Page UI**



 Navigate to the UI of the page.


 Drag and drop a button and set the following properties:


 button name: **Call API**


 (click): Click the **Pick a Flow **mat chip and select the** call API **flow in the Flow Picker editor. See [Bind Page Flows to Components](/articles/studio-guide-9/bind-page-flows-to-components) to learn more about Flow Picker.




 Drag and drop an **HTML 5** component below the button. We will display the response of the API on this component. Select the **Element Type **of the component as **Div**.


 Click the **HTML Editor** of the Div component and enter {{page.apiRes | json}} in the code window.

 ![binding the API response to the Div](/resources/Storage/studio-guide-9/apires_html.png)




 Save and preview the page.




 Click the **Call API **button. You should get a response similar to this:



 ![Preview of the app](/resources/Storage/studio-guide-9/env_preview.png)

Accessing Environment Properties in Server Service Flows

You can access the server-side environment properties using the process.env.<property_name> or the bh.system.environment.properties.<property_name> property in the server service flows that you design in your app.

---

### Accessing Environment Properties in Client Service Flows

You can access the client-side (front-end) environment properties using the bh.system.environment.properties.<property_name> property in the client service flows. You can also use the [Environment](/smart/project-service-designer-user-s-guide/environments-node) node to access these properties.
