# How to Use

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/child-process-node>

The **Child Process** node allows you to spawn child processes. For example, any Command-line Interface (CLI) command that you run on the terminal can be run through this node.

You can spawn multiple child processes from your parent process (server service) to perform any operation.

| ![Information](/resources/Storage/server-services-designer-9/info.png) | This node is available for you to use from Neutrinos Studio release 7.1.0. |
| --- | --- |

| ![Information](/resources/Storage/server-services-designer-9/info.png) | You can have multiple child processes in a service flow. |
| --- | --- |

### How to Use

- Open the Services editor window.
- Click the** plus icon** to add a new server-service or open an existing service from the service list.
- In the Nodes Palette, drag and drop a **Child process** node to the workspace.
- Drag and drop other nodes to create a flow. Make sure the flow starts with a **Start node** or an **HTTP In** node.

### Associated Attributes

- **Name****: **The name of the node. This name will be displayed on the canvas when you save the node.
- **Command: **The command that you want to execute.
  - To map the command to a variable, choose bh. , bh.input or bh.local property from the drop-down list and enter the variable name which contains the command. ![Child process command](/resources/Storage/server-services-designer-9/cp_bh.png)
  - To enter the command, choose string and enter the command directly.![Child process command](/resources/Storage/server-services-designer-9/cp_exec.png)
- **Output:** The mode of output you want to receive for the command that you are executing. You can choose between **Exec mode, Spawn mode, **and** Fork**. Based on the mode you select, the below fields will change.

---

### Examples

#### Exec Mode

Here is an example of how to use the** Child Process** node to perform the execution of the npm install command using** Exec **mode:

![Child Process example1](/resources/Storage/server-services-designer-9/exec.png)

**HTTP In node:**

![The HTTP IN node](/resources/Storage/server-services-designer-9/exec1.png)

**Script node:**

![Script node](/resources/Storage/server-services-designer-9/exec2.png)

**Child process node in Exec mode:**

![Child Process node](/resources/Storage/server-services-designer-9/exec3.png)

**HTTP Out node:**

![HTTP Out node](/resources/Storage/server-services-designer-9/exec4.png)

---

#### Spawn Mode

Here is an example of how to use the** Child Process** node to perform the execution of the  npm install command using** Spawn **mode and log all the result mapping outputs:

![Spawn mode](/resources/Storage/server-services-designer-9/spawn.png)

**HTTP In node:**

![HTTP In node](/resources/Storage/server-services-designer-9/spawn1.png)

**Script node:**

![Script node](/resources/Storage/server-services-designer-9/spawn2.png)

**Child Process Node in Spawn Mode:**

![child process- spawn node](/resources/Storage/server-services-designer-9/spawn3.png)

**Script and File out nodes to capture Standard Output:**

The **Script** node copies the string value to a variable. The variable saves the standard output of the npm install command to a file specified in the **File Out **node.

![](/resources/Storage/server-services-designer-9/spawn4.png)

![File out node](/resources/Storage/server-services-designer-9/spawn7.png)

**Script and File out nodes to capture Standard Errors:**

The Script node copies the string value to a variable. The variable saves the standard warnings and error messages while executing the npm install command which is then saved to a file using the **File Out **node.

![script node](/resources/Storage/server-services-designer-9/spawn5.png)

![File out node](/resources/Storage/server-services-designer-9/spawn8.png)

**Script and HTTP out nodes to capture the exit code when the execution completes:**

The **Script** node constructs the response message to send it back to the client. The **HTTP Out **node sends the response message as a plain text to the client.

![script node](/resources/Storage/server-services-designer-9/spawn6.png)
