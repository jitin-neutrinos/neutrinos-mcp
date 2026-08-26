# Integrate with Active Directory

<https://documentation.neutrinos.com/articles/#!how-to-articles/integrate-with-active-directory>

Neutrinos allow you to easily integrate with your existing Active Directory. Once your existing Active Directory is configured with the app, you can authenticate your user, find a user, find user groups, check if a user exists, and perform more such operations.

You can also re-use Active Directory groups and distribution lists your customer is already managing and based on users and groups, you can control who has access to what information within your application.

In this example, you will learn how to configure your Active Directory on [Server Services Designer](/smart/project-concepts/server-services-designer) and make your app navigate to different pages based on the group membership of the user.

**Step 1**: Create three pages home, page1, and page2.

**Step 2**: Open the home page and navigate to the **ts editor** of the page. Enter the following code within the ngOnInit().

```code
this.adResult =  (await this.ad.callADAPI()).result        if (this.adResult) {            this.router.navigate(['/page1']);        } else {            this.router.navigate(['/page2']);        }
```

**Step 3**: Create Server Services. Perform the following steps:

1. Open the **Server Services** editor from the [Studio Application page](/smart/project-concepts/studio-application-page).
2. Click the** Add a Server Service** button to add a new service.
3. From the Nodes Palette, drag and drop an **HTTP In** node to the workspace. The **HTTP In **node provides an API end-point for creating web services. In this example, we are creating an API endpoint called **getGroupMember**.
4. Double-click the Http In node to open its **Properties** window.
  1. Enter the node name as** **getGroupMem********ber****.
  2. Select the **Get** HTTP method.
  3. Enter the path as** activedirectory**. Click the **Done **icon to save the properties.
5. Drag and drop an Active Directory node to the workspace. Double click the node and add the following properties:
  1. Select an existing Active Directory configuration or you can configure a new Active Directory.
  2. Select Operation Type as **getGroupMembershipForUser**.
  3. Enter sAMAccountName as **sAMAccountName.**
  4. Enter** result **in the Result Mapping Field.
6. Drag and drop Htpp Out node. Double click to open its properties window. In the properties window, add the following properties:
  1. Select **Json** as the Response Types.
  2. In the Status code field, select number property and enter **200**.
  3. In the Response Body
  4. field, select bh.local property and enter **result**.

**Step 4**: Create Client Services. Perform the following steps:

1. Open the **Client Services** editor from the Studio Application page.
2. Click the** Add a Server Service** button to add a new service.
3. From the Nodes Palette, drag and drop a **Start** node to the workspace. Double click the node and add the following properties:
  1. Enter the name of the node as callADAPI.
  2. Save the node.
4. Drag and drop a Call Server API node. Double click the node and enter the following properties:
  1. Choose **GET activedirectory **from the drop-down list of the API field.
  2. In the Result Mapping field, select bh. property and enter **result**.
  3. Save the node.
5. Connect the nodes.

**Step 5**: Initialize and run the app.
