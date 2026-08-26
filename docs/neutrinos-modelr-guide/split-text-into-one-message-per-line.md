# Split text into one message per line

<https://documentation.neutrinos.com/articles/#!neutrinos-modelr-guide/split-text-into-one-message-per-line>

## Split text into one message per line

### Problem

You want to perform an operation on every line in a block text. For example, you want to add the line number to the beginning of each line.

### Solution

The `Split` node can be used to split the message into one message per line. It can be followed by the nodes needed to operate on the individual lines of text, followed by a `Join` node to recombine them back into a single block of text.

#### Example

![](https://cookbook.nodered.org/images/basic/split-text.png)

### Discussion

In the example, the `**Inject**` and `**Template**` nodes are used to inject a block of text with multiple lines say one two three four five

The `**Split**` node’s default behavior, when passed a string, is to split it into one message per line.

The `**Change**` node modifies each message payload using a JSONata expression: `**(parts.index+1) & ": " & payload**` - which uses `**msg.parts.index**` to get the line number and prepends it to the existing `**msg.payload**`.

Finally the `**Join**` node reassembles the messages into a single block of text:

1: one 2: two 3: three 4: four 5: five
