# Global Custom Code edge over Custom Code

<https://documentation.neutrinos.com/articles/#!alpha-platform/global-custom-code>

In the Neutrinos Alpha platform, Custom Code refers to user-defined logic or scripts that extend the platform’s default functionality. It enables developers to implement complex business logic, perform custom data transformations, or integrate with plugins, enabling capabilities that go beyond what is achievable through standard visual components and workflow configurations.




 Previously, custom code was written within individual triggers, limiting its scope to that specific trigger. This approach led to code redundancy, as the same logic is duplicated across multiple triggers whenever required, making it inefficient and increasing maintenance effort.




 The global custom code is modularized and reused across workflows and components. Global custom code is not confined to a single project—it can be written once, published to the Marketplace, and accessed from any project by referencing its name and version. This promotes code reusability, reduces duplication, and streamlines development efforts.

## Global Custom Code edge over Custom Code

- Allows you to create and execute code snippets independently, without integrating them into actual projects..
- Enables testing of code snippets against specific project tasks and global pages.
- Allows users to publish code snippets to the on-premises marketplace, making them readily available for use in project triggers.
- Global custom code can be used as a trigger within the Inbox, Enquiry Inbox, Admin Inbox, and across all page-level triggers.
- Plugins can be managed independently at both the global custom code and project levels. Users can select specific plugin versions directly, enabling easier upgrades without requiring additional deployments.
- Upgrades to plugin versions published will not affect existing global custom codes. Each custom code snippet continues to run against its originally selected plugin version, ensuring stability and reliability.

In summary, Global Custom Code = Custom Code + Reusability + Scalability + Centralization

| **Topic** |
| --- |
| [Create Global Custom Code](/articles/alpha-platform/create-global-custom-code) |
| [Global Custom COde with Triggers](/articles/alpha-platform/global-custom-code-with-triggers) |
| [Versioning Global Custom Code](/articles/alpha-platform/versioning-global-custom-code) |
| [Debugging and Testing Global Custom Codes](/articles/alpha-platform/debugging-and-testing-global-custom-codes) |
| [Compatibility and Migration](/articles/alpha-platform/compatibility-and-migration) |
| [Plugins](/articles/alpha-platform/plugins-global-custom-code) |
