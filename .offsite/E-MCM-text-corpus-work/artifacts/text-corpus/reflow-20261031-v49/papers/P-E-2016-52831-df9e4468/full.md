# P-E-2016-52831-df9e4468

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
For office use only T1 ________________ T2 ________________ T3 ________________ T4 ________________ Team Control Number 52831 Problem Chosen E For office use only F1 ________________ F2 ________________ F3 ________________ F4 ________________ 2016 MCM/ICM Summary Sheet (Your team's summary should be included as the first page of your electronic submission.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000002 | title | pages [1] -->
Tackling Water Scarcity: Modeling Water Access in India Using Multiple Regression Analysis

<!-- b000003 | prose | pages [1] -->
“Water, water, every where,” lamented the Ancient Mariner, “Nor any drop to drink” [8].  Samuel Taylor Coleridge might as well have been describing India’s water crisis.  It is not an absolute lack of water that threatens India’s water security, but a challenge of managing this critical resource.  Our task was to construct a mathematical model capable of measuring a country’s ability to provide clean water for its population, to use this model to forecast India’s water security fifteen years into the future, to develop an intervention policy to enhance water security, and to use our model to predict the policy’s success over the same time frame.

<!-- b000004 | prose | pages [1] -->
We approached the problem by constructing a series of multiple linear regression models using publicly available data in order to account for the wide variety of factors that influence water access.  We first used a simple two-predictor model that explained 43.7% of the variance in access to water.  Using this basic model as a foundation, we considered a variety of predictors for water security and used a variable selection algorithm to develop a refined model that explained 71.6% of the variance in access to water.

<!-- b000005 | prose | pages [1] -->
After testing the model’s applicability to India’s water supply by comparing model-generated predictions of access to water against published statistics, we used an autoregressive multivariate model to forecast the change of each water access predictor variable over the next fifteen years and the resulting projections to predict changes to India’s water security through the year 2031.  Our model did not directly account for climate change, so we used published data on effects of climate change on water supply to create a climate-corrected forecast model.

<!-- b000006 | prose | pages [1] -->
Finally, we developed a multidisciplinary intervention policy designed to increase the availability of clean water in India.  Using published data to determine appropriate alterations to the predictor values, we simulated the changes in access to water fifteen years after implementation of our proposed policy changes, resulting in a 3.78% increase in water access.

<!-- b000007 | furniture | pages [2] -->
Team # 52831

<!-- b000008 | furniture | pages [2] -->
Page 1

<!-- b000009 | contents | pages [2] -->
Tackling Water Scarcity: Modeling Water Access in India Using

<!-- b000010 | contents | pages [2] -->
Multiple Regression Analysis

<!-- b000011 | heading | pages [2] -->
Contents

<!-- b000012 | contents | pages [2] -->
INTRODUCTION....................................................................................................................................... 2

<!-- b000013 | contents | pages [2] -->
DEFINITIONS.............................................................................................................................................. 2

<!-- b000014 | contents | pages [2] -->
ASSUMPTIONS ........................................................................................................................................... 3

<!-- b000015 | contents | pages [2] -->
Basic Model Assumptions..................................................................................................................... 3

<!-- b000016 | contents | pages [2] -->
Refined Model Assumptions ................................................................................................................. 3

<!-- b000017 | contents | pages [2] -->
MODELS OF THE WATER SCARCITY CRISIS ................................................................................. 4

<!-- b000018 | contents | pages [2] -->
THE BASIC MODEL.................................................................................................................................... 4

<!-- b000019 | contents | pages [2] -->
Description of the Model...................................................................................................................... 4

<!-- b000020 | contents | pages [2] -->
Results................................................................................................................................................... 4

<!-- b000021 | contents | pages [2] -->
Discussion............................................................................................................................................. 4

<!-- b000022 | contents | pages [2] -->
REFINED MODEL ....................................................................................................................................... 5

<!-- b000023 | contents | pages [2] -->
Description of refinements ................................................................................................................... 5

<!-- b000024 | contents | pages [2] -->
Results................................................................................................................................................... 7

<!-- b000025 | contents | pages [2] -->
Discussion............................................................................................................................................. 7

<!-- b000026 | contents | pages [2] -->
APPLICATION OF THE REFINED MODEL TO INDIA..................................................................................... 7

<!-- b000027 | contents | pages [2] -->
Background on the Indian Water Crisis............................................................................................... 7

<!-- b000028 | contents | pages [2] -->
Testing the Model’s Applicability to India ........................................................................................... 8

<!-- b000029 | contents | pages [2] -->
Forecast to 2031................................................................................................................................... 8

<!-- b000030 | contents | pages [2] -->
Forecast accounting for climate change .............................................................................................. 9

<!-- b000031 | contents | pages [2] -->
Discussion............................................................................................................................................. 9

<!-- b000032 | contents | pages [2] -->
INTERVENTION PLAN.......................................................................................................................... 10

<!-- b000033 | contents | pages [2] -->
OVERVIEW AND JUSTIFICATION OF INTERVENTIONS .............................................................................. 10

<!-- b000034 | contents | pages [2] -->
Interventions for water supply............................................................................................................ 10

<!-- b000035 | contents | pages [2] -->
Interventions for sanitation ................................................................................................................ 11

<!-- b000036 | contents | pages [2] -->
Interventions for population growth................................................................................................... 11

<!-- b000037 | contents | pages [2] -->
Interventions for GDP ........................................................................................................................ 11

<!-- b000038 | contents | pages [2] -->
Interventions for pollution and technology ........................................................................................ 11

<!-- b000039 | contents | pages [2] -->
MATHEMATICAL DESCRIPTION OF THE INTERVENTION PLAN................................................................. 12

<!-- b000040 | contents | pages [2] -->
ANALYSIS OF INTERVENTION PLAN ........................................................................................................ 13

<!-- b000041 | contents | pages [2] -->
DISCUSSION............................................................................................................................................. 13

<!-- b000042 | contents | pages [2] -->
CONCLUSIONS........................................................................................................................................ 14

<!-- b000043 | contents | pages [2] -->
FUTURE WORK ...................................................................................................................................... 14

<!-- b000044 | contents | pages [2] -->
REFERENCES.......................................................................................................................................... 15

<!-- b000045 | furniture | pages [3] -->
Team # 52831

<!-- b000046 | furniture | pages [3] -->
Page 2

<!-- b000047 | heading | pages [3] -->
Introduction

<!-- b000048 | prose | pages [3] -->
Human life depends on access to clean water.  While the world possesses an abundance of water, many populations lack access to the clean freshwater essential for life.  The world’s population is currently estimated to have exceeded 7.3 billion people and is projected to reach 8.5 billion by 2030 [20].  Ensuring all these people have access to clean water is a challenge that must be addressed on multiple fronts.

<!-- b000049 | prose | pages [3] -->
Though water is a renewable resource, groundwater and surface freshwater available for drinking or agriculture accounts for only 1% of the world’s total water supply (the vast majority of the rest being ocean water) [14].  Human populations are generally established in regions near water, with only 10% of the world’s population living more than 10 km from a surface freshwater body [12].  However, presence of a freshwater body alone does not guarantee access to safe and clean water.  Despite improvements through technology and education, some regions still practice open defecation or lack sanitation facilities, resulting in contaminated water supplies [26].

<!-- b000050 | prose | pages [3] -->
Numerous factors, ranging from the physical and ecological to the political and socioeconomic, affect whether a country or region experiences water scarcity.  Among these are population growth, agriculture and food production, climate, climate change, land use, water quality or water pollution, demand for water, economic status, professional capacity (including education and working conditions), political issues, social issues [3], and catastrophic events such as droughts or floods.  As of 2007, an estimated 1.2 billion people experience physical scarcity and an additional 1.6 billion experience economic scarcity [21].

<!-- b000051 | prose | pages [3] -->
In India, attempts by the government and other organizations have had some success in developing municipal water supplies [11], but have failed to solve the problem for many Indians, in part due to the country’s large and growing population, which is expected to exceed 1.5 billion people by 2030 [20].

<!-- b000052 | prose | pages [3] -->
In this paper, we address the challenge of modeling (and designing intervention policies against) water scarcity by developing a series of regression models of increasing complexity.  We apply these models, combined with projections of future events such as population growth and climate change, to develop a forecast of future water scarcity in India absent any intervention plan.  Finally, we use our model to propose a possible policy for addressing water scarcity in India and suggest the likely outcome of its implementation.

<!-- b000053 | prose | pages [3] -->
Definitions Because water scarcity is a complicated interdisciplinary problem, it is important to exercise care in operationally defining one’s terms.  Toward that end, in the interest of clarity, we use the following definitions in this paper:

<!-- b000054 | prose | pages [3] -->
• Access to electricity is the percentage of a country’s population with access to electricity according to data from “industry, national surveys, and international sources” [28].

<!-- b000055 | prose | pages [3] -->
• Access to water is the percentage of a country’s population actively using an improved water source [38].

<!-- b000056 | prose | pages [3] -->
• Air pollution, expressed in micrograms per cubic meter, is “the average level of exposure of a nation’s population to concentrations of suspended particles measuring less than 2.5 microns in aerodynamic diameter, which are capable of penetrating deep into the respiratory tract and causing severe health damage” [39].

<!-- b000057 | prose | pages [3] -->
• Clean water is freshwater that meets the criteria of an improved water source.

<!-- b000058 | prose | pages [3] -->
• Freshwater is defined as water that is not ocean water or other salt water.

<!-- b000059 | prose | pages [3] -->
• GDP per capita is a country’s gross domestic product divided by that same country’s midyear population and is reported in current US dollars  [34].

<!-- b000060 | prose | pages [3] -->
• Improved water sources are defined as “piped water on premises” or “other improved drinking water sources” including “public taps or standpipes, tube wells or boreholes, protected dug wells, protected springs, [and] rainwater collection” [27].

<!-- b000061 | furniture | pages [4] -->
Team # 52831

<!-- b000062 | furniture | pages [4] -->
Page 3

<!-- b000063 | prose | pages [4] -->
• Improved sanitation facilities are defined as “likely to ensure hygienic separation of human excreta from human contact” and include systems that flush to a sewer, septic tank, or pit latrine, pit latrines with slab, and composting toilets [27].

<!-- b000064 | prose | pages [4] -->
• Intervention, in the context of this paper, refers to any measure or measures implemented by governments or organizations to directly or indirectly increase a population’s access to clean water.

<!-- b000065 | prose | pages [4] -->
• Pollution is any contaminant introduced into an otherwise safe water supply and which renders the water supply unfit (or less fit) for drinking or use in agriculture.

<!-- b000066 | prose | pages [4] -->
• Population growth is the annual increase in a country’s population counting all permanently settled residents, defined in our models as “the exponential rate of growth of midyear population from year t - 1 to t, expressed as a percentage” [41].

<!-- b000067 | prose | pages [4] -->
• Sanitation is the percentage of a country’s population using improved sanitation facilities [37].

<!-- b000068 | prose | pages [4] -->
• Scarcity of water is a relative measure of the supply of water available to a region against the region’s demand for water; specifically in this case, scarcity of water refers to scarcity of clean water, and is operationally defined as lack of access to water.

<!-- b000069 | prose | pages [4] -->
• Water security is a measure of the ability of a population to ensure supply of clean water meets or exceeds demand; in this paper, we operationally define water security as access to water.

<!-- b000070 | prose | pages [4] -->
• Water supply, expressed in cubic meters, is defined as “renewable internal freshwater resources per capita” [43]

<!-- b000071 | heading | pages [4] -->
Assumptions

<!-- b000072 | prose | pages [4] -->
Water scarcity is a complex interdisciplinary issue with international significance.  Contained within the problem are variables pertaining to politics, economics, culture, human biology, ecology, climatology, geology, and many other disciplines.  It is impossible to fully model every possible relevant factor.  As such, we made several assumptions and simplifications.

<!-- b000073 | prose | pages [4] -->
First, in all cases, we assume that the data we used in our models were both complete and accurate. Inherent in our use of linear regression for the construction of our model, we must assume that all variables included are linearly related to access to clean water, that none of our predictor variables are correlated, the data are normally distributed, and the errors from the regression are normally distributed with mean zero and constant variance. In all models, we assume that percent of population with access to clean water is a direct (inverse) proxy for water scarcity.  Because our model incorporates a forecast, we assume that the relationships between variables will remain consistent for at least the next fifteen years. Finally, due to availability of data, we model 2012 as the “current” year.

<!-- b000074 | prose | pages [4] -->
In addition, each of the particular models we constructed have their own sets of assumptions.

<!-- b000075 | heading | pages [4] -->
Basic Model Assumptions

<!-- b000076 | prose | pages [4] -->
The basic model is our simplest model, so the assumptions we made are few and far-reaching. Specifically, we assume that population growth is a direct proxy for clean water demand and that GDP per capita is a direct proxy for a country’s ability to meet that demand.

<!-- b000077 | heading | pages [4] -->
Refined Model Assumptions

<!-- b000078 | prose | pages [4] -->
For the refined model, the same assumptions apply, with the following additions and modifications:

<!-- b000079 | prose | pages [4] -->
• GDP per capita is a direct proxy for economic ability to promote water security, • A country’s continent and latitude together provide a direct proxy for geographic variance and climate, • Access to electricity is a direct proxy for a country’s technological ability to promote water security, • Air pollution is a direct proxy for industrial and agricultural water pollution.

<!-- b000080 | furniture | pages [5] -->
Team # 52831

<!-- b000081 | furniture | pages [5] -->
Page 4

<!-- b000082 | heading | pages [5] -->
Models of the Water Scarcity Crisis

<!-- b000083 | prose | pages [5] -->
To account for the numerous physical and socioeconomic factors that influence water scarcity, we developed a series of multiple linear regression models of increasing refinement.  The Basic Model provides an extremely simplified view, but served as the basis on which we built the Refined Model, which accounts for more variables.  We used the Refined Model, in turn, to forecast Indian water scarcity and to develop an intervention plan for improving water security in India.

<!-- b000084 | prose | pages [5] -->
For clarity, please note that in our models, all data given as a percentage are reported on a 0 to 100 scale rather than a 0 to 1 scale.

<!-- b000085 | heading | pages [5] -->
The Basic Model

<!-- b000086 | prose | pages [5] -->
For the Basic Model, our goal was simply to establish a baseline against which to measure the improvements of our Refined Model and to quickly locate the limitations of our technique.

<!-- b000087 | heading | pages [5] -->
Description of the Model

<!-- b000088 | prose | pages [5] -->
In this model, we examine two predictors of water security.  First, we treated population growth (annual % increase), as a proxy for a population’s increasing demand for clean water.  Second, we treated GDP per capita (current US$) as a proxy for a population’s ability to meet that demand.  We measured water security as the percentage of the population with access to an improved water source.

<!-- b000089 | prose | pages [5] -->
Using data on 212 countries from the World Bank [34; 38; 41], we constructed a linear regression model in R, treating GDP per capita and population growth as predictors of access to water in 2012.  Plots of the data are shown in Figure 1.

<!-- b000090 | caption | pages [5] -->
Figure 1. Plots of Basic Model data

<!-- b000091 | heading | pages [5] -->
Results

<!-- b000092 | prose | pages [5] -->
Our Basic Model yielded the linear regression equation:

<!-- b000093 | prose | pages [5] -->
W = 0.0002971G −5.354P + 91.38 where:

<!-- b000094 | prose | pages [5] -->
W = Access to water G = GDP per capita P = Population growth, with an adjusted R2 value of 0.437 and statistical significance ( pG = 6.37 ×10−12;pP < 2 ×10−16) on both variables.

<!-- b000095 | heading | pages [5] -->
Discussion

<!-- b000096 | prose | pages [5, 6] -->
These preliminary results show that, under the assumptions of the Basic Model, an increase in the rate of a country’s population growth by one percentage point is, on average, associated with a 5.35% decrease in access to water, holding all other variables constant; similarly, every $1000 increase in GDP per capita results in a 0.297% increase in access to water, with all other variables held constant.  These results make intuitive sense if one considers GDP per capita a proxy for a country’s economic ability to meet water demands and population growth a representation of increase in that demand.

<!-- b000097 | furniture | pages [6] -->
Team # 52831

<!-- b000098 | furniture | pages [6] -->
Page 5

<!-- b000100 | prose | pages [6] -->
Though it ignores numerous important factors, the Basic Model demonstrates the possibility of using multiple linear regression to predict water scarcity, so we used it as a starting point for our Refined Model.

<!-- b000101 | heading | pages [6] -->
Refined Model

<!-- b000102 | prose | pages [6] -->
Beginning from the skeleton of the Basic Model, we chose a set of twenty variables to consider as possible predictors of access to water.  We then chose the subset of these variables resulting in the highest adjusted R2 value.  We used the resulting set of eight predictors to model access to water in 2012.

<!-- b000103 | heading | pages [6] -->
Description of refinements

<!-- b000104 | prose | pages [6] -->
In order to more accurately model access to water, we selected twenty variables from publicly-available datasets.  An overview of these variables and our justification for their selection is presented in Table 1 below.  Once we achieved this cross-section of the physical, social, and economic variables that can affect water scarcity, we culled the subset with the highest adjusted R2 value using the “regsubsets” function in R.  Our Refined Model contains this subset of eight variables (designated with an asterisk in Table 1).

<!-- b000105 | prose | pages [6] -->
We then used a multiple linear regression in R to model these selected variables over 147 countries as predictors of access to water in 2012.  The resulting regression equation is our Refined Model.

<!-- b000106 | caption | pages [6] -->
Table 1. Overview of variables considered for Refined Model (* indicates variables included in Refined

<!-- b000107 | prose | pages [6] -->
Model) Variable Units Justification *Population Annual % We treat population growth as a proxy for a country’s demand for clean Growth [41] increase water; increased population growth is considered to be an increase in demand.

<!-- b000108 | prose | pages [6] -->
*GDP Per Current US $ GDP per capita is our proxy for a country’s economic ability to increase the Capita [34] supply of clean water. *Water Supply Cubic meters Water supply per capita serves as a measure of a country’s total supply of Per Capita [43] freshwater (clean or otherwise), controlled for population size.

<!-- b000109 | prose | pages [6] -->
*Continent Categorical Combined with latitude (see below), the continent on which a country resides serves as a partial metric of geographic variance in access to water between countries.

<!-- b000110 | prose | pages [6] -->
*Access to % of population The proportion of a country’s population has access to electricity is our Electricity [28] proxy for that country’s technological ability to increase the supply of clean water. *Air Pollution Micrograms per Air pollution serves as our proxy for a country’s level of industrial and [39] cubic meter agricultural water pollution in the absence of quality data on levels of water pollution.

<!-- b000111 | prose | pages [6] -->
*Latitude [9] Degrees Combined with the continent on which a country resides, we use latitude as a partial metric of geographic variance in access to water between countries. *Sanitation [37] % of population The portion of a country’s population with access to improved sanitation with access facilities is our (inverse) proxy for individual or domestic water contamination. Total Population Number of The total population of a country serves as a metric of the current demand for [42] individuals clean water.

<!-- b000112 | prose | pages [6] -->
Population People per sq. We use population density as a measurement of a how efficiently a country Density [40] km of land can distribute clean water. Total GDP [33] Current US $ Total GDP is an alternative (to GDP per capita) proxy for a country’s economic ability to increase the supply of clean water.

<!-- b000113 | prose | pages [6] -->
Annual Millimeters per We used annual precipitation as a measure of the climatic variance between Precipitation year countries.

<!-- b000114 | prose | pages [6, 7] -->
[32] Model) Variable Units Justification Rural Population % of total Because water supply strategies may vary between urban and rural [44] population populations, the proportion of a population living in rural areas could affect a country’s ability to supply clean water.

<!-- b000115 | furniture | pages [7] -->
Team # 52831

<!-- b000116 | furniture | pages [7] -->
Page 6

<!-- b000117 | caption | pages [7] -->
Table 1. Overview of variables considered for Refined Model (* indicates variables included in Refined

<!-- b000119 | prose | pages [7] -->
Water Used: % of total Because the amount of water used for various purposes (agricultural, Agriculture [29] freshwater industrial, domestic) differs from country to country, the relative proportions withdrawal of water used in each context could affect the efficiency of a country’s water program.

<!-- b000120 | prose | pages [7] -->
Water Used: % of total See above.

<!-- b000121 | prose | pages [7] -->
Industry [31] freshwater withdrawal Water Used: % of total See above. Domestic [30] freshwater withdrawal Public Health % of total health Because water-borne communicable diseases are a possible result of water Expenditures expenditures scarcity, a country with large public health expenditures may be well- [35] invested in water distribution programs in the public interest; alternatively, countries with large public health expenditures may be facing the consequences of water scarcity.

<!-- b000122 | prose | pages [7] -->
Educational Average years Educated individuals may be able better situated to contribute individually to Attainment [5] per person water conservation; educated societies may be more likely to develop technological advances to improve access to water.

<!-- b000123 | prose | pages [7] -->
Distance to Kilometers Especially in countries without a municipal water supply, the distance to a Navigable River freshwater body such as a river may affect the proportion of the population [9] with access to water. Plots of population growth and GDP per capita are identical to those from the Basic Model and are presented in Figure 1.  Plots of the remaining six variables we used are presented in Figure 2.

<!-- b000124 | caption | pages [7] -->
Figure 2. Plots of Refined Model data

<!-- b000125 | furniture | pages [8] -->
Team # 52831

<!-- b000126 | furniture | pages [8] -->
Page 7

<!-- b000127 | heading | pages [8] -->
Results

<!-- b000128 | prose | pages [8] -->
Our multiple linear regression resulted in the coefficients and p-values reported in Table 2 below, with an adjusted R2 value of 0.716.  Note that because the continent on which a country resides is categorical rather than quantitative data, the continent variable has been split into sub-variables with the following continent codes: AS (Asia), EU (Europe), NA (North America), OC (Oceania), SA (South America).

<!-- b000129 | caption | pages [8] -->
Table 2. Coefficients and p-values for Refined Model variables

<!-- b000130 | prose | pages [8] -->
(variables in bold are significant at the p<0.05 level) Variable Coefficient p-value Population Growth -1.789 0.01523 1.009x10-4 GDP Per Capita 0.02860 1.772x10-5 Water Supply Per Capita 0.19477 Continent: AS -2.448 0.37877 Continent: EU 2.790 0.48747 Continent: NA -0.1394 0.96595 Continent: OC -16.99 0.00853 Continent: SA -6.617 0.08423 7.16x10-7 Access to Electricity 0.2771 Air Pollution 0.1864 0.02161 Sanitation 0.1490 0.00808 Latitude -0.1664 0.00511

<!-- b000131 | heading | pages [8] -->
Discussion

<!-- b000132 | prose | pages [8] -->
All of the data used in the multiple regression to construct this model was from the year 2012.  While we were able to locate some more recent data, 2012 was the most recent year in which we located annual data for a majority of our variables.  Our data on air pollution, however, was the only variable used which did not have any values for 2012.  In order to repair this deficiency, we took the arithmetic mean of 2011 and 2013 values for each country to approximate the 2012 values.  Because this gap is only one year long and we believe catastrophic leaps in air quality are unlikely in such a time frame, we are confident that this estimation introduces a smaller error into our model than would using data from different years.

<!-- b000133 | prose | pages [8] -->
We note also that the coefficient for air pollution is a positive number, where one would intuitively expect a negative number, but we consider this a byproduct of the multiple regression, rather than an error in our model.

<!-- b000134 | heading | pages [8] -->
Application of the Refined Model to India

<!-- b000135 | prose | pages [8] -->
Our goal in this section is to apply our Refined Model to the country of India, use it to forecast India’s water security for the next fifteen years, and then develop and model the success of an intervention designed to increase the Indian population’s access to water.

<!-- b000136 | prose | pages [8] -->
Background on the Indian Water Crisis Though India has the world’s seventh largest economy by nominal GDP [10], and efforts to improve access to water in India have had some success [18] a confluence of factors have placed the country on the brink of water crisis.  Though the drivers of water scarcity are too numerous to address in this paper, we have identified several key causes of the problem.

<!-- b000137 | prose | pages [8] -->
We first note that, though there are environmental factors related to water scarcity (including climate change [36], rainfall patterns, and geographic features such as rivers and groundwater sources), the impending water crisis in India is “predominantly a manmade problem” [7] resulting from failures of socioeconomic systems.

<!-- b000138 | prose | pages [8, 9] -->
India’s population growth is easily the leading threat to water security.  Though India is not a particularly dry country [7], its large and growing population places increasing demands on the water supply, with the result that, though much of the country has access to some water, the current water supply in India is less than 1,000 cubic meters per person, already less than the 1,700 cubic meter per person threshold for considering a country water-stressed [13] and the population is still increasing [20].

<!-- b000139 | furniture | pages [9] -->
Team # 52831

<!-- b000140 | furniture | pages [9] -->
Page 8

<!-- b000142 | prose | pages [9] -->
Additional problems include an insufficient sanitation system (in 2012, only 38% of the Indian population had access to improved sanitation facilities [37], and many individuals are reluctant to use such facilities for cultural reasons [6]) and over-extraction of groundwater resources for agricultural purposes [13].

<!-- b000143 | prose | pages [9] -->
Though our Refined Model does not account for all of these variables, it was drawn from a pool of variables that included measures of water used for agriculture [29], sanitation [37], water supply [43], and population growth [41] (see Table 1).  Additionally, a later extension to the model (see the “Forecast to 2031” section below) accounted for climate change.

<!-- b000144 | heading | pages [9] -->
Testing the Model’s Applicability to India

<!-- b000145 | prose | pages [9] -->
In order get a sense of our forecast’s accuracy, we first tested the model for its applicability to India. Because our model is based on values from 2012, we looked up a literature value and determined that 92.2% of the Indian population had access to water that year [38].

<!-- b000146 | prose | pages [9] -->
Because India was included in the 147 countries in our model, we re-ran the regression with India’s values removed in order to perform and out-of-sample test.  The coefficients and p-values for each variable in this modified model are presented in Table 3.

<!-- b000147 | caption | pages [9] -->
Table 3. Coefficients and p-values for Refined Model with India

<!-- b000148 | prose | pages [9] -->
removed (variables in bold are significant at the p<0.05 level) Variable Coefficient p-value Population Growth -1.723 0.01980 9.826x10-5 GDP Per Capita 0.03320 1.741x10-5 Water Supply Per Capita 0.20258 Continent: AS -2.838 0.31205 Continent: EU 2.537 0.55940 Continent: NA -0.4585 0.88885 Continent: OC -17.11 0.00808 Continent: SA -6.712 0.07994 1.59x10-6 Access to Electricity 0.2698 Air Pollution 0.1713 0.03735 Sanitation 0.1615 0.00509 Latitude -0.1608 0.00701

<!-- b000149 | prose | pages [9] -->
With India’s values removed, our model suggests that 83.2% of India’s population should have had access to water in 2012, while the version with India’s values included suggests that 84.2% of the population should have had access to water in the same year.

<!-- b000150 | prose | pages [9] -->
Though our model’s values for 2012 do not match the actual values, they are close enough to each other that we don’t feel the model is significantly influenced by the presence of India’s own data.  Indeed, we suspect these data support the model’s validity.  The difference between our model’s values and the actual value will be considered in the discussion below.

<!-- b000151 | prose | pages [9] -->
Forecast to 2031 To turn our model from a simple multiple linear regression into a forecast model, we generated forecast data for each variable in the model independently and then re-ran the model as applied to India with the projected data for each of the next fifteen years.  Specifically, we used four techniques to generate the forecast data.

<!-- b000152 | prose | pages [9, 10] -->
For population growth, GDP per capita, and sanitation, we used autoregression in R on each predictor. That is, we ran a regression for each predictor using its most recent value as the dependent variable and the previous 10 years of values as independent variables.  The resulting coefficients were used to forecast the data through the year 2031.  Continent and latitude, as non-variable predictors, were held constant.

<!-- b000153 | furniture | pages [10] -->
Team # 52831

<!-- b000154 | furniture | pages [10] -->
Page 9

<!-- b000156 | prose | pages [10] -->
Because we had limited data available for the remaining three variables, we accounted for their forecasts through various means.  In the case of water supply, we assumed that (absent changes from climate change accounted for later) the total water supply of a country should remain relatively constant.  As such, we averaged the 2012 and 2013 values for water supply and held that value constant through 2031. For access to electricity, we lacked sufficient data for an autoregression, so we assumed the percentage of people without access to electricity would decrease at the same rate as between 1990 and 2012 (approximately 3.7% annually in India).  We then used this rate to project values from 2012 to 2031. Finally, we similarly lacked sufficient data for an autoregression on our air pollution statistic, so we assumed its rate of increase to be constant from 2000 to 2013 (approximately 2.5% annually) and used this rate to project values from 2013 to 2031.

<!-- b000157 | prose | pages [10] -->
Our forecast suggests that by the year 2031, 94.4% of the Indian population should have access to water, up from 84.2% in 2012.  The remainder of the forecast data are shown in Table 4.

<!-- b000158 | caption | pages [10] -->
Table 4. Access to water (% of population) in India from 2012 to 2031

<!-- b000159 | prose | pages [10] -->
Year 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 Access 84.2 84.8 85.5 85.9 86.5 87.2 87.5 88.2 88.6 89.0 to Water Year 2022 2023 2024 2025 2026 2027 2028 2029 2030 2031 Access 89.7 90.1 90.5 91.2 91.6 91.9 92.8 92.9 93.3 94.4 to Water

<!-- b000160 | prose | pages [10] -->
Forecast accounting for climate change In order to account for the effects of climate change, we made a simple alteration to our projections. According to a report by the World Bank, a 3° C increase in temperature by the 2080s could result in a 10% decrease in water supply in South Asia (including India) [45].  We interpret “water supply” in the context of this report to mean a supply of usable clean water, so we treat it as directly applicable to our projections of access to water.  Assuming, then, that the report’s projections hold and that both increase in temperature and decrease in availability of water follow a linear trend, we determined that India might experience a 0.044° C increase in temperature per year and thus a 0.149% decrease in access to water per year, beginning in 2013.

<!-- b000161 | prose | pages [10] -->
Projecting these values forward, we predict a 0.792° C increase in temperature in India by 2031, accompanied by a reduction in access to water of 2.68 percentage points, resulting in a 2031 value for access to water of 91.7% of the population.

<!-- b000162 | heading | pages [10] -->
Discussion

<!-- b000163 | prose | pages [10] -->
We observe that, even though our model’s initial (2012) values for access to water in India are below published values as mentioned above, the positive trend in our forecast is at odds with other forecasts of an impending water crisis in India.  We will discuss possible extensions of this work to further explain this discrepancy in the “Future Work” section.  For now, we interpret this difference in projections as a result of differing metrics of water scarcity.  Even though our model accounts for population growth and sanitation, it is likely that our model is predicting the total freshwater available to the Indian population, and not necessarily the amount the Indian infrastructure is capable of delivering to individual communities or residents.  Therefore, it is possible that India may not have a water shortage in absolute terms, but may still experience a devastating water crisis due to failures in distribution or treatment.

<!-- b000164 | furniture | pages [11] -->
Team # 52831

<!-- b000165 | furniture | pages [11] -->
Page 10

<!-- b000166 | prose | pages [11] -->
Intervention Plan Drinking water is the obvious concern most people would consider when they think of water scarcity. Indeed, according to the World Health Organization, 1.1 billion people lack access to any improved source of clean drinking water [24].  In India, despite past and current efforts to improve drinking water, 21% of communicable diseases remain water-related [18].  Clearly, for this reason alone, any intervention capable of successfully improving access to clean water could improve the lives of millions or billions of people.

<!-- b000167 | prose | pages [11] -->
Despite this obvious consideration, improvement of access to clean water has other, far-reaching consequences.  About 70% of the world’s freshwater supply is used in agriculture [23].  Water scarcity, then, plays a significant role in feeding the world’s population.  In particular, India has become the world’s sixth largest agricultural exporter [22].

<!-- b000168 | prose | pages [11] -->
Water scarcity in India threatens not only the availability of drinking water, but the agricultural supply both for India itself and for importers of Indian crops.  All of this can have complex and far-reaching consequences, but a partial list of effects Indians could experience from water scarcity include: drinking water shortage, poorer health, diminishing food crops, and diminishing international trade.  On the other hand, improved water security can provide exactly the opposite benefits: plentiful clean drinking water, improved health, a strong agricultural industry, and robust international trade.  As such, it is essential to develop interventions designed to improve access to water.

<!-- b000169 | prose | pages [11] -->
In this section, we suggest several different policies designed to improve India’s water security.  While these interventions were considered specifically with India in mind, many of them could easily be applied to other countries or regions.

<!-- b000170 | prose | pages [11] -->
Overview and justification of interventions Because our model accounts for several different variables, we developed intervention techniques focused on different aspects of the water scarcity problem.  Specifically, we looked at:

<!-- b000171 | prose | pages [11] -->
• Water supply, • Sanitation, • Population growth, • GDP per capita, • Pollution, • Technology. Though our model accounts for water pollution through the proxy of air pollution and technological advancement through the proxy of access to electricity, we consider the variables of pollution and technology more broadly in our intervention plan.  In the end, we selected two of these interventions to test in our model, but present our entire collection of proposals for consideration.

<!-- b000172 | prose | pages [11] -->
Interventions for water supply Though water is a renewable resource, it’s part of a dynamic system and regularly changes location. Practically speaking, it is possible to consider the total supply of water on Earth as constant.  It is also generally inefficient to transport large quantities of water long distances.  Furthermore, India is not a particularly dry region [7].  Therefore, we do not consider any methods for increasing the absolute quantity of water available to India.  Instead, we focus on methods of increasing the availability or utility of water that already exists.

<!-- b000173 | prose | pages [11] -->
First, we consider that removal of contaminants could open up vast new reserves of usable freshwater in India.  For instance, the Ganges River is so polluted that the total of toxins, hazardous chemicals, and bacteria in the river are almost 3000 times the WHO’s “safe” limit [1].  Increased regulation to prevent industrial pollution and the introduction of an improved treatment infrastructure, while perhaps costly in the short term, could significantly reduce pollution in existing bodies of water, making available vast quantities of otherwise-unusable freshwater.

<!-- b000174 | furniture | pages [12] -->
Team # 52831

<!-- b000175 | furniture | pages [12] -->
Page 11

<!-- b000176 | prose | pages [12] -->
Furthermore, much of the freshwater in India is transitory.  As much as 45% of the water from precipitation in India is never used as rivers deposit the water into either the Arabian Sea or the Bay of Bengal [2].  Our suggested intervention plan thus includes the collection and storage of rainwater for later use.  This could also reduce the current over-exploitation of groundwater sources for agriculture [13].

<!-- b000177 | prose | pages [12] -->
Interventions for sanitation One of the biggest contributors to water pollution in India is poor individual sanitation practices.  Part of the problem is institutional, in that as of 2012, only 38% of the Indian population had access to improved sanitation facilities [37].  Compounding the problem, certain subsets of the Indian population are reluctant to give up the practice of open defecation for cultural reasons [6].  In order to increase access to improved sanitation facilities, we suggest a large-scale government program dedicated to providing every Indian with access to improved sanitation.  In order to overcome cultural resistance, this program must be accompanied by an educational campaign, and perhaps a program of incentives, to maximize use of the new facilities.

<!-- b000178 | prose | pages [12] -->
Interventions for population growth Three general approaches, best implemented in concert with one another, suggest themselves as interventions to decrease growth in population.  The first and simplest is a program to increase distribution of condoms and increase their use.  Primarily, this must be an education campaign, as the Indian government already distributes condoms free of charge, but the rate at which they are used has recently declined from 26 million in 2007 to 16 million in 2011 [15].  Fortunately, this change is hypothesized to be due to a preference for other contraceptive measures.  However, maintaining or even increasing condom distribution should help to reduce India’s population growth as well as contribute to public health.

<!-- b000179 | prose | pages [12] -->
The second approach, which we have considered in our model, is to increase women’s education.  It is well-established that increasing women’s liberation correlates with declining rates of population growth [17].  We propose a government program to incentivize (and perhaps to subsidize) enrollment in secondary education for women with a goal of increasing women’s secondary education enrollment rates by 1% annually.

<!-- b000180 | prose | pages [12] -->
We also considered a program to educate citizens about family planning alternatives and, perhaps, to incentivize certain family-planning practices.  While the former remains a good idea to help people voluntarily reduce population growth, we suspect the latter could breed contempt among the people for cultural reasons [4].  Additionally, a more aggressive plan such as China’s one-child policy would likely be doomed to failure because as a democracy, India lacks the centralized control to make such policies feasible.

<!-- b000181 | prose | pages [12] -->
Interventions for GDP Because India already has the world’s seventh-largest nominal GDP [10], we don’t feel any intervention is necessary to increase GDP in absolute terms (though any healthy economy should strive toward increasing GDP in general).  However, India also has one of the world’s lowest values of GDP per capita (1262.64 US dollars in 2014), due to its overwhelming population size [19].  Because of this, our recommendation to increase GDP per capita is to focus on reducing population growth, perhaps using the methods suggested above, while maintaining an increase in nominal GDP.

<!-- b000182 | prose | pages [12, 13] -->
Interventions for pollution and technology Our model used proxy statistics for pollution and technology, so we were unable to model any direct interventions for these predictors of water scarcity.  However, we recommend increased investment in renewable clean energy and research for innovative water treatment facilities as an essential part of any plan to maximize water security.  By developing and deploying new water treatment technologies, India can begin to clean up existing pollution, and by investing in renewable clean energy, they can minimize future pollution.  Because India’s shortage is of usable clean water, not water in general, this would go a long way toward solving their problem.  Furthermore, though the effects would not likely be felt within the fifteen years our model forecasts, investment in alternative energy sources can, in the long term, minimize the effects of climate change on water availability.

<!-- b000183 | furniture | pages [13] -->
Team # 52831

<!-- b000184 | furniture | pages [13] -->
Page 12

<!-- b000186 | prose | pages [13] -->
Mathematical description of the intervention plan Because of time constraints and due to the large scope of our intervention plan, we chose to use our model to test two of the interventions: specifically, the sanitation intervention and the women’s education intervention for population growth.

<!-- b000187 | prose | pages [13] -->
To model the effects of the sanitation program, we examined the results of a similar sanitation education program in Bangladesh, the result of which was a drop in open defecation rates from 34% in 1990 to 3% in 2012 [25].  We assumed the results of a comparable program would be similar in India, an estimate we believe to be conservative because our proposed sanitation intervention also includes a large program of distribution of toilets or other sanitation facilities.  Thus, we estimated that the sanitation program would increase our access to sanitation statistic by 1.41% per year, so we modified the sanitation statistic in our Refined Model to reflect this annual increase.

<!-- b000188 | prose | pages [13] -->
It was more difficult to determine a value for the effect of women’s education on population growth.  We first chose a 1% annual increase in women’s secondary education as an arbitrary but, we think, realistic value for the results of a directed campaign to increase women’s social standing through education.  We then used a linear regression analysis comparing published women’s secondary education enrollment data [16] to population growth in order to determine the effect this change would have on the rate of population growth.  The results of this regression are shown in Figure 3.

<!-- b000189 | prose | pages [13] -->
The regression yielded the equation:

<!-- b000190 | prose | pages [13] -->
G = −0.023589E + 3.212242,

<!-- b000191 | prose | pages [13] -->
where:

<!-- b000192 | prose | pages [13] -->
G = Population growth (%) E = Women’s gross enrollment in secondary school (%).

<!-- b000193 | prose | pages [13] -->
The result was significant (p = 7.38x10-8; R2 = 0.2105), so we used the result of this regression analysis to determine the effect on population growth of our hypothetical 1% increase in women’s secondary education.  Specifically, the 1% increase in women’s education resulted in a 0.24% decrease in population growth.

<!-- b000194 | caption | pages [13] -->
Figure 3. Effect of women's secondary education on population growth

<!-- b000195 | prose | pages [13] -->
To account for the results of this intervention, therefore, we subtracted 0.24% from the population growth statistic each year in our Refined Model.

<!-- b000196 | furniture | pages [14] -->
Team # 52831

<!-- b000197 | furniture | pages [14] -->
Page 13

<!-- b000198 | prose | pages [14] -->
Analysis of intervention plan We used our Refined Model to forecast access to water in India fifteen years into the future with and without these interventions in various combinations.  First, we projected water access with and without the interventions without accounting for climate change.  These results are presented in Table 5 and shown graphically in Figure 4.

<!-- b000199 | caption | pages [14] -->
Table 5. Projected access to water in India (2031) with and without interventions and

<!-- b000200 | prose | pages [14] -->
climate change Conditions Access to Water (% of Population) No intervention; not controlled for climate change 94.4 With interventions; not controlled for climate change 98.2 No interventions; controlled for climate change 92.1 With interventions; controlled for climate change 95.9

<!-- b000201 | caption | pages [14] -->
Figure 4. Effects of interventions on access to water in India

<!-- b000202 | prose | pages [14] -->
Finally, we re-ran this forecast to project Indian access to water with and without the interventions and with our model of climate change introduced.  Again, the results are presented in Table 5, and these results are shown graphically in Figure 5.

<!-- b000203 | caption | pages [14] -->
Figure 5. Effects of interventions on access to water in India, controlled for climate change

<!-- b000204 | heading | pages [14] -->
Discussion

<!-- b000205 | prose | pages [14, 15] -->
Though we are not convinced that our model accurately measures the precise amount of clean water available in India, we are convinced that it accurately demonstrates the relative impacts of the various predictors we considered.  We note that both of the interventions we modeled each improved access to water in India over the timeframe considered, and that the conjunction of both interventions resulted in a greater improvement than either did alone.

<!-- b000206 | furniture | pages [15] -->
Team # 52831

<!-- b000207 | furniture | pages [15] -->
Page 14

<!-- b000209 | prose | pages [15] -->
When we introduced climate change into the model, the prospects of access to water worsened.  However, the introduction of both interventions completely mitigated the predicted effects of climate change, resulting in greater access to water than without the interventions, even with climate change excluded from the forecast.

<!-- b000210 | prose | pages [15] -->
This gives us confidence that our intervention plan would significantly improve access to clean water in India.  However, we must also consider the possible impacts of each intervention on neighboring regions or on the ecosystem as a whole.  Fortunately, we anticipate that most interventions will either have no measurable impact on other regions or will have a net positive impact:

<!-- b000211 | prose | pages [15] -->
• Because the bulk of India’s river water is deposited into oceans rather than traversing other countries, collection of precipitation will not deprive downstream regions of an essential water supply.

<!-- b000212 | prose | pages [15] -->
• Removal of pollution from India’s rivers will result in a decrease in pollution of ocean waters.

<!-- b000213 | prose | pages [15] -->
• Reduction of population growth will place less strain on the regional ecology.

<!-- b000214 | prose | pages [15] -->
• Increased women’s education will open up new business opportunities, growing GDP within India and fostering international trade.

<!-- b000215 | prose | pages [15] -->
We do offer this word of caution, however: though we designed our interventions to include alternative energy sources that could combat climate change, it is possible that if only some of the interventions are pursued, or if they are pursued incompletely, an increase in India’s economic productivity could increase carbon dioxide emissions, driving increased climate change.

<!-- b000216 | heading | pages [15] -->
Conclusions

<!-- b000217 | prose | pages [15] -->
India’s water crisis is not caused by any single factor.  Instead, it is an interdisciplinary problem resulting from a perfect storm of otherwise unrelated variables: political, economic, social, geophysical, meteorological, and so on.  While our model does not (indeed, probably can not) account for all of these factors, it used a representative cross-section of the available data to show inexact values for India’s water security, but clearly-defined trends in India’s water security.

<!-- b000218 | prose | pages [15] -->
Our model shows that it is possible to improve India’s water situation and that the most important factors in need of intervention are socioeconomic.  Even though climate change will worsen the problem for India, as our model shows, the greatest challenge for India is to develop the cultural attitudes and to build the critical infrastructure necessary to guarantee access to clean water to all of its people.

<!-- b000219 | heading | pages [15] -->
Future Work

<!-- b000220 | prose | pages [15] -->
Due to time constraints, we were unable to include every variable in our model that we considered. Furthermore, published data on access to water in India belie the severity of India’s water crisis.  As such, though we feel our model was successful in our goal of demonstrating the effects of our variables of interest upon the water supply, we also feel that there is more work to be done to expand this into a more robust model.

<!-- b000221 | prose | pages [15, 16] -->
We would like to address several key areas in future work.  First, some of the necessary data in our model was missing from our publicly-available sources, so any future expansion of this work should strive to expand the data pool for the regression.  Even more importantly, though the initial twenty predictors of water access we used were carefully considered to be a representative cross-section of the factors that influence water security, we would like to reconstruct the model using a much larger pool of variables upon which our variable selection function could act.  In particular, some of our variables (including air pollution and access to electricity) were used as proxy variables that we assume correlated strongly with variables of interest (such as water pollution and technological advancement) for which we could not find quality data.  In the next model, these proxy variables should be replaced with more direct measures.  We would also like to include more quantifiable information about Indian culture in the expanded model.

<!-- b000222 | furniture | pages [16] -->
Team # 52831

<!-- b000223 | furniture | pages [16] -->
Page 15

<!-- b000225 | prose | pages [16] -->
Because the model was not constructed in a country-specific manner, it would be useful to apply the same model to other countries or regions to develop a more complete portrait of the world’s water supply. Results from such an analysis could lead to the development of a model accounting for changes not only to the national water supply of a particular country but to the international water supply.  It could also lead to the development of a concerted international intervention against water scarcity.

<!-- b000226 | prose | pages [16] -->
Finally, moving beyond expansions to the current model, we would like to construct an entirely new model to determine if and how the predictors of water scarcity are interrelated.  Additionally, such a model should account for the possibility of transient or catastrophic events such as droughts.  This could lead to a more refined intervention strategy by targeting specific variables with the goal of creating a cascade effect.

<!-- b000227 | prose | pages [16] -->
No single model will likely ever be able to fully account for the complexity of water scarcity, but through efforts to develop increasingly accurate and refined models, the world can inform its countries and its peoples about continuously improved management strategies so that, in time, no human being should ever have to worry about access to clean water.

<!-- b000228 | heading | pages [16] -->
References

<!-- b000229 | references | pages [16] -->
[1] All About India. “Ganges River Pollution.” The Complete Guide to India. <http://www.all-about-

<!-- b000230 | references | pages [16] -->
india.com/Ganges-River-Pollution.html> (accessed 31 January, 2016)

<!-- b000231 | references | pages [16] -->
[2] Almeida, J. & Dias, R (January, 2016). “Impact of Climate Change on Indian Water Resources.”

<!-- b000232 | references | pages [16] -->
Journal of Global Resources. <http://isdesr.org/sites/vol/jan_2016/6.pdf> (accessed 31 January,

<!-- b000233 | references | pages [16] -->
2016)

<!-- b000234 | references | pages [16] -->
[3] Appelgren, B.G (November 1997). “Proceedings of the Second Expert Consultation on National

<!-- b000235 | references | pages [16] -->
Water Policy Reform in the Near East; Appendix 3: Keynote Paper - Management of Water

<!-- b000236 | references | pages [16] -->
Scarcity: National Water Policy Reform in Relation to Regional Development Cooperation.”

<!-- b000237 | references | pages [16] -->
FAO Corporate Document Repository. <http://www.fao.org/docrep/006/ad456e/ad456e0a.htm>

<!-- b000238 | references | pages [16] -->
(accessed 29 January, 2016)

<!-- b000239 | references | pages [16] -->
[4] Balaiah, D., et al. (April, 2001). “Fertility Attitudes and Family Planning Practices of Men in a Rural

<!-- b000240 | references | pages [16] -->
Community of Maharashtra.” The Journal of Family Welfare.

<!-- b000241 | references | pages [16] -->
<http://medind.nic.in/jah/t01/i1/jaht01i1p56g.pdf> (accessed 1 February, 2016)

<!-- b000242 | references | pages [16] -->
[5] Barro, R., & Lee, J. (2015). “Projections of Educational Attainment by Country.” Barro-Lee

<!-- b000243 | references | pages [16] -->
Educational Attainment Dataset. <http://barrolee.com/data/oup_download_c.htm> (accessed 30

<!-- b000244 | references | pages [16] -->
January, 2016)

<!-- b000245 | references | pages [16] -->
[6] Biswas, S. (October, 2014). “Why India’s sanitation crisis needs more than toilets.” BBC News.

<!-- b000246 | references | pages [16] -->
<http://www.bbc.com/news/world-asia-india-29502603> (accessed 31 January, 2016)

<!-- b000247 | references | pages [16] -->
[7] Brooks, N (August, 2007). “Imminent Water Crisis in India.” Arlington Institute.

<!-- b000248 | references | pages [16] -->
<http://www.arlingtoninstitute.org/wbp/global-water-crisis/606> (accessed 31 January, 2016)

<!-- b000249 | references | pages [16] -->
[8] Coleridge, S.T. (1798). “The Rime of the Ancient Mariner.” Republished by The Poetry Foundation.

<!-- b000250 | references | pages [16] -->
<http://www.poetryfoundation.org/poem/173253> (accessed 31 January, 2016)

<!-- b000251 | references | pages [16] -->
[9] Gallup, J.L., Mellinger, A.D., & Sachs, J.D (November 2007). “Geography Datasets.” Center for

<!-- b000252 | references | pages [16] -->
International Development at Harvard University.

<!-- b000253 | references | pages [16] -->
<http://www.cid.harvard.edu/ciddata/geographydata.htm> (accessed 30 January, 2016)

<!-- b000254 | references | pages [16] -->
[10] Knoema (2015). “World GDP Ranking 2015.” Knoema. <http://knoema.com/nwnfkne/world-gdp-

<!-- b000255 | references | pages [16] -->
ranking-2015-data-and-charts> (accessed 31 January, 2016)

<!-- b000256 | references | pages [16] -->
[11] Kulkarni, V. “Overcoming Water Scarcity.” UNICEF India.

<!-- b000257 | references | pages [16] -->
<http://unicef.in/Story/516/Overcoming-Water-Scarcity> (accessed 29 January, 2016)

<!-- b000258 | furniture | pages [17] -->
Team # 52831

<!-- b000259 | furniture | pages [17] -->
Page 16

<!-- b000260 | references | pages [17] -->
[12] Kummu, M., de Moel, H., Ward, P.J., & Varis, O. (June, 2011) “How Close Do We Live to Water?

<!-- b000261 | references | pages [17] -->
A Global Analysis of Population Distance to Freshwater Bodies.” PLoS ONE.

<!-- b000262 | references | pages [17] -->
<http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3110782/> (accessed 29 January, 2016)

<!-- b000263 | references | pages [17] -->
[13] Luthra, S., & Kundu, A. (August, 2013). “India’s Water Crisis: Causes and Cures.” The National

<!-- b000264 | references | pages [17] -->
Bureau of Asian Research. <http://www.nbr.org/research/activity.aspx?id=356> (accessed 31

<!-- b000265 | references | pages [17] -->
January, 2016)

<!-- b000266 | references | pages [17] -->
[14] McMichael, C.E. (September, 2014). “Freshwater.” The Encyclopedia of Earth.

<!-- b000267 | references | pages [17] -->
<http://www.eoearth.org/view/article/152861/> (accessed 29 January, 2016)

<!-- b000268 | references | pages [17] -->
[15] Mohan, K. (October, 2013). “Condom Use in India Drops By Nearly 40 Percent In 5 Years As Use

<!-- b000269 | references | pages [17] -->
Of Women-Centric Contraceptives Rises.” International Business Times.

<!-- b000270 | references | pages [17] -->
<http://www.ibtimes.com/condom-use-india-drops-nearly-40-percent-5-years-use-women-

<!-- b000271 | references | pages [17] -->
centric-contraceptives-rises-1429642> (accessed 31 January, 2016)

<!-- b000272 | references | pages [17] -->
[16] Nation Master. “Education > School enrollment, secondary, female > % gross: Countries

<!-- b000273 | references | pages [17] -->
Compared.” Nation Master. <http://www.nationmaster.com/country-info/stats/Education/School-

<!-- b000274 | references | pages [17] -->
enrollment%2C-secondary%2C-female/%25-gross#country> (accessed 31 January, 2016)

<!-- b000275 | references | pages [17] -->
[17] Palmer, L. (2014). “Faminie Is a Feminist Issue: To feed the world, start by teaching girls to read.”

<!-- b000276 | references | pages [17] -->
Slate.

<!-- b000277 | references | pages [17] -->
<http://www.slate.com/articles/health_and_science/feed_the_world/2014/04/educate_women_an

<!-- b000278 | references | pages [17] -->
d_save_babies_how_to_control_population_and_end_hunger.html> (accessed 1 February, 2016)

<!-- b000279 | references | pages [17] -->
[18] Snyder, S. “Water in Crisis - India.” The Water Project. <https://thewaterproject.org/water-in-crisis-

<!-- b000280 | references | pages [17] -->
india> (accessed 31 January, 2016)

<!-- b000281 | references | pages [17] -->
[19] Trading Economics (2016). “India GDP per capita 1960-2016.” Trading Economics

<!-- b000282 | references | pages [17] -->
<http://www.tradingeconomics.com/india/gdp-per-capita> (accessed 1 February, 2016)

<!-- b000283 | references | pages [17] -->
[20] United Nations Department of Economic and Social Affairs (2015). “World Population Prospects:

<!-- b000284 | references | pages [17] -->
Key findings & advance tables: 2015 revision.” United Nations Department of Economic and

<!-- b000285 | references | pages [17] -->
Social Affairs. <http://esa.un.org/unpd/wpp/Publications/Files/Key_Findings_WPP_2015.pdf>

<!-- b000286 | references | pages [17] -->
(accessed 29 January, 2016)

<!-- b000287 | references | pages [17] -->
[21] United Nations Water (March 2007). “Coping With Water Scarcity: Challenge of the Twenty-First

<!-- b000288 | references | pages [17] -->
Century.” Food and Agriculture Organization of the United Nations.

<!-- b000289 | references | pages [17] -->
<http://www.fao.org/nr/water/docs/escarcity.pdf> (accessed 29 January, 2016)

<!-- b000290 | references | pages [17] -->
[22] USDA (August, 2014). “India’s Agricultural Exports Climb to Record High.” United States

<!-- b000291 | references | pages [17] -->
Department of Agriculture Foreign Agricultural Service. <http://www.fas.usda.gov/data/india-s-

<!-- b000292 | references | pages [17] -->
agricultural-exports-climb-record-high> (accessed 31 January, 2016)

<!-- b000293 | references | pages [17] -->
[23] USGS. “Irrigation water use.” The USGS Water Science School.

<!-- b000294 | references | pages [17] -->
<http://water.usgs.gov/edu/wuir.html> (accessed 31 January, 2016)

<!-- b000295 | references | pages [17] -->
[24] WHO. “Health through safe drinking water and basic sanitation.” World Health Organization.

<!-- b000296 | references | pages [17] -->
<http://www.who.int/water_sanitation_health/mdg1/en/> (accessed 31 January, 2016)

<!-- b000297 | references | pages [17] -->
[25] WHO (2014). “Progress on Drinking Water and Sanitation: 2014 Update.” World Health

<!-- b000298 | references | pages [17] -->
Organization.

<!-- b000299 | references | pages [17] -->
<http://www.wssinfo.org/fileadmin/user_upload/resources/JMP_report_2014_webEng.pdf>

<!-- b000300 | references | pages [17] -->
(accessed 31 January, 2016)

<!-- b000301 | references | pages [17] -->
[26] WHO, UNICEF (2014). “Progress on sanitation and drinking-water - 2014 update.” World Health

<!-- b000302 | references | pages [17] -->
Organization.

<!-- b000303 | references | pages [17] -->
<http://apps.who.int/iris/bitstream/10665/112727/1/9789241507240_eng.pdf?ua=1> (accessed 29

<!-- b000304 | references | pages [17] -->
January, 2016)

<!-- b000305 | references | pages [17] -->
[27] WHO, UNICEF (2015). “Progress on sanitation and drinking-water: 2015 update and MDG

<!-- b000306 | references | pages [17] -->
Assessment” World Health Organization.

<!-- b000307 | references | pages [17] -->
<http://www.wssinfo.org/fileadmin/user_upload/resources/JMP-Update-report-

<!-- b000308 | references | pages [17] -->
2015_English.pdf> (accessed 29 January, 2016)

<!-- b000309 | references | pages [17] -->
[28] World Bank (2015). “Access to electricity (% of population).” World Bank Data.

<!-- b000310 | references | pages [17] -->
<http://data.worldbank.org/indicator/EG.ELC.ACCS.ZS> (accessed 30 January, 2016)

<!-- b000311 | references | pages [17] -->
[29] World Bank (2015). “Annual freshwater withdrawals, agriculture (% of total freshwater

<!-- b000312 | references | pages [17] -->
withdrawal).” World Bank Data. <http://data.worldbank.org/indicator/ER.H2O.FWAG.ZS>

<!-- b000313 | references | pages [17] -->
(accessed 30 January, 2016)

<!-- b000314 | furniture | pages [18] -->
Team # 52831

<!-- b000315 | furniture | pages [18] -->
Page 17

<!-- b000316 | references | pages [18] -->
[30] World Bank (2015). “Annual freshwater withdrawals, domestic (% of total freshwater withdrawal).”

<!-- b000317 | references | pages [18] -->
World Bank Data. <http://data.worldbank.org/indicator/ER.H2O.FWDM.ZS> (accessed 30

<!-- b000318 | references | pages [18] -->
January, 2016)

<!-- b000319 | references | pages [18] -->
[31] World Bank (2015). “Annual freshwater withdrawals, industry (% of total freshwater withdrawal).”

<!-- b000320 | references | pages [18] -->
World Bank Data. <http://data.worldbank.org/indicator/ER.H2O.FWIN.ZS> (accessed 30

<!-- b000321 | references | pages [18] -->
January, 2016)

<!-- b000322 | references | pages [18] -->
[32] World Bank (2015). “Average precipitation in depth (mm per year).” World Bank Data.

<!-- b000323 | references | pages [18] -->
<http://data.worldbank.org/indicator/AG.LND.PRCP.MM> (accessed 30 January, 2016)

<!-- b000324 | references | pages [18] -->
[33] World Bank (2015). “GDP at market prices (current US$).” World Bank Data.

<!-- b000325 | references | pages [18] -->
<http://data.worldbank.org/indicator/NY.GDP.MKTP.CD> (accessed 30 January, 2016)

<!-- b000326 | references | pages [18] -->
[34] World Bank (2015). “GDP per capita (current US$).” World Bank Data.

<!-- b000327 | references | pages [18] -->
<http://data.worldbank.org/indicator/NY.GDP.PCAP.CD> (accessed 30 January, 2016)

<!-- b000328 | references | pages [18] -->
[35] World Bank (2015). “Health expenditure, public (% of total health expenditure).” World Bank Data.

<!-- b000329 | references | pages [18] -->
<http://data.worldbank.org/indicator/SH.XPD.PUBL> (accessed 30 January, 2016)

<!-- b000330 | references | pages [18] -->
[36] World Bank (June, 2013). “India: Climate Change Impacts.” The World Bank.

<!-- b000331 | references | pages [18] -->
<http://www.worldbank.org/en/news/feature/2013/06/19/india-climate-change-impacts>

<!-- b000332 | references | pages [18] -->
(accessed 31 January, 2016)

<!-- b000333 | references | pages [18] -->
[37] World Bank (2015). “Improved sanitation facilities (% of population with access).” World Bank

<!-- b000334 | references | pages [18] -->
Data. <http://data.worldbank.org/indicator/SH.STA.ACSN> (accessed 30 January, 2016)

<!-- b000335 | references | pages [18] -->
[38] World Bank (2015). “Improved water source (% of population with access).” World Bank Data.

<!-- b000336 | references | pages [18] -->
<http://data.worldbank.org/indicator/SH.H2O.SAFE.ZS> (accessed 30 January, 2016)

<!-- b000337 | references | pages [18] -->
[39] World Bank (2015). “PM2.5 air pollution, mean annual exposure (micrograms per cubic meter).”

<!-- b000338 | references | pages [18] -->
World Bank Data <http://data.worldbank.org/indicator/EN.ATM.PM25.MC.M3> (accessed 30

<!-- b000339 | references | pages [18] -->
January, 2016)

<!-- b000340 | references | pages [18] -->
[40] World Bank (2015). “Population density (people per sq. km of land area).” World Bank Data.

<!-- b000341 | references | pages [18] -->
<http://data.worldbank.org/indicator/EN.POP.DNST> (accessed 30 January, 2016)

<!-- b000342 | references | pages [18] -->
[41] World Bank (2015) “Population growth (annual %).” World Bank Data.

<!-- b000343 | references | pages [18] -->
<http://data.worldbank.org/indicator/SP.POP.GROW> (accessed 30 January, 2016)

<!-- b000344 | references | pages [18] -->
[42] World Bank (2015). “Population, total.” World Bank Data.

<!-- b000345 | references | pages [18] -->
<http://data.worldbank.org/indicator/SP.POP.TOTL> (accessed 30 January, 2016)

<!-- b000346 | references | pages [18] -->
[43] World Bank (2015). “Renewable internal freshwater resources per capita (cubic meters).” World

<!-- b000347 | references | pages [18] -->
Bank Data. <http://data.worldbank.org/indicator/ER.H2O.INTR.PC> (accessed 30 January, 2016)

<!-- b000348 | references | pages [18] -->
[44] World Bank (2015). “Rural population (% of total population).” World Bank Data.

<!-- b000349 | references | pages [18] -->
<http://data.worldbank.org/indicator/SP.RUR.TOTL.ZS> (accessed 30 January, 2016)

<!-- b000350 | references | pages [18] -->
[45] World Bank (June, 2013). “Turn Down the Heat: Climate Extremes, Regional Impacts, and the Case

<!-- b000351 | references | pages [18] -->
for Resilience.” The World Bank.

<!-- b000352 | references | pages [18] -->
<http://www.worldbank.org/content/dam/Worldbank/document/Full_Report_Vol_2_Turn_Down

<!-- b000353 | references | pages [18] -->
_The_Heat_%20Climate_Extremes_Regional_Impacts_Case_for_Resilience_Print%20version_F

<!-- b000354 | references | pages [18] -->
INAL.pdf> (accessed 31 January, 2016)
