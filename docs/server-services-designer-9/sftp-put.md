# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/sftp-put>

**SFTP Put **node is used to upload one or more files from the folders.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Select SFTP Config: **The name of the config that connects to the **SFTP Server**.
  - If you have a textract config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new textract config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new textract config. See [Attributes for a new SFTP Config](/articles/server-services-designer-9/ftp/a/newsftpconfig) to know what are the properties to configure.
4. **Operation: **Select the operation that the node should perform. The operations include Get, FastGet, and DownloadDir.
  1. **Put**: Upload data from local system to remote server.
    1. **Remote path**: Path to the remote file to be created on the server.
    2. **Options**: Additional options passed to the Put operation.
    3. **Source**: Data source for data to copy to the remote server.
  2. **Fast Put**: Uploads the data in file at local Path to a new file on remote server using concurrency.
    1. **Remote ****path**: Path to remote file to create.
    2. **Options**: Additional options passed to the Fast Put operation.
    3. **Source**: Path to local file to upload.
  3. **Upload Dir:** Upload the directory specified by in the source to the particular destination.
    1. **Destination directory**: A remote file path specified as a string.
    2. **Source directory**: A local file path specified as a string.
5. **Result Mapping**: Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the file.
