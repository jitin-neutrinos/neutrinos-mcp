# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-8/quotation-node>

The** Quotation** node is used to send a proposal quotation. See [eBAO documentation](https://demo.insuremo.com/api-mgmt-web/#operation/simpleQuoteUsingPOST) to learn more.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Config: **The name of the config.
  - If you have an eBaoCloud connection that is already configured, choose that config from the drop-down list.
  - If you want to configure a new eBaoCloud connection, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for EBAO Configuration](/articles/server-services-designer-8/ebao/a/h3_1457337614) to learn the properties to configure.
- **Client Request ID: **Optional. The external request ID.
- **Policy: **An object containing the policy information of the customer. Create an object in the [Script](/articles/server-services-designer-8/script-node) node and pass the object name in this field. The object should contain the following information:Copy CodeJavaScript"policy": {
    "customers": [],
    "issueDate": "2019-08-24T14:15:22Z",
    "policyType": 1,
    "applyDate": "2019-08-24T14:15:22Z",
    "discountType": "string",
    "installPrem": 0,
    "currency": 1,
    "inceptionDate": "2019-08-24T14:15:22Z",
    "expiryDate": "2019-08-24T14:15:22Z",
    "deliverType": "M",
    "quotationCode": "string",
    "submissionDate": "2019-08-24T14:15:22Z",
    "serviceAgentCode": "string",
    "salesChannelCode": "string",
    "insurerCode": "string",
    "preprintedProposalNumber": "string",
    "introducerNo": "string",
    "preDefinedPolicyNumber": "string",
    "preDefinedProposalNumber": "string",
    "policyPackage": {},
    "coverages": [],
    "policyHolder": {},
    "insureds": [],
    "beneficiaries": [],
    "payers": [],
    "payerAccounts": [],
    "trustees": [],
    "declarations": [],
    "agentDeclarations": [],
    "extendedProps": {}
   },
- **Extended Properties:** An object containing extended information such as Map type, and Key-Value. Create an object in the [Script](/articles/server-services-designer-8/script-node) node and pass the object name in this field. The object should contain the following information: Copy CodeJavaScript"extendedProps":
   {
    "property1": "string",
    "property2": "string"
   }
- **Result mappi****ng: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.
