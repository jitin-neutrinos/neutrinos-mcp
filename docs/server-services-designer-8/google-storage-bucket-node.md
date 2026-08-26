# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/google-storage-bucket-node>

Google Storage buckets are basic containers used to hold any type of data. Every data stored in google storage must be contained in a bucket. These buckets can be used to organize data and control access to the data stored.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Storage Config: **The name of the config.
  - If you have a Storage config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new storage config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new storage config. See [Attributes for a new Storage Config](/articles/server-services-designer-8/google-storage/a/newgoogleconfig) to know what are the properties to configure.
4. **Task Type: **Select the type of task that the node should perform.
  - **Create Bucket**: Select this to create a bucket.
  - **Delete Bucket**: Select this to delete a bucket.
5. **Bucket name: **The name of the bucket you are Creating or Deleting.
6. **Params Object: **Map the key-value to the bh. bh.input or bh.local property, and enter the variable name. The variable name that you map should be of an object with the parameters defined. For example, bh.local.params = {"name" : "Branch", "products" : [Journeys,Email,Universal%20Ads].
7. **Result:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from google storage.
