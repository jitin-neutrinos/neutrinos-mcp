# Features

<https://documentation.neutrinos.com/articles/#!pulse-publication/language-translation-plugin-gcc>

The Alpha Module Language Translation is a comprehensive internationalization (i18n) service that provides dynamic language translation capabilities for Alpha applications. It integrates with Handlebars templating to offer flexible and powerful translation features, supporting multiple languages and dynamic content translation.

### Features

- Dynamic Translation: Real-time translation of configuration objects and content
- Handlebars Integration: Powerful templating engine for complex translation scenarios
- Multi-language Support: Support for multiple languages and locales
- Project-based Translations: Integration with Alpha project language translations
- Case Instance Integration: Access to case instance data for contextual translations

### Installation

This module is automatically available via the global ap object when using Alpha UI Base.

### Usage

#### Basic Translation

```javascript
// Access language service via ap.language
const languageService = ap.language;

// Translate configuration object
const config = {
  title: '{{lang.welcome_message}}',
  description: '{{lang.app_description}}',
  button: '{{lang.submit_button}}'
};

const translatedConfig = languageService.translateConfig(config);
console.log(translatedConfig);
// Output: { title: 'Welcome', description: 'Application Description', button: 'Submit' }
```

#### Direct Translation

```javascript
// Translate with custom translations
const customTranslations = {
  lang: {
    greeting: 'Hello',
    farewell: 'Goodbye'
  },
  co: {
    userName: 'John Doe'
  }
};

const content = {
  message: '{{lang.greeting}}, {{co.userName}}!',
  goodbye: '{{lang.farewell}}'
};

const translated = languageService.translate(content, customTranslations);
console.log(translated);
// Output: { message: 'Hello, John Doe!', goodbye: 'Goodbye' }
```
