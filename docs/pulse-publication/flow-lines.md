# Flowlines between Gateways and Nodes

<https://documentation.neutrinos.com/articles/#!pulse-publication/flow-lines>

In process management, flow lines (also known as sequence flows) represent the directional connections between process nodes, such as events, tasks, and gateways. They define how and in what order activities are executed within a process.

- **Purpose**: To control the logical progression of the workflow.
- **Notation**: Shown as solid arrows connecting two nodes.
- **Flow type**: Usually one incoming and one outgoing for linear steps; multiple flows can exist when gateways are used.

## Flowlines between Gateways and Nodes

Gateways are decision or merging points in a process. The flow lines entering and leaving gateways determine how the process branches or converges.

1. From Task to Gateway
  - The outgoing flow line from a task leads into a gateway to evaluate conditions or choices.
  - This indicates that once a task is completed, the gateway logic determines the next path(s).
2. From Gateway to Task
  - The outgoing flow line from a gateway points to one or more subsequent tasks.
  - This represents conditional routing, where one or several branches may activate depending on the gateway type.

## Flow Lines for Different Gateway Types

1. **Exclusive Gateway (XOR Gateway)**: Used when only one path can be taken among multiple possible paths as shown in the below GIF:
    ![pulse-exclusive-gateway-flowline](/resources/Storage/pulse-publication/images/pulse-exclusive-gateway-flowline.gif)
  - **Flow logic**: The gateway evaluates all outgoing flow conditions and follows exactly one that evaluates to true.
  - **Flow behavior**:
    - **Diverging (Splitting)**: One incoming line, multiple outgoing lines.
      - Each outgoing line has a condition expression (e.g., “Amount > 5000”).
      - Only the first condition that evaluates to true is taken.
    - **Converging (Merging)**: Multiple incoming lines, one outgoing line.
      - Used to join alternative paths back into a single flow.
2. **Inclusive Gateway (OR Gateway)**: Used when one or more paths can be taken simultaneously, based on defined conditions.
  - **Flow logic**: The gateway evaluates all outgoing conditions and may activate multiple flow lines if more than one condition evaluates to true.
  - **Flow behavior**:
    - **Diverging (Splitting)**: One incoming line, multiple outgoing lines.
      - Multiple paths may be executed in parallel if their conditions are satisfied.
    - **Converging (Merging)**: Multiple incoming lines, one outgoing line.
      - Waits for all active incoming branches to complete before continuing.

## Add Condition to Flowlines

These conditions determine how the flow lines transfer control to the next set of tasks, gateways, or events in the process. To add conditions to the flow lines, follow the steps below:

1. Create the process by adding the required nodes and gateways. Then, connect the nodes by linking them to one another using flow lines.
2. Navigate to the flowline for which a condition needs to be added. Click on the Flowline, add the following details:
    ![pulse-exclusive-gateway-add-flow-values](/resources/Storage/pulse-publication/images/pulse-exclusive-gateway-add-flow-values.gif)
  - **Name**: A name assigned to the flow line for identification.
  - **Priority**:
  - **Condition**: Can be either a script (custom code) or an expression to be evaluated.
  - **Expression**: Enter the expression to be evaluated for the condition specified in the previous step.
3. Click Save at the bottom of the page to save the condition applied to the flow line.

### Note:

1. Conditions on flow lines are supported only for Exclusive and Inclusive gateway nodes.
2. In the case of Parallel gateway nodes, conditions cannot be applied to the flow lines, as the gateway allows parallel execution of tasks regardless of conditions.
3. In the case of Event gateway nodes, the subsequent node must be of the Event type. Based on the event that is triggered, the corresponding flow line continues the process. For example, if two Timer nodes follow the Event gateway, the process flow proceeds along the path of the timer that is triggered first.

[Next Toopic](/articles/pulse-publication/user-tasks)

[Previous Topic](/articles/pulse-publication/nodes)
