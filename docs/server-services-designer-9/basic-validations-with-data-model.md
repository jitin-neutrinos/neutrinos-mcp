# Basic Validations within Data Model

<https://documentation.neutrinos.com/articles/#!server-services-designer-9/basic-validations-with-data-model>

Validating a Data Model syntactically means checking each entity if it is correct and complies with database modeling standards. When you validate data models, the validations help you correct data models, optimize queries, and enhance the performance.

We have added the following validations within Data Models:

- **Validation for email** - a regex pattern is added to verify whether a given input string is a valid email id match.

![](/resources/Storage/server-services-designer-9/regexpattern.png)

```
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```
