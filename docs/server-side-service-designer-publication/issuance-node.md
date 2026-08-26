# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/issuance-node>

The** Issuance** node is used to issue the policy after the premium is collected. See [eBAO documentation](https://demo.insuremo.com/api-mgmt-web/#operation/issueUsingPOST_1) to learn more.

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you enter in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Config: **The name of the config.
  - If you have an eBaoCloud connection that is already configured, choose that config from the drop-down list.
  - If you want to configure a new eBaoCloud connection, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for EBAO Configuration](/articles/server-side-service-designer-publication/ebao/a/h3_1457337614) to learn the properties to configure.
- **Client Request ID: **The external request ID.
- **Policy: **An object containing the policy information. Create an object in the [Script](/articles/server-side-service-designer-publication/script-node) node and pass the object name in this field. The object should contain the following information:Copy CodeJavaScript"policy": {
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
- **Collection:** An object containing the payment information. Create an object in the [Script](/articles/server-side-service-designer-publication/script-node) node and pass the object name in this field. The object should contain the following information: Copy CodeJavaScript"collection":
   {
    "collectionDate": "2019-08-24T14:15:22Z",
    "premPurpose": "string",
    "payMode": 3,
    "currency": 1,
    "feeAmount": 2314,
    "paymentPlatform": "0",
    "thirdPtyPayNO": "string",
    "extendedProps": {}
   },
- **Extended Properties:** An object containing extended information such as Map type, and Key-Value. Create an object in the [Script](/articles/server-side-service-designer-publication/script-node) node and pass the object name in this field. The object should contain the following information: Copy CodeJavaScript"extendedProps":
   {
    "property1": "string",
    "property2": "string"
   }
- **Result mappi****ng: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.
