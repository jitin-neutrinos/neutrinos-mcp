# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/azure-storage-blob-node>

Azure Blob storage node is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that doesn't adhere to a particular data model or definition, such as text or binary data.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Azure Config: **The name of the config.
  - If you have an Azure config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new azure config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new azure config. See [Attributes for a new Azure Config](/articles/server-services-designer-9/azure-storage/a/newazurecongif) to know what are the properties to configure.
4. **Task Type: **Select the type of task that the node should perform.
  - **Create Blob**: Select this task type to create a blob.
  - **Read Blob**: Select this task type to read a blob.
  - **Delete Blob**: Select this task type to delete a blob.

Depending on the task type that you select, the attributes to configure changes.

**Create Blob**

- **Container name**: The name of the container for which you are creating a Blob.
- **Blob Name**: The name of the blob which must be a valid DNS (Domain Name System) name.
- **Blob Create Type**: Select the type of blob you are creating. The type of output can be either Block or a page.
- **Blob Input type**: Select the type of Input. The type of Input can be either a Local file or a Stream.
- **Blob Input**: Select String in the drop-down list and enter the Blob input. If you want to map this field to a bh.input, env, or bh.local property, click the **Map** icon, select the property, and enter the variable that contains the input for the Blob. If you choose env, enter the environment property which contains the value. Make sure that the environment property is added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before calling this property here.
- **Stream length**: The length of the Blob Input. The accepted value is a multiple of 512 bytes.

**Read Blob**

- **Container Name: **The name of the container from which you are reading a Blob.
- **Blob name: **The name of the blob which must be a valid DNS (Domain Name System) name.
- **Blob Output Type: **Select the type of output. The type of output can be either a Local file or a Stream.
- **Blob Output: **Select String in the drop-down list and enter the Output. If you want to map this field to a bh.input, env, or bh.local property, click the **Map** icon, select the property, and enter the variable in which the output should be stored. If you choose env, enter the environment property which contains the value. Make sure that the environment property is added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before calling this property here.

**Delete Blob**

- **Container name: ** The name of the container from which you are deleting a Blob.
- **Blob name: **The name of the blob which must be a valid DNS (Domain Name System) name.

5. **Params Object: **Map the key-value to the bh. bh.input or bh.local property, and enter the variable name. The variable name that you map should be of an object with the parameters defined. For example, bh.local.params = {"name" : "Branch", "products" : [Journeys,Email,Universal%20Ads].

6.** Result:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the Azure storage.
