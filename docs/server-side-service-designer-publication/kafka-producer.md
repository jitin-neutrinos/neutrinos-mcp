# Associated Attributes

<https://documentation.neutrinos.com/articles/#!server-side-service-designer-publication/kafka-producer>

The Kafka Producer node allows you to send streams of data to topics in the Kafka cluster.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the Name field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Kafka Config: **The name of the config.
  - If you have an existing Kafka config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new storage config. See [Attributes for a new Kafka Config](/articles/server-side-service-designer-publication/kafka/a/h3_1756699968) to know what are the properties to configure.
4. **Kafka Producer Config: **The name of the config.
  - If you have an existing Kafka Producer config that is already configured, choose that config from the drop-down list.
  - If you want to configure a new config, select **Add new config** from the drop-down list and click the **Map** icon to configure a new Kafka producer config. See [Attributes for a new Kafka producer Config](/articles/server-side-service-designer-publication/kafka-producer/a/h3_1756699968) to know what are the properties to configure.
5. **Topic:** Enter the topics for the Kafka producer. A topic is a category name to which records are stored and published.
6. **Messages**: Enter the message that the system should send between the servers or application.
7. **Acks (Acknowledgment)**: Enter the number of required acks.
  - -1 = all in sync replicas must acknowledge
  - 0 = no acknowledgments
  - 1 = only waits for the leader to acknowledge
8. **Timeout(milliseconds): **Enter the time to await a response.
9. **Result Mapping:** Map the data retrieved to bh. , bh.local or bh.input property. Select the property type and enter the variable that holds the result. For example, if you specify bh.local.result in this field, then that property will hold the data retrieved from google storage.

### Attributes for a new Kafka Producer Config

For every option, you can choose the env type and enter the environment property that holds the value or choose the datatype that the respective field supports. Make sure that the environment property is already added to the [Environments](/smart/project-sample-how-to-guide/what-is-an-environment) editor before you specify it in these fields.

- **Name**: The name of the config.
- **Create Partitioner**: Enter the name for creating a partitioner. A partitioner is a function that returns another function responsible for the partition selection.
- **Retry**: The option retry can be used to customize the configuration for the producer.
- **Metadata MaxAge:** Specify the time after which the force refresh of metadata should happen even if any partition leadership changes to proactively discover any new brokers or partitions
- **Allow Auto Topic Creation**: Allow topic creation when querying metadata for non-existent topics.
- **Transaction Timeout (milliseconds)**: The maximum amount of time that the transaction coordinator will wait for a transaction status update from the producer before proactively aborting the ongoing transaction.
- **Idempotent**: If enabled producer will ensure each message is written exactly once.
- **Maxin Flight Requests**: Specify the max number of requests that may be in progress at any time.
