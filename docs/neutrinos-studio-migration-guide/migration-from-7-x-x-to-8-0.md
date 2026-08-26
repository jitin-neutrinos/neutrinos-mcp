# Migration Steps

<https://documentation.neutrinos.com/articles/#!neutrinos-studio-migration-guide/migration-from-7-x-x-to-8-0>

### Migration Steps

Make sure you [Migrate the App](/articles/neutrinos-studio-migration-guide/migrate-your-application) to Studio version 8.0.0 and perform the following step:

Remove the following Marketplace URL from the **s****ettings.json** file. This URL is automatically computed by Neutrinos Studio when it is launched and is no longer valid.

Copy CodeJSON"marketplaceUrl": "https://store.neutrinos.co/api/7.x.x/"

The **settings.json** file resides in the $Home/.neutrinos folder of your local machine.

---

When you migrate your app to the 8.X.X version and run the npm run tsc command, you will be getting an error.

To solve this error, you need to regenerate the IDS flows and move the logic of your IDS flows (if you have any) to the migrated version of the app.
