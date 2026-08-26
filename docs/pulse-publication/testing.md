# Single Test

<https://documentation.neutrinos.com/articles/#!pulse-publication/testing>

Testing a created rule, rule group, or workflow is essential to ensure it functions as expected. Since upstream services consume these rules through API calls, thorough testing helps validate their behavior. This topic provides details on how to perform testing on rules.

Rules in Neutrinos Reels can be tested using three methods:

- **Single tests**: In this type of test, a single input value is used, and the output is verified.
- **Bulk tests**: In this type of test, multiple input values are passed to the rule through an excel sheet, and the output is verified.
- **API tests**: This testing method allows you to validate the rule's output by downloading the **Swagger** documentation and testing it in **Postman**.

## Single Test

To perform a single test on a rule, or rule group, or a workflow follow the steps below:

| ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png) | Note that the following steps use a decision table rule as an example. The same approach applies to all rule types. |
| --- | --- |

1. Click the Testing tab on the Rule Details page. The image below illustrates the layout of the Testing tab, which includes details such as the Run ID, the version of the rule that was tested, the date the test was run, the user who executed the test, the test status (success or failure), the input provided, and the output results.
    ![testing-layout](/resources/Storage/pulse-publication/images/rule-testing-layout.png)
2. This will open the summary page, which displays an overview of the testing performed on the rule. You can add a new test by clicking the **Add** button in the top-right corner of the page.
3. Choose either a **Single** Test or a **Bulk** Test.
4. In the **Sandbox Testing** page, select the version of the rule you wish to test from the dropdown at the top of the page.
5. Enter the input values and click the **Calculate** button to test the rule.

The GIF below illustrates a sample test performed on a Rule.

![decision-table-testing](/resources/Storage/pulse-publication/images/decision-table-testing.gif)

Additionally, you can add tags to specify which version of the rule should be used by upstream services. You can also configure the keys for testing by clicking the Configure button. For more details, refer to the [Configurations](/smart/project-neutrinos-reels/configurations) topic.

## Bulk Testing

Bulk testing allows you to test multiple inputs and expected outputs using a template in the form of an Excel sheet. The sheet, containing input values and corresponding expected results, is uploaded to the **Reels** platform for testing. The platform displays the test results, indicating how many inputs passed or failed. A detailed log of the results is stored and can be viewed under the **Bulk** section in the **Testing** tab.

To perform a **Bulk** test for a rule, rule group, or workflow follow the steps below:

1. Click the **Testing** tab on the Rules Details page. The image below illustrates the layout of the Testing tab, which includes details such as the Run ID, the version of the rule that was tested, the date the test was run, the user who executed the test, the test status (success or failure), the input provided, and the output results.
    ![testing-bulk](/resources/Storage/pulse-publication/images/testing-bulk.png)
2. The **Bulk Testing** page allows you to upload an Excel sheet containing test data. If you already have a test sheet, upload the file. Otherwise, download the template for the specific rule being tested, which includes the required columns for data entry. The image below shows a sample template Excel sheet for a **Decision Table** rule. It includes one input and one output field, populated with corresponding test data:
    ![testing-bulk-sample](/resources/Storage/pulse-publication/images/testing-bulk-sample-data.png)
3. Prepare the Excel sheet and upload it for testing the rule. Enter a test name and click **Save** to proceed with the test.
4. Once the test is complete, go to the **Bulk** section in the **Testing** tab to view the results. Expand the test to see the detailed breakdown of passed and failed test cases. The GIF below illustrates the bulk testing for a decision table rule:
    ![testing-bulktesting](/resources/Storage/pulse-publication/images/testing-bulktesting.gif)

## API Testing

The created Rules, Rule Groups, and Workflows can be viewed as JSON. You can test them in Postman by downloading their corresponding Swagger documentation.

To perform **API** testing using Postman, follow the steps below:

1. In the sub-module navigation bar, click **Rule**, **Workflow**, or **Master Data**, then select a specific rule, rule group, workflow, or master data to open its details page. On the details page, navigate to the **Deployment** section and click **Download Swagger**.
    ![download-swagger](/resources/Storage/pulse-publication/images/download-swagger.gif)
2. Open the Swagger documentation (import) downloaded from the Reels platform.
    ![swagger-rule-import](/resources/Storage/pulse-publication/images/swagger-rule-import.gif)
    The Swagger for any rule contains three API endpoints:
    ![swagger-integra-rule-end-points](/resources/Storage/pulse-publication/images/swagger-integra-rule-end-points.png)
  1. **Runtime Sync:** Provides the result synchronously after rule execution.
  2. **Runtime:** Returns a **Run ID** immediately, even before the rule is executed. You can also configure a **webhook** to receive the result automatically.
  3. **Get Rule Execution Result:** Accepts the **Run ID** to retrieve the final output once execution is complete.
3. Click the **Authorize** button in Swagger. Provide the bearer token obtained from IDS by entering "Bearer " followed by a space and then pasting the token. Alternatively, you can use a token generated from the Reels platform for authorization.
4. Navigate to any endpoint. Here, for instance, we are using the Runtime Sync endpoint. Expand its section. Then, enter the following details:
  1. **ruleID**: Specifies the rule ID. This field is pre-filled and does not require editing.
  2. **caseId**: An optional field that represents the case ID.
  3. **Version**: Specifies the version of the rule. This field is pre-filled and does not require editing unless you want to execute a different version and know its version number.
  4. **inputObj**: An array of objects that serves as input for the API. It contains all the input keys defined in the rule during its creation on the Reels platform.
  5. **subFlowIDs**: An array that accepts the IDs of sub-flow rules, if required. This is an optional field.
5. In the expanded section, click the **Try it out** button to make the request body editable. Then, enter the required details as defined in the rule. In the below example, we provide the information for the inputObj as:
    You can remove the unnecessary fields like caseID and other fields, which are not required to execute the rule.
  1. inputAge: 19
6. Click the Execute button to run the API. The result "Eligible" will be returned and can be viewed by scrolling down the page. Note that a 200 status code indicates a successful execution. If an error occurs during execution, a specific error code will be returned.

The GIF below demonstrates how to test a rule in **Swagger**:

![testing-api-rule](/resources/Storage/pulse-publication/images/testing-api-rule.gif)

[Next Topic](/articles/pulse-publication/integration)

[Previous Topic](/articles/pulse-publication/master-data-versioning)
