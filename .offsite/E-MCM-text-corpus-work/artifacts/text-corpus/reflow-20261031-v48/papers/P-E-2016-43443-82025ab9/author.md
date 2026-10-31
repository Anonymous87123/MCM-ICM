For ofﬁce use only

For ofﬁce use only

T1 ________________ F1 ________________ T2 ________________ Problem Chosen F2 ________________

T3 ________________ F3 ________________ T4 ________________ F4 ________________

MCM/ICM

Summary Sheet

(Your team's summary should be included as the first page of your electronic submission.)

Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

In this paper, we formulate an “excess water ratio” (EWR) metric for water scarcity that improves upon currently used metrics such as the Water Stress Index (WSI) by computing the per capita excess water available in a region. This provides a more illuminating description of the impact of water shortages on individuals. To determine the amount of excess water in a region, we start with  the amount of naturally available water, then subtract out water usage from each primary category: personal use, industrial use, and agricultural use. Dividing this by the total population of a region allows us to determine the annual amount of water that is available but unused for every individual, a goal which is unique to our model.  We note as well that depriving an ecosystem of all available water carries serious environmental consequences. In our case study, we apply our model to India, which in addition to having the second largest population in the world, also suffers from a large scale lack of safe drinking water and a high rate of waterborne diseases. In applying our model to predictions of India's water scarcity in 2031, we ﬁrst model growth rates for the environmental and social factors that inﬂuence water use to determine the growth of water needs over the next ﬁfteen years. We develop a secondary model on MATLAB that utilizes local predictions of water use and population growth from the Indian government to extrapolate our EWR measure. Taking these two models together, we conclude that the excess water per capita in India will be around half of its current level by 2031. We proceed to explore several intervention measures for India's water crisis that emphasize the need to address the supply and demand sides of the water equation, including watershed development, waste treatment, and broader cultural changes in food production. We ﬁnd the cumulative impact of the proposed infrastructure improvements to be minimal. Implementing both these changes would delay the point at which India's EWR diminishes to zero by just one year (from 2083 to 2084). When we assume changes in agriculture we begin to see more impact. Speciﬁcally, switching all rice and wheat production in the country to millet over a thirty year period pushes the year India hits zero EWR back to 2097. All of this means that large cultural shifts in demand for water will ultimately be necessary for India to achieve long-term water sustainability.

1 Introduction

Water has been absolutely critical for all humans, everywhere, since the be- ginning of time. Every human needs at a bare minimum 20 liters of water to survive. [1] The need for that water is rooted deeply in our biology: at 1% water deﬁciency humans get thirsty, a 5% shortfall causes fever, at 10% short we are rendered immobile, and death strikes after just a week of 12-15% water loss. [2] Given these biological realities, it is not a surprise that the ﬁrst and most basic category of water use in human society is personal consumption.

However, it is not enough to simply have suﬃcient water to drink. In terms of total water consumption, personal use is actually a fairly small – if absolutely essential – piece of the pie, just 5% on average of a given country’s consumption. [3] By far the majority of water that all societies consume, 75% on average, is used not to keep from dying of thirst but rather to keep from dying of hunger; on agriculture. And in the middle, at 20% of water consumption, is industry.

On the face of it, it is hard to imagine why water scarcity could ever be an issue on a planet that is 70% covered with water [4]. The problem arises when we consider the conditions that make water usable: it must be fresh (not too salty), liquid, and physically accessible. The ﬁrst condition eliminates all but 2.5% of all water from consideration, the second eliminates two thirds of that which remains, and the ﬁnal condition brings the total fresh, liquid water near or at the surface (ie usable water) down to just 0.003% of earth’s fresh water. [3] All that said, due to natural replenishment through the water cycle, even that tiny fraction of available water has managed to sustain all human life that has existed since antiquity. The main reason to expect that condition to be dif- ferent going forward is that the exponential nature of human population growth that has been occurring since roughly the Industrial Revolution is completely unprecedented historically. To contextualize the current situation, realize that it took almost 12,000 years for the human population to go from zero (circa 10,000 BCE) to one billion (circa 1800 CE). It took 125 years to go from one billion to two circa 1930, 30 years to get from two to three billion in 1959, and 15 years or less to acquire each remaining billion, all the way up to today’s current global population: about 7.3 billion people. [5] [6] And globally we are continuing to grow; the UN projects that there will be over 11 billion people by the year 2100. [7] This ongoing massive increase in the number of people around the world drives up water usage in all three categories. More people means more direct individual consumers of their 20 daily liters, it means that more societies will develop water intensive industry, and most importantly it means that everyone must grow more crops. Incidentally the latter two have also historically and currently contributed to increasing pollution, thereby even further decreasing the total amount of usable water available. [8] In short, humanity currently faces conditions of water scarcity that are com- pletely unprecedented in human history. As a global community accurately modeling future water needs and developing strategies we are all able and will- Page 3 Control # 43443

ing to implement to bring necessary water consumption down to (or preferably somewhere far below) the upper limit of physical water availability will be one of the deﬁning challenges of our time. But we must ﬁnd a way; the survival of the human race hangs precariously in the balance.

2 Model for Water Needs

2.1 Outline of Our Approach

In formulating a quantitative measure of water scarcity, we start with a reﬂection of the Water Stress Indicator (WSI) which was created in 2005 by Smakhthin, et al. [9] This model has credibility due to its precedent of use in informing international policy making, as the UN Environmental Programme uses the WSI as its measure of water scarcity on public maps.[10] The WSI is calculated using the following formula:

Water Withdrawals Water Stress Indicator(WSI) = Mean Annual Runoﬀ(MAR)

Water withdrawals are thus interpreted as a reﬂection of water use and the MAR is interpreted as a reﬂection of water availability. According to the U.S. Geological Survey, mean annual runoﬀis equivalent to the diﬀerence between water available from precipitation and water lost due to evaporation.[11] Water withdrawals are taken as a sum of water withdrawals for the primary uses of water within a region: industrial, agricultural, and personal. Beyond its use in the WSI, this summation has precedent in Vorosmarty’s index of local relative water use and reuse (2005) and Shiklomanov and Markova’s water resources vulnerability index (1993). [10] A signiﬁcant weakness with the use of the WSI is that it does not allow for any conclusions to be drawn about the average impact of water scarcity on an individual level. Two regions with the same levels of water availability and water use will have diﬀerent strains on the daily living of individuals within the regions depending on their populations. Thus a more thorough reﬂection of a region’s water scarcity should be dependent on the population of the region. Our approach in developing our model is thus to use data that is representative of water use and availability and formulating a ratio that determines how much water this leaves per capita for recreational, commercial, or hygienic uses.

2.2 Assumptions

There are a myriad of cultural and environmental factors that impact the avail- ability of water and how much water is needed to sustain the standards of living of the region. Because it is impossible to account for the impact of each of these factors on the overall water demands and availability, we adopt a number of simplifying assumptions for our model:

Page 4 Control # 43443

• The only source of water for a region is its MAR. There is precedent for this assumption in the prevailing models of the Water Stress Indicator (WSI) and the USGS. The assumption is reasonable because while other technologies exist to acquire water, these are not yet widespread enough to present long term solutions to water shortages.

• Utility from water use for individuals is a strictly increasing monotonic function. This assumption allows us to conclude that individuals, regard- less of current water levels, would enjoy having more water available to them. Therefore, although cultural practices in various regions create a perceived need of diﬀerent water levels, we assume that an increase in water availability would be appreciated by any individual.

• The current aggregate level of water use is in a temporary equilibrium, as the region seeks to eﬃciently use all of the water that it has available based on existing demands and technologies. This assumption is reasonable be- cause to assume the opposite would imply that the region is currently using more water than is physically present.

• Government policy and individuals are informed about the safety of the water available to them and accordingly use the available water for appro- priate purposes. Historically, this assumption has not always held because the assumption of unclean water has led to diseases. A more complex model would take into account the ubiquity of this knowledge throughout the population.

• Geographic distribution of water sources and consumption is not a factor in a country’s water scarcity. In reality, available water in one region does not necessarily provide adequate water to another region due to the economic and logistical challenges of transporting large quantities of water.

However, because people commonly settle and farm in land with abundant water, we do not consider the eﬀects of transportation of water in our model.

2.3 An Approach to Projecting Water Availability

In the ﬁrst formulation of the model, we use the process outlined above to come up with a general formula for water use and water availability, and then create an Excess Water Ratio (EWR). The excess water ratio represents the amount of unused water in a region that is available per person. A higher ratio implies that more water is available per person, and thus a higher EWR for a region suggests that water scarcity is less of a concern for the region:

Water Use = Water Use from Industry + Water Use for Agriculture + Water Use for Personal Use

Water Availability = Mean Annual Runoﬀ Page 5 Control # 43443

EWR = Water Availability −Water Use = MAR −WUi −WUa −WUp Population Population In order for the model to be used for projections into how the water scarcity of a region will change in the future, it is important to break down the variables of the EWR into components that factor into the long term growth rate. By understanding the trends of these components and the relationship between the components and the long term growth rate of water use, rates for future water needs can be extrapolated.

Water use from agriculture has several factors that are similar to the factors of water use from industry, such as the level of agricultural production and the water-intensivity of agricultural products. For instance, in low-income coun- tries, irrigation can make up to 90 percent of water withdrawals. The most water-intensive crops include rice and cotton, which require up to 29,000 and 5,000 liters of water per kilogram of crop respectively.[12] Other factors that are important to take into consideration for water use from agriculture are the availability of irrigation technology and the increase in needed water due to climate change. In particular, climate change increases the amount of water needed for agriculture through rising temperatures and requires modiﬁcations in agricultural practices due to shifts in global climate systems. [13] Water use from industry is primarily inﬂuenced by the level of production in a country and the water eﬃciency of the production. [14] The most water- intensive industries include paper, chemicals, and coal products.[15] The water- intensity of the industry is typically determined by a measure called the “water footprint” which indicates the amount of water needed throughout production. We assume that water use from industry within a country is proportional a product of the amount of the economy based in industry and the average water footprint of industry in that country. This would be scaled diﬀerently depending on the total economic output of a country.

Water use from personal use is directly related to the population of the region, and we assume that for every given region, an individual’s water use re- mains constant over time. We acknowledge that there may be variations in water use depending on the economic development of a region, but because signiﬁcant changes in economic development are diﬃcult to predict and often occur spo- radically, economic development should only be taken into consideration when there is a large potential for a region to experience signiﬁcant growth.

Finally, mean annual runoﬀis most directly related to the climate of the region and the amount of precipitation that it receives. [16] When extrapolating the potential mean annual runoﬀfor a region in the future, the historic MAR of the region should be plotted against factors such as precipitation and average temperature to project the future MAR.

Page 6 Control # 43443

2.4 Evaluation of the Model

2.4.1 Correlation with Water Stress Indicator (WSI)

The scatterplot below compares the WSI (on the x-axis) and the EWR (on the y- axis). We observe that there is a strong relationship between our model and the commonly used model of the WSI. One signiﬁcant strength of our model is that the diﬀerences between the EWR in water-scarce and water-abundant countries is more extreme than the WSI, which allows for a more precise measure of water scarcity. Additionally, the impact of water scarcity on individual citizens is made more clear by factoring in population. For instance, China and the United States have a very similar WSI (0.478 and 0.499, respectively), but the diﬀerence in populations means that this water shortage has a larger impact on a citizen of China than on a citizen of United States, so China’s EWR is over three times smaller.

WSI EWR (gal / person / year) Argentina 0.352 421760 Colombia 0.037 1672841 China 0.478 116302 India 0.967 5481 Russia 0.111 956034 Saudi Arabia 0.995 975 South Africa 0.687 273378 Spain 0.181 836927 Sweden 0.04 1674537 USA 0.499 393186 ·106

3 EWR (gal / person / year) 2

1

0

0 0.2 0.4 0.6 0.8 1 WSI Page 7 Control # 43443

2.4.2 Strengths

• Impact of population — The most pertinent statistic in water scarcity is how much spare water there is per person, which is taken into account by our model. This accurately reﬂects that countries with large populations face more signiﬁcant challenges in harnessing their water supply.

• Lack of an upper limit on available water — Other measures such as the WSI include a lower limit of 0 on water stress, which makes it diﬃcult to determine the extent to which countries have a surplus of water. Because our equation goes in the opposite direction such that a high value corre- lates to little water scarcity, regions can potentially continue to increase their Excess Water Ratio (EWR).

• Predictive power — By breaking up the data into the components that impact their long term trajectories, our model has more predictive power than preexisting models. It accounts for the underlying causes of changes in water usage and can take the growth rates of those factors into consid- eration when predicting the growth rate of water usage.

2.4.3 Weaknesses

• Availability of data — Ideally, the model should be applied to a region of any size to determine the overall water scarcity in the area. However, typically information is only available on a national level or on a state level in the United States, which makes it particularly hard to determine levels of water scarcity in small regions within countries.

• Broadness of categories — Our model treats agriculture, industry, and personal use as monolithic categories, when in reality each of these factors has various components that can move independently. However, other models such as the WSI have this same drawback, so our model is no weaker than established models in that regard.

2.5 A More Complex Model for Water Availability

More recent formulations of the Water Stress Indicator (WSI) acknowledge the importance of environmental needs in calculations of a region’s water use.[9] Such calculations are an improvement to the previous model because they rec- ognize that the maintenance of the environment of a region requires a constant ﬂow of water for the well-being of nearby plants and animals (WUe). While this water previously was included in the water available to humans for indus- trial, personal, and agricultural use, the previous model ignores the fact that dipping into the supply of water required for the environment harms the overall ecosystem.

Additionally, a more complex model recognizes that while a region used to get all of its water primarily from its surroundings, technology now enables regions to import water from areas that naturally have more abundant water Page 8 Control # 43443

sources. For instance, Singapore recently has been importing water from the Johore River catchment in Malaysia to make up for its large water needs, and India has established water treaties with Pakistan and China. [16] A more complex model for water is therefore reﬂected below:

EWR(Excess Water Ratio) = MAR + Import −WUi −WUa −WUp −WUe Population

3 Case Study: India

3.1 Rationale

We have selected India as the country for our case study. As of January 12th, 2016 there were about 1.3 billion people living in India. [17] This amounts to just over 18% of the total population of Earth. Simply put, this massive country that is home to so much of the world’s population is in a major water crisis. The following excerpt from a paper published by the National Bureau for Asian Research sets the scene: “The World Health Organization estimates that 97 million Indians lack access to safe water today, second only to China. As a result, the World Bank estimates that 21% of communicable diseases in India are related to unsafe water. Without change, the problem may get worse as India is projected to grow signiﬁcantly in the coming decades.” [18]

3.2 Main Drivers of Water Scarcity

One important cause of the water scarcity in India is “large spatial and temporal variability in the rainfall.” [19] Eﬀectively this means that water is distributed incredibly unevenly throughout the country in both in terms of geography and of time. Each of these conditions produces water scarcity in speciﬁc contexts: the former in relatively dry regions during otherwise wet months, and the latter during relatively dry months in regions both wet and dry.

Another factor exacerbating water stress is poor irrigation systems. [19] This unfortunately is a self perpetuating problem, because the rates charged for users of the system are very low. The low rates mean that insuﬃcient revenue is generated to support the operation and maintenance of high quality infras- tructure. This results in low quality infrastructure, which renders stakeholders reticent to pay more for it, which means the quality won’t get better etc.

Some farmers have responded to the previous two challenges by drawing water directly from the ground to irrigate their crops. This has led over the years to widespread overuse of the groundwater, far past the point of environmental sustainability. The resulting depletion of naturally occurring groundwater for agricultural/irrigation purposes has become a driver of water scarcity in its own right. [20] Notice that all three leading causes of water stress examined thus far have been agricultural in nature. This is because currently agriculture is responsible for a staggering 92% of water usage in India. However, in the relatively short Page 9 Control # 43443

term future, the population is expected to rapidly grow and industrialize. Both of these trends will require more water, both in absolute terms, and as a percent- age of water used. What this means is that over the long term, the country will be required to “produce more [food, to support the expanded population and industrialization] with less water.” [19] Or face massive food shortages and/or be unable to develop more advanced industrial resources.

Finally, one additional challenge related to rapid population growth that is very much in evidence in India is contamination. “More than 100 million people in India are living in places where water is severely polluted. Out of the 632 districts examined to determine the quality of groundwater, only 59 districts had water safe enough to drink.” [21] Even assuming that the same amount of water is being collected – which may or not be a valid assumption – keeping all of it clean enough to use will be imperative as the country grows.

4 Prediction of Water in India in 15 Years

4.1 Determining the Current State of Water Scarcity

Applying our model for water needs to India in the present day allows us to calculate an excess water ratio for India that can be compared to that of other countries. A variable in our model that is not readily available for the country as a whole is the MAR, because it varies signiﬁcantly throughout the country. For example, the MAR of the Ganges River at Farakka, India was approxi- mately 415 · 109m3, while the MAR of the Brahmaputra at Pandu, India was approximately 511·109m3 in 1997.[22] However, the calculation of the published WSI statistic requires an estimate of a total MAR for the country, so we can manipulate the formula for WSI to write the EWR in terms of WSI rather than MAR: WSI = withdrawals MAR  withdrawals EWR = MAR −withdrawals  1 WSI −1 = population population

India has a WSI of 0.967 as of 2009, total water withdrawals of 761 · 109m3, and a population of 1,251,695,584. [14][23] This gives it an EWR of 20.75m3 or 5481.59 gallons. To put this into context, this means that the average individual in India has 15 gallons per day of extra water that could theoretically be used. This number is extremely low relative to the amount of water currently being used. We note that the estimated amount of excess mean annual runoﬀnot being used per person at any given time, but a lack of technology in much of rural India prevents this water from being used in its current state. Thus, there is a large strain on India’s water that require immediate action, especially when compared to the EWR of other countries. For example, China – which has a much lower WSI of 0.478 – has an EWR of 373.9m3, which puts it in a much better position to provide water for the country’s needs.

Page 10 Control # 43443

4.2 Preliminary Estimation of Growth Rates of Water Use

In this stage of the modeling, we assume that in the relatively short time span of 15 years, the mean annual runoﬀfor India will remain relatively constant. We note that this assumption is not fully accurate, as climate change will likely alter India’s climate in a way that decreases water availability. However, the proposed model will still be helpful because it places a lower bound on the state of India’s water scarcity, such that water shortages in the next 15 years will be at least as bad as proposed by the model assuming the calculations for water use.

We start by formalizing our assumptions about the factors that impact the water use from each of the following sources: industry, agriculture, and personal. Water use from industry and agriculture are each assumed to be a product of their respective production levels and water footprints. Personal water use is assumed to be dependent on the rural population versus the urban population, and will then take into account the diﬀerent water use rates for each group. We also assume that there are two distinct population groups- urban and rural, and we then assume that all of the people in these populations consumer water at the average rate. These equations are formalized below:

Industrial Water Use(I) = Industrial Output(Oi) · Industrial Water Footprint(Fi)

Agricultural Water Use(A) = Agricultural Output(Oa) · Agricultural Water Footprint(Fa)

Domestic Water Use(I) = Urban Pop.(U) · Avg. Urban Water Use(Wu) + Rural Pop.(R) · Avg. Rural Water Use(Wr)

Total Water Use(W) = I + A + D

Growth Rate of Water Use from I(g(I)) = g(Oi) + g(Fi)

g(A) = g(Oa) + g(Fa) g(D) = U · Wu g(U) + R · Wr g(R) D D

Water Use(target year) = I(1+g(I))target−current +A(1+g(A))target−current + P(1 + g(D))target−current

Note that in the above equations, we utilize the commonly used approxi- mation that the growth rate of a product is approximately equal to the sum of the growth rate of each factor. According to the World Bank, India’s urban population growth is 2.38% and rural population growth is 0.68% with a total Page 11 Control # 43443

population growth of 1.2%.[24] Additionally, the average urban citizen of India uses 126 liter of water per day for personal use.[25] Factoring in information on India’s population, total personal water use in India, and the current percent- age of the population that is urban, we calculate the growth rate of water for personal use:

g(D) = (0.319)(0.0238) + (0.681)(0.0068) = 0.0122

We note as well that because of the large variations in water footprints for diﬀerent industries and crops in India, we assume that g(Fa) = g(Fi) = 0 within the 15 years of our projections. However, we ultimately conclude that this assumption is reasonable, since India’s government has been slow to adopt policies that promote drastic economic change. [26] Therefore, within the relatively short timespan of 15 years it is unlikely that the economy will change in a way that drastically alters the average water footprint of industries. Based on the World Bank, the growth rate of India’s agriculture sector varies signiﬁcantly each year but has centered around 3.8% between 2006 and 2014.[27] Additionally, the growth rate of India’s industrial sector has been about 5.0% during the same timespan. [28] We therefore estimate that the water use in 2031 will be given by:

Water Use(2031) = (688 · 109m3)(1.038)15 + (56 · 109m3)(1.012)15 + (17 · 109m3)(1.050)15 = 1306 · 109m3

This means that unless water use decreases or water availability increases beyond this projection over the next 15 years, the EWR will become negative as water use will surpass water availability. Eﬀectively, this simplistic ﬁrst model shows that with no change in current behavior India will be out of water before 2031. We note that this model presents a more extreme outcome than other models, such as those of the Indian government.[29] One factor that accounts for this is the fact that each area of water use is assumed to be growing expo- nentially, which represents a worst-case scenario. Additionally, we previously assumed that average water footprints remain constant, while it is entirely pos- sible that the average water footprint decreases with the scale of industry.

4.3 A More Robust Computer Model

Because the Indian government predicts the amount of water available and water used in diﬀerent sectors of the economy, we can estimate the excess water ratio in a given year by matching the amount of water in each category to a polynomial function using MATLAB’s “polyﬁt” function. We use the Indian government’s predictions for our data rather than exclusively data from past years. We reason that an estimation of the excess water ratio for a year between the years predicted by the government will be more accurate than an estimation extrapolated from data from many years before. To ﬁnd the excess water ratio, we compute the excess water ratio with each component’s value corresponding to its output of the polynomial function for that year.

Page 12 Control # 43443

By incorporating the components provided in the “Water & Water Related Statistics” report, the excess water ratio can be evaluated as follows: [29]

Excess Water Ratio = WUa + WUd + WUi + WUp + WUin + WUec + WUev −WAPC population

WUa represents water use for agriculture and irrigation, WUd represents domestic water use, WUi represents industrial water use, WUp represents water use for power, WUin represents water use for inland navigation, WUec represents water use for ecology, and WUev represents water lost to evaporation. These are all of the categories detailed in the report as signiﬁcant Indian water uses. WAPC is water available per capita.

Furthermore, the model can be used to assess the eﬀects of intervention policies. By adding the increases of water availability of a certain improvement to the total available water after the year of the improvement’s completion, we can graph the excess water ratio without (Figure 1) and with (Figure 2) the estimated eﬀects of interventions. The curve below graphs high projections for increases of water usage while the curve above graphs low projections. Because their predictions assume the development of the nation as a whole, these added components are restricted to intervention policies not already occurring that would be accounted for by the Indian government.

Using this model, we construct a graph for India’s excess water ratio be- tween 2000 and 2050 rooted in the Indian government’s predictions of water availability and usages in 1997, 2010, 2025, and 2050. Similarly, we generated a graph that demonstrates the eﬀects of intervention policies on India’s EWR. For the purpose of demonstrating the model, we assume that intervention projects will increase the amount of water by 30 and 50 billion m3 in 2020 and 2030 respectively.

Page 13 Control # 43443

Estimated Water Ratio Per Year with No Intervention 1400 Upper Bound Lower Bound

1200

1000

Excess Water Ratio 800

600

400

200

0 2000 2005 2010 2015 2020 2025 2030 2035 2040 2045 2050 Year

2050

Estimated Water Ratio Per Year with Example Interventions 1400 Upper Bound Lower Bound

1200

1000

Excess Water Ratio 800

600

400

200

0 2000 2005 2010 2015 2020 2025 2030 2035 2040 2045 2050 Year Page 14 Control # 43443

4.3.1 Assumptions for the Computer Model

• Changes to population and amounts of water available and used are pre- dictable. A variety of political, economic, and social factors inﬂuence how much water India consumes and has available, some of which are not quantiﬁable. To avoid arbitrarily quantifying possible events, our model assumes that the Indian government’s predictions in their “Water & Water Related Statistics” will be accurate. [29]

• Changes to quantities over our time interval can be approximated using polynomial functions. Due to the relatively few number of data points over our time interval, polynomial functions are a way to approximate a curve that contains those points. While imperfect in accuracy, it provides a solid estimation for excess water ratio between the established points.

4.4 Conclusions for Impacts on Citizens

From the ﬁrst model, we note that a demographic shift impacting water scarcity in India is the increasing proportion of the population living in urban areas. Because urban populations typically use more water than rural populations, this puts a larger strain on India’s water supply, and is one of the largest sources of predicted water increases in the next 15 years. Therefore, an impact of water scarcity will be a decrease in standard of living for cities, as resources strain.

The ﬁrst model also assumes that water use will increase along with the current growth rates of industry and agriculture. However, one of our assump- tions in constructing our initial model for water use was that society cannot use water beyond the water physically available. Thus, the prediction of water use from the ﬁrst model should be interpreted as the ideal amount of water availability given current growth rates. Realistically, a water shortage will limit India’s economic growth potential, as agriculture and industry will have to slow down their current rate of expansion with water as a limiting resource. However, the most powerful impacts are the impacts of water shortages on the lives of ordinary citizens in India. With its current water shortages, over 21% of India’s diseases are water-related and only 33% of the country has access to traditional sanitation.[31] Unless the pace of technology improvement is somehow able to keep up with the pace of water needs, these issues will only be worsened.

5 Intervention Plans for India

5.1 Intervention Plans for India’s Water Scarcity

In its water report “Coping with water scarcity,” the FAO notes that the most comprehensive water scarcity interventions address both the demand and supply sides of water scarcity to help align the goals of parties on each side.[32] This report deals with interventions that can be taken for agricultural water use in India, which is particularly relevant since this category makes up the largest Page 15 Control # 43443

share of India’s water use. We will discuss intervention strategies that focus on increasing India’s water supply: watershed development and water recycling from waste. We will also discuss intervention strategies that focus on decreasing the demand for water such as societal changes in food consumption and changes in agricultural production. We note that this is by no means an exhaustive list of possible changes to alleviate water scarcity in India. Some additional projects that may be helpful are limited. For instance, dams have historically been used in attempts to increase water supplies for irrigation. Many scientists believe that dams would be helpful in improving India’s water supply, but they also have many adverse side eﬀects, as illustrated by the Narmada Dam project in India.[30] The construction of the dam displaced 200,000 people and had disastrous environmental consequences such as the ﬂooding and salination of land near the dam that ruined crops.

5.1.1 Watershed Development

Water supply can ﬁrst be improved by constructing watersheds throughout In- dia. A report from the World Resources Institute describes a 2005 study that performed a meta-analysis of 311 watershed development case studies, and de- termined that the construction of watersheds increases water storage capacity, increases cropping intensity, reduces water lost to runoﬀ, and reduces soil loss. [33] The same report concludes that approximately 380 watershed projects have been constructed in India, which have allowed for an increase of 260,000 hectares of agricultural production. On average then, each project has provided irrigation needed for 684 hectares. We acknowledge that diﬀerent crops require diﬀerent amounts of water, so the water requirement is not uniform among each hectare of land. However, due to the absence of more speciﬁc data, we make the sim- plifying assumption that water consumption per hectare is constant throughout India’s farmland. Based on Aquastat data, India current cultivates 170,000,000 hectares and uses 688·109m3 of water for irrigation, which averages out to 404.7 m3 per hectare. We conclude that each completed watershed allows for an in- crease of 276,800 m3 of water to be used for agriculture. Of course, watersheds cannot be constructed inﬁnitely because there is a limit on how much water can be recovered, but so far no limiting capacity of watershed development has been seen in India. We therefore recommend that the Indian government selects 50 areas that could potentially beneﬁt from a watershed and begin construction immediately, which would give a yearly increase of 1.38 · 107m3 of water for agriculture. When determining where these structures should be located, stud- ies suggest that the areas that would beneﬁt most are semi-arid regions with erratic monsoons that prevent water from quickly recharging. [34] We assume in our model that these watersheds will begin construction in the next year, and will follow the timeline of the Neeranchal National Watershed, which was built over six years. The changes will then go into eﬀect in 2022. [35] Page 16 Control # 43443

5.1.2 Water Recycling and Waste Treatment

With the second largest population of any country in the world, India’s popula- tion produces a large amount of waste that can be treated to be used for agricul- tural purposes. There is precedent for treating waste that can be expanded over the next several years to provide a consistent source of water. Water from waste can only be used in agricultural purposes, because it does not meet the quality standards for personal or industrial use.[30] Currently, this water is being used to irrigate trees in public parks in Hyderabad, to cultivate wheat paddies over 2100ha along the Musi River, and to support ﬁsheries in East Calcutta. Based on public data from Aquastat, as of 2011 India had 270 municipal wastewater treatment facilities, which have the total capacity of treating 4.573 · 109m3 per year. They treat 4.416 · 109m3 per year, but 11.03 · 109m3 per year is left un- treated. Based on the current capacity of the treatment facilities, each facility can treat 1.69·107m3 per year, so constructing new facilities for the treatment of wastewater would require the construction of 651 new treatment plants. While pricing information for waste treatment plants is not readily available, the con- struction would be very expensive. However, we believe that the plants would be worth the cost in the long run because they would provide a future sustainable source of water for agriculture. When we account for this intervention policy in our model, we assume that all untreated wastewater will eventually be treated and used for agriculture, adding 11.03·109m3 per year. Based on building times for large-scale waste treatment facilities in the United States, we estimate that these could be built in three years and begin working by 2019.

5.1.3 Societal Changes in Food Consumption

One of the largest impacts on demand for water is currently due to food con- sumption, as “90% of personal water footprints are devoted to food in the form of crop and animal production.” [36] For the purposes of constructing our model to predict future water availability, we do not assume that this change will be enacted or successful. However, to approach the supply and demand sides of the water consumption issue, governments will soon need to address the un- sustainable eating habits of populations. Meat and dairy products are much more water intensive than crops, and the consumption of these foods increases as populations move to urban areas. A cultural shift in eating habits, while requiring a change in attitudes toward foods that would take several years, may eventually become necessary as lower water levels decrease the potential for water-intensive farming.

5.1.4 Changes in Food Production

One of the most signiﬁcant intervention techniques that India can undertake is to decrease the demand for water from agriculture by subsidizing the production of more water-eﬃcient crops. For example, millet is a much more water-eﬃcient crop than rice or wheat, which currently make up the largest shares of India’s agriculture based on data from AQUASTAT. Speciﬁcally, the growth of rice Page 17 Control # 43443

requires 1250 mm on average of rain or irrigated water, wheat requires 550 mm, and millet requires just 350 mm.[40] [41]Millet can also be grown in soil that is far poorer quality than traditional crops. Critically, millet is nutritionally equiv- alent to rice or wheat, containing comparable levels of protein, ﬁber, minerals, iron, and calcium.

In our model, we have considered the water impact of switching all of India’s wheat and rice production to millet over the course of 30 years. For each land unit of water converted from rice to millet we save 900 mm of water annually, with 200 mm more in savings added for each land unit converted from wheat to millet. Over the timespan modeled, we expect this intervention to produce considerable water savings.

5.2 Impact of Water Available of Surrounding Area

One of the most signiﬁcant strengths of watershed development is that there is no evidence of negative impacts on the surrounding areas. Typically, watershed development serves the purpose of making degraded lands suitable for agricul- ture, which is independent of the agricultural output of surrounding regions. While the treatment of wastewater has the potential to provide large amounts of additional water for agriculture, studies suggest that the use of treated wa- ter may alter soil quality over time. [30] According to the International Water Management Institute: “Ample evidences are available which show that the groundwater in all wastewater irrigated areas has high salt levels and is unﬁt for drinking. Further, high groundwater tables and water-logging are also com- mon features of these areas.” This poses a health risk to communities that are located downstream of the area, since it may be diﬃcult to separate this agricul- tural water from personal use in communities that do not have the technology for advanced water puriﬁcation.

5.3 Evaluation of Strengths and Weaknesses

The World Resource Institute report identiﬁes many social and economic ben- eﬁts of watershed development, and concludes that there is a net present value between $5.08 million and $7.43 million. It also points out other beneﬁts that could not be included in the cost-beneﬁt analysis, such as “improvements in nu- trition, dietary diversity, and human health” as well as “improved resilience to drought and temperature ﬂuctuations.” A weakness of this proposal is that the development of watersheds can be expensive, and modiﬁcations of the natural environment can have unpredictable consequences on the ecosystems. Addition- ally, a social problem brought up by watershed construction is that historically the construction of watersheds has negatively impacted women in India. [37] The development of watersheds required the closing of common areas where poorer women grazed goats, which deprived them of a large source of income. However, in carrying out future projects, Kerr notes that “Some of the negative eﬀects on women could be overcome if a great eﬀort was made to include them in decision making.” Finally, watersheds require a signiﬁcant upkeep cost, and Page 18 Control # 43443

historically a lack of attention to constructed watersheds has caused them to be leaky or damaged. [38] One strength of waste treatment is that it creates a reliable source of wa- ter supply for agriculture, removing much of the uncertainty that characterizes water scarcity in developing countries. The Weighted Anomaly Standardized Precipitation (WASP) index computes deviations in monthly precipitation, and shows that parts of Central India frequently are drier than their average precip- itation, making it diﬃcult to group crops given uncertain weather conditions. [39] By diverting treated wastewater to these areas, water can be more eﬃciently used. Additionally, the treatment of wastewater has a positive externality of long term economic growth for workers in the region. The construction of the facilities requires the hiring of several construction workers, and the constant treatment of waste requires a large permanent staﬀ. As noted above, however, wastewater has the potential to make water less usable downstream, and the construction of the facilities will require a large initial cost from the government. Thus it is unlikely that the government would be able to fund the construction of all of the plants at one time.

The main beneﬁt of shifting crop production away from rice/wheat and to- wards millet (and more generally away from water eﬃcient crops towards more water eﬃcient varieties) is of course massive water savings. Other strengths of this approach include consumers taking advantage of the enhanced nutritional value of millets vs. wheat and rice, and the existence in the status quo of pro- totype models of eﬀective programs that already provide “training via internet and mobile phone, adapted to smallholder farmers and practitioners, on the best farming practices for drought and heat tolerant crops such as millet and sorghum.” [42] There are at least two key challenges standing in the way of adopting this approach. First, local tastes have to be taken into account. If no one wants to eat millet, and thus there was no demand for it, no sensible farmer would grow it. Accordingly, gathering and heeding input from the local population of both farmers and consumers to create demand for millet as a food crop would be critical to the success of this intervention. Second, even assum- ing that it were possible to convince everyone to love millet overnight, far more investment would be needed to ensure that suﬃcient training in proper millet growing techniques, and ﬁnancial support to purchase millet seed was available to every small farmer that could and would use it to convert their wheat or rice farm into a millet farm. [42]

6 Projection of Future Water Availability for

India

With interventions in infrastructure (Figure 3), the improvements are almost insigniﬁcant in the India’s future water scarcity. With these investments in infrastructure, India will run out of water between 2084 and 2094, rather than 2083 and 2093 without improvements.

Page 19 Control # 43443

Estimated Water Ratio Per Year 1400 Upper Bound without Intervention Lower Bound without Intervention Upper Bound with Intervention Lower Bound with Intervention 1200

1000

Excess Water Ratio 800

600

400

200

0 2000 2005 2010 2015 2020 2025 2030 2035 2040 2045 2050 Year

interventions, 2000 to 2050

Estimated Water Ratio Per Year 1400 Upper Bound without Intervention Lower Bound without Intervention Upper Bound with Intervention Lower Bound with Intervention 1200

1000

Excess Water Ratio 800

600

400

200

0 2000 2005 2010 2015 2020 2025 2030 2035 2040 2045 2050 Year

tions, 2000 to 2050 Page 20 Control # 43443

By replacing wheat and rice crops with millet (Figure 4), the water used signiﬁcantly decreases, leading to a much higher EWR. Instead, India will run out of water between 2097 and 2107

7 Conclusion

We began by creating the new metric of “excess water ratio” that improves upon currently used measures by illustrating the extent to which water shortages im- pact an average individual in the region. Turning to the case study of India, we then identiﬁed the components that make up each of the contributions to the excess water ratio and predicted their growth rates in order to extrapolate the growth rate of water needs in India over the next 15 years. Our results illustrated that at current growth rates, the average excess water per capita will be half of the current value by 2031. We concluded by exploring inter- vention possibilities to develop long-term solutions for India’s water issues. We ﬁrst looked at strategies that increase the supply of water, but found that these techniques were expensive and did very little to oﬀset the rapidly increasing wa- ter demands. When we turned to attempts to decrease the demand for water, such as switching some crop production to the water-eﬃcient grain millet, we concluded that these could be much more eﬀective in the long term assuming that they are properly implemented by governments. This result makes sense, since the global supply of water is currently limited to what is already physically available, while demand for water can potentially always be lowered. Funda- mentally though, we conclude that more drastic societal changes will need to be adopted to decrease India’s water demand enough to matter.
