# Use Token

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/tokens>

When a rule, rule group, or workflow needs to be tested using the Swagger UI, tokens are required for authentication and API execution. These tokens can now be generated from the Reels platform. To generate token follow the steps below:

1. Click the **Tokens** button in the left-side navigation bar to open the **Tokens** List page. This page displays a list of tokens created in the Reels platform in a tabular format, including details such as the Token Name, Date of Creation, and Last Accessed Date and Time, Expiry, and Action.
2. Click the **Create** button on the top-right corner of the page.
    ![tokens-create-button](/resources/Storage/neutrinos-reels-publication/images/tokens-create-button.png)
3. In the pop-up window, enter a name for the token and select an expiration time from the dropdown. The expiration time can range from 1 day to 1 year, or never.
4. Click the **Generate** button to generate the token.
    ![Note](/resources/Storage/neutrinos-reels-publication/project-trailproject/note.png)
    Once a token is added, the key will be hidden and inaccessible. Please store it securely.
5. Finally, click the **Okay** button to close the pop-up window.

The GIF below illustrates how to create a token:




 ![token-generate](/resources/Storage/neutrinos-reels-publication/images/token-generate.gif)

## Use Token

To use a created token follow the steps below:

1. Copy the token when it is created and store it in a safe location for future use.
2. Paste the token where necessary, such as for authorization during API execution. Storing and reusing tokens prevents unnecessary token recreation.

The GIF below illustrates how to use the token created on the Reels platform for authorization:

![reels-token-usage](/resources/Storage/neutrinos-reels-publication/images/reels-token-usage.gif)

## Revoke Token

You can delete a token you created on the Reels platform. To delete the token follow the steps below:

1. Click the **Tokens** button in the left-side navigation bar to open the **Tokens** List page.
2. In the **Action** column, click the **Revoke** button, to delete the token.

The GIF below illustrates how to delete the token:




 ![token-delete](/resources/Storage/neutrinos-reels-publication/images/token-delete.gif)

[Next Topic](/articles/neutrinos-reels-publication/testing)

[Previous](/articles/neutrinos-reels-publication/master-data-versioning)
