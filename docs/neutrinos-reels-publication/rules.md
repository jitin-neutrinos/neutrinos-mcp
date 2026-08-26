# Types of Rules

<https://documentation.neutrinos.com/articles/#!neutrinos-reels-publication/rules>

Rules are the fundamental unit of Reels, representing a single business entity that determines the outcome of a business event based on incoming data. Rules encapsulate specific logic, driving decisions across various business scenarios. The image below illustrates the layout of the Rule List page:

![rule-list-page](/resources/Storage/neutrinos-reels-publication/images/rule-list-page.png)

1. **Search Bar**: Search for a rule or rule group by name.
2. **Rule and Rule Group Tab**: Switch between Rules and Rule Groups. This displays a list of available rules or rule groups.
3. **Name**: This column displays the name of the rule or rule group.
4. **ID**: This column displays the ID of the rule or rule group.
5. **Version**: This column displays the latest version of the rule or rule group.
6. **Rule Type**: This column displays the type of the rule or rule group.
7. **Author**: This column displays the User ID of the author who created the rule or rule group.
8. **Available From**: This column displays the creation date of the rule or rule group.
9. **Last Update and Time**: This column displays the date and time of the latest update to the rule or rule group.
10. **Actions**: This column provides options to **Clone**, **Export**, or **Delete** the rule or rule group.

## Types of Rules

In the Reels platform, rules are classified into two types: Basic and NLP-based.

### Basic Rule Type

The Basic rule type includes decision tables, formulas, Excel rules, decision trees, APIs, and script rules.

| **Rule Type  ** | **  Description  ** |
| --- | --- |
| Decision Table | Decision tables provide a structured way to represent decision-making logic in a tabular format. They help manage complex rules by specifying various conditions and their corresponding actions. Decision tables are ideal for scenarios where decisions depend on multiple input combinations. For more information, see [Decision Table](/articles/neutrinos-reels-publication/decision-table) topic. |
| Excel Rule | Excel rules enable seamless data and rule management using the familiar spreadsheet interface. They provide data manipulation and rule execution capabilities within a well-known environment. Excel rules are ideal for handling large data volumes, performing calculations, and applying rule logic directly in a spreadsheet format, making them especially useful for spreadsheet users. For more information, see [Excel Rule](/articles/neutrinos-reels-publication/excel-rule) topic. |
| Formula Rule | The Formula rule enables calculations using mathematical or logical expressions. It is designed to compute values based on given inputs, automating tasks such as totals, averages, date differences, and date-based calculations. Formula rules are particularly useful in scenarios requiring dynamic numerical processing. For more information, see [Formula Rule](/articles/neutrinos-reels-publication/formula-rule) topic |
| API Rule | The API rule facilitates integration with external services and systems through an Application Programming Interface (API). It enables seamless interaction with other software, allowing data retrieval and transmission. API rules can connect to third-party services, access external data sources, and integrate with other applications. For more information, see [API Rule](/articles/neutrinos-reels-publication/api-rule) topic. |
| Script Rule | The Script rule allows you to create and execute custom code, enabling complex logic beyond standard rule capabilities. It is used to develop custom functions, automate processes, and perform advanced operations. Script rules are ideal for users with coding experience. For more information, see [Script Rule](/articles/neutrinos-reels-publication/script-rule) topic. |
| Decision Tree | A Decision Tree graphically represents decisions and their possible outcomes in a tree-like structure. It helps visualize decision-making processes by outlining various decision paths and their corresponding results. Decision trees are useful when decisions involve multiple branching conditions. For more information, see [Decision Tree](/articles/neutrinos-reels-publication/decision-tree) topic. |

### NLP Rule Types

Natural Language Processing (NLP) Rule Types process and interpret user inputs in conversational AI applications. These include the Levenshtein Distance Rule, Phonetics Rule, and Sentiment Analysis Rule.

| **  Rule Type  ** | **  Description** |
| --- | --- |
| Levenstein Distance Rule | The Levenshtein Distance Rule calculates the minimum number of edits—insertions, deletions, or substitutions—needed to transform one string into another. It is commonly used in:      Spell checkers.      Autocorrect systems.      Fuzzy matching processes to find words that have similar spellings.     For more information, see [Levenshtein Distance Rule](/articles/neutrinos-reels-publication/levenshtein-distance-rule) topic. |
| Phonetics Rule | Phonetic algorithms like Soundex and Metaphone convert words into codes based on sound rather than spelling. These rules are useful for:      Matching similar-sounding words.      Aid in tasks like search optimization.      Aid in tasks like data deduplication.     For more information, see [Phonetics Rule](/articles/neutrinos-reels-publication/phonetics-rule) topic. |
| Sentiment Analysis Rule | This rule determines the emotional tone (positive, negative, neutral) of the user's text. It is commonly used in:      Analyzing customer feedback.      Social media posts.      Reviews to gauge public opinion and sentiment.     For more information, see [Sentiment Analysis Rule](/articles/neutrinos-reels-publication/sentiment-analysis-rule) topic. |

[Next Topic](/articles/neutrinos-reels-publication/decision-table)

[Previous Topic](/articles/neutrinos-reels-publication/navigating-interface)
