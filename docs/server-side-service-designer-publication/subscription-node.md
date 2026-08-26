# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/subscription-node>

The AWS SNS **Subscription node** is used to subscribe an endpoint to an Amazon SNS topic. Using the Subscription node you can perform the following actions:

- [Subscribe](/articles/server-side-service-designer-publication/subscription-node/a/h4__419851974)
- [Unsubscribe](/articles/server-side-service-designer-publication/subscription-node/a/h4__2018652737)
- [List subscriptions](/articles/server-side-service-designer-publication/subscription-node/a/h4_446146768)
- [List subscriptions by topic](/articles/server-side-service-designer-publication/subscription-node/a/h4__1865693262)
- [Confirm subscription](/articles/server-side-service-designer-publication/subscription-node/a/h4_1231541725)

### Associated Attributes

- **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name** field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
- **Select AWS Config: **The name of the config.
  - If you have an Amazon config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new Amazon config, select **Add new config** from the drop-down list and click the **Map** icon to create a new configuration. See [Attributes for a new Amazon Configuration](/articles/server-side-service-designer-publication/textract-node/a/h3_1541343129) to know what are the properties to configure.
- **Select Operation:** Select the [Subscribe operation](/articles/server-side-service-designer-publication/subscription-node/a/h3__1139094956) to be performed. Based on the operation you choose, the attributes list will differ.

---

### Subscribe Operations

#### Subscribe

Subscribe to a topic. See [the Amazon documentation on Subscribe Topic](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html) to learn more.

- **Protocol: **The protocol that you want to use. Supported protocols include:
  - **http** – delivery of JSON-encoded message via HTTP POST
  - **https** – delivery of JSON-encoded message via HTTPS POST
- **Topic ARN:** The ARN of the topic you want to subscribe to.
- **Attributes: **The list of attributes to subscribe to the topic.
- **Endpoint:** The endpoint that you want to receive notifications. Endpoints vary by protocol:
- **ReturnSubscribeARN: **Sets whether the response from the Subscribe request includes the subscription ARN, even if the subscription is not yet confirmed. If you set this parameter to true, the response includes the ARN in all cases, even if the subscription is not yet confirmed. The default value is **false**.
- **Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

#### Confirm Subscription

Verifies an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action. If the token is valid, the action creates a new subscription and returns its Amazon Resource Name (ARN). This call requires an AWS signature only when the AuthenticateOnUnsubscribe flag is set to true.

See [Amazon's documentation on Confirm Subscription](https://docs.aws.amazon.com/sns/latest/api/API_ConfirmSubscription.html) to learn more.

- **TopicArn:** The ARN of the Topic for which you want to confirm your subscription.
- **Token:** Short-lived token sent to an endpoint during the subscribe action.
- **AuthenticateOnUnsubscribe:** Disallows unauthenticated unsubscribes of the subscription. If this toggle button is enabled, and if the request has an AWS signature, then only the topic owner and the subscription owner can unsubscribe the endpoint.
- **Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

#### Unsubscribe

Deletes a subscription. If the subscription requires authentication for deletion, only the owner of the subscription or the topic's owner can unsubscribe, and an AWS signature is required. If the Unsubscribe call does not require authentication and the requester is not the subscription owner, a final cancellation message is delivered to the endpoint so that the endpoint owner can easily resubscribe to the topic if the Unsubscribe request was unintended.

See [Amazon's documentation on Unsubscribe](https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html) to learn more.

- **SubscriptionArn:** The ARN of the subscription to be deleted.
- **Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

#### List Subscriptions

Returns a list of the requester's subscriptions. Each call returns a limited list of subscriptions, up to 100.

See [Amazon's documentation on List Subscriptions](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html) to learn more.

- **NextToken:** If there are more than 100 subscriptions, the NextToken attribute is returned, which you can use in a new List Subscriptions call to get further results.
- **Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.

#### List Subscriptions by Topic

Returns a list of the requester's subscriptions to a specific topic.

See [Amazon's documentation on List Subscriptions by Topic](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html) to learn more.

- **TopicARN:** The ARN of the topic for which you wish to find subscriptions.
- **NextToken:** If there are more than 100 subscriptions, the NextToken attribute is returned, which you can use in a new List Subscriptions call to get further results.
- **Result Mapping: **Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that should hold the output. For example, if you specify bh.local.result in this field, then that local property will hold the result of this operation.
