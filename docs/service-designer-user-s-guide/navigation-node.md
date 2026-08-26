# How to Use

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/navigation-node>

A **Navigation** node is used when you want to navigate the user to a specified path. To choose the path for navigation, you should first configure how the user should navigate from one page to another within the app by using the [Routes editor](/smart/project-sample-how-to-guide/adding-routes).

### How to Use

- Open the Services editor window.
- Click the **plus** icon to add a new service or open an existing service in the service list.
- From the Nodes Palette, drag and drop a **N****avigation **node to the service designer.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start **node.
- After the flow is created, import the service flow to the application page. See [Import a service](/articles/service-designer-user-s-guide/service-designer-variables/a/h3_519852009) to learn more.

### Associated Attributes

- **Name:** A unique name for the node. This name will display on the canvas when you save the node.
- **Path to Navigate****: **A drop-down list that shows the paths configured in the **Routes** tab of the Studio application page. See [Add Routes](/smart/project-sample-how-to-guide/adding-routes) to learn more. To assign a path, you can either:
  - Select a path from the drop-down list.
  - Add a string value or map the path to the bh.input or bh.local variables that you created in the **Start **or** Script **node. See [Properties](/articles/service-designer-user-s-guide/service-designer-variables) to learn more.

If you make any changes to paths in the **Routes **tab, you can use the **refresh **icon to get the latest routes.

- **Path parameters:** **This field appears only if the path selected has path parameters associated with them.**
    Path parameters are variable parts of a URL path. They are typically used to point to a specific resource within a collection, such as a user identified by ID. A URL can have several path parameters, each starting with a colon (:). For example, in
     /users/:id, :id is the path parameter.
    You can assign a string value, or bh.input or bh.local variables for each path parameter, or you can map the whole path parameters property to any of the bh.input or bh.local properties.
- **Query parameters:** These are the key-value pairs that you send in the URL string. They appear at the end of the request URL after a question mark (?), with different **key=value** pairs separated by ampersands (&). For example: GET /info?offset=100&limit=50.
    Query parameters can also be mapped to bh.local or bh.input parameters by clicking the map icon, selecting the property type, and entering the variable name which contains the query parameter.
- **Result mapping:** Stores the result of the navigation to the specified URL. This property can be mapped to the bh.input or bh.local properties. The result is true if the selected path was navigated successfully. Else, it is false.
