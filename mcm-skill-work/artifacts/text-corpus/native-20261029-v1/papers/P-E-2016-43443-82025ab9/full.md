# P-E-2016-43443-82025ab9

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
For ofﬁce use only

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
43443

<!-- b000005 | prose | pages [1] -->
T1 ________________ F1 ________________

<!-- b000006 | prose | pages [1] -->
T2 ________________ Problem Chosen F2 ________________

<!-- b000007 | title | pages [1] -->
E

<!-- b000008 | prose | pages [1] -->
T3 ________________ F3 ________________

<!-- b000009 | prose | pages [1] -->
T4 ________________ F4 ________________

<!-- b000010 | title | pages [1] -->
2016

<!-- b000011 | prose | pages [1] -->
MCM/ICM

<!-- b000012 | heading | pages [1] -->
Summary Sheet

<!-- b000013 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.)

<!-- b000014 | prose | pages [1] -->
Type a summary of your results on this page. Do not include the name of your school, advisor, or

<!-- b000015 | prose | pages [1] -->
team members on this page.

<!-- b000016 | prose | pages [1] -->
In this paper, we formulate an “excess water ratio” (EWR) metric for water scarcity that improves upon currently used metrics such as the Water Stress Index (WSI) by computing the per capita excess water available in a region. This provides a more illuminating description of the impact of water shortages on individuals. To determine the amount of excess water in a region, we start with  the amount of naturally available water, then subtract out water usage from each primary category: personal use, industrial use, and agricultural use. Dividing this by the total population of a region allows us to determine the annual amount of water that is available but unused for every individual, a goal which is unique to our model.  We note as well that depriving an ecosystem of all available water carries serious environmental consequences. In our case study, we apply our model to India, which in addition to having the second largest population in the world, also suffers from a large scale lack of safe drinking water and a high rate of waterborne diseases. In applying our model to predictions of India's water scarcity in 2031, we ﬁrst model growth rates for the environmental and social factors that inﬂuence water use to determine the growth of water needs over the next ﬁfteen years. We develop a secondary model on MATLAB that utilizes local predictions of water use and population growth from the Indian government to extrapolate our EWR measure. Taking these two models together, we conclude that the excess water per capita in India will be around half of its current level by 2031. We proceed to explore several intervention measures for India's water crisis that emphasize the need to address the supply and demand sides of the water equation, including watershed development, waste treatment, and broader cultural changes in food production. We ﬁnd the cumulative impact of the proposed infrastructure improvements to be minimal. Implementing both these changes would delay the point at which India's EWR diminishes to zero by just one year (from 2083 to 2084). When we assume changes in agriculture we begin to see more impact. Speciﬁcally, switching all rice and wheat production in the country to millet over a thirty year period pushes the year India hits zero EWR back to 2097. All of this means that large cultural shifts in demand for water will ultimately be necessary for India to achieve long-term water sustainability.

<!-- b000017 | heading | pages [2] -->
A Model for Projected Water Needs and

<!-- b000018 | prose | pages [2] -->
Intervention Strategies in India

<!-- b000019 | prose | pages [2] -->
Control #43443

<!-- b000020 | prose | pages [2] -->
February 1, 2016

<!-- b000021 | heading | pages [2] -->
Contents

<!-- b000022 | contents | pages [2] -->
1

<!-- b000023 | heading | pages [2] -->
Introduction

<!-- b000024 | prose | pages [2] -->
2

<!-- b000025 | heading | pages [2] -->
Model for Water Needs

<!-- b000026 | prose | pages [2] -->
2

<!-- b000027 | prose | pages [2] -->
3 . . . . . . . . . . . . . . . . . . . . . . 2.1 Outline of Our Approach 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000028 | heading | pages [2] -->
Assumptions

<!-- b000029 | prose | pages [2] -->
3 An Approach to Projecting Water Availability 2.3 . . . . . . . . . .

<!-- b000030 | prose | pages [2] -->
4 Evaluation of the Model . . . . . . . . . . . . . . . . . . . . . . . 2.4 6 Correlation with Water Stress Indicator (WSI) . . . . . . 2.4.1 6 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4.2 7 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4.3 7 A More Complex Model for Water Availability 2.5

<!-- b000031 | prose | pages [2] -->
3 Case Study: India

<!-- b000032 | prose | pages [2] -->
. . . . . . . . . .

<!-- b000033 | prose | pages [2] -->
7

<!-- b000034 | prose | pages [2] -->
8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 Rationale 8 Main Drivers of Water Scarcity . . . . . . . . . . . . . . . . . . . 3.2 8

<!-- b000035 | prose | pages [2] -->
Prediction of Water in India in 15 Years 4 9 Determining the Current State of Water Scarcity . . . . . . . . . 4.1 9 Preliminary Estimation of Growth Rates of Water Use . . . . . . 4.2 10 A More Robust Computer Model . . . . . . . . . . . . . . . . . . 4.3 11 Assumptions for the Computer Model . . . . . . . . . . . 4.3.1 14 Conclusions for Impacts on Citizens 4.4

<!-- b000036 | prose | pages [2] -->
5 Intervention Plans for India

<!-- b000037 | prose | pages [2] -->
. . . . . . . . . . . . . . . .

<!-- b000038 | prose | pages [2] -->
14

<!-- b000039 | prose | pages [2] -->
14 Intervention Plans for India’s Water Scarcity 5.1 . . . . . . . . . . .

<!-- b000040 | prose | pages [2] -->
14 Watershed Development . . . . . . . . . . . . . . . . . . . 5.1.1 15 Water Recycling and Waste Treatment . . . . . . . . . . . 5.1.2 16 Societal Changes in Food Consumption 5.1.3 . . . . . . . . . .

<!-- b000041 | prose | pages [2] -->
16 Changes in Food Production 5.1.4 . . . . . . . . . . . . . . . .

<!-- b000042 | prose | pages [2] -->
16 Impact of Water Available of Surrounding Area . . . . . . . . . . 5.2 17 Evaluation of Strengths and Weaknesses . . . . . . . . . . . . . . 5.3 17

<!-- b000043 | prose | pages [2] -->
Projection of Future Water Availability for India 6

<!-- b000044 | prose | pages [2] -->
7

<!-- b000045 | heading | pages [2] -->
Conclusion

<!-- b000046 | prose | pages [2] -->
18

<!-- b000047 | prose | pages [2] -->
20

<!-- b000048 | prose | pages [2] -->
1 1

<!-- b000049 | prose | pages [3] -->
Page 2 Control # 43443

<!-- b000050 | prose | pages [3] -->
1

<!-- b000051 | heading | pages [3] -->
Introduction

<!-- b000052 | prose | pages [3] -->
Water has been absolutely critical for all humans, everywhere, since the be- ginning of time. Every human needs at a bare minimum 20 liters of water to survive. [1] The need for that water is rooted deeply in our biology: at 1% water deﬁciency humans get thirsty, a 5% shortfall causes fever, at 10% short we are rendered immobile, and death strikes after just a week of 12-15% water loss. [2] Given these biological realities, it is not a surprise that the ﬁrst and most basic category of water use in human society is personal consumption.

<!-- b000053 | prose | pages [3] -->
However, it is not enough to simply have suﬃcient water to drink. In terms of total water consumption, personal use is actually a fairly small – if absolutely essential – piece of the pie, just 5% on average of a given country’s consumption. [3] By far the majority of water that all societies consume, 75% on average, is used not to keep from dying of thirst but rather to keep from dying of hunger; on agriculture. And in the middle, at 20% of water consumption, is industry.

<!-- b000054 | prose | pages [3] -->
On the face of it, it is hard to imagine why water scarcity could ever be an issue on a planet that is 70% covered with water [4]. The problem arises when we consider the conditions that make water usable: it must be fresh (not too salty), liquid, and physically accessible. The ﬁrst condition eliminates all but 2.5% of all water from consideration, the second eliminates two thirds of that which remains, and the ﬁnal condition brings the total fresh, liquid water near or at the surface (ie usable water) down to just 0.003% of earth’s fresh water. [3]

<!-- b000055 | prose | pages [3] -->
All that said, due to natural replenishment through the water cycle, even that tiny fraction of available water has managed to sustain all human life that has existed since antiquity. The main reason to expect that condition to be dif- ferent going forward is that the exponential nature of human population growth that has been occurring since roughly the Industrial Revolution is completely unprecedented historically. To contextualize the current situation, realize that it took almost 12,000 years for the human population to go from zero (circa 10,000 BCE) to one billion (circa 1800 CE). It took 125 years to go from one billion to two circa 1930, 30 years to get from two to three billion in 1959, and 15 years or less to acquire each remaining billion, all the way up to today’s current global population: about 7.3 billion people. [5] [6] And globally we are continuing to grow; the UN projects that there will be over 11 billion people by the year 2100. [7]

<!-- b000056 | prose | pages [3] -->
This ongoing massive increase in the number of people around the world drives up water usage in all three categories. More people means more direct individual consumers of their 20 daily liters, it means that more societies will develop water intensive industry, and most importantly it means that everyone must grow more crops. Incidentally the latter two have also historically and currently contributed to increasing pollution, thereby even further decreasing the total amount of usable water available. [8]

<!-- b000057 | prose | pages [3] -->
In short, humanity currently faces conditions of water scarcity that are com- pletely unprecedented in human history.

<!-- b000058 | prose | pages [3] -->
As a global community accurately modeling future water needs and developing strategies we are all able and will-

<!-- b000059 | prose | pages [4] -->
Page 3 Control # 43443

<!-- b000060 | prose | pages [4] -->
ing to implement to bring necessary water consumption down to (or preferably somewhere far below) the upper limit of physical water availability will be one of the deﬁning challenges of our time. But we must ﬁnd a way; the survival of the human race hangs precariously in the balance.

<!-- b000061 | prose | pages [4] -->
2

<!-- b000062 | heading | pages [4] -->
Model for Water Needs

<!-- b000063 | prose | pages [4] -->
2.1 Outline of Our Approach

<!-- b000064 | prose | pages [4] -->
In formulating a quantitative measure of water scarcity, we start with a reﬂection of the Water Stress Indicator (WSI) which was created in 2005 by Smakhthin, et al. [9] This model has credibility due to its precedent of use in informing international policy making, as the UN Environmental Programme uses the WSI as its measure of water scarcity on public maps.[10] The WSI is calculated using the following formula:

<!-- b000065 | prose | pages [4] -->
Water Withdrawals Water Stress Indicator(WSI) = Mean Annual Runoﬀ(MAR)

<!-- b000066 | prose | pages [4] -->
Water withdrawals are thus interpreted as a reﬂection of water use and the MAR is interpreted as a reﬂection of water availability. According to the U.S. Geological Survey, mean annual runoﬀis equivalent to the diﬀerence between water available from precipitation and water lost due to evaporation.[11] Water withdrawals are taken as a sum of water withdrawals for the primary uses of water within a region: industrial, agricultural, and personal. Beyond its use in the WSI, this summation has precedent in Vorosmarty’s index of local relative water use and reuse (2005) and Shiklomanov and Markova’s water resources vulnerability index (1993). [10]

<!-- b000067 | prose | pages [4] -->
A signiﬁcant weakness with the use of the WSI is that it does not allow for any conclusions to be drawn about the average impact of water scarcity on an individual level. Two regions with the same levels of water availability and water use will have diﬀerent strains on the daily living of individuals within the regions depending on their populations. Thus a more thorough reﬂection of a region’s water scarcity should be dependent on the population of the region. Our approach in developing our model is thus to use data that is representative of water use and availability and formulating a ratio that determines how much water this leaves per capita for recreational, commercial, or hygienic uses.

<!-- b000068 | prose | pages [4] -->
2.2

<!-- b000069 | heading | pages [4] -->
Assumptions

<!-- b000070 | prose | pages [4] -->
There are a myriad of cultural and environmental factors that impact the avail- ability of water and how much water is needed to sustain the standards of living of the region. Because it is impossible to account for the impact of each of these factors on the overall water demands and availability, we adopt a number of simplifying assumptions for our model:

<!-- b000071 | prose | pages [5] -->
Page 4 Control # 43443

<!-- b000072 | prose | pages [5] -->
• The only source of water for a region is its MAR. There is precedent for this assumption in the prevailing models of the Water Stress Indicator (WSI) and the USGS. The assumption is reasonable because while other technologies exist to acquire water, these are not yet widespread enough to present long term solutions to water shortages.

<!-- b000073 | prose | pages [5] -->
• Utility from water use for individuals is a strictly increasing monotonic function. This assumption allows us to conclude that individuals, regard- less of current water levels, would enjoy having more water available to them. Therefore, although cultural practices in various regions create a perceived need of diﬀerent water levels, we assume that an increase in water availability would be appreciated by any individual.

<!-- b000074 | prose | pages [5] -->
• The current aggregate level of water use is in a temporary equilibrium, as the region seeks to eﬃciently use all of the water that it has available based on existing demands and technologies. This assumption is reasonable be- cause to assume the opposite would imply that the region is currently using more water than is physically present.

<!-- b000075 | prose | pages [5] -->
• Government policy and individuals are informed about the safety of the water available to them and accordingly use the available water for appro- priate purposes. Historically, this assumption has not always held because the assumption of unclean water has led to diseases. A more complex model would take into account the ubiquity of this knowledge throughout the population.

<!-- b000076 | prose | pages [5] -->
• Geographic distribution of water sources and consumption is not a factor in a country’s water scarcity.

<!-- b000077 | prose | pages [5] -->
In reality, available water in one region does not necessarily provide adequate water to another region due to the economic and logistical challenges of transporting large quantities of water. However, because people commonly settle and farm in land with abundant water, we do not consider the eﬀects of transportation of water in our model.

<!-- b000078 | prose | pages [5] -->
2.3 An Approach to Projecting Water Availability

<!-- b000079 | prose | pages [5] -->
In the ﬁrst formulation of the model, we use the process outlined above to come up with a general formula for water use and water availability, and then create an Excess Water Ratio (EWR). The excess water ratio represents the amount of unused water in a region that is available per person. A higher ratio implies that more water is available per person, and thus a higher EWR for a region suggests that water scarcity is less of a concern for the region:

<!-- b000080 | prose | pages [5] -->
Water Use = Water Use from Industry + Water Use for Agriculture

<!-- b000081 | prose | pages [5] -->
+ Water Use for Personal Use

<!-- b000082 | prose | pages [5] -->
Water Availability = Mean Annual Runoﬀ

<!-- b000083 | prose | pages [6] -->
Page 5 Control # 43443

<!-- b000084 | prose | pages [6] -->
EWR = Water Availability −Water Use

<!-- b000085 | prose | pages [6] -->
= MAR −WUi −WUa −WUp Population

<!-- b000086 | prose | pages [6] -->
Population

<!-- b000087 | prose | pages [6] -->
In order for the model to be used for projections into how the water scarcity of a region will change in the future, it is important to break down the variables of the EWR into components that factor into the long term growth rate. By understanding the trends of these components and the relationship between the components and the long term growth rate of water use, rates for future water needs can be extrapolated.

<!-- b000088 | prose | pages [6] -->
Water use from agriculture has several factors that are similar to the factors of water use from industry, such as the level of agricultural production and the water-intensivity of agricultural products. For instance, in low-income coun- tries, irrigation can make up to 90 percent of water withdrawals. The most water-intensive crops include rice and cotton, which require up to 29,000 and 5,000 liters of water per kilogram of crop respectively.[12] Other factors that are important to take into consideration for water use from agriculture are the availability of irrigation technology and the increase in needed water due to climate change. In particular, climate change increases the amount of water needed for agriculture through rising temperatures and requires modiﬁcations in agricultural practices due to shifts in global climate systems. [13]

<!-- b000089 | prose | pages [6] -->
Water use from industry is primarily inﬂuenced by the level of production in a country and the water eﬃciency of the production. [14] The most water- intensive industries include paper, chemicals, and coal products.[15] The water- intensity of the industry is typically determined by a measure called the “water footprint” which indicates the amount of water needed throughout production. We assume that water use from industry within a country is proportional a product of the amount of the economy based in industry and the average water footprint of industry in that country. This would be scaled diﬀerently depending on the total economic output of a country.

<!-- b000090 | prose | pages [6] -->
Water use from personal use is directly related to the population of the region, and we assume that for every given region, an individual’s water use re- mains constant over time. We acknowledge that there may be variations in water use depending on the economic development of a region, but because signiﬁcant changes in economic development are diﬃcult to predict and often occur spo- radically, economic development should only be taken into consideration when there is a large potential for a region to experience signiﬁcant growth.

<!-- b000091 | prose | pages [6] -->
Finally, mean annual runoﬀis most directly related to the climate of the region and the amount of precipitation that it receives. [16] When extrapolating the potential mean annual runoﬀfor a region in the future, the historic MAR of the region should be plotted against factors such as precipitation and average temperature to project the future MAR.

<!-- b000092 | prose | pages [7] -->
Page 6

<!-- b000093 | prose | pages [7] -->
2.4

<!-- b000094 | heading | pages [7] -->
Evaluation of the Model

<!-- b000095 | prose | pages [7] -->
Control # 43443

<!-- b000096 | prose | pages [7] -->
Correlation with Water Stress Indicator (WSI) 2.4.1

<!-- b000097 | prose | pages [7] -->
The scatterplot below compares the WSI (on the x-axis) and the EWR (on the y- axis). We observe that there is a strong relationship between our model and the commonly used model of the WSI. One signiﬁcant strength of our model is that the diﬀerences between the EWR in water-scarce and water-abundant countries is more extreme than the WSI, which allows for a more precise measure of water scarcity. Additionally, the impact of water scarcity on individual citizens is made more clear by factoring in population. For instance, China and the United States have a very similar WSI (0.478 and 0.499, respectively), but the diﬀerence in populations means that this water shortage has a larger impact on a citizen of China than on a citizen of United States, so China’s EWR is over three times smaller.

<!-- b000098 | prose | pages [7] -->
WSI Argentina 0.352 Colombia 0.037 China 0.478 India 0.967 Russia 0.111 Saudi Arabia 0.995 South Africa 0.687 Spain 0.181 Sweden 0.04 USA 0.499

<!-- b000099 | prose | pages [7] -->
·106

<!-- b000100 | prose | pages [7] -->
3

<!-- b000101 | prose | pages [7] -->
EWR (gal / person / year)

<!-- b000102 | prose | pages [7] -->
2

<!-- b000103 | prose | pages [7] -->
1

<!-- b000104 | prose | pages [7] -->
0

<!-- b000105 | prose | pages [7] -->
0 0.2

<!-- b000106 | prose | pages [7] -->
EWR (gal / person / year) 421760 1672841 116302 5481 956034 975 273378 836927 1674537 393186

<!-- b000107 | prose | pages [7] -->
0.4 0.6 0.8 1

<!-- b000108 | prose | pages [7] -->
WSI

<!-- b000109 | prose | pages [8] -->
Page 7 Control # 43443

<!-- b000110 | prose | pages [8] -->
2.4.2

<!-- b000111 | heading | pages [8] -->
Strengths

<!-- b000112 | prose | pages [8] -->
• Impact of population — The most pertinent statistic in water scarcity is how much spare water there is per person, which is taken into account by our model. This accurately reﬂects that countries with large populations face more signiﬁcant challenges in harnessing their water supply.

<!-- b000113 | prose | pages [8] -->
• Lack of an upper limit on available water — Other measures such as the WSI include a lower limit of 0 on water stress, which makes it diﬃcult to determine the extent to which countries have a surplus of water. Because our equation goes in the opposite direction such that a high value corre- lates to little water scarcity, regions can potentially continue to increase their Excess Water Ratio (EWR).

<!-- b000114 | prose | pages [8] -->
• Predictive power — By breaking up the data into the components that impact their long term trajectories, our model has more predictive power than preexisting models. It accounts for the underlying causes of changes in water usage and can take the growth rates of those factors into consid- eration when predicting the growth rate of water usage.

<!-- b000115 | prose | pages [8] -->
2.4.3

<!-- b000116 | heading | pages [8] -->
Weaknesses

<!-- b000117 | prose | pages [8] -->
• Availability of data — Ideally, the model should be applied to a region of any size to determine the overall water scarcity in the area. However, typically information is only available on a national level or on a state level in the United States, which makes it particularly hard to determine levels of water scarcity in small regions within countries.

<!-- b000118 | prose | pages [8] -->
• Broadness of categories — Our model treats agriculture, industry, and personal use as monolithic categories, when in reality each of these factors has various components that can move independently.

<!-- b000119 | prose | pages [8] -->
However, other models such as the WSI have this same drawback, so our model is no weaker than established models in that regard.

<!-- b000120 | prose | pages [8] -->
2.5

<!-- b000121 | heading | pages [8] -->
A More Complex Model for Water Availability

<!-- b000122 | prose | pages [8] -->
More recent formulations of the Water Stress Indicator (WSI) acknowledge the importance of environmental needs in calculations of a region’s water use.[9] Such calculations are an improvement to the previous model because they rec- ognize that the maintenance of the environment of a region requires a constant ﬂow of water for the well-being of nearby plants and animals (WUe). While this water previously was included in the water available to humans for indus- trial, personal, and agricultural use, the previous model ignores the fact that dipping into the supply of water required for the environment harms the overall ecosystem.

<!-- b000123 | prose | pages [8] -->
Additionally, a more complex model recognizes that while a region used to get all of its water primarily from its surroundings, technology now enables regions to import water from areas that naturally have more abundant water

<!-- b000124 | prose | pages [9] -->
Page 8 Control # 43443

<!-- b000125 | prose | pages [9] -->
sources. For instance, Singapore recently has been importing water from the Johore River catchment in Malaysia to make up for its large water needs, and India has established water treaties with Pakistan and China. [16]

<!-- b000126 | prose | pages [9] -->
A more complex model for water is therefore reﬂected below:

<!-- b000127 | prose | pages [9] -->
EWR(Excess Water Ratio) = MAR + Import −WUi −WUa −WUp −WUe

<!-- b000128 | prose | pages [9] -->
Population

<!-- b000129 | prose | pages [9] -->
3 Case Study: India

<!-- b000130 | prose | pages [9] -->
3.1 Rationale

<!-- b000131 | prose | pages [9] -->
We have selected India as the country for our case study. As of January 12th, 2016 there were about 1.3 billion people living in India.

<!-- b000132 | prose | pages [9] -->
[17] This amounts to just over 18% of the total population of Earth. Simply put, this massive country that is home to so much of the world’s population is in a major water crisis. The following excerpt from a paper published by the National Bureau for Asian Research sets the scene: “The World Health Organization estimates that 97 million Indians lack access to safe water today, second only to China. As a result, the World Bank estimates that 21% of communicable diseases in India are related to unsafe water. Without change, the problem may get worse as India is projected to grow signiﬁcantly in the coming decades.” [18]

<!-- b000133 | prose | pages [9] -->
3.2 Main Drivers of Water Scarcity

<!-- b000134 | prose | pages [9] -->
One important cause of the water scarcity in India is “large spatial and temporal variability in the rainfall.” [19] Eﬀectively this means that water is distributed incredibly unevenly throughout the country in both in terms of geography and of time. Each of these conditions produces water scarcity in speciﬁc contexts: the former in relatively dry regions during otherwise wet months, and the latter during relatively dry months in regions both wet and dry.

<!-- b000135 | prose | pages [9] -->
Another factor exacerbating water stress is poor irrigation systems.

<!-- b000136 | prose | pages [9] -->
[19] This unfortunately is a self perpetuating problem, because the rates charged for users of the system are very low. The low rates mean that insuﬃcient revenue is generated to support the operation and maintenance of high quality infras- tructure. This results in low quality infrastructure, which renders stakeholders reticent to pay more for it, which means the quality won’t get better etc.

<!-- b000137 | prose | pages [9] -->
Some farmers have responded to the previous two challenges by drawing water directly from the ground to irrigate their crops. This has led over the years to widespread overuse of the groundwater, far past the point of environmental sustainability. The resulting depletion of naturally occurring groundwater for agricultural/irrigation purposes has become a driver of water scarcity in its own right. [20]

<!-- b000138 | prose | pages [9] -->
Notice that all three leading causes of water stress examined thus far have been agricultural in nature. This is because currently agriculture is responsible for a staggering 92% of water usage in India. However, in the relatively short

<!-- b000139 | prose | pages [10] -->
Page 9 Control # 43443

<!-- b000140 | prose | pages [10] -->
term future, the population is expected to rapidly grow and industrialize. Both of these trends will require more water, both in absolute terms, and as a percent- age of water used. What this means is that over the long term, the country will be required to “produce more [food, to support the expanded population and industrialization] with less water.” [19] Or face massive food shortages and/or be unable to develop more advanced industrial resources.

<!-- b000141 | prose | pages [10] -->
Finally, one additional challenge related to rapid population growth that is very much in evidence in India is contamination. “More than 100 million people in India are living in places where water is severely polluted. Out of the 632 districts examined to determine the quality of groundwater, only 59 districts had water safe enough to drink.” [21] Even assuming that the same amount of water is being collected – which may or not be a valid assumption – keeping all of it clean enough to use will be imperative as the country grows.

<!-- b000142 | prose | pages [10] -->
Prediction of Water in India in 15 Years 4

<!-- b000143 | prose | pages [10] -->
Determining the Current State of Water Scarcity 4.1

<!-- b000144 | prose | pages [10] -->
Applying our model for water needs to India in the present day allows us to calculate an excess water ratio for India that can be compared to that of other countries. A variable in our model that is not readily available for the country as a whole is the MAR, because it varies signiﬁcantly throughout the country. For example, the MAR of the Ganges River at Farakka, India was approxi- mately 415 · 109m3, while the MAR of the Brahmaputra at Pandu, India was approximately 511·109m3 in 1997.[22] However, the calculation of the published WSI statistic requires an estimate of a total MAR for the country, so we can manipulate the formula for WSI to write the EWR in terms of WSI rather than MAR:

<!-- b000145 | prose | pages [10] -->
WSI = withdrawals

<!-- b000146 | prose | pages [10] -->
EWR = MAR −withdrawals

<!-- b000147 | prose | pages [10] -->
population

<!-- b000148 | prose | pages [10] -->
MAR

<!-- b000149 | prose | pages [10] -->
 withdrawals

<!-- b000150 | prose | pages [10] -->
 1 WSI −1

<!-- b000151 | prose | pages [10] -->
=

<!-- b000152 | prose | pages [10] -->
population

<!-- b000153 | prose | pages [10] -->
India has a WSI of 0.967 as of 2009, total water withdrawals of 761 · 109m3, and a population of 1,251,695,584. [14][23] This gives it an EWR of 20.75m3 or 5481.59 gallons. To put this into context, this means that the average individual in India has 15 gallons per day of extra water that could theoretically be used. This number is extremely low relative to the amount of water currently being used. We note that the estimated amount of excess mean annual runoﬀnot being used per person at any given time, but a lack of technology in much of rural India prevents this water from being used in its current state. Thus, there is a large strain on India’s water that require immediate action, especially when compared to the EWR of other countries. For example, China – which has a much lower WSI of 0.478 – has an EWR of 373.9m3, which puts it in a much better position to provide water for the country’s needs.

<!-- b000154 | prose | pages [11] -->
Page 10 Control # 43443

<!-- b000155 | prose | pages [11] -->
4.2 Preliminary Estimation of Growth Rates of Water Use

<!-- b000156 | prose | pages [11] -->
In this stage of the modeling, we assume that in the relatively short time span of 15 years, the mean annual runoﬀfor India will remain relatively constant. We note that this assumption is not fully accurate, as climate change will likely alter India’s climate in a way that decreases water availability. However, the proposed model will still be helpful because it places a lower bound on the state of India’s water scarcity, such that water shortages in the next 15 years will be at least as bad as proposed by the model assuming the calculations for water use.

<!-- b000157 | prose | pages [11] -->
We start by formalizing our assumptions about the factors that impact the water use from each of the following sources: industry, agriculture, and personal. Water use from industry and agriculture are each assumed to be a product of their respective production levels and water footprints. Personal water use is assumed to be dependent on the rural population versus the urban population, and will then take into account the diﬀerent water use rates for each group. We also assume that there are two distinct population groups- urban and rural, and we then assume that all of the people in these populations consumer water at the average rate. These equations are formalized below:

<!-- b000158 | prose | pages [11] -->
Industrial Water Use(I)

<!-- b000159 | prose | pages [11] -->
= Industrial Output(Oi) · Industrial Water Footprint(Fi)

<!-- b000160 | prose | pages [11] -->
Agricultural Water Use(A)

<!-- b000161 | prose | pages [11] -->
= Agricultural Output(Oa) · Agricultural Water Footprint(Fa)

<!-- b000162 | prose | pages [11] -->
Domestic Water Use(I) = Urban Pop.(U) · Avg. Urban Water Use(Wu)

<!-- b000163 | prose | pages [11] -->
+ Rural Pop.(R) · Avg. Rural Water Use(Wr)

<!-- b000164 | prose | pages [11] -->
Total Water Use(W) = I + A + D

<!-- b000165 | prose | pages [11] -->
Growth Rate of Water Use from I(g(I)) = g(Oi) + g(Fi)

<!-- b000166 | prose | pages [11] -->
g(A) = g(Oa) + g(Fa)

<!-- b000167 | prose | pages [11] -->
g(D) = U · Wu

<!-- b000168 | prose | pages [11] -->
g(U) + R · Wr

<!-- b000169 | prose | pages [11] -->
g(R)

<!-- b000170 | prose | pages [11] -->
D

<!-- b000171 | prose | pages [11] -->
D

<!-- b000172 | prose | pages [11] -->
Water Use(target year) = I(1+g(I))target−current +A(1+g(A))target−current

<!-- b000173 | prose | pages [11] -->
+ P(1 + g(D))target−current

<!-- b000174 | prose | pages [11] -->
Note that in the above equations, we utilize the commonly used approxi- mation that the growth rate of a product is approximately equal to the sum of the growth rate of each factor. According to the World Bank, India’s urban population growth is 2.38% and rural population growth is 0.68% with a total

<!-- b000175 | prose | pages [12] -->
Page 11 Control # 43443

<!-- b000176 | prose | pages [12] -->
population growth of 1.2%.[24] Additionally, the average urban citizen of India uses 126 liter of water per day for personal use.[25] Factoring in information on India’s population, total personal water use in India, and the current percent- age of the population that is urban, we calculate the growth rate of water for personal use:

<!-- b000177 | prose | pages [12] -->
g(D) = (0.319)(0.0238) + (0.681)(0.0068) = 0.0122

<!-- b000178 | prose | pages [12] -->
We note as well that because of the large variations in water footprints for diﬀerent industries and crops in India, we assume that g(Fa) = g(Fi) = 0 within the 15 years of our projections.

<!-- b000179 | prose | pages [12] -->
However, we ultimately conclude that this assumption is reasonable, since India’s government has been slow to adopt policies that promote drastic economic change. [26] Therefore, within the relatively short timespan of 15 years it is unlikely that the economy will change in a way that drastically alters the average water footprint of industries. Based on the World Bank, the growth rate of India’s agriculture sector varies signiﬁcantly each year but has centered around 3.8% between 2006 and 2014.[27] Additionally, the growth rate of India’s industrial sector has been about 5.0% during the same timespan. [28] We therefore estimate that the water use in 2031 will be given by:

<!-- b000180 | prose | pages [12] -->
Water Use(2031) = (688 · 109m3)(1.038)15 + (56 · 109m3)(1.012)15

<!-- b000181 | prose | pages [12] -->
+ (17 · 109m3)(1.050)15 = 1306 · 109m3

<!-- b000182 | prose | pages [12] -->
This means that unless water use decreases or water availability increases beyond this projection over the next 15 years, the EWR will become negative as water use will surpass water availability. Eﬀectively, this simplistic ﬁrst model shows that with no change in current behavior India will be out of water before 2031. We note that this model presents a more extreme outcome than other models, such as those of the Indian government.[29] One factor that accounts for this is the fact that each area of water use is assumed to be growing expo- nentially, which represents a worst-case scenario. Additionally, we previously assumed that average water footprints remain constant, while it is entirely pos- sible that the average water footprint decreases with the scale of industry.

<!-- b000183 | prose | pages [12] -->
4.3

<!-- b000184 | heading | pages [12] -->
A More Robust Computer Model

<!-- b000185 | prose | pages [12] -->
Because the Indian government predicts the amount of water available and water used in diﬀerent sectors of the economy, we can estimate the excess water ratio in a given year by matching the amount of water in each category to a polynomial function using MATLAB’s “polyﬁt” function. We use the Indian government’s predictions for our data rather than exclusively data from past years. We reason that an estimation of the excess water ratio for a year between the years predicted by the government will be more accurate than an estimation extrapolated from data from many years before. To ﬁnd the excess water ratio, we compute the excess water ratio with each component’s value corresponding to its output of the polynomial function for that year.

<!-- b000186 | prose | pages [13] -->
Page 12 Control # 43443

<!-- b000187 | prose | pages [13] -->
By incorporating the components provided in the “Water & Water Related Statistics” report, the excess water ratio can be evaluated as follows: [29]

<!-- b000188 | prose | pages [13] -->
Excess Water Ratio

<!-- b000189 | prose | pages [13] -->
= WUa + WUd + WUi + WUp + WUin + WUec + WUev

<!-- b000190 | prose | pages [13] -->
−WAPC population

<!-- b000191 | prose | pages [13] -->
WUa represents water use for agriculture and irrigation, WUd represents domestic water use, WUi represents industrial water use, WUp represents water use for power, WUin represents water use for inland navigation, WUec represents water use for ecology, and WUev represents water lost to evaporation. These are all of the categories detailed in the report as signiﬁcant Indian water uses. WAPC is water available per capita.

<!-- b000192 | prose | pages [13] -->
Furthermore, the model can be used to assess the eﬀects of intervention policies. By adding the increases of water availability of a certain improvement to the total available water after the year of the improvement’s completion, we can graph the excess water ratio without (Figure 1) and with (Figure 2) the estimated eﬀects of interventions. The curve below graphs high projections for increases of water usage while the curve above graphs low projections. Because their predictions assume the development of the nation as a whole, these added components are restricted to intervention policies not already occurring that would be accounted for by the Indian government.

<!-- b000193 | prose | pages [13] -->
Using this model, we construct a graph for India’s excess water ratio be- tween 2000 and 2050 rooted in the Indian government’s predictions of water availability and usages in 1997, 2010, 2025, and 2050. Similarly, we generated a graph that demonstrates the eﬀects of intervention policies on India’s EWR. For the purpose of demonstrating the model, we assume that intervention projects will increase the amount of water by 30 and 50 billion m3 in 2020 and 2030 respectively.

<!-- b000194 | prose | pages [14] -->
Page 13 Control # 43443

<!-- b000195 | prose | pages [14] -->
Estimated Water Ratio Per Year with No Intervention 1400

<!-- b000196 | prose | pages [14] -->
1200

<!-- b000197 | prose | pages [14] -->
1000

<!-- b000198 | prose | pages [14] -->
Excess Water Ratio

<!-- b000199 | prose | pages [14] -->
800

<!-- b000200 | prose | pages [14] -->
600

<!-- b000201 | prose | pages [14] -->
400

<!-- b000202 | prose | pages [14] -->
200

<!-- b000203 | prose | pages [14] -->
0

<!-- b000204 | prose | pages [14] -->
2000 2005 2010 2015 2020

<!-- b000205 | prose | pages [14] -->
Upper Bound Lower Bound

<!-- b000206 | prose | pages [14] -->
2025 2025 2030 2035 2040 2045 2050 Year Year

<!-- b000207 | caption | pages [14] -->
Figure 1: India’s projected excess water ratio without interventions, 2000 to

<!-- b000208 | prose | pages [14] -->
2050

<!-- b000209 | prose | pages [14] -->
Estimated Water Ratio Per Year with Example Interventions 1400

<!-- b000210 | prose | pages [14] -->
1200

<!-- b000211 | prose | pages [14] -->
1000

<!-- b000212 | prose | pages [14] -->
Excess Water Ratio

<!-- b000213 | prose | pages [14] -->
800

<!-- b000214 | prose | pages [14] -->
600

<!-- b000215 | prose | pages [14] -->
400

<!-- b000216 | prose | pages [14] -->
200

<!-- b000217 | prose | pages [14] -->
0

<!-- b000218 | prose | pages [14] -->
2000 2005 2010 2015 2020

<!-- b000219 | prose | pages [14] -->
Upper Bound Lower Bound

<!-- b000220 | prose | pages [14] -->
2025 2025 2030 2035 2040 2045 2050 Year Year

<!-- b000221 | caption | pages [14] -->
Figure 2: India’s projected excess water ratio with interventions, 2000 to 2050

<!-- b000222 | prose | pages [15] -->
Page 14 Control # 43443

<!-- b000223 | prose | pages [15] -->
4.3.1

<!-- b000224 | heading | pages [15] -->
Assumptions for the Computer Model

<!-- b000225 | prose | pages [15] -->
• Changes to population and amounts of water available and used are pre- dictable.

<!-- b000226 | prose | pages [15] -->
A variety of political, economic, and social factors inﬂuence how much water India consumes and has available, some of which are not quantiﬁable. To avoid arbitrarily quantifying possible events, our model assumes that the Indian government’s predictions in their “Water & Water Related Statistics” will be accurate. [29]

<!-- b000227 | prose | pages [15] -->
• Changes to quantities over our time interval can be approximated using polynomial functions. Due to the relatively few number of data points over our time interval, polynomial functions are a way to approximate a curve that contains those points. While imperfect in accuracy, it provides a solid estimation for excess water ratio between the established points.

<!-- b000228 | prose | pages [15] -->
4.4

<!-- b000229 | heading | pages [15] -->
Conclusions for Impacts on Citizens

<!-- b000230 | prose | pages [15] -->
From the ﬁrst model, we note that a demographic shift impacting water scarcity in India is the increasing proportion of the population living in urban areas. Because urban populations typically use more water than rural populations, this puts a larger strain on India’s water supply, and is one of the largest sources of predicted water increases in the next 15 years. Therefore, an impact of water scarcity will be a decrease in standard of living for cities, as resources strain.

<!-- b000231 | prose | pages [15] -->
The ﬁrst model also assumes that water use will increase along with the current growth rates of industry and agriculture. However, one of our assump- tions in constructing our initial model for water use was that society cannot use water beyond the water physically available. Thus, the prediction of water use from the ﬁrst model should be interpreted as the ideal amount of water availability given current growth rates. Realistically, a water shortage will limit India’s economic growth potential, as agriculture and industry will have to slow down their current rate of expansion with water as a limiting resource. However, the most powerful impacts are the impacts of water shortages on the lives of ordinary citizens in India. With its current water shortages, over 21% of India’s diseases are water-related and only 33% of the country has access to traditional sanitation.[31] Unless the pace of technology improvement is somehow able to keep up with the pace of water needs, these issues will only be worsened.

<!-- b000232 | prose | pages [15] -->
5 Intervention Plans for India

<!-- b000233 | prose | pages [15] -->
5.1 Intervention Plans for India’s Water Scarcity

<!-- b000234 | prose | pages [15] -->
In its water report “Coping with water scarcity,” the FAO notes that the most comprehensive water scarcity interventions address both the demand and supply sides of water scarcity to help align the goals of parties on each side.[32] This report deals with interventions that can be taken for agricultural water use in India, which is particularly relevant since this category makes up the largest

<!-- b000235 | prose | pages [16] -->
Page 15 Control # 43443

<!-- b000236 | prose | pages [16] -->
share of India’s water use. We will discuss intervention strategies that focus on increasing India’s water supply: watershed development and water recycling from waste. We will also discuss intervention strategies that focus on decreasing the demand for water such as societal changes in food consumption and changes in agricultural production. We note that this is by no means an exhaustive list of possible changes to alleviate water scarcity in India. Some additional projects that may be helpful are limited. For instance, dams have historically been used in attempts to increase water supplies for irrigation. Many scientists believe that dams would be helpful in improving India’s water supply, but they also have many adverse side eﬀects, as illustrated by the Narmada Dam project in India.[30] The construction of the dam displaced 200,000 people and had disastrous environmental consequences such as the ﬂooding and salination of land near the dam that ruined crops.

<!-- b000237 | prose | pages [16] -->
5.1.1 Watershed Development

<!-- b000238 | prose | pages [16] -->
Water supply can ﬁrst be improved by constructing watersheds throughout In- dia. A report from the World Resources Institute describes a 2005 study that performed a meta-analysis of 311 watershed development case studies, and de- termined that the construction of watersheds increases water storage capacity, increases cropping intensity, reduces water lost to runoﬀ, and reduces soil loss. [33] The same report concludes that approximately 380 watershed projects have been constructed in India, which have allowed for an increase of 260,000 hectares of agricultural production. On average then, each project has provided irrigation needed for 684 hectares. We acknowledge that diﬀerent crops require diﬀerent amounts of water, so the water requirement is not uniform among each hectare of land. However, due to the absence of more speciﬁc data, we make the sim- plifying assumption that water consumption per hectare is constant throughout India’s farmland. Based on Aquastat data, India current cultivates 170,000,000 hectares and uses 688·109m3 of water for irrigation, which averages out to 404.7 m3 per hectare. We conclude that each completed watershed allows for an in- crease of 276,800 m3 of water to be used for agriculture. Of course, watersheds cannot be constructed inﬁnitely because there is a limit on how much water can be recovered, but so far no limiting capacity of watershed development has been seen in India. We therefore recommend that the Indian government selects 50 areas that could potentially beneﬁt from a watershed and begin construction immediately, which would give a yearly increase of 1.38 · 107m3 of water for agriculture. When determining where these structures should be located, stud- ies suggest that the areas that would beneﬁt most are semi-arid regions with erratic monsoons that prevent water from quickly recharging. [34] We assume in our model that these watersheds will begin construction in the next year, and will follow the timeline of the Neeranchal National Watershed, which was built over six years. The changes will then go into eﬀect in 2022. [35]

<!-- b000239 | prose | pages [17] -->
Page 16 Control # 43443

<!-- b000240 | prose | pages [17] -->
5.1.2 Water Recycling and Waste Treatment

<!-- b000241 | prose | pages [17] -->
With the second largest population of any country in the world, India’s popula- tion produces a large amount of waste that can be treated to be used for agricul- tural purposes. There is precedent for treating waste that can be expanded over the next several years to provide a consistent source of water. Water from waste can only be used in agricultural purposes, because it does not meet the quality standards for personal or industrial use.[30] Currently, this water is being used to irrigate trees in public parks in Hyderabad, to cultivate wheat paddies over 2100ha along the Musi River, and to support ﬁsheries in East Calcutta. Based on public data from Aquastat, as of 2011 India had 270 municipal wastewater treatment facilities, which have the total capacity of treating 4.573 · 109m3 per year. They treat 4.416 · 109m3 per year, but 11.03 · 109m3 per year is left un- treated. Based on the current capacity of the treatment facilities, each facility can treat 1.69·107m3 per year, so constructing new facilities for the treatment of wastewater would require the construction of 651 new treatment plants. While pricing information for waste treatment plants is not readily available, the con- struction would be very expensive. However, we believe that the plants would be worth the cost in the long run because they would provide a future sustainable source of water for agriculture. When we account for this intervention policy in our model, we assume that all untreated wastewater will eventually be treated and used for agriculture, adding 11.03·109m3 per year. Based on building times for large-scale waste treatment facilities in the United States, we estimate that these could be built in three years and begin working by 2019.

<!-- b000242 | prose | pages [17] -->
5.1.3 Societal Changes in Food Consumption

<!-- b000243 | prose | pages [17] -->
One of the largest impacts on demand for water is currently due to food con- sumption, as “90% of personal water footprints are devoted to food in the form of crop and animal production.” [36] For the purposes of constructing our model to predict future water availability, we do not assume that this change will be enacted or successful. However, to approach the supply and demand sides of the water consumption issue, governments will soon need to address the un- sustainable eating habits of populations. Meat and dairy products are much more water intensive than crops, and the consumption of these foods increases as populations move to urban areas. A cultural shift in eating habits, while requiring a change in attitudes toward foods that would take several years, may eventually become necessary as lower water levels decrease the potential for water-intensive farming.

<!-- b000244 | prose | pages [17] -->
5.1.4 Changes in Food Production

<!-- b000245 | prose | pages [17] -->
One of the most signiﬁcant intervention techniques that India can undertake is to decrease the demand for water from agriculture by subsidizing the production of more water-eﬃcient crops. For example, millet is a much more water-eﬃcient crop than rice or wheat, which currently make up the largest shares of India’s agriculture based on data from AQUASTAT. Speciﬁcally, the growth of rice

<!-- b000246 | prose | pages [18] -->
Page 17 Control # 43443

<!-- b000247 | prose | pages [18] -->
requires 1250 mm on average of rain or irrigated water, wheat requires 550 mm, and millet requires just 350 mm.[40] [41]Millet can also be grown in soil that is far poorer quality than traditional crops. Critically, millet is nutritionally equiv- alent to rice or wheat, containing comparable levels of protein, ﬁber, minerals, iron, and calcium.

<!-- b000248 | prose | pages [18] -->
In our model, we have considered the water impact of switching all of India’s wheat and rice production to millet over the course of 30 years. For each land unit of water converted from rice to millet we save 900 mm of water annually, with 200 mm more in savings added for each land unit converted from wheat to millet. Over the timespan modeled, we expect this intervention to produce considerable water savings.

<!-- b000249 | prose | pages [18] -->
5.2 Impact of Water Available of Surrounding Area

<!-- b000250 | prose | pages [18] -->
One of the most signiﬁcant strengths of watershed development is that there is no evidence of negative impacts on the surrounding areas. Typically, watershed development serves the purpose of making degraded lands suitable for agricul- ture, which is independent of the agricultural output of surrounding regions. While the treatment of wastewater has the potential to provide large amounts of additional water for agriculture, studies suggest that the use of treated wa- ter may alter soil quality over time. [30] According to the International Water Management Institute: “Ample evidences are available which show that the groundwater in all wastewater irrigated areas has high salt levels and is unﬁt for drinking. Further, high groundwater tables and water-logging are also com- mon features of these areas.” This poses a health risk to communities that are located downstream of the area, since it may be diﬃcult to separate this agricul- tural water from personal use in communities that do not have the technology for advanced water puriﬁcation.

<!-- b000251 | prose | pages [18] -->
5.3

<!-- b000252 | heading | pages [18] -->
Evaluation of Strengths and Weaknesses

<!-- b000253 | prose | pages [18] -->
The World Resource Institute report identiﬁes many social and economic ben- eﬁts of watershed development, and concludes that there is a net present value between $5.08 million and $7.43 million. It also points out other beneﬁts that could not be included in the cost-beneﬁt analysis, such as “improvements in nu- trition, dietary diversity, and human health” as well as “improved resilience to drought and temperature ﬂuctuations.” A weakness of this proposal is that the development of watersheds can be expensive, and modiﬁcations of the natural environment can have unpredictable consequences on the ecosystems. Addition- ally, a social problem brought up by watershed construction is that historically the construction of watersheds has negatively impacted women in India. [37] The development of watersheds required the closing of common areas where poorer women grazed goats, which deprived them of a large source of income. However, in carrying out future projects, Kerr notes that “Some of the negative eﬀects on women could be overcome if a great eﬀort was made to include them in decision making.” Finally, watersheds require a signiﬁcant upkeep cost, and

<!-- b000254 | prose | pages [19] -->
Page 18 Control # 43443

<!-- b000255 | prose | pages [19] -->
historically a lack of attention to constructed watersheds has caused them to be leaky or damaged. [38]

<!-- b000256 | prose | pages [19] -->
One strength of waste treatment is that it creates a reliable source of wa- ter supply for agriculture, removing much of the uncertainty that characterizes water scarcity in developing countries. The Weighted Anomaly Standardized Precipitation (WASP) index computes deviations in monthly precipitation, and shows that parts of Central India frequently are drier than their average precip- itation, making it diﬃcult to group crops given uncertain weather conditions. [39] By diverting treated wastewater to these areas, water can be more eﬃciently used. Additionally, the treatment of wastewater has a positive externality of long term economic growth for workers in the region. The construction of the facilities requires the hiring of several construction workers, and the constant treatment of waste requires a large permanent staﬀ. As noted above, however, wastewater has the potential to make water less usable downstream, and the construction of the facilities will require a large initial cost from the government. Thus it is unlikely that the government would be able to fund the construction of all of the plants at one time.

<!-- b000257 | prose | pages [19] -->
The main beneﬁt of shifting crop production away from rice/wheat and to- wards millet (and more generally away from water eﬃcient crops towards more water eﬃcient varieties) is of course massive water savings. Other strengths of this approach include consumers taking advantage of the enhanced nutritional value of millets vs. wheat and rice, and the existence in the status quo of pro- totype models of eﬀective programs that already provide “training via internet and mobile phone, adapted to smallholder farmers and practitioners, on the best farming practices for drought and heat tolerant crops such as millet and sorghum.” [42] There are at least two key challenges standing in the way of adopting this approach. First, local tastes have to be taken into account. If no one wants to eat millet, and thus there was no demand for it, no sensible farmer would grow it. Accordingly, gathering and heeding input from the local population of both farmers and consumers to create demand for millet as a food crop would be critical to the success of this intervention. Second, even assum- ing that it were possible to convince everyone to love millet overnight, far more investment would be needed to ensure that suﬃcient training in proper millet growing techniques, and ﬁnancial support to purchase millet seed was available to every small farmer that could and would use it to convert their wheat or rice farm into a millet farm. [42]

<!-- b000258 | prose | pages [19] -->
6 Projection of Future Water Availability for India

<!-- b000259 | prose | pages [19] -->
With interventions in infrastructure (Figure 3), the improvements are almost insigniﬁcant in the India’s future water scarcity.

<!-- b000260 | prose | pages [19] -->
With these investments in infrastructure, India will run out of water between 2084 and 2094, rather than 2083 and 2093 without improvements.

<!-- b000261 | prose | pages [20] -->
Page 19 Control # 43443

<!-- b000262 | prose | pages [20] -->
Estimated Water Ratio Per Year 1400

<!-- b000263 | prose | pages [20] -->
1200

<!-- b000264 | prose | pages [20] -->
1000

<!-- b000265 | prose | pages [20] -->
Excess Water Ratio

<!-- b000266 | prose | pages [20] -->
800

<!-- b000267 | prose | pages [20] -->
600

<!-- b000268 | prose | pages [20] -->
400

<!-- b000269 | prose | pages [20] -->
200

<!-- b000270 | prose | pages [20] -->
0

<!-- b000271 | prose | pages [20] -->
2000 2005 2010 2015 2020

<!-- b000272 | prose | pages [20] -->
Upper Bound without Intervention Lower Bound without Intervention Upper Bound with Intervention Lower Bound with Intervention

<!-- b000273 | prose | pages [20] -->
2025 2025 2030 2035 2040 2045 2050 Year Year

<!-- b000274 | caption | pages [20] -->
Figure 3: India’s projected excess water ratio with and without infrastructure

<!-- b000275 | prose | pages [20] -->
interventions, 2000 to 2050

<!-- b000276 | prose | pages [20] -->
Estimated Water Ratio Per Year 1400

<!-- b000277 | prose | pages [20] -->
1200

<!-- b000278 | prose | pages [20] -->
1000

<!-- b000279 | prose | pages [20] -->
Excess Water Ratio

<!-- b000280 | prose | pages [20] -->
800

<!-- b000281 | prose | pages [20] -->
600

<!-- b000282 | prose | pages [20] -->
400

<!-- b000283 | prose | pages [20] -->
200

<!-- b000284 | prose | pages [20] -->
0

<!-- b000285 | prose | pages [20] -->
2000 2005 2010 2015 2020

<!-- b000286 | prose | pages [20] -->
Upper Bound without Intervention Lower Bound without Intervention Upper Bound with Intervention Lower Bound with Intervention

<!-- b000287 | prose | pages [20] -->
2025 2025 2030 2035 2040 2045 2050 Year Year

<!-- b000288 | caption | pages [20] -->
Figure 4: India’s projected excess water ratio with and without millet interven-

<!-- b000289 | prose | pages [20] -->
tions, 2000 to 2050

<!-- b000290 | prose | pages [21] -->
Page 20 Control # 43443

<!-- b000291 | prose | pages [21] -->
By replacing wheat and rice crops with millet (Figure 4), the water used signiﬁcantly decreases, leading to a much higher EWR. Instead, India will run out of water between 2097 and 2107

<!-- b000292 | prose | pages [21] -->
7

<!-- b000293 | heading | pages [21] -->
Conclusion

<!-- b000294 | prose | pages [21] -->
We began by creating the new metric of “excess water ratio” that improves upon currently used measures by illustrating the extent to which water shortages im- pact an average individual in the region. Turning to the case study of India, we then identiﬁed the components that make up each of the contributions to the excess water ratio and predicted their growth rates in order to extrapolate the growth rate of water needs in India over the next 15 years. Our results illustrated that at current growth rates, the average excess water per capita will be half of the current value by 2031. We concluded by exploring inter- vention possibilities to develop long-term solutions for India’s water issues. We ﬁrst looked at strategies that increase the supply of water, but found that these techniques were expensive and did very little to oﬀset the rapidly increasing wa- ter demands. When we turned to attempts to decrease the demand for water, such as switching some crop production to the water-eﬃcient grain millet, we concluded that these could be much more eﬀective in the long term assuming that they are properly implemented by governments. This result makes sense, since the global supply of water is currently limited to what is already physically available, while demand for water can potentially always be lowered. Funda- mentally though, we conclude that more drastic societal changes will need to be adopted to decrease India’s water demand enough to matter.

<!-- b000295 | heading | pages [21] -->
References

<!-- b000296 | references | pages [21] -->
[1] “How much water does a Person Need?” Every Little Drop, 2010.

<!-- b000297 | references | pages [21] -->
[2] Steven Solomon. Water: The Epic Struggle for Wealth, Power, and Civi-

<!-- b000298 | references | pages [21] -->
lization. HarperCollins, 2009.

<!-- b000299 | references | pages [21] -->
[3] “Vital Water Graphics: An Overview of the State of the World’s Fresh and

<!-- b000300 | references | pages [21] -->
Marine Waters.” United Nations Environment Programme, 2008.

<!-- b000301 | references | pages [21] -->
[4] “How much water is there on, in, and above the Earth?” U.S. Geological

<!-- b000302 | references | pages [21] -->
Survey, 2015.

<!-- b000303 | references | pages [21] -->
[5] “World Population: Historical Estimates of World Population.” United

<!-- b000304 | references | pages [21] -->
States Census Bureau, 2015.

<!-- b000305 | references | pages [21] -->
[6] “U.S. World and Population Clock.” United States Census Bureau, 2016.

<!-- b000306 | references | pages [21] -->
[7] “UN projects world population to reach 8.5 billion by 2030, driven by

<!-- b000307 | references | pages [21] -->
growth in developing countries.” UN News Centre, 2015.

<!-- b000308 | references | pages [22] -->
Page 21

<!-- b000309 | references | pages [22] -->
Control # 43443

<!-- b000310 | references | pages [22] -->
[8] “Threats: Water Scarcity.” World Wildlife Fund, 2016.

<!-- b000311 | references | pages [22] -->
[9] Amber Brown, Marty D. Matlock, “A Review of Water Scarcity Indices

<!-- b000312 | references | pages [22] -->
and Methodologies.” Sustainability Consortium, 2011.

<!-- b000313 | references | pages [22] -->
[10] Water Stress Indicator in Major Basin [map]. 2004. Scale not given. “Vital

<!-- b000314 | references | pages [22] -->
Water Graphics.”

<!-- b000315 | references | pages [22] -->
[11] “Mean annual runoﬀ, precipitation, and evapotranspiration in the glaciated

<!-- b000316 | references | pages [22] -->
northeastern United States, 1951-80.” U.S. Geological Survey, Department

<!-- b000317 | references | pages [22] -->
of the Interior, 2014.

<!-- b000318 | references | pages [22] -->
[12] “Thirsty Crops.” Living Waters, World Wildlife Fund, 1996.

<!-- b000319 | references | pages [22] -->
[13] Hugh Turral, “Climate change, water and food security.” FAO Water Re-

<!-- b000320 | references | pages [22] -->
ports, Food and Agriculture Organization of the United Nations, 2011.

<!-- b000321 | references | pages [22] -->
[14] “The Growing Blue Tool.” Growing Blue, 2016.

<!-- b000322 | references | pages [22] -->
[15] Adrienne Harling, “Memorandum: What industries/products are the most

<!-- b000323 | references | pages [22] -->
water-intensive within the United States?”

<!-- b000324 | references | pages [22] -->
Humboldt State University,

<!-- b000325 | references | pages [22] -->
Oﬃce for Economic & Community Development, 2009.

<!-- b000326 | references | pages [22] -->
[16] David G Tarboton, “Chapter 3:

<!-- b000327 | references | pages [22] -->
Physical Factors Aﬀecting Runoﬀ.”

<!-- b000328 | references | pages [22] -->
Rainfall-RunoﬀProcesses, Utah State University, 2003.

<!-- b000329 | references | pages [22] -->
[17] “Population, total.” The World Bank, 2016.

<!-- b000330 | references | pages [22] -->
[18] Sonia Luthra, Amrita Kundu, “India’s Water Crisis: Causes and Cures.”

<!-- b000331 | references | pages [22] -->
The National Bureau of Asian Reference, 2013.

<!-- b000332 | references | pages [22] -->
[19] “India.” Irrigation in Southern and Eastern Asia in ﬁgures - AQUASTAT

<!-- b000333 | references | pages [22] -->
Survey - 2011. AQUASTAT, 2011.

<!-- b000334 | references | pages [22] -->
[20] Kapil Narula, Ram Fishman, Vijay Modi, Lakis Polycarpou. “Addressing

<!-- b000335 | references | pages [22] -->
the Water Crisis in Gujarat, India.” Columbia Water Center, 2011.

<!-- b000336 | references | pages [22] -->
[21] Saptarishi Dutta. “India is already facing a water crisis - and it is only

<!-- b000337 | references | pages [22] -->
going to get worse.” Quartz India, 2015.

<!-- b000338 | references | pages [22] -->
[22] M.M.Q. Mirza et al. “Are Floods Getting Worse?” Climate Change and

<!-- b000339 | references | pages [22] -->
Water Resources in South Asia. CRC Press, 2005.

<!-- b000340 | references | pages [22] -->
[23] [21] “India,” The World Factbook 2013-14. Washington, DC: Central Intel-

<!-- b000341 | references | pages [22] -->
ligence Agency, 2013.

<!-- b000342 | references | pages [22] -->
[24] “Urban population (% of total).” The World Bank, 2016.

<!-- b000343 | references | pages [22] -->
[25] “The Karnataka Urban Water Sector Improvement Project.” Water and

<!-- b000344 | references | pages [22] -->
Sanitation Project, The World Bank, 2010.

<!-- b000345 | references | pages [23] -->
Page 22

<!-- b000346 | references | pages [23] -->
Control # 43443

<!-- b000347 | references | pages [23] -->
[26] Neha Thirani Bagri. “India Continues Slow Pace of Economic Growth.”

<!-- b000348 | references | pages [23] -->
The New York Times, 2014.

<!-- b000349 | references | pages [23] -->
[27] “Agriculture, value added (annual % growth).” The World Bank, 2016.

<!-- b000350 | references | pages [23] -->
[28] “Industry, value added (annual % growth).” The World Bank, 2016.

<!-- b000351 | references | pages [23] -->
[29] “Water and Related Statistics.” Water Resources Information System Di-

<!-- b000352 | references | pages [23] -->
rectorate, 2015.

<!-- b000353 | references | pages [23] -->
[30] “Narmada: A history of controversy.” BBC News, 2000.

<!-- b000354 | references | pages [23] -->
[31] Shannyn Snyder. “Water in Crisis - India.” The Water Project, 2015.

<!-- b000355 | references | pages [23] -->
[32] “Coping with water scarcity: an action framework for agriculture and food

<!-- b000356 | references | pages [23] -->
security.” FAO Water Reports, Food and Agriculture Organization of the

<!-- b000357 | references | pages [23] -->
United Nations, 2012.

<!-- b000358 | references | pages [23] -->
[33] Erin Gray, Arjuna Srinidhi. “Watershed Development in India: Economic

<!-- b000359 | references | pages [23] -->
Valuation and Adaptation Considerations.” World Resources Institute,

<!-- b000360 | references | pages [23] -->
2013.

<!-- b000361 | references | pages [23] -->
[34] Kaushal K. Garg, Suhas P. Wani. “Opportunities to Build Groundwater

<!-- b000362 | references | pages [23] -->
Resilience in the Semi-Arid Tropics.” Groundwater 51, No. 5 (2013): 679-

<!-- b000363 | references | pages [23] -->
691.

<!-- b000364 | references | pages [23] -->
[35] “World Bank Approves Neeranchal National Watershed Project, India.”

<!-- b000365 | references | pages [23] -->
The World Bank, 2014.

<!-- b000366 | references | pages [23] -->
[36] D.L. Marrin. “Reducing water and energy footprints via dietary changes

<!-- b000367 | references | pages [23] -->
among consumers.” International Journal of Nutrition and Food Sciences

<!-- b000368 | references | pages [23] -->
3, No. 5 (2014): 361-369.

<!-- b000369 | references | pages [23] -->
[37] J.M. Kerr, Ganesh Pangare, Vasudha Pangare. “Natural Resource Manage-

<!-- b000370 | references | pages [23] -->
ment and Productivity on Uncultivated Lands,” Watershed Development

<!-- b000371 | references | pages [23] -->
Projects in India: An Evaluation, 2002.

<!-- b000372 | references | pages [23] -->
[38] Prem Singh, H.C. Behera, Aradhana Singh. “Impact and Eﬀectiveness of

<!-- b000373 | references | pages [23] -->
Watershed Development Programmes in India.” Lal Bahadur Shastri Na-

<!-- b000374 | references | pages [23] -->
tional Academy of Administration, 2010.

<!-- b000375 | references | pages [23] -->
[39] “Global WASP Analyses.” US National Centers for Environmental Predic-

<!-- b000376 | references | pages [23] -->
tion, 2015.

<!-- b000377 | references | pages [23] -->
[40] “Millets: Future of Food and Farming.” Millet Network of India, Deccan

<!-- b000378 | references | pages [23] -->
Development Society, 2009.

<!-- b000379 | references | pages [23] -->
[41] “Crop Water Information: Wheat.” FAO Water, FAO Water Development

<!-- b000380 | references | pages [23] -->
and Management Unit, 2015.

<!-- b000381 | references | pages [23] -->
[42] Jerome Bossuet. “Millet for our bread in 2050?” Thomson Reuters Foun-

<!-- b000382 | references | pages [23] -->
dation News, 2012.
