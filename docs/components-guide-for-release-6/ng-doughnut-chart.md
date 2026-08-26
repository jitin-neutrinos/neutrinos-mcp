# Doughnut Chart

<https://documentation.neutrinos.com/articles/#!components-guide-for-release-6/ng-doughnut-chart>

## Doughnut Chart

### Overview

Doughnut chart is similar to the pie chart but the difference is that the doughnut chart has a circular hollow gap in the middle of the chart. This circular hollow gap is called cutoutPercentage which represents what percentage of the inner chart should be cut out.

### Usage

A Doughnut chart is widely used in the business world, mass media, and institutions. Let us consider a health center scenario where a particular hospital wants to plot a chart to record the number of patients admitted to different wards. The chart should represent the overall hospital and be divided into different sections which represent the wards of the hospital. This can be achieved by using the Doughnut chart where a complete chart represents the hospital and the slices represent the wards of the hospital. There are some other popular use cases as well. Some of them are:

- Pharmaceutical Industries (indicating the different types of drugs)
- Industries (for providing information on different products and services )
- Government offices (like revenue department)
- Retails (for different types of products they provide)

### How to Use

1. Drag and drop the **Doughnut Chart** from the **Ng Charts **category.
2. Switch to the **Ts** file of the page and then declare the variable and provide values for the following in the component class:

- A dataset array (contains y-axis values and labels of the legend). For example, Copy CodeJavaScriptpublic doughnutChartData: Array<any> = [
    {
    data: [
    25,
    11,
    8,
    9,
    18,
    29
    ]
    }
    ];

- A labels array (contains x-axis values). For example: Copy CodeJavaScriptpublic doughnutChartLabels:string [
   ] = [
    'Emergency & Casualty',
    'Labor Ward',
    'Endoscopy Ward',
    'Coronary Ward',
    'Surgical Ward',
    'General Ward'
   ];

- Legend value (either** true** or **false**). For example, public legend=false;
- Options value. For example, Copy CodeJavaScriptpublic doughnutChartOptions:any = {
    responsive: true
    };

4. Now switch back to Html file of the page and provide the dataset array name in the [datasets] attribute. For example, [datasets] = doughnutChartData

5. Provide the labels name in [labels] attribute. For example, [labels] = doughnutChartLabels

6. Provide the options name in [options] attribute. For example, [options] = doughnutChartOptions

7. Provide the legend name in [legend] attributes. For example, [legend] = legend

8. Save the page and run the application.

### Associated Attributes

- **[label] (String Array): **Labels are the identity of the data series in a doughnut chart. It appears in the legend and tooltips. It gives a specific name to each slice in the doughnut chart. For example, Copy CodeJavaScriptpublic doughnutChartLabels:string [
   ] = [
    'Emergency & Casualty',
    'Labor Ward',
    'Endoscopy Ward',
    'Coronary Ward',
    'Surgical Ward',
    'General Ward'
   ]
   ;

- ** [datasets] (JSON Objects Array):** It is the data of the chart which is framed in a circular slice depending upon the dataset values. For example: Copy CodeJavaScriptpublic doughnutChartData: Array<any> = [
    {
    data: [
    25,
    11,
    8,
    9,
    18,
    29
    ]
    }
   ];

- **chartHover** and** chartClick** (mouse Events): It is an event that appears when the mouse is clicked or placed over the slice of the doughnut chart. For example, displaying labels and point values when the mouse is clicked on the slice of the chart or the mouse is moved over it.
- **Show Legends (Boolean):** It is a name given to the same category of data that is used in plotting the doughnut chart. If it is true, it shows the legends otherwise it does not show.
- **[colors] (Color/color hexadecimal code):** This property provides the user's desired color to the doughnut chart. For example, background-color: #92a8d1;
- **[data]: **Specify the name of the array defined in the TS editor in which the data for the Doughnut Chart is embedded.
- **fxflex: **This property should be used on elements within a fxLayout container and identifies the resizing of that element within the flexbox container flow such as flex-grow, flex-basis, flex-shrink,flex-grow.
- **fxlayout:** Specifies the flex-direction and whether the contents should be wrapped or not. Example, fxLayout=column wrap.
- **[options]: **Specify the name of an array which is defined in the TS editor from which the drop-down list of options must be displayed. For example, [option]=doughtnutchartOptions.
- **Style:** It accepts a string value and affects the different properties (height, width, color, etc.) of the component based on the values provided (eg. background:orange;height:200px;).
- **Class:** The Class attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the Style tab which is opened by selecting the Style side menu. The Class attribute accepts space-separated class names (eg. class1 class2) which are defined in the Style tab as shown below. Copy CodeCSS.class1 {
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

Consider an example of a hospital that wants to record the percentage of patients admitted to different wards such as emergency & casualty, labor ward, Endoscopy Ward, Coronary Care ward, and Surgical Ward using a Doughnut chart.

| Hospital Wards | Emergency & Casualty | Labor Ward | Endoscopy Ward | Coronary Ward | Surgical Ward | General Ward |
| --- | --- | --- | --- | --- | --- | --- |
| Patients(%) | 25 | 11 | 8 | 9 | 18 | 29 |

Perform the following steps:

1. Drag and drop a **Doughnut Chart** to the page container.
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
   doughnutareaChartLabels [datasets]
   doughnutareaChartData [options]doughnutareaChartOptions
5. Save and run the page.
