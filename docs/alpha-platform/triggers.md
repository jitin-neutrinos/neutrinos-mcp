# Navigate

<https://documentation.neutrinos.com/articles/#!alpha-platform/triggers>

The triggers can initiate several functionality from the page. The below are triggers that can be called on the initialization of the page, click of a button, validating an input field, and so on.

## Navigate

Navigate from one page to another. You can choose to display an intermediary page before directing the Workbench user to the intended page.

 The GIF below demonstrates how to configure the navigation option to display the Enquiry Inbox upon page initialization.




 ![workflow-studio-navigate-on-init-gif](/resources/Storage/alpha-platform/images/workflow-studio-navigate-on-init-gif.gif)

Follow the steps below to navigate user to Enquiry inbox from a Global Page.

1. Click the Plus icon on the On Init trigger > Select **Navigate** from the available options > Expand the **Navigate** tab.
2. Choose from the available pages in the **Select Page** dropdown.
3. Click the **Save** button.
4. Navigate to Workbench > In Main Menu section, click the **New Case **page and observe the output.

## Dialog

You can configure the current page to display a dialog upon initialization. The GIF below demonstrates how to display a pop-up during page initialization to show a sample login page.




 ![workflow-studio-dialog-on-init-gif](/resources/Storage/alpha-platform/images/workflow-studio-dialog-on-init-gif.gif)

Follow the steps below to add a dialog on initialization of the page:

1. Click the Plus icon on the On Init trigger > Select **Dialog** from the available options > Expand the **Dialog** tab.
2. Choose from the available pages in the **Select pop-up** dropdown.
3. Set the **Width**, **Height**, and **Header** for the pop-up screen. Note, if the width and height values are not supplied, by default it would be 50%.
4. Click the **Save** button.
5. Navigate to Workbench > In Main Menu section, click the **New Case **page and observe a dialog displayed as the output.

## Custom Code

Choose to write a custom JavaScript on initialization of the page. The GIF below illustrates how to add a custom code to display an alert on initialization of the page.




 ![workflow-studio-on-init-custom-code-gif](/resources/Storage/alpha-platform/images/workflow-studio-on-init-custom-code-gif.gif)

Follow the steps below to add custom code:

1. Click the Plus icon on the On Init trigger > Select **Custom Code **from the available options > Expand the **Custom Code **tab.
2. Write the JavaScript code as per requirement.
3. Click the **Save** button.
4. Navigate to Workbench > In Main Menu section, click the **New Case **page and observe an alert displaying "Hello, this is Alpha application" as the output.

| ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png) | In future releases, adding custom code in this format will be deprecated. To add custom code, refer to the [Global Custom Code](/articles/alpha-platform/global-custom-code) topic. However, existing custom code implementations will continue to function without interruptions in current projects. |
| --- | --- |

| ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png) | Note: When using custom code with inbox triggers, the Inbox Projection feature requires you to explicitly specify any keys that are not configured as part of the inbox columns. For more information, refer to the [Inbox Projection](/articles/alpha-platform/inbox-projection) topic. |
| --- | --- |

## Case Service

Call any Case Service API. For example, Create Case, Get Case, Add case comments, Delegate case to User, take a Decision, and so on. Follow the steps below to add a Case Service. The example illustrates how to add Case Service to perform a Case Decision in a workflow. The GIF below illustrates how to add Case Service in a task page to perform a Case Decision in a workflow **On Init**.

![workflow-studio-case-service-case-decision-gif](/resources/Storage/alpha-platform/images/workflow-studio-case-service-case-decision-gif.gif)

1. Click the Plus icon on the On Init trigger > Select **Case Service** from the available options > Expand the **Case Service **tab.
2. Choose Case Decision.
3. Enter the following details:
    **Field**
    **Value**
    cid (required)
    It accepts value that uniquely identifies the case. It can be through Case Instance, Task Instance, CO, Session, or Local, and so on.
    taskId (required)
    It accepts value that uniquely identifies the task. It can be through Case Instance, Task Instance, CO, Session, or Local, and so on.
    userName (required)
    It accepts value that uniquely identifies the user. It can be through CO, Session, string or Local, and so on.
    Decision Input (required)
    It accepts the input value that will determine the workflow decision outcome.
    Output Mapping (optional)
    If the output of the decision needs to be stored for further processing, this field can be used. It can be either CO or Local object.
    ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png)
    The Decision Inputs in this example is passed as a local value written in a custom code.
4. Click the **Save** button.
5. Navigate to Workbench > From My Tasks inbox, click a case > In the task pages, go to "New Case" page > observe the output.
    ![Note](/resources/Storage/alpha-platform/project-trailproject/note.png)
    If a Case Service is applied to Global Pages and accessed via Main Menu navigation, ensure you provide the applicable values to pass to the Case Services.

## API Request

External APIs can be integrated to send and receive information or data. The example below demonstrates how to fetch all cases. Follow the steps below to add an API request using the POST method on a task page, triggered by a button click to retrieve cases.

1. In a task page, drag and drop a button > Double-click a button and enter the name for a button.
    ![triggers-api-request-add-button](/resources/Storage/alpha-platform/images/triggers-api-request-add-button.gif)
2. Navigate to the **Trigger** section, select the **Add Trigger** button, and choose **On Click**. Next, click the **Plus** button and select **API Request**.
    ![trigger-api-request-button-add-trigger](/resources/Storage/alpha-platform/images/trigger-api-request-button-add-trigger.gif)
3. Expand the API Request trigger added in the previous step. Add the below details:
    ![triggers-api-request-add-trigger-details](/resources/Storage/alpha-platform/images/triggers-api-request-add-trigger-details.gif)
  1. **Method**: This supports HTTP methods such as GET, POST, PUT, and DELETE. Select the appropriate method based on the API's requirements. You can provide the parameters to this method either through a string or an Environmental Variable configured.
  2. **Path**: Accepts the actual path of the API endpoint.
  3. **Query Params**: Accepts the query parameters. It is an optional field.
  4. **Headers**: Accepts parameters to be sent in the API call header. It can specify either **Content-Type**, **Authorization**, or **Custom-Header**.
      **Type**
      **Options**
      Content-Type
      application/json, application/xml, application/x-www-form-unlencoded, multipart/form-data, text/plain, image/jpeg, image/png, application/pdf
      Authorization
      CO, Case Instance, Task Instance, Event, Number, String, Boolean, Environment, Local, Trigger Result
      Custom-Header
      CO, Case Instance, Task Instance, Event, Number, String, Boolean, Environment, Local, Trigger Result
  5. **API Authorization**: Supports various authorization methods for the API, including:
    1. None.
    2. Client (accepts Client ID and Client Secret).
    3. Bearer (accepts a bearer token from the IDS).
    4. Basic (accepts a username and password).
  6. **Before Request**: Accepts custom code that can be executed before the API request.
  7. **Output Mapping**: Map the results returned by the API to the desired variables or fields. The fields can be CO (case object), Case Instance, Task Instance, or a Local variable.
  8. **After Response**: Accepts custom code that can be executed after the API response. This is used to retrieve selected information from the API response.
  9. **Add Toast**: Create a toast message to notify users in case of **success** or **failure**.
4. After configuring a button to trigger an API call, create a UI element to handle and display the API response by dragging and dropping a table that can display the response data.
    ![trigger-api-request-add-table](/resources/Storage/alpha-platform/images/trigger-api-request-add-table.gif)
5. Double-click the table added to the page. Under the Basic section, provide the following details:
  1. **Data Source**: Specify the data source from which the table should retrieve the information.
      **Type**
      **Description**
      CO
      Map the data source to the corresponding object of the CO
      API
      Enter the details for Method, Path, Query Params, Header, API Authentication, Before Request, and so on.
      Reels
      Enter the name of the Master Data from which the information should be fetched.
      DMS
      Specify the operation to be performed and provide the necessary details required to process the request.
      Local
      Specify the variable name from which the information should be fetched.
  2. In this illustration, the Case Object (CO) is used. After selecting the CO, enter the case object name specified in the previous step during output mapping.
      ![trigger-api-request-add-datasource](/resources/Storage/alpha-platform/images/trigger-api-request-add-datasource.gif)
  3. Click the Plus button under Columns to add columns for displaying the data retrieved from the API. Create the required number of columns based on your needs. Provide a name and title for each column based on the data retrieved from the API.
      ![trigger-api-request-add-columns](/resources/Storage/alpha-platform/images/trigger-api-request-add-columns.gif)
6. Save the changes done in the Workflow Studio, and navigate to the Workbench.
7. Click on a case, navigate to the task page, and select the Fetch All Cases button. Observe the cases populated in the table.
    ![triggers-api-request-complete](/resources/Storage/alpha-platform/images/triggers-api-request-complete.gif)

## Reels

Reels can be triggered to fetch the Master Data or Products from reels.

### Master Data

The below section demonstrates fetching the data from the Reels Master Data to a table on a button click.

1. In a task page, drag and drop a button > Double-click a button and enter the name for a button.
    ![alpha-reels-master-data-fetch-1](/resources/Storage/alpha-platform/images/alpha-reels-master-data-fetch-1.gif)
2. Navigate to the **Trigger** section, select the **Add Trigger** button, and choose **On Click**. Next, click the **Plus** button and select **Reels**
    ![alpha-reels-master-data-fetch-2](/resources/Storage/alpha-platform/images/alpha-reels-master-data-fetch-2.gif)
3. Expand the Reels trigger added in the previous step. Add the below details:
    ![alpha-reels-master-data-fetch-3](/resources/Storage/alpha-platform/images/alpha-reels-master-data-fetch-3.gif)
    For this example, Master Data is selected.
  - **Domain URL**: This field contains the base URL of the Reels Master Data. It is automatically populated when the Reels trigger is added through the trigger configuration.
  - **Select Features**: Use this dropdown to choose between **Products** or **Master Data**.
    - **Products**: Rules created within the Reels platform.
    - **Master Data**: Master Data created within the Reels platform.
4. Once Master Data is selected, you are prompted to choose the Master Data file created in the Reels platform, which will be triggered from the Alpha platform.
    ![alpha-reels-master-data-fetch-4](/resources/Storage/alpha-platform/images/alpha-reels-master-data-fetch-4.gif)
5. After selecting the Master Data file, you are prompted to choose either a tag or a version of the file. This allows you to select the appropriate version of the Master Data file to be triggered from the Alpha platform based on your requirement.
    In this example, the Version of the Master Data file is selected for illustration purposes.
  - **Tag**: Tags are associated with a Master Data file to help differentiate between its versions. A single version of a Master Data file can have multiple tags.
  - **Version**: Represents the different versions of a Master Data file, for example, 1.0.0, 1.0.1, and so on.
6. Once the Version is selected from the dropdown, specify the following:
    **Field**
    **Description**
    Inputs
    multiplicity
    Specifies whether multiple values or a single value matching the selected criteria should be fetched.
    select
    Specifies the values to be selected from the Master Data file. You can choose the required columns from the available Master Data values.
    distinct
    Specifies the Distinct operation to fetch non-duplicate data from the Master Data file. You can select the column on which the Distinct operation should be applied.
    Filter
    key
    Specifies the key on which the fetched content from the Master Data file should be filtered before generating the output.
    Output
    success
    Indicates a boolean value that specifies whether the action performed was successful.
    statusCode
    Specifies the status code that is returned from the trigger.
    records
    Contains all the information returned from the trigger, including data from the Master Data file if the trigger is configured to call Master Data.
    totalRecords
    Contains the number that specifies the total records returned from the trigger call to the Master Data.
    message
    Contains the message returned upon the execution of the trigger. The message can be either a success message or an error message, depending on the value of the success boolean key.
    For this example, the Reels trigger is configured to fetch all the data from the mapped Master Data file into a CO variable. This variable can later be mapped as the data source for a table in subsequent steps.
    ![alpha-reels-master-data-fetch-5](/resources/Storage/alpha-platform/images/alpha-reels-master-data-fetch-5.gif)
7. Once all the required fields are filled, save the trigger and preview the configuration from the workbench. In this example, the Reels trigger is used to fetch data from the Master Data configured in the Reels platform. The retrieved data is then mapped to a table, which will be populated when the button is clicked.
8. In this step, drag and drop a table component and configure it to display the data fetched from the button-click trigger.
  - In a task page, drag and drop a table > Double-click the table > Navigate to the basic section of the attributes.
  - In the Basic section, set the Data Source to the CO object created to fetch the records, as shown in the GIF below:
      ![alpha-reels-master-data-fetch-6](/resources/Storage/alpha-platform/images/alpha-reels-master-data-fetch-6.gif)
  - After mapping the CO object to the table, add the required columns to fetch and display data from the Master Data file. To do this, click the plus (+) button in the Columns section, then provide the Column Name and the corresponding Value to be displayed.
      ![alpha-reels-master-data-fetch-7](/resources/Storage/alpha-platform/images/alpha-reels-master-data-fetch-7.gif)
  - Click Save, and then preview the trigger in the workbench by clicking Preview.
      ![alpha-reels-master-data-fetch-8](/resources/Storage/alpha-platform/images/alpha-reels-master-data-fetch-8.gif)

Alternatively, you can use Tags to choose between different versions of the Master Data file available on the Reels platform. The GIF below illustrates how to select a Master Data file using Tags under Triggers.




 ![alpha-reels-master-data-tags-usage](/resources/Storage/alpha-platform/images/alpha-reels-master-data-tags-usage.gif)

### Products

While the previous section explained selecting Master Data, you can also configure Products (rules) created on the Reels platform to be triggered from the Alpha platform. The process of configuring triggers for Products is the same as for Master Data. You can specify the Tag or Version of the Product on the selected components to trigger the corresponding rules from the Reels platform.




 ![alpha-reels-products-fetch](/resources/Storage/alpha-platform/images/alpha-reels-products-fetch.png)

After selecting the desired product and version, provide the necessary details—including headers, inputs, filters, and output values—to trigger the rules according to your specific requirements. For example, the screenshot below displays a sample layout that includes the fields where you must provide input values for a specific product (rule):

![alpha-reels-product-headers](/resources/Storage/alpha-platform/images/alpha-reels-product-headers.png)
DMS

Manage documents from DMS service.

## CMS

Manage content using CMS service.
