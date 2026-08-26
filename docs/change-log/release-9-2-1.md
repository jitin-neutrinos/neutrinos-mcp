# Release 9.2.1

<https://documentation.neutrinos.com/articles/#!change-log/release-9-2-1>

**Features:**

- In studio, Removed the unused imports in `ts` file and re-organized them.
- Auto-Generating API's for PCML files using PCML Node.
- For IDS, Generate password reset logout callback changes.

**Bug Fixes:**

- For Data Model, Created `@PrimaryColumn` decorator, when a relation is drawn from Primary Key.
- For Studio, Refactored Schema Builder.
- For Studio, Refactored Erd-Schema Builder.
- For Studio, prevented leaking of server software info by disabling "x-powered-by" for 'app' and 'baseApp' in index.js.
