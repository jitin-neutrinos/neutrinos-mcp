# Global Custom Code with Triggers

<https://documentation.neutrinos.com/articles/#!pulse-publication/global-custom-code-with-triggers>

Global custom codes are a modularized method of creating custom codes that can be leveraged in various projects. To use the custom code in triggers within a project, follow the steps below:

1. Click the **Custom Code** icon on the top bar, next to the user profile icon, to open the **Custom Code** page. To create a new custom code, click the Create button located at the top right of the page. Alternatively, to edit or use an existing custom code, select it from the list to open it in the editor.
2. Save and publish the custom code. While publishing, provide appropriate release notes for the published version. Note: Only published versions of custom code from the Global Custom Code page are available for use within projects in Alpha.
3. In Workflow Studio, select a project and open the relevant Task Page, Global Page, or Inbox where the custom code needs to be executed. Click the component in which the custom code should run, then double-click it to open its Attributes and Trigger window.
4. Under the Trigger section, select the desired trigger, then choose Global Custom Code from the dropdown menu.
5. Select the custom code created in the Global Custom Code section, then choose the appropriate version from the dropdown.
6. Save the project.
7. Click the Preview button, navigate to the page where the Global Custom Code was assigned to the component’s trigger, and observe the output.

For example, a custom code was written to display an alert with the message: "This is an Alpha Application." This custom code was assigned to the On Click trigger of a button on a page. The GIF below demonstrates the alert message being displayed when the button is clicked.




 ![global-custom-code-display-alert-on-click-trigger](/resources/Storage/pulse-publication/images/global-custom-code-display-alert-on-click-trigger1.gif)

Additionally, project components can be accessed within custom code using plugins such as alpha-module-dom-util. For example, the illustration below demonstrates how to calculate the sum of two numbers entered in separate input fields and display the result in a third field when a button is clicked.




 ![global-custom-code-access-alpha-components-in-code](/resources/Storage/pulse-publication/images/global-custom-code-access-alpha-components-in-code.gif)


 Here, ap.$ key is used to reference the DOM ID of Alpha components within the custom code. Input values retrieved from the respective fields are explicitly cast to integers using the parseInt() method. These integer values are then passed as arguments to a function, and the result is assigned to the third input field.

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | Note: When using custom code with inbox triggers, the Inbox Projection feature requires you to explicitly specify any keys that are not configured as part of the inbox columns. For more information, refer to the [Inbox Projection](/smart/project-alpha-platform/inbox-projection) topic. |
| --- | --- |
