# Create Versions

<https://documentation.neutrinos.com/articles/#!pulse-publication/versioning-global-custom-code>

Versioning in Global Custom Code is automatically handled each time changes are made and the code is saved. This allows developers to create new versions without impacting the version currently used in existing projects. As a result, projects remain stable and unaffected by newer versions until a specific version is manually selected for use.

### Create Versions

To create versions of the Global Custom Code follow the steps below:

1. Click the **Custom Code** icon on the top bar, next to the user profile icon, to open the **Custom Code** page. Then, click **Create** in the upper-right corner of the page. Alternatively, to edit or use an existing custom code, select it from the list to open it in the editor.
2. When a new Custom Code page is opened, the default version of the code is set to v1. Once changes are made—such as writing and updating saving the code—a new version (v2) is automatically created, which becomes the latest available version. Note: If no changes are made, clicking the Save button will not create a new version.
3. Any number of versions can be created and saved for a given custom code. However, to use a specific version within an Alpha project, it must first be published to the Marketplace. Once published, the version can be consumed in triggers on any page—whether it's an Inbox, Global, or Task page.

### Bundle with Project

When a project is published, it is tagged with a specific version. At this point, all the global custom code used within the project is also tagged with the corresponding project version.




 For example, if a project is tagged twice and both versions use custom code version v1, that version of the custom code remains associated with those project versions. If the global custom code is later updated (to v2) and the project is tagged again (resulting in a third version), only the third version of the project will include v2.




 Earlier project versions retain their originally bundled custom code (v1) and are not affected by subsequent changes. This ensures version consistency and backward compatibility. This version-locking mechanism is known as bundling custom code with the project.

The steps below demonstrate how a mapped version of global custom code is bundled with a specific project version during export:

1. In Workflow Studio, navigate to the desired project and open it.
2. Use the required global custom codes within the relevant task page, global page, or inbox as needed.
3. Save the project and click Preview to test its functionality in the Alpha Workbench.
4. Once verified, click the Publish button to publish the version.
5. To export the project, click the dropdown arrow next to the Publish button and select the desired version of the published project. The exported project will include the corresponding versions of the Global Custom Codes used in that project.

### Plugin Dependency

Custom code can directly consume Alpha plugins within its implementation. Consider the following scenario: When a global custom code is created, it automatically includes all the latest plugins available on the Alpha platform at that time. Once this custom code is saved, it retains the specific versions of the plugins that were mapped to it during that save.

In the future, if updates are made to the Alpha plugins and the custom code is saved again, the new version of the custom code will include the updated plugin versions. However, earlier versions of the custom code continue to function with the previously mapped plugin versions. This ensures backward compatibility and prevents errors due to version mismatches.

This versioning strategy effectively manages plugin dependencies within the custom code. For more information about supported plugins, refer [Plugins Global Custom Code](/articles/pulse-publication/plugins-global-custom-code) topic.
