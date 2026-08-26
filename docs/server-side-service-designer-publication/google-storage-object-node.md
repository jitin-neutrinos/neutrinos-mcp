# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/google-storage-object-node>

The storage objects are pieces of data that can be uploaded to google storage. Every object resides in a Storage bucket.

The **Storage Object** node allows you to create and delete objects.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Storage Config: **The name of the config.
  - If you have a Storage config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new storage config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new storage config. See [Attributes for a new Storage Config](/articles/server-side-service-designer-publication/google-storage/a/newgoogleconfig) to know what are the properties to configure.
4. **Task Type: **Select the type of task that the node should perform.
  - **Create Object**: Select this to create an object.
  - **Read Object**: Select this to Read an object.
  - **Delete Object**: Select this to delete an object.
5. **Bucket name: **The name of the bucket you are Creating or Deleting an object.
6. **Source**: Enter a file path to perform the operation that you have selected in the **Task Type** field.
7. **Destination**: Enter the destination file path to read a file. **This field appears only when you select Read Object as the operation in the Task type field.**
8. **Params Object: **Map the key-value to the bh. bh.input or bh.local property, and enter the variable name. The variable name that you map should be of an object with the parameters defined. For example, bh.local.params = {"name" : "Branch", "products" : [Journeys,Email,Universal%20Ads].
9. **Result Mapping:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that holds the path of the output file. For example, if you specify bh.local.result in this field, then that property will hold the data retrieved from google storage.

### Attributes for a new Storage Config

For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name**: The name of the config.
- **Key Filename: **Upload a file that contains the key of the Google Storage Account
- **Project ID(String)**: Enter the project ID to authenticate your storage account. You can fetch the project id from the storage key file JSON.
