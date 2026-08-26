# Deploy

<https://documentation.neutrinos.com/articles/#!pulse-publication/create-process>

A process is a structured workflow defined using BPMN 2.0. It has a clear start and end, with tasks, events, and gateways executed in a predefined order. Processes are best suited for repeatable and predictable business operations such as order approvals or invoice processing.

To create a process on the platform, follow the steps below:

1. From the landing page, click the required project to open it. Then, in the main left navigation pane, click Process Design to open the Process Design page.
2. On the Process Design page, click the Add button in the top-right corner of the page and choose New from the dropdown.
    ![up-process-add-process](/resources/Storage/pulse-publication/images/up-process-add-process.png)
    Additionally, you can also choose to import a process.
3. The Process Designer page opens with a design canvas and a palette of process nodes. Drag the required nodes onto the canvas and connect them to create the process flow based on your business requirements.
    Configure each node by specifying the required properties. The configuration options vary depending on the node type. For example, for a Timer node, specify the duration for which the process should pause before resuming execution. The following example illustrates a process containing an intermediate Timer node configured to pause the process for 10 seconds before execution resumes.
    ![up-process-example-process](/resources/Storage/pulse-publication/images/up-process-example-process.png)
4. Provide a name for the process by replacing the default name with the required process name.
5. Click the Save icon in the top-right corner of the page to save the process. **Note**: Saving the process is a prerequisite for publishing it, and publishing the process is a prerequisite for deployment.
    ![up-process-and-publish-icons](/resources/Storage/pulse-publication/images/up-process-and-publish-icons.png)
6. After saving the process, click Publish in the upper-right corner of the page. A new version of the process is created when it is published. In the Publish dialog box, click Save to complete the publishing process.
    ![up-process-publish-process-save](/resources/Storage/pulse-publication/images/up-process-publish-process-save.png)

## Deploy

To deploy the process definition follow the steps below:

1. After a process is saved and published, it is displayed on the Process List page.
2. On the Process List page, select the checkbox preceding the name of the process that you want to deploy.
    ![up-process-definition-deploy1](/resources/Storage/pulse-publication/images/up-process-definition-deploy1.png)
3. After selecting the required process, click Deploy at the top of the page to deploy the selected process. **Note**: You can deploy multiple processes simultaneously by selecting multiple processes on the Process List page before clicking Deploy.
    ![up-process-definition-deploy2](/resources/Storage/pulse-publication/images/up-process-definition-deploy2.png)
4. In the dialog box, select the published version that you want to deploy from the Version drop-down list, and then click Deploy.
   ![up-process-definition-deploy3](/resources/Storage/pulse-publication/images/up-process-definition-deploy3.png)
