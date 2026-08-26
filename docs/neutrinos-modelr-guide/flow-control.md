# Flow Control

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/flow-control>

## Flow Control

These recipes address problems specific to **flow control** and shows by example how they can be solved using the capabilities of Modelr .

- [Perform an operation on each element in an array](/articles/neutrinos-modelr-guide/flow-control/a/h3__1529682646)
- [Trigger a flow if a message isn’t received after a defined time](/articles/neutrinos-modelr-guide/flow-control/a/triggeraflowismsgisntreceived)
- [Slow down messages passing through a flow](/articles/neutrinos-modelr-guide/flow-control/a/triggeraflowismsgisntreceived)
- [Handle messages at a regular rate](/articles/neutrinos-modelr-guide/flow-control/a/handlemsgatregularrate)
- [Drop messages that have not changed the value](/articles/neutrinos-modelr-guide/flow-control/a/dropmsgthathavenotchanged)
- [Create a single message from separate streams of messages](/articles/neutrinos-modelr-guide/flow-control/a/singlemsgfromseparatestream)

---

### Perform an operation on each element in an array

#### Problem

You want to perform an operation on every element in an array. For example, given an array of numbers, you want to round each value to the nearest integer.

#### Solution

The `**Split** node can be used to send a message for every element in the array. It can be followed by the nodes needed to operate on the individual elements, followed by a ``**Join** node to recombine them back into a single array.`

#### Example

![](https://cookbook.nodered.org/images/basic/operate-on-array.png)

### Discussion

In other programming environments, this task would be accomplished by creating a loop over the elements of the array.

In Modelr, the way to achieve the same thing is to turn the single message containing the array into a stream of messages that can be processed individually and finally recombine them back into one message.

The `Split/``Join` node pair are commonly used together to achieve this. The `Split node adds the ``msg.parts property to each message in the stream which allows the ``Join node to properly reassemble the original message.`

---

### Trigger a flow if a message isn’t received after a defined time

#### Problem

You want a flow to be triggered if a message is not received after a defined time. For example, you expect to receive a sensor reading every 5 seconds and need to know if it fails to arrive.

#### Solution

Use the `Trigger` node to detect when a message has not arrived after a defined interval.

#### Example

![](https://cookbook.nodered.org/images/basic/trigger-timeout.png)

#### Discussion

In the example flow, the top branch represents the normal flow of the messages. They also get passed to the `Trigger` node on a second branch of the flow.

The `Trigger` node is configured to initially send nothing, then to wait for 5 seconds before sending a `timeout `message. The option to extend the delay if new messages arrive is also selected. This means as long as messages continue to arrive, the node will not do anything. Once 5 seconds passes after the last message to arrive, it will send on the timeout message.

---

### Slow down messages passing through a flow

#### Problem

You want to slow down the messages passing through a flow. For example, you have a message containing an array of values that you split into a stream of messages and want to process each message in that stream at a rate of one per second.

#### Solution

Use a `Delay` node configured to rate limit the messages passing through it.

#### Example

![](https://cookbook.nodered.org/images/basic/rate-limit-messages.png)

#### Discussion

The rate limiting mode of the `Delay `node can be used to change the rate of messages passing through it. It is configured with the desired number of messages to pass through the node per time interval. It will evenly spread the delivery of messages across the time period.

---

### Handle messages at a regular rate

#### Problem

You want to handle messages at a regular rate, ignoring messages that arrive too quickly. For example, you have a sensor sending data every second but you only want to handle an update every 5 seconds. The messages you handle must be the most recent.

#### Solution

Use a Delay node configured to rate limit the messages passing through it with the option to drop intermediate messages enabled.

#### Example

![](https://cookbook.nodered.org/images/basic/rate-limit-message-stream.png)

#### Discussion

The rate limiting mode of the Delay node can be used to change the rate of messages passing through it. With the option to drop intermediate messages enabled, it will discard any message that arrives within the rate limit interval.

---

### Drop messages that have not changed the value

#### Problem

You want to drop a message if the value of its payload has not changed since the last message. For example, you have a sensor sending the state of a switch at regular intervals and you only want to know when the value has changed.

#### Solution

Use the `RBE` node (Report By Exception) to block messages unless its value has changed.

#### Example

![](https://cookbook.nodered.org/images/basic/report-by-exception.png)

#### Discussion

The RBE node can be used to drop messages unless their value has changed. This is useful for detecting changes.

If the property being checked is a number, the node can also be configured with a threshold for how much the value must change for the message to be passed on.

---

# Create a single message from separate streams of messages

### Problem

You have messages arriving from different sources that you need to combine into a single message.

For example, you have three different sensors publishing values and you want to insert them into a database as a single entry.

### Solution

Give each stream a unique `msg.topic` value and use the `Join` node to group them into a single message.

#### Example

In the example flow, each `**Inject**` node represents a different source of messages. They each set a unique `msg.topic ` value so they can be identified later in the flow.

The `**Join**` node has been configured in manual mode to create a key/value object using `msg.topic `as the key name. As we know there are three separate streams of messages to join, the node has been to configure to send on a message when it receives that number of parts.

This means it will send on a message each time it receives at least one message from three different topics - using the most recent value from each topic.

Copy CodeHTML{"temperature":10,"humidity":0,"pressure":999}

The node has further options to change its behavior that have not been used in this recipe. For example, a timeout can be set to ensure it sends *something* in case one of the sensors stops sending values. If that is a concern, you may consider [this recipe](https://cookbook.nodered.org/basic/trigger-timeout) for providing a placeholder value.
