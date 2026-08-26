# Working with Messages

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/working-with-messages>

## Working with Messages

In Modelr, a flow works by passing messages between nodes. The messages are simple JavaScript objects that can have any set of properties. The default properties are:

- payload property - this is the default property that most nodes will work with.
- _msgid - this is an identifier for the message which can be used to trace its progress through a flow.

```javascript
{"_msgid": "12345","payload": "..."}
```

The value of a property can be any valid JavaScript type, such as:

- Boolean - true, false
- Number - eg 0, 123.4
- String - "hello"
- Array - [1,2,3,4]
- Object - { "a": 1, "b": 2}
- Null

To understand more about messages, see:

- [Understanding the structure of a message](/articles/neutrinos-modelr-guide/working-with-messages/a/h3_2119823719)
- [Working with JSON](/articles/neutrinos-modelr-guide/working-with-messages/a/h3_623053843)
- [Changing message properties](/articles/neutrinos-modelr-guide/working-with-messages/a/h3_13625854)
- [Working with message sequences](/articles/neutrinos-modelr-guide/working-with-messages/a/h3_244217943)
- [Working with sequences](/articles/neutrinos-modelr-guide/working-with-messages/a/h3__465981401)

---

### Understand the Structure of a Message

The easiest way to understand the structure of a message is to pass it to a **Debug** node and view it in the** Debug **sidebar. By default, the **Debug** node will display the msg.payload property. But, it can be configured to display any property or the whole message.

When displaying an Array or Object, the sidebar provides a structured view that can be used to explore the message.

- At the top, it shows the name of the property that has been passed in. Here, the default msg.payload has been used.
- Next to the property name is the type of the property - Object, String, Array etc.
- It then shows the contents of the property. For Arrays and Objects, the property is collapsed into a single line. By clicking on it, the property will expand to show more detail.

---

### Work with JSON

JSON, (JavaScript Object Notation), is a standard way for representing a JavaScript object as a String. It is commonly used by web APIs to return data. If a message property contains a JSON string it must first be parsed to its equivalent JavaScript object before the properties it contains can be accessed. To determine whether a property contains a String or Object, the **Debug** node can be used.

---

### Change Message Properties

A common task in a flow is to modify the properties of a message as it passes between nodes. For example, the result of an HTTP Request may be an object with many properties, of which only some are needed.

There are two main nodes for modifying a message, the** Function** node, and the **Change** node.

- The Function node allows you to run any JavaScript code against the message. This gives you complete flexibility in what you do with the message, but does require familiarity with JavaScript and is unnecessary for many simple cases. More information about writing Functions is available here.
- The Change node provides a lot of functionality without needing to write JavaScript code. Not only can it modify message properties, but it can also access flow.

It provides four basic operations:

- Set a property to a value
- Change a String property by performing a search and replace
- Delete a property
- Move a property

For the set operation, you will have to first identify what property you want to set, then the value you want it to have. That value can either be a hardcoded value, such as a string or number, or it can be taking from another message or flow/global context property. It also supports using the JSONata expression language to calculate a new value.

For example, using the Debug node’s ability to determine a message element’s path, you can paste the path straight into the ‘to’ field, with msg. selected from the list. That will then set msg.payload to the value of msg.payload.Phone[2].type.

Another example, using a JSONata expression, is to convert temperature held in msg.payload.temperature, from Fahrenheit to Celsius and store the result in a new message property msg.payload.temperature_c.

```javascript
{"payload": {"temperature": 90,"temperature_c": 32.22222}}
```

Note that JSONata expressions look a lot like JavaScript, but have some key differences. Refer to the [jsonata.org](http://jsonata.org/) site for more information.

---

### Message Sequences

A message sequence is an ordered series of messages that are related in some way. For example, the **Split** node can turn a single message whose payload is an Array, into a message sequence where each message has a payload corresponding to one of the array elements.

**Understanding msg.parts**

Each message in a sequence has a property called msg.parts. This is an object that contains information on how the message fits in the sequence. It has the following properties:

- msg.parts.id: a unique identifier for the sequence
- msg.parts.index: the message's position within the sequence
- msg.parts.count: if known, the total number of messages in the sequence

The parts array may contain additional meta-data about the sequence. For example, the **Split** node also attaches information that can be used by the join node to reassemble the sequence.

---

### Work with Sequences

There are a number of core nodes that can work across message sequences:

**Split**

Turns a single message into a sequence of messages. The exact behavior of the node depends on the type of msg.payload:

- String/Buffer: the message is split using the specified character (default: `\n`), buffer sequence or into fixed lengths.
- Array: the message is s![](https://neutrinos.clickhelp.co/DXR.axd?r=1_121-P7fri)plit into either individual array elements or arrays of a fixed-length.
- Object: a message is sent for each key/value pair of the object.

**Join**

Turns a sequence of messages into a single message. The node provides three modes of operation:

- **Automatic**: attempts to reverse the action of a previous Split node
- **Manual**: allows finer control on how the sequence should be joined
- **Reduce: **New in 0.18 - allows a JSONata expression to be run against each message in the sequence and the result accumulated to produce a single message.

**Sort**

Sorts the sequence based on a property value or JSONata expression result.

**Batch**

Creates new sequences of messages from those received. The node provides three modes of operation:

- **Number of messages**: groups messages into sequences of a given length. The overlap option specifies how many messages at the end of one sequence should be repeated at the start of the next sequence.
- **Time interval**: groups messages that arrive within the specified interval. If no messages arrive within the interval, the node can optionally send on an empty message.
- **Concatenate sequences**: creates a message sequence by concatenating incoming sequences. Each sequence must have a msg.topic property to identify it. The node is configured with a list of topic values to identify the order sequences are concatenated.
