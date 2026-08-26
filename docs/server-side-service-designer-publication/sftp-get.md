# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/sftp-get>

SFTP Get node helps you to retrieve a file from a remote SFTP server.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Select SFTP Config: **The name of the config that connects to the **SFTP Server**.
  - If you have an SFTP config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new textract config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new SFTP config. See [Attributes for a new SFTP Config](/articles/server-side-service-designer-publication/ftp/a/newsftpconfig) to know what are the properties to configure.
4. **Operation: **Select the operation that the node should perform. The operations include Get, FastGet, and DownloadDir.
5. **Result Mapping**: Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the data retrieved from the file.

---

### Attributes for different Operations

1. **Get**: Retrieve a file from a remote SFTP server.
2. **FastGet**: Downloads a file at remotePath to localPath using parallel reads for faster throughput. This is the simplest method if you just want to download a file.
  - **Local Path**: Path of the local file system for the downloaded file. The local path should include the filename to use for saving the file.
  - **Options**: Additional options for the fastGet operation.
  - **Remote Path: **Path to the remote file to download.
3. **DownloadDir**: Download the remote directory specified by srcDir to the local file system directory specified by destination dir.
  - **Source Directory**: A remote file path specified as a string.
  - **Destination Directory**: A local file path specified as a string.
