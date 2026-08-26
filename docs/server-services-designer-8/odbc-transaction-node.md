# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/odbc-transaction-node>

A **transaction** is a batch of one or more SQL statements. It groups SQL statements so that they are either all committed, which means they are applied to the database, or all rolled back, which means they are undone from the database.

The **Transaction** node is used to begin, commit, or rollback a transaction on the database.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Select ODBC Config: **The name of the config.
  - If you have an existing OBDC connection, choose that config from the drop-down list.
  - If you want to configure a new ODBC Connection, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for ODBC Configuration](/articles/server-services-designer-8/odbc/a/ODBC Configuration) to learn the properties to configure.
- **Select Operation: **The operation to be performed on the transaction. Options include:In a service flow, you should always start a transaction by issuing the **Begin Transaction** operation. After the transaction is complete, you should either issue the **Commit Transaction **operation or the **Rollback Transaction **operation. If no operation is specified, by default, the transaction will be rolled back.
  - **Begin transaction:** To begin a transaction.
  - **Commit transaction: **To apply the changes to the database.
  - **Rollback Transaction: **To undo the changes from the database.
