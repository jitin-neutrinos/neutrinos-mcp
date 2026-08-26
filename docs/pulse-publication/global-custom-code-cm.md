# Global Custom Code edge over Custom Code

<https://documentation.neutrinos.com/articles/#!pulse-publication/global-custom-code-cm>

In the Pulse platform, Custom Code refers to user-defined logic or scripts that extend the platform’s default functionality. It enables developers to implement complex business logic, perform custom data transformations, or integrate with plugins, enabling capabilities that go beyond what is achievable through standard visual components and workflow configurations.



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
| [Create Global Custom Code](/smart/project-alpha-platform/create-global-custom-code) |
| [Global Custom COde with Triggers](/smart/project-alpha-platform/global-custom-code-with-triggers) |
| [Versioning Global Custom Code](/smart/project-alpha-platform/versioning-global-custom-code) |
| [Debugging and Testing Global Custom Codes](/smart/project-alpha-platform/debugging-and-testing-global-custom-codes) |
| [Compatibility and Migration](/smart/project-alpha-platform/compatibility-and-migration) |
| [Plugins](/smart/project-alpha-platform/plugins-global-custom-code) |
