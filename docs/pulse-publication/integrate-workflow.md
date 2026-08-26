# Integrate Workflow

<https://documentation.neutrinos.com/articles/#!pulse-publication/integrate-workflow>

To integrate a Workflow, follow the steps below:

1. In the sub-module navigation bar, click **Workflow**, then choose a specific workflow to open its details page. On the details page, navigate to the **Deployment** section and click **Download Swagger**.
    ![workflow-download-swagger](/resources/Storage/pulse-publication/images/workflow-download-swagger.png)
2. Open the Swagger documentation (import) downloaded from the Reels platform.
    ![swagger-import-workflow](/resources/Storage/pulse-publication/images/swagger-import-workflow.gif)
    The Swagger for any workflow contains three API endpoints:
    ![swagger-workflow-endpoints](/resources/Storage/pulse-publication/images/swagger-workflow-endpoints.png)
  1. A runtime synchronous endpoint that returns results synchronously.
  2. An asynchronous runtime endpoint that returns a result before the workflow execution is complete. This result can be accessed through a webhook.
  3. The Get Execution Result endpoint can also retrieve results from an asynchronous call.
3. Click the **Authorize** button in Swagger. Provide the bearer token obtained from IDS by entering "Bearer " followed by a space and then pasting the token. Alternatively, you can use a token generated from the Reels platform for authorization.
4. Navigate to any endpoint. Here, for instance, we are using the **Runtime**** Sync** endpoint. Expand its section. Then, enter the following details:
  1. **workflowID**: Specifies the ruleGroupID. This field is pre-filled and does not require editing.
  2. **caseId**: An optional field that represents the case ID.
  3. **Version**: Specifies the version of the rule. This field is pre-filled and does not require editing unless you want to execute a different version and know its version number.
  4. **inputObj**: An array of objects that serves as input for the API. It contains all the input keys defined in the rule during its creation on the Reels platform.
  5. **subFlowIDs**: An array that accepts the IDs of sub-worflows, if required. This is an optional field.
5. In the expanded section, click the **Try it out** button to make the request body editable. Then, enter the required details as defined in the rule group. In the below example, we provide the information for the inputObj as:
    You can remove the unnecessary fields like caseID and other fields, which are not required to execute the workflow.
  1. basePremium: 10000
  2. inputAge: 19
  3. inputGender: "Male"
6. Click the **Execute** button to run the API. The result will be returned and can be viewed by scrolling down the page. Note that a 200 status code indicates a successful execution. If an error occurs during execution, a specific error code will be returned.

The GIF below illustrates how to execute a workflow using Swagger:




 ![swagger-execute-workflow](/resources/Storage/pulse-publication/images/swagger-execute-workflow.gif)

[Next Topic](/articles/pulse-publication/integrate-master-data)

[Previous Topic](/articles/pulse-publication/integrate-rule-group)
