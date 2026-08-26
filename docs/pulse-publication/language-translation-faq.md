# Language Translation

<https://documentation.neutrinos.com/articles/#!pulse-publication/language-translation-faq>

Ensure that the following API has been called for the respective project ID.

1. curl -X POST "https://yourDomain/configservice/language-translation/add-default-translations"
2. -H "accept: /"
3. -H "Content-Type: application/json"
4. -d '{"projectId": "your-project-id"}'
