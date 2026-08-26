# Node Properties

<https://documentation.neutrinos.com/articles/#!flow-designer-guide/navigation-node>

This is the default topic template.

The **Navigation **node is used to navigate the user to a specific path/page within an application.

### Node Properties

- **Name:** The name of the node. It is used to uniquely identify the node on the canvas. It does not make any behavioral difference on the end app.
- **Function Name:** This is a read-only field. The function name is generated based on the name that you entered in the **Name** field. It is used to identify the node while debugging.
- **Path to Navigate:** A drop-down list that shows the paths configured in the [Routes](/smart/project-sample-how-to-guide/adding-routes) editor.
    Before you choose the path here, you should have configured how the user navigates between application pages on the [Routes](/smart/project-sample-how-to-guide/adding-routes) editor.
    To assign a path, you can either:
  - Select a path from the drop-down list.
  - Or, click the **Map **button to map the path to the [variables](/articles/flow-designer-guide/properties-page-designer).
- **Path parameters:** This field appears only if the path selected has path parameters associated with it. Path parameters are variable parts of a URL. They are typically used to point to a specific resource within a collection, such as a user identified by ID. A URL can have several path parameters, each starting with a colon (:). For example, in /users/:id, :id is a path parameter.
    You can add path parameters directly or click the **Map** icon to map them to a page or flow variable.
- **Query parameters:** These are the key-value pairs that are to be appended to the URL string. In a URL, they appear at the end of the request after a question mark (?), with different key-value pairs separated by ampersands (&).
    For example: GET /info?offset=100&limit=50. In the **Query parameters** field, you can add a new key-value pair, or click the **Map** icon and map them to a page or flow variable.
- **Result mapping:** Stores the result of the navigation. The result is True if the selected path was navigated successfully. Else, it is False. Specify the flow variable that should save the result.

| ![Information](/resources/Storage/flow-designer-guide/info.png) | If you make any changes to paths in the [Routes](/smart/project-sample-how-to-guide/adding-routes) editor, click the **Refresh** icon in the **Path to Navigate** field to fetch the latest changes. |
| --- | --- |
