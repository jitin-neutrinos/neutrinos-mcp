# Associated Attributes

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/remove-node>

The** Remove** node is used to delete a record or records from the object store in the [IndexDB database](/articles/service-designer-user-s-guide/indexed-db-node).

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Store Name:** The object store on which you want to perform transactions. Enter the [flow object](/articles/service-designer-user-s-guide/service-designer-variables)containing the object store name.
4. **Primary Key Path Value:** The primary key path of the record(s) that you want to delete.
5. **Transaction Object: **Optional. The result mapping variable of the [Transaction](/articles/service-designer-user-s-guide/transaction-node) node.
6. **Result Mapping:** The result of the operation. Enter the [flow object](/articles/service-designer-user-s-guide/service-designer-variables)in which you want to save the result.
