# Call a Client Service Flow on the Page UI

<https://documentation.neutrinos.com/articles/#!studio-guide-8/import-client-services-to-the-page-ui>

To call a client service flow on a page UI:

1. Design the service flow on [Client Services Designer](/smart/project-concepts/client-services-designer).
2. On the Page UI, open the attributes window of the component.
3. Click the **Pick a Flow** mat chip on the component attribute for which you want to bind the flow. For example, click the **Pick a Flow** mat chip on the (click) property of a button.
4. The **Flow picker** editor opens up. On the editor, select the **Services** tab to view flows designed on the Client Services Designer. Flows are displayed based on the function name of the Start node. After picking a flow, the function name of the flow, along with its input and output variables, are displayed to the right.
    ![calling client flow on the Page UI](/resources/Storage/studio-guide-8/call_client_flow.png)
5. Optionally, you can assign values to the input variables which will be taken as the input arguments for the flow.
6. Click** Save** to bind the selected flow to the component’s attributes.

If you want to make changes to the flow properties, click the **Edit** icon next to the function name. You will be navigated to the flow on the Client Services Designer to make the changes.

| ![Information](/resources/Storage/studio-guide-8/info.png) | If you have migrated your app from a previous version, and have already entered a value for a component property, then the **Pick a Flow** mat chip will not be visible to bind the component property to a flow. |
| --- | --- |
