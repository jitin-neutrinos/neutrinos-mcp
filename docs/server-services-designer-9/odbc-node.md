# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/odbc-node>

The **Open Database Connectivity (ODBC)** node is used to perform operations on data available in a variety of Relational Database Management Systems(RDBMS).

If you want to manually commit or roll back the changes made to the database, you can create a service flow by using the [Transaction](/articles/server-services-designer-9/odbc-transaction-node) node before and after the ODBC node to begin and commit/rollback the transaction.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Select ODBC Config: **The name of the config.
  - If you have an existing OBDC connection, choose that config from the drop-down list.
  - If you want to configure a new ODBC Connection, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for ODBC Configuration](/articles/server-services-designer-9/odbc/a/ODBC Configuration) to learn the properties to configure.
- **SQL Query: **A SQL query to be executed. Can optionally be given parameter markers (?) and also given an array of values to bind to the parameters.
  - Choose **string **from the drop-down list and enter the query such as:
      Copy CodePL/SQLINSERT INTO odbctest.student (Name, Class) VALUES('abc', '6th');
  - or map the query to a flow object in a script node, and enter the variable name. For example:
      ![](/resources/Storage/server-services-designer-9/script_insert.png)
- **Parameters:** Optional. An array of values to bind to the parameter markers (if any). The number of values in this array must match the number of parameter markers in the SQL statement. For example, if the SQL Query is select * from odbctest.student where class = ?', bh.param;, then bh.param can be bh.param = ['6th'];.
- **Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.
