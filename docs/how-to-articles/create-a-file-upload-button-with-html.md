# Step 1: Design the User Interface

<https://documentation.neutrinos.com/articles/#!how-to-articles/create-a-file-upload-button-with-html>

The **File Upload **button allows a user to choose one or more files (from their device storage) to be uploaded to a server.

Follow the example below to create a **File upload** button using which you can upload files and save them in the MongoDB Database. This button will also have an upload loading indicator, which will indicate the progress of the upload.

Perform the following steps:

#### Step 1: Design the User Interface

1. Create a page named **fileupload **(or any name of your choice).
2. Drag and drop a **Column** and set the following properties in the component's attributes window:
  - **style**: padding-top: 25px;
  - **fxLayoutgap**: 20px;
3. Drag and drop an **HTML ****5 **component inside the **Column** component.
  - Enter the following in the **Basic Properties** section:
    - **Element Type**: Click the **Edit **button next to this field and enter i**nput**.
    - **Style**: color:blue;
  - Add the following Key&Value pairs in the **Custom Properties **section:
    - **type**: file
    - **Multiple****Select**: multiple
    - **(change):** upload($event.target.files)
4. Switch to the TS editor of the page and enter the following code. The logic defined here triggers the server flow and renders the response to the page UI.
5. Drag and drop another **HTML ****5** component inside the **Column** component. Enter the following properties:
  1. **Style**: color:red;
  2. **Element type: **Div
6. Click the HTML editor and add the following text in the code editor and enter Upload Percent: {{percentDone}}
7. Switch to the TS editor and declare the percentDone variable inside the component class.
8. Drag and drop another **HTML 5** component inside the **Column** component. Set the **Element type** as **Div**.
9. Click the HTML editor of this HTML 5 and add the following text in the code editor and enter Upload Successful
10. Switch to the TS editor and declare the uploadSuccess variable inside the component class.

#### Step 2: Design Server Flows

Navigate to the [Server Services Designer](/smart/project-concepts/server-services-designer).

1. Create a service named **fileserver.**
2. Drag and drop an** HTTP In **node. This node is used to create an endpoint to upload a file. Enter the following properties:
  - **Method**: POST
  - **Path**: upload
  - Trigger **Accepts file upload **to **True**.
  - **Destination**: Memory
  - **File ****option**: Enter **file **in the **name **field and enter **5 **in the **max count** field. Click the **plus** icon.
3. Drag and drop a **script **node. This node Is used to define the logic for finding the length of the file.
  - Double click the node and enter the name as **file length**. In the code editor, enter the following code:
4. Drag and Drop a **switch** node. This node is used to define the conditions for the file upload. If the length of the file is greater than the index, then the file is uploaded. If the length of the file is less than the index, the file upload process will be terminated. Enter the following properties:
  - **property**: select** bh.** and enter** index**.
  - Set the following conditions. After entering each property, click **+ Add** to add the condition to the conditions list.
      **Condition**
      **Type**
      **Value**
      <
      bh.
      filelength
      >=
      bh.
      filelength
  - Select **stopping after first match **from the drop-down list.
5. Drag and drop a **script **node. This node is used to define the logic for assigning the file name and file path to variables. Double click the node and enter the name as **file path**. In the code editor, enter the following code:
6. Drag and drop a **MongoDB **node. This node is used to upload the files in the mongo database. Enter the following properties:
  - **Database Config: **Select your MongoDB database configuration. If you have no database configured, see [Mongo Database](https://www.mongodb.com/cloud/atlas/lp/try2-in?utm_source=google&utm_campaign=gs_apac_india_search_brand_atlas_desktop&utm_term=mongodb%20cluster&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=6501677905&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9HjzuaXaxiYmghWRTarnBNuO2_hPPxQnt4S-HDU-8WGucwwc4lhuFEaAnGEEALw_wcB) to learn how to configure a new MongoDB database connection.
  - **Collection: **Select **string** and enter **fileupload**
  - **Operation**: Select** uploadFile** from the drop-down list.
  - **File name:** Select **bh.** and enter **file**
  - **File Path: **Select **bh.** and enter **filepath**
  - **Result Mapping:** Select **bh.** and enter **response**
7. Drag and drop a **script **node. This node is used to define the logic for increasing the index of the variable that is used to compare with the file length. Double click the node and enter the name as **index.** In the code editor, enter the following code:
8. Connect the nodes in the following format:
9. ![Flow cnnect fasion 1](/resources/Storage/how-to-articles/Flow_connect_1.png)
10. The script node is connected back to the switch node because this flow is executed every time when a file upload process is initiated.
11. Next, drag and drop a **script **node. This node is used to define the logic for the success response. Double click the node and enter the name as **response.** In the code editor, enter the following code:
12. Drag and drop a **Catch **node. This node is used to catch errors that occur when executing this flow. Select **All nodes** in the **Catch Errors from** the field.
13. Drag and drop a **script **node. This node is used to define the logic for failure response. Double click the node and enter the name as response failure. In the code editor, enter the following code:
14. Drag and drop an **HTTP Out** node. This node is used to define the response of the execution of this flow. and enter the following:
  - Response Type: JSON
  - Status Code: Select **bh. **variable and enter **status**
  - **Response Body: **Select **bh.** variable and enter **response**
15. Here is how the complete flow should look at the end:
    ![flow server services](/resources/Storage/how-to-articles/file_upload_new_server_service.png)
16. Save your changes.
17. Initialize the app and preview the page.
18. Click Choose Files and upload one or more files.
    ![](/resources/Storage/how-to-articles/2021-06-15_12h43_10.png)
19. The files will be saved in the MongoDB Database.
