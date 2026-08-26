# Use Token

<https://documentation.neutrinos.com/articles/#!pulse-publication/tokens>

When Reels, Case Manager, or Process modules need to be tested or integrated, authentication tokens are required to execute APIs securely. These tokens can be generated from the Pulse platform. To generate a token, follow these steps:

1. On the landing page, click the required project card to open the project. Alternatively, use the search bar to locate the required project.
2. Click Tokens from the module or the main left navigation pane to open the Tokens page. This page displays all the tokens created on the platform in a tabular format. The table includes details such as the **Token Name**, **Creation Date**, **Last Accessed Date and Time**, **Expiry**, and **Actions**.
   ![up-tokens-landing-page](/resources/Storage/pulse-publication/images/up-tokens-landing-page.png)
3. Click the **Create** button on the top-right corner of the page.
    ![up-tokens-create-button](/resources/Storage/pulse-publication/images/up-tokens-create.png)
4. On the Create Token page, enter a name for the token and select an expiration period from the Expiration drop-down list. You can configure the token to expire after 1 to 60 days or set it to Never. Click Next.
5. On the next page, select the scope for the token. The scope determines the modules and specific resources for which the token is valid. Select one or more modules from the list on the left. When you select a module, the available resources for that module are displayed in the pane on the right. Select the specific resource that the token should be authorized to access.
    You can configure a single token for multiple modules. However, you can select only one resource from each module. For example, under Reels, you can select either a Rule, Rule Group, or Workflow. You can then select another module, such as Process, and choose one resource from that module to include in the same token scope.
   **Note**: If the token scope is set to Case Manager, the same token can be used to trigger all the processes that are mapped to the selected case in the right pane.
    ![Note](/resources/Storage/pulse-publication/project-trailproject/note.png)
    Once a token is added, the key will be hidden and inaccessible. Please store it securely.
6. Finally, click the **Okay** button to close the pop-up window.

The GIF below illustrates how to create a token:




 ![up-token-generate](/resources/Storage/pulse-publication/images/up-tokens-create-token-gif.gif)

## Use Token

To use a created token follow the steps below:

1. Copy the token when it is created and store it in a safe location for future use.
2. Paste the token where necessary, such as for authorization during API execution. Storing and reusing tokens prevents unnecessary token recreation.

The GIF below illustrates how to use the token created on the Reels platform for authorization:




 ![reels-token-usage](/resources/Storage/pulse-publication/images/reels-token-usage.gif)

## Revoke Token

You can delete a token you created on the pulse platform. To delete the token follow the steps below:

1. Click Tokens from the module or the main left navigation pane to open the Tokens page. On the Tokens page, locate the token that you want to delete.
2. In the **Action** column, click the **Revoke** button, to delete the token.

The GIF below illustrates how to delete the token:




 ![token-delete](/resources/Storage/pulse-publication/images/token-delete.gif)

[Next Topic](/articles/pulse-publication/global-variables-wf-cm)

[Previous](/articles/pulse-publication/cache-manager-plugins-gcc)
