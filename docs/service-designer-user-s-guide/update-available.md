# Associated Attributes

<https://documentation.neutrinos.com/articles/#!service-designer-user-s-guide/update-available>

The **Update** **Available** node is used to emit an event whenever a new version of the app is available.

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Result Mapping:** The result of the operation. Enter the [flow object](/articles/service-designer-user-s-guide/service-designer-variables)in which you want to save the emitted event.

An example of an emitted event:

```json
available:  appData: undefined  hash: "c34f0841868178def01fd4cca38c1178581bcc47"  __proto__: Objectcurrent:  appData: undefined  hash: "a7c6ae0188a513b855f4867b90ca7888634e9d8c"  __proto__: Object  type: "UPDATE_AVAILABLE"  __proto__: Object\
```
