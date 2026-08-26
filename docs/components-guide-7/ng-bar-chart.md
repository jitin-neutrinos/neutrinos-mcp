# Bar Chart

<https://documentation.neutrinos.com/articles/#!components-guide-7/ng-bar-chart>

## Bar Chart

### Overview

A **Bar chart** plots the data points using the vertical or horizontal bars providing a good comparison of multiple data points by plotting them side by side.

A **Bar chart** includes additional properties over the Line** chart** such as **barPercentage**, **categoryPercentage**,** barThickness**, and **maxBarThickness**.

### Usage

A **Bar chart** is widely used in the scenario where there is a need for a comparison of multiple data points by plotting them side by side.

Let’s take a banking scenario where the bank generates a chart on the report of its performance. The report chart should consist of net profit margin, assets,

investors, and net bank credit to government (NBCG) for different years. The chart should be self-explanatory and should provide a good comparison.

This can be achieved using the bar chart which plots the data using vertical or horizontal bars. Some of the other popular use cases of bar charts are:

- Industry (product analysis).
- Health Centre (Disease and cure comparison).
- Retails (Sales Comparision).
- Government Surveys (GDP(Gross Domestic Product), PCI(Per Capita Income)).

### How To Use

1. Open the newly created page.
2. Drag and drop a **Bar chart** from** Ng Charts** category.
3. Switch to the **Ts** editor of the page. Declare variables and provide values for the following in the **component **class:
  - A dataset array (contains y-axis values and labels of the legend). For example,

```javascript
public barChartData:Array<any> = [  {    data: [65, 59, 55, 81, 56, 55, 40], label: 'Series A'}  ,  {    data: [28, 48, 40, 19, 86, 27, 90], label: 'Series B'}];
```

- A labels array (contains x-axis values). For example, Copy CodeJavaScriptpublic barChartLabels:Array<any> = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July'
   ]
    ;

- Legend value (either true or false). For example, public legend = false;

- options value. For example, Copy CodeJavaScriptpublic barChartOptions:any = {
    responsive: true
    }
   ;

4. Now switch back to the Html editor of the page and set the following values in the chart's attributes window:

- **[datasets]** = barChartsData
- **[labels]** = barChartLabels
- **[options] **= barChartOptions
- **[legend]** = legend

5. Save the page and run the application.

### Associated Attributes

- **[labels] (String Array): **Labels are the identity of the data series in a chart. It appears in the legend and tooltips. For example, Copy CodeJavaScriptChartLabels:Array<any> = [
    'January',
    ‘February’,
    'March',
    'April',
    'May',
    'June',
    'July'
   ]
   ;

- **[datasets] (JSON Objects Array): **It is a data of the chart which is framed on vertical or horizontal bars. For example, Copy CodeJavaScript{
    data: [
    69,
    72,
    82,
    79,
    92
    ],
    label: 'Net Profit Margin (%)'
   }
   ]
   ;

- **(chartHover)** and **(chartClick) mouse Events:** Events that appear when the mouse is clicked or placed over the bar chart. For example, displaying labels and pointing values when the mouse is clicked on the chart or mouse is moved over the chart.

- **Show Legends (Boolean): **It is a name given to the same category of data that is used in plotting the bar chart. If it is true, it shows the legends otherwise it does not show.
- **[data]:** Specify the name of the array in which the custom data is embedded for the Bar Chart. For example, [data]= bubbleChartData
- **[options]: **Specify the name of an array which is defined in the TS editor from which the drop-down list of options must be displayed. For example, [options]= bubbleChartOptions
- **fxlayout:** Specifies the flex-direction and whether the contents should be wrapped or not. eg. fxLayout=column wrap.
- **fxflex: **This property should be used on elements within a fxLayout container and identifies the resizing of that element within the flexbox container flow such as **flex-grow, flex basis, flex-shrink,flex-grow**.
- **Style:** It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background: orange; height:200px;).
- **Class: **Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the** Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space-separated class names (eg. class1 class2) which are defined in the Style tab as shown below. Copy CodeCSS.class1 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }
   .class2 {
    border-radius:10px;
    flex-basis:10%;
    height:100px;
   }

### Example

Let's take an example of a bank generating a report on different years which includes the performance parameters such as net profit margin, assets, investors, and net bank credit. This is to be submitted to the government (NBCG) in the form of a chart.

| Years | Net Profit Margin(%) | Assets(%) | Investors(%) | Net bank credit to govt(%) |
| --- | --- | --- | --- | --- |
| 2013 | 69 | 60 | 47 | 23 |
| 2014 | 72 | 64 | 59 | 47 |
| 2015 | 82 | 69 | 65 | 50 |
| 2016 | 79 | 79 | 69 | 55 |
| 2017 | 92 | 60 | 80 | 65 |

To create the chart, perform the following steps:

1. Drag and drop a **Bar Chart **component from the **NG Charts** section.
2. In the TS editor of the page, enter the following code: Copy CodeJavaScriptbarChartData:any[] = [
    { data: [65, 59, 80, 81, 56, 55, 40], label: 'Series A' },
    { data: [28, 48, 40, 19, 86, 27, 90], label: 'Series B' }
    ];
   barChartLabels: string[] = ['2006', '2007', '2008', '2009', '2010', '2011', '2012'];
   mycharclick(){
    alert("chart clicked");
    }
3. Navigate back to the **HTML** editor. Double-click the chart to open its attributes window.
4. Enter the following values: AttributeValue[labels]
   barChartLabels
   [datasets]
   barChartData
   [options]barChartOptions
   (chartClick)
   mycharclick()
5. Save and run the page.
