# Ng Bubble Chart

<https://documentation.neutrinos.com/articles/#!components-guide/ng-bubble-chart>

## Ng Bubble Chart

### Overview

It plots the point using a bubble in three dimensions at the same time. The place to plot the data value is determined by the first two dimensions and the corresponding horizontal and vertical axes. The third dimension of the chart represents the size of the individual bubble which depends on the data values.

### Usage

Bubble charts are widely used in industries. Let's consider a use case where the industry wants to show the services and products it provides, in the different parts of the country. The collected data needs to be plotted on a map of the country region. The bubble graph displays the services provided by the corresponding industry in the different parts of the country. There are some other popular use cases where a bubble chart is used. Some of them are:

- Government Survey
- Healthcare center
- Experimental surveys

### How to use

### 1. Open the newly created page.

2. Drag and drop the bubble chart from the Ng Charts category.

3. Switch to Ts file of the page and then declare the variable and provide values for the following in the component class

- A dataset array (contains y-axis values and labels of the legend). For example,Copy CodeJSONpublic bubbleChartData: Array<any> =
   [
    {
    label: [
    'Deer Population'
    ],
    data: [
    {
    x: 100,
    y: 5,
    r: 10
    },
    {
    x: 60,
    y: 30,
    r: 20
    },
    {
    x: 40,
    y: 60,
    r: 25
    },
    {
    x: 80,
    y: 80,
    r: 50
    }
    ]
    }
   ];

A labels array (contains x-axis values). For example,
Copy CodeJSONpublic bubbleChartLabels:string [
] = [
 'Deer Population'
]
;

- Legend value (either true or false). For example, Copy CodeJSONpublic legend=false;

Options value. For example
Copy CodeJSONpublic bubbleChartOptions:any = {
 responsive: true
}; 4. Now switch back to Html file of the page and provide the dataset array name in the [datasets] attribute. For example,Copy CodeJSON[datasets] = bubbleChartData5. Provide the labels name in [labels] attribute. For example,Copy CodeJSON[
 labels
]
= radarChartLabels6. Provide the legend name in [legend] attribute. For example,Copy CodeJSON[
 legend
]
= legend7. Provide the option name in [Options] attributes. For example,Copy CodeJSON[
 options
]
= radarChartOptions8. Save the page and run the application.**Example**Consider a survey on the population, at different parts of the country. The population in a particular area needs to be displayed on a country map using a bubble. For example,Data/AreaXYRadius of Circle**Area1**1005020**Area2**603010`**Area3**`806515
**Datasets**Here is a sample of a dataset that is declared and initialized in the component class Ts file of the project.Copy CodeJSONpublic bubbleChartData: Array<any> =
[
 {
 label: [
 'Deer Population'
 ],
 data: [
 {
 x: 100,
 y: 5,
 r: 10
 },
 {
 x: 60,
 y: 30,
 r: 20
 },
 {
 x: 40,
 y: 60,
 r: 25
 },
 {
 x: 80,
 y: 80,
 r: 50
 }
 ]
 }
];

**Labels**Here is a sample of a label that is declared and initialized in the component class of **Ts** file of the project.Copy CodeJSONpublic bubbleChartLabels:string [
] = [
 'Deer Population'
]
;
**Legend**Here is a sample of the legend that is declared and initialized in the component class of Ts file of the project.Copy CodeJSONpublic legend=true;**Options**Here is a sample of the options that are declared and initialized in the component class of Ts file of the project.Copy CodeJSONpublic bubbleChartOptions:any = {
 responsive: true
}
;
**Associated Attributes****Label (String Array): **Labels are the identity of the data series in a chart. It appears in the legend and tooltips. It gives a specific name to each data plotted in a circular shape. For example,**Copy CodeJSONpublic bubbleChartLabels:string [
] = [
 'Deer Population'
]
;****Datasets (JSON Objects Array):**Copy CodeJSONpublic bubbleChartData: Array<any> =
 [{
label: ['Deer Population'],
data: [{
 x: 100,
 y: 5,
 r: 10
}, {
 x: 60,
 y: 30,
 r: 20
}, {
 x: 40,
 y: 60,
 r: 25
}, {
 x: 80,
 y: 80,
 r: 50
}]
}];**ChartHover/ChartHistory (mouseEvents):** It is an event which appears when the mouse is clicked or placed over the chart area. For example, displaying label and point value when the mouse is clicked on the bubble of the chart or mouse is moved over it. **Legends (Boolean): **It is a name given to the same category of data that is used in plotting the bubble chart. If it is true, it shows the legends otherwise it does not show.**Color (Color/color hexadecimal code): **This property provides user's desired color to the chart. For example, Copy CodeHTMLbackground-color: #92a8d1;**Key:**Key is used to provide a user custom key point into the chart. It is like a user’s custom parameter provided to the chart section.**Value: **It is a value of the key that the user has provided manually.**Style: **It accepts a string value and affects the different properties (height, width, color etc.) of the component based on the values provided (eg. background:orange;height:200px;).**Class**: **Class** attribute is used to point to a class in a style sheet. A class contains one or more style statements. Classes are created inside the **Style** tab which is opened by selecting the **Style** side menu. The **Class** attribute accepts space separated class names (eg. class1 class2) which are defined in the **Style** tab as shown below. Copy CodeCSS.class1 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
.class2 {
 border-radius:10px;
 flex-basis:10%;
 height:100px;
}
**Support****Devices:** Android, iOS**Browsers:** Latest version of all modern browsers**Dependencies version:**Angular CLI version: 6.0.0 +Cordova version: 7.1.0 +
