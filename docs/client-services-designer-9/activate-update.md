# Associated Attributes

<https://documentation.neutrinos.com/articles/#!client-services-designer-9/activate-update>

This node is used to update the app to the new version and emit an event whenever the app has been updated to a new version.

| ![Warning](/resources/Storage/client-services-designer-9/warning.png) | This node is available from Neutrinos Studio Release 7.7.0. |
| --- | --- |

### Associated Attributes

1. **Name: **The name of the node. This name will be displayed on the canvas when you save the node.
2. **Function Name:** This is a read-only field. The function name gets generated based on the label name that you entered in the **Name **field. To call the flow, you can use this function name in the [Call Service](/articles/server-side-service-designer-publication/call-service-node) node.
3. **Result Mapping:** The result of the operation. Enter the [flow object](/articles/client-services-designer-9/service-designer-variables)in which you want to save the emitted event.

Example of an emitted event:

```json
current:  appData: undefined  hash: "c34f0841868178def01fd4cca38c1178581bcc47"  __proto__: Objectprevious:  appData: undefined  hash: "a7c6ae0188a513b855f4867b90ca7888634e9d8c"  __proto__: Object  type: "UPDATE_ACTIVATED"  __proto__: Object
```
