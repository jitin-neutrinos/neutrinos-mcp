# Debug Custom Code

<https://documentation.neutrinos.com/articles/#!pulse-publication/debugging-and-testing-global-custom-codes>

The Global Custom Code interface consists of two panels:

- Code: The left panel is used for writing or editing the code.
- Runtime Panel: The right panel displays the output when the code is executed.

The image below illustrates the interface layout for a custom code:




 ![custom-code-two-sections](/resources/Storage/pulse-publication/images/custom-code-two-sections.png)


 Click the Run button on the top of the Code editor, to execute. The output can be visualized on the right panel which is the runtime panel.

### Debug Custom Code

To debug and test the Custom Code, follow the steps below:

1. Implement the custom code that encapsulates the required logic based on the specified functionality.
2. Click the Run button at the top of the Code panel to execute the code.
3. After executing the code, the Runtime panel on the right displays the results. If the code contains errors, they will be listed in the panel. Otherwise, the panel shows the successful output.

The GIF below illustrates debugging and testing a custom code on the platform:




 ![global-custom-code-debug-test](/resources/Storage/pulse-publication/images/global-custom-code-debug-test.gif)

### Debug Project mapped Custom Code

To debug a custom code mapped to a particular project, follow the steps below:

1. Implement the custom code that encapsulates the required logic based on the specified functionality. This code can be executed within the context of a specific project, such as on a project task page, a global page, or within the Inbox.
2. To map the custom code, select the target project and choose the specific page where the code should run. Note: If the code references any components from the selected project, ensure that their corresponding component IDs are correctly mapped within the code. Once executed, the output of the custom code can be viewed in the Runtime panel. Navigate to the Output tab within the Runtime panel to see the execution results.
