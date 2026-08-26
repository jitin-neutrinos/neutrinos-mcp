# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/sftp-command>

**SFTP Command node **is used to write command line interface for using the SFTP protocol. It transfers files securely over a network connection.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Select SFTP Config: **The name of the config that connects to the **SFTP Server**.
  - If you have a textract config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new textract config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new textract config. See [Attributes for a new SFTP Config](/articles/server-services-designer-8/ftp/a/newsftpconfig) to know what are the properties to configure.
4. **Operation: **Select the operation that the node should perform.
  - **Exists:** Tests to see if remote file or directory exists. Returns type of remote object if it exists or false if it does not.
    - **Remote path:** The remote path to directory or file on the remote server. Select String in the drop-down list and enter the remote path. If you want to map this field to a bh.input, .bh, as is  or bh.local property, select the property and enter the variable that contains the remote path.
  - **Stat: **Returns the attributes associated with the object pointed to by path.
    - **Remote path: **The remote path to directory or file on the remote server. Select String in the drop-down list and enter the remote path. If you want to map this field to a bh.input, .bh, as is  or bh.local property, select the property and enter the variable that contains the remote path.
  - **Append: **Append the input data to an existing remote file. There is no integrity checking performed apart from normal writeStream checks. This function simply opens a writeStream on the remote file in append mode and writes the data passed in to the file.
    - **Remote path: **The remote path to directory or file on the remote server. Select String in the drop-down list and enter the remote path. If you want to map this field to a bh.input, .bh, as is  or bh.local property, select the property and enter the variable that contains the remote path.
    - **Options: **Options to pass to writeStream
    - **Input:** Data to append to remote file
  - **Make directory: **Create a new directory. If the recursive flag is set to true, the method will create any directories in the path which do not already exist. Recursive flag defaults to false.
    - **Remote path:** The remote path to directory or file on the remote server. Select String in the drop-down list and enter the remote path. If you want to map this field to a bh.input, .bh, as is  or bh.local property, select the property and enter the variable that contains the remote path.
    - **Recursive: If true, create any missing directories in the path as well **
  - **Remove Directory**: Removes the specified listener from the event specified in eventType. Note that the end() method automatically removes all listeners from the client object.
    - **Remote path: **The remote path to directory or file on the remote server. Select String in the drop-down list and enter the remote path. If you want to map this field to a bh.input, .bh, as is  or bh.local property, select the property and enter the variable that contains the remote path.
    - **Recursive: **If true, create any missing directories in the path as well
  - **Delete: **Delete a file on the remote server.
    - **Remote path: **The remote path to directory or file on the remote server. Select String in the drop-down list and enter the remote path. If you want to map this field to a bh.input, .bh, as is  or bh.local property, select the property and enter the variable that contains the remote path.
  - **Rename: **Rename a file or directory from fromPath to toPath. You must have the necessary permissions to modify the remote file.
    - **From path:** Path to existing file to be renamed
    - **To path: **Path to new file existing file is to be renamed to. Should not already exist.
  - **PosixRename: **This method uses the openssh POSIX rename extension introduced in OpenSSH.
    - **From path: **Path to existing file to be renamed.
    - **To path: **Path for new name. If it already exists, it will be replaced by file specified in fromPath.
  - **Change the mode: **Change the mode (read, write or execute permissions) of a remote file or directory.
    - **Remote path**: The remote path to directory or file on the remote server. Select String in the drop-down list and enter the remote path. If you want to map this field to a bh.input, .bh, as is  or bh.local property, select the property and enter the variable that contains the remote path.
    - **Mode: ** New mode to set for the remote file or directory.
  - **Current remote working directory: **Returns what the server believes is the current remote working directory.
