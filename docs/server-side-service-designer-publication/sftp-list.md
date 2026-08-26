# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/sftp-list>

**SFTP List **node is used to retrieve a list of directories. This node returns a promise which on acknowledgment returns an object which contains the items in the directory.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Select SFTP Config: **The name of the config that connects to the **SFTP Server**.
  - If you have a textract config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new textract config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new textract config. See [Attributes for a new SFTP Config](/articles/server-side-service-designer-publication/ftp/a/newsftpconfig) to know what are the properties to configure.
4. **Operation: **Select the operation that the node should perform.
  - **List**: Retrieves a directory listing.
5. **Pattern: **This field is used to filter the items included in the returned array. A pattern can be a simple string or a regular expression. Select String in the drop-down list and enter the pattern. If you want to map this field to a bh.input, .bh, as is or bh.local property, select the property and enter the variable that contains the pattern. For example, select **string** as the property type and enter **/.*/ **to be the pattern.
6. **Remote Path: **The remote path to directory or file on the remote server. Select String in the drop-down list and enter the remote path. If you want to map this field to a bh.input, .bh, as is  or bh.local property, select the property and enter the variable that contains the remote path.
