# Binding a Page Flow to a component's Attribute

<https://documentation.neutrinos.com/articles/#!studio-guide-9/bind-page-flows-to-components>

You can bind a page flow to a component’s attribute by using the **Flow picker **editor. This editor allows you to pick an already defined page or client service flow and bind it to the component’s event or property.

For example, you can bind a page flow to the (click) function of the button to perform some action on the click event.

#### Binding a Page Flow to a component's Attribute

To bind a flow to a component’s attribute:

1. Open the attributes window of the component.
2. Click the **Pick a Flow** mat chip on the attribute for which you want to bind the flow.
3. The **Flow picker** editor opens up. On the editor, select the **Pages** Tab to pick a page flow. Or, select the **Services** tab to pick a flow from client service. Flows are displayed based on the function name of the Start node.
4. ![Flow picker](/resources/Storage/studio-guide-9/flow_pickwer1.png)
5. After picking a flow, the function name of the flow, along with its input and output variables, are displayed to the right.
6. ![Flow picker](/resources/Storage/studio-guide-9/flow_pickwer2.png)
7. Optionally, you can assign values to the input variables which will be taken as the input arguments for the flow.
8. Click** Save** to bind the selected flow to the component’s attributes.

If you want to create a flow from the Flow Picker UI, click the **Create New **button to navigate to the page flow designer with a new start node on the canvas.

If you want to make changes to the flow properties, click the **Edit** icon on the selected function to navigate to the selected page/service flow in the respective flow designer.

If you have migrated your app from a previous version, and have already entered a value for a component property, then the **Pick a Flow** mat chip will not be visible to bind the component property to a flow.

#### Bind Page Flows to Custom Property

To bind a page flow to a [custom property](/smart/project-concepts/component/a/h4_1169636058), you should first create the property and then bind the flow.

1. Open the attributes window of the component to which you want to bind a page flow.
2. Create a custom property of type **key&value**. See [Work with Component Properties](/articles/studio-guide-9/work-with-component-properties).
3. Click the Pick a Flow mat chip to open the **Flow Picker **editor and select a page flow.

| ![Information](/resources/Storage/studio-guide-9/info.png) | You cannot bind a page flow to a custom property of type **Attribute**. |
| --- | --- |
