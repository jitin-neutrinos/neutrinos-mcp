# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/kafka-consumer>

The Kafka Consumer node allows applications to read streams of data from topics in the Kafka cluster.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Kafka Config: **The name of the config.
  - If you have an existing kafka config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new config. See [Attributes for a new Kafka Config](/articles/server-services-designer-9/kafka/a/h3_1756699968) to know what are the properties to configure.
4. **Kafta Consumer Config**: The name of the config.
  - If you have an existing Kafka Consumer config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new config. See [Attributes for a new Kafka Consumer Config](/articles/server-services-designer-9/kafka-consumer/a/h3_1756699968) to know what are the properties to configure.
5. **Topic: **Enter the topics for the Kafka consumer. A topic is a category name to which records are stored and published.
6. **From Beginning: **When this is set to true, the node uses the earliest offset. If it is set to false, then the latest offset is used.
7. **Result Mapping:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that holds the result. For example, if you specify bh.local.result in this field, then that property will hold the data retrieved from google storage.

### Attributes for a new Kafka Consumer Config

For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name**: The name of the config.
- **Group ID**: Specify the group ID of the consumer group a Kafka consumer belongs to.
- **Partition ****Assigners**: List of partition assigners
- **Session ****Timeout (milliseconds)**: Specify the time used to detect failures. The consumer sends periodic heartbeats to indicate its liveness to the broker. If no heartbeats are received by the broker before the expiration of this session timeout, then the broker will remove this consumer from the group and initiate a rebalance
- **Rebalance ****Timeout (milliseconds)**: The maximum time that the coordinator will wait for each member to rejoin when rebalancing the group
- **Heartbeat ****Interval (milliseconds)**: The expected time between heartbeats to the consumer coordinator. Heartbeats are used to ensure that the consumer's session stays active. The value must be set lower than the session timeout
- **Metadata ****MaxAge **(milliseconds)** **: The time after which we force a refresh of metadata even if we haven't seen any partition leadership changes to proactively discover any new brokers or partitions
- **Allow ****Auto ****Topic ****Creation**: Allow topic creation when querying metadata for non-existent topics
- **Max ****Bytes ****Per ****Partition**: The maximum amount of data per partition the server will return.
- **Min Bytes:** Minimum amount of data the server should return for a fetch request,.
- **Max Bytes**: Maximum amount of bytes to accumulate in the response.
- **Max Wait Time**(milliseconds)** **: The maximum amount of time the server will block before answering the fetch request if there is no sufficient data to immediately satisfy the requirement given by minBytes
- **Max in Flight Requests**: Max number of requests that may be in progress at any time.
- **RackId**: Specify the rack in which the consumer resides to enable follower fetching.
