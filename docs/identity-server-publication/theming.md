# Core Concepts

<https://documentation.neutrinos.com/articles/#!identity-server-publication/theming>

The IDS UI is typically delivered with the default Neutrinos branding and color scheme. These elements can be customized with organizational branding requirements. This topic guides configuring, maintaining, and troubleshooting themes for IDS login and authentication screens across clients and organizations.




 This document serves as the reference for developers when onboarding new tenants, configuring new clients, or programmatically customizing brand identity.

To update the branding image, color scheme, and logo in the UI, follow the steps below:

## Core Concepts

Developers must understand the following core concepts before configuring themes.

### Theme Resolution Priority

Theme resolution is determined by a strict priority hierarchy, with higher-priority configurations overriding lower-priority ones:

1. Client -> `ui_config` (Highest Priority)
2. Organisation -> `ui_config`
3. Default CSS variables (Fallback)

**Note**: Misconfiguration of the priority hierarchy can lead to unintended overrides and inconsistent theme behavior.

### Rendering Modes

Each `ui_config` must explicitly specify the rendering mode by setting the `selectedType` attribute.

#### UI Mode (selectedType = 'UI')

- The theme is generated using `generatedCss`
- Used when themes are created using a UI builder
- Minimal developer intervention required

#### CSS Mode (selectedType = 'CSS')

- The theme is applied using `editorCss`
- Provides full control using raw CSS
- Recommended for enterprise-level implementations
- Supports version control and code review

### Asset Storage

Theme assets are stored indirectly based on the database type:

#### SQL Environments

- File paths or Base64 content are stored in database columns

**Note**: Developers must ensure that asset references resolve correctly during runtime.

## Database Entities

Developers primarily interact with the following entities:

### ui_config

The `ui_config` entity stores theme-related configurations such as:

- Colors
- CSS
- Logos
- Favicons
- Animated Assets
- UI Styling Elements

Use this entity when:

- Creating new themes
- Updating existing themes
- Switching from default to custom themes

### client

The `client` entity references `ui_config` when a client requires a dedicated theme. Use this entity when:

- A single application requires a unique login experience

### organisations

The `organisations` entity references `ui_config` for organization-wide themes. Use this entity when:

- Multiple clients require consistent branding

## Theme Configuration Workflow

This section describes the end-to-end workflow for configuring themes.

1. **Determine Scope**: Select the appropriate scope based on business requirements.
    **Client-Specific Theme**: Use this when a single application requires unique branding.
    Configure:
    Copy CodeCodeclient."uiConfigId"
    **Organisation-Wide Theme**: Use this when multiple applications require consistent branding.
    Configure:
    Copy CodeCodeorganisations."uiConfigId"
2. Create a Theme (`ui_config`):
    Example:
    Copy CodePL/SQLINSERT INTO ui_config (
    id,
    "selectedType",
    "editorCss",
    logo,
    favicon,
    animated_logo,
    bg_color,
    login_card_bg_color,
    primary_button_bg,
    primary_button_color,
    footer_bg,
    footer_color
   )
   VALUES (
    uuid_generate_v4(),
    'CSS',
    ':root {
    --primary-button-bg: #2b6cb0;
    --primary-button-color: #ffffff;
    --bg-color: #f7fafc;
    --login_card_bg_color: #ffffff;
    }',
    'path/to/logo.png',
    'path/to/favicon.ico',
    'path/to/animated.gif',
    '#f7fafc',
    '#ffffff',
    '#2b6cb0',
    '#ffffff',
    '#e2e8f0',
    '#2d3748'
   )
   RETURNING id;
    **Important**
  - If `selectedType = 'CSS'`, provide `editorCss`
  - If `selectedType = 'UI'`, provide `generatedCss`
3. **Bind Theme**
    **Bind to Client**
    Copy CodePL/SQLUPDATE client
   SET "uiConfigId" = 'new-theme-uuid'
   WHERE client_id = 'your_client_id';
    **Bind to Organisation**
    Copy CodePL/SQLUPDATE organisations
   SET "uiConfigId" = 'new-theme-uuid'
   WHERE "organisationId" = 'your_org_id';
    **Validation Rule**: Only one level should contain the theme unless intentional overrides are required.

## Theme Resolution Flow

When a request is received:

```code
/interaction/:id
```

The following sequence is executed:

1. Resolve client
2. Resolve organisation
3. Select the highest-priority UI config
4. Determine rendering mode
5. Apply CSS
6. Resolve asset paths
7. Render login screen

## CSS Variables

Default CSS variables are defined in:

These variables can be overridden using `editorCss` or `generatedCss`.

```code
public/css/layout.css
```

| **Token  ** | **  Description** |
| --- | --- |
| --bg-color | Background Color |
| --login_card_bg_color | Login card background |
| --welcome_color | Welcome text color |
| --field_color | Field text color |
| --input-bg | Input background |
| --primary-button-bg | Primary button background |
| --primary-button-color | Primary button text color |
| --footer-bg | Footer background |
| --footer-color | Footer text color |
| --forgot_pwd_color | Forgot password link color |
| --input-border | Input border color |
| --logo-width | Logo width |
| --logo-margin | Logo margin |
| --logo-gif-width | Animated logo width |
| --logo-gif-margin | Animated logo margin |

**Note**: Overriding undefined variables may not produce any effect.

## Asset Management

### SQL Environment

Upload assets to static storage and store file paths in:

- logo
- animated_logo
- favicon

**Note**: All previously referenced assets, such as the logo, animated logo, and favicons, can be converted to Base64-encoded images. The resulting Base64 strings can be embedded directly within the configuration, replacing external asset references.

### Fallback Behaviour

If an asset fails to load, the system automatically loads a default asset:

```html
onerror="this.src='/static/img/logo.png'"
```

## Updating Themes

### Update CSS

```pl/sql
UPDATE ui_config
SET
    "selectedType" = 'CSS',
    "editorCss" = ':root {
        --primary-button-bg: #1a202c;
        --bg-color: #edf2f7;
    }'
WHERE id = 'theme-id';
```

### Update Assets

```pl/sql
UPDATE ui_config
SET logo = 'new/path/logo.png'
WHERE id = 'theme-id';
```

### Switch Rendering Mode

```pl/sql
UPDATE ui_config
SET "selectedType" = 'CSS'
WHERE id = 'theme-id';
```

## Reset or Delete Theme

### Reset Client Theme

```pl/sql
UPDATE client
SET "uiConfigId" = NULL
WHERE client_id = 'client_id';
```

### Reset Organisation Theme

```pl/sql
UPDATE organisations
SET "uiConfigId" = NULL
WHERE "organisationId" = 'org_id';
```

### Delete Theme

```pl/sql
DELETE FROM ui_config
WHERE id = 'theme-id';
```

**Note**: Delete only after confirming that the configuration is not referenced.

## Troubleshooting

### CSS Not Applying

**Check client configuration**:

```pl/sql
SELECT "uiConfigId"
FROM client
WHERE client_id = 'x';
```

**Check organisation configuration**:

```pl/sql
SELECT "uiConfigId"
FROM organisations
WHERE "organisationId" = 'y';
```

**Check CSS configuration**:

```pl/sql
SELECT "selectedType", "editorCss", "generatedCss"
FROM ui_config
WHERE id = 'id';
```

**Note**: Validate CSS syntax and inspect browser developer tools.

### Logo Not Displaying

Verify:

- File exists
- URL reachable
- No CORS issues
- File integrity
- Valid GridFS reference

### Incorrect Theme Inheritance

Check:

```pl/sql
SELECT "uiConfigId"
FROM client
WHERE client_id = 'x';
```

**Note**: If present, client-level configuration overrides organisation-level themes.

## Best Practices

1. Use CSS Mode for enterprise clients
2. Store CSS in version control
3. Use CSS variables instead of hardcoding
4. Optimize asset sizes
5. Test across browsers
6. Avoid mixing UI and CSS modes
