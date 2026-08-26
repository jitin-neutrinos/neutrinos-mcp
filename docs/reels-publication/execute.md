# Execute

<https://documentation.neutrinos.com/articles/#!reels-publication/execute>

The Execute node is built on a synchronous model. The node is designed to deliver data directly in real-time as soon as the requested operation is completed.

To use an Execute node:

1. Login to Neutrinos Studio using valid credentials.
2. Navigate to the Server Services editor window.
   ![](/resources/Storage/reels-publication/Services.png)
3. Click the ![](/resources/Storage/reels-publication/project-server-side-service-designer/dm-processor-2023-04-27.png)button to add a new service.
4. In the Reels Nodes Palette drag and drop the Execute node.
    ![](/resources/Storage/reels-publication/execute/execute.png)

**Note: **Both the "execute node" and "execute publish node" can be utilized in both server and client services.

**Execute Node Properties**

**![](/resources/Storage/reels-publication/execute/Screenshot%202024-01-12%20144401.png)
**

| **Property** | **Description** |
| --- | --- |
| Name | Unique name to identify Execute node. This name will be displayed on the canvas once you save the node. |
| Reels URL | The base URL of the reels api. |
| Product ID | This is a unique UUID associated with each reels product. |
| Product Version | Product version is version of the product to be executed. The version number is passed as a string.(example: "1.0.0"). |
| Input Object | The input object used during product execution. This is an object which contains user input for the input fields configured inside the product rules flow. |
| Deployment Token | Authentication token used for authorization when executing the product. |
| Result | The synchronous API execution results in a result object that includes execution result and a "run ID". This run ID can be utilized to retrieve the execution result through an API call later. The corresponding API endpoint for this purpose is "/api/execution-result/<run_id>". |
| IDS Enabled | Toggle the button to enable authentication using IDS (ensure it is also enabled in Studio). When the IDS button is activated, the Deployment Token field will become invisible. |
