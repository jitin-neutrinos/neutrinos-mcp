# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/s3-upload>

**S3 Upload node **is used to upload files directly to the S3 storage.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Select AWS Config: **The name of the config that connects to the **AWS Server**.
  - If you have an AWS config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new textract config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new textract config. See [Attributes for a new AWS Config](/articles/server-side-service-designer-publication/aws-s3/a/newawsconfig) to know what are the properties to configure.
4. **Type of Operation: **Select the operation that the node should perform.
  - **Upload**
5. **Params Object: **Map the key-value to the bh. bh.input or bh.local property, and enter the variable name. The variable name that you map should be of an object with the parameters defined. For example, bh.local.params = {"name" : "Branch", "products" : [Journeys,Email,Universal%20Ads].
6. **Options**: The optional settings that you can perform for each operation that you select in the** Type of Operation** field. Map the options to bh. or bh.local properties and specify the variable name.
7. **Result:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the database.
