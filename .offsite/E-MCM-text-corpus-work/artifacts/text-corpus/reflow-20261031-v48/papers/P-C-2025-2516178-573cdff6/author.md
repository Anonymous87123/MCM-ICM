Summary

Predicting the number of Olympic medals each country will win is crucial for various stakeholders. We therefore developed an Olympic medal model based on the dataset of past Olympic Games.

First, following model screening, we developed a dual-stage XGBoost model for predicting Olympic medal counts. The dual-stage XGBoost model is composed of an XGBoost binary classifier and a TPE-XGBoost regressor whose hyperparameters are optimized by the Tree-structured Parzen Estimator algorithm. The classifier serves to analyze historical data patterns in depth and effectively identify the potential competitiveness of small-scale participating countries. The regressor, on the other hand, accurately forecasts the specific number of medals for countries likely to win. Given the time-series nature of Olympic data, we employed the last-block cross-validation approach, a type of time-series cross-validation.

Second, an evaluation of the dual-stage XGBoost model's prediction performance was carried out. The model demonstrated outstanding performance in predicting the 2021 and 2024 Olympic Games, achieving a classification accuracy of 95% and an overall prediction accuracy of 68%, significantly outperforming existing Olympic prediction models. Confidence interval estimation was conducted using the non-parametric Bootstrap method. After 1000 iterative verifications, the model's sample coverage probability exceeded 0.95, and the probability that the predicted values fell within the confidence interval was over 70%. Based on these results, we predicted the medal distribution for the 2028 Olympic Games. Moreover, we innovatively combined the classifier and regressor to quantify the first-time medal-winning probability of small Olympic countries. Simultaneously, SHAP value analysis was utilized to uncover the contribution of different events to each country's medal-winning.

Third, we quantified the Olympic medal-winning scores and then developed a difference-in-differences model. The double-difference term incorporated in this model effectively controlled interfering variables other than the coach factor. For the Chinese and Dutch teams, the p-values of the regression coefficient tests of the model were 0.03 and 0.05 respectively, both reaching the significance level, providing reliable statistical evidence for the existence of the “great coach” effect. When applying this model to relevant projects of other countries, the predicted medal-number growth trend was highly consistent with the actual situation.

Finally, the SHAP Summary Plot was utilized to analyze the mechanism through which the standardized number of participants affects the number of Olympic medals. Based on this, a two-track optimization strategy was proposed: strategically expanding the overall participation scale while focusing on developing emerging projects with potential competitive advantages.

In addition, a sensitivity analysis was conducted to assess the model's responsiveness to changes in input parameters. The results indicated that the model exhibited high accuracy and robustness in handling diverse scenarios.

1 Introduction

1.1 Problem Background

In 2024, people worldwide witnessed the first Olympic Games following the COVID-19 pandemic. This grand event held in Paris rekindled the public's enthusiasm for this renowned sports event and spurred the audience's anticipation for the 2028 Los Angeles Olympics, spe- cifically, how countries would perform in the upcoming Olympics. To address this question, this paper endeavors to predict the outcomes of the next Olympics through model-building.

微信公众号：数学模型 微信号：MATHmodels

Since Ball [1] developed a correlation-based scoring model, the methodology for predict- ing Olympic results has witnessed remarkable evolution. Prediction models have advanced from the early ordinary least squares regression (OLS) to a probability-model system based on the Poisson distribution, encompassing Poisson regression and negative binomial models. Re- cently, research has trended towards a dual-stage approach: initially estimating the probability of medal-winning and subsequently predicting the specific number of medals. The Mundlak transformation of the Tobit model and the Hurdle model are the most emblematic. Simultane- ously, the dimensions of prediction data have been continuously broadened, manifested in finer-grained data, an extended time span, and diverse explanatory variables. Nevertheless, during the data-expansion process, the validity of variables and the issue of multicollinearity must be carefully considered.

1.2 Restatement of the Problem

Considering the information given and conditions provided in the problem statement, we conclude that 4 objectives must be completed to finish all the goals required.  Objective 1: Accurately reflect and predict the medal-less status of many countries.  Objective 2: Build a mathematical model to evaluate if and how much “great coach” effect and other factors work.  Objective 3: Predict changes in the role of momentum, analyze what factors influence this fluctuation, and use the conclusions to guide player play. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m  Objective 4: Evaluate the results of the prediction and apply them to other sports events.

1.3 Our Work

2 Assumptions and Justifications

We make the following basic assumptions to simplify the problem, each of which is well justified.  Assumption 1: Only consider historical medal data, event factors, and coaching; ignore external non-sports-specific factors.

⇒ Justification: Political changes, natural disasters, and economic crises can have an impact on a country's sports development, which are difficult to predict and quantify. By fo- cusing on historical medal-winning data, event-related factors, and coaching, we can establish a relatively stable and analyzable model.  Assumption 2: Coaches' impacts are comparable across countries and sports, overlooking cultural differences.

⇒ Justification: The cultural background of a coach should not have an impact on their coaching performance when working with different national teams. A committed coach is ex- pected to provide thorough and unsparing guidance to their athletes, regardless of the country they are coaching in.  Assumption 3: Olympic event rules and scoring systems are stable.

⇒ Justification: The International Olympic Committee (IOC) has the responsibility and ability to maintain the stability of the Olympic competition rules. Over the past century or so, regardless of how turbulent the global situation has been, the competition rules have always remained immune to the influence of international political situations. This is one of the reasons why the Olympic Games have always enjoyed great trust.  Assumption 4: Based on the resolutions officially approved by the IOC, when predicting

关注数学模型 the medal count for the 2028 Los Angeles Olympics, each of the Cricket, Squash, Base- ball/Softball, Lacrosse, and Flag Football events will have 2 additional medals.

⇒ Justification: The model in this paper is built as of the current time, considering only the known event changes. The International Olympic Committee has the authority to decide on adding competition events and their associated medal arrangements. Given the available infor- mation, we only consider the approved new events and their corresponding medal increments to ensure the model is based on existing and certain data.

3 Notations

The key mathematical notations used in this paper are listed in Table 1.

Table 1Notations used in this paper

Symbol

Description The total number of participants of country i in the Olympic Games held in Peoplei,t year t i Country number ● Year t Whether a country is a host country Host y predicted value of the ith sample under b Bootstrap models The medal score in the ith year scorei ATTe

4 Model Preparation

4.1 Data Pre-processing

4.1.1 Time Limitation

First, we only adapt data from 1952 onwards as the post-war period saw significant trans- formations in the global sports landscape with countries recovering and rebuilding their sports systems, greater standardization of sports events ensuring data comparability and reliability, an expansion of international sports participation providing a more diverse dataset. 4.1.2 Identification and Processing of Invalid Data Additionally, we excluded the data of years when countries such as East Germany and Russia, which had major scandals, participated. To be specific, incidents such as large-scale boycotts as occurred at the 1980 Moscow and 1984 Los Angeles Games and the East German doping program responsible for 17 percent of the medals awarded to female athletes in 1972 skewed the medal count in the past. 4.1.3 Processing of NOC We also merged the names of certain teams. For instance, "Taiwan" and "Chinese Taipei" were combined. And some countries' names have random spaces or numbers attached, which have also been processed. Furthermore, certain countries that have ceased to exist, like Yugo- slavia, were excluded from our analysis.

4.1.4 Event Data Cleaning

Moreover, in the dataset, there was some data with format or content errors, such as some data showing incorrect characters or being vacant. By identifying and eliminating or correcting such faulty data, we have improved the quality of the dataset and made our subsequent analysis more reliable and valid. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

4.1.5 Processing of Participant Numbers

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We not only tabulated the number of participants from each country in every event but m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m also recorded the number of medals each event yielded. Given that the number of participants m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m varies across different events-for instance, a football team has eleven players, which might lead m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

to the misconception of counting 11 medals per team — we standardized the number of par- ticipants. Specifically, we set the number of participants in the team with the fewest members in a particular event as 1 and scaled down the numbers of other countries proportionally.

4.1.6 Processing of the Medal Standings

By collating data on athletes' participation and medal-winning, we identified a set of coun- tries that have never won medals throughout history.

5 Model I: Dual-staged XGBoost Medal Prediction

Based on the theoretical frameworks of the Tobit model and the Hurdle model, this paper proposes an innovative dual-stage machine learning approach [2].

 Stage 1: Addressing the Zero-Medal Scenario A classifier is employed to specifically address the "zero-medal problem". The signifi- cance of this design lies in its ability to effectively capture the competitive characteristics of small-scale participating countries, preventing their medal-winning potential from being masked by the data characteristics of Olympic powerhouses. By deeply analyzing the latent patterns in historical data, the classifier can identify countries on the verge of breaking through the zero-medal barrier.

 Stage 2: Medal Quantity Prediction A regressor is then introduced to estimate the specific number of medals for countries predicted to win medals. This design avoids systematic bias that could result from directly predicting medal counts for all participating countries, thereby significantly enhancing the overall prediction accuracy of the model.

This divide-and-conquer strategy not only improves the reliability of the predictions but also offers a novel methodological perspective for future research. Subsequently, the task is to select the most appropriate model architecture from existing machine learning algorithms to handle these two prediction tasks.

5.1 Parameterization of Influencing Factors

In this section, we identify the core independent variables of the developed model and elaborate on their quantification methods.

5.1.1 Standardization of Total Participants Number

After standardization, we define the total number of participants of country 𝑖 in the Olympic Games held in year 𝑡 as 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡. To enhance the model's interpretability and the robustness of its predictions, we apply the equal-frequency binning algorithm to discretize

关注数学模型 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡. Specifically, we transform the continuous variable 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡 into the discrete var- iable 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑑𝑖𝑠𝑐𝑟𝑒𝑡𝑒 based on the 20%, 40%, 60%, and 80% frequency quantiles. The math- ematical expression is as follows:

(1)

微信公众号：数学模型 Here, 𝑄𝑛 denotes the value of the total number of participants at the 𝑛% quantile. Due to the non-constant marginal returns between participant and medal counts, discretization ena- bles us to abandon the constant returns assumption, thereby enhancing model robustness.

5.1.2 Standardization of Participants Number in Each Event

We define the standardized number of participants of country 𝑖 in a particular event at the 𝑡 -year Olympic Games as 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡 , where 𝑠𝑝𝑜𝑟𝑡 represents the specific event name. This variable is a continuous variable reflecting differences in geographical conditions and sports development levels across regions.

微信号：MATHmodels

5.1.3 The "Host-country Effect”

We define the "host-country effect” on country 𝑖 in the Olympic Games as 𝐻𝑜𝑠𝑡. Host nations enjoy significant advantages: athletes avoid travel fatigue and benefit from venue fa- miliarity, while potentially receiving favorable officiating decisions. The seven-year prepara- tion period following host selection enables systematic athletic development, often yielding performance improvements in pre-host Olympics. These enhancements frequently persist in post-hosting due to elite athletes' multi-Olympic career spans.

To quantify these temporal host-country effects, we implement three binary variables [3]:

(2)

Here, 𝑡ℎ𝑜𝑠𝑡 denotes the year when country 𝑖 hosts the Olympics. The discrete variables 𝐻𝑜𝑠𝑡𝑡, 𝐻𝑜𝑠𝑡𝑡−4, and 𝐻𝑜𝑠𝑡𝑡+4 are respectively used to capture the "host-country effect” dur- ing the hosting year, four years before, and four years after the hosting year for country 𝑖.

5.1.4 Host Year

We define the year of the Olympic Games as 𝑦𝑒𝑎𝑟. This variable not only captures the historical evolution of the Olympic Games' scale but also reflects the development trends of global competitive sports among countries.

5.1.5 Event Medal Setup

Regarding the event-specific medal setup, we denote the total number of medals allocated by the IOC for a particular 𝑠𝑝𝑜𝑟𝑡 at the 𝑡-year Olympics as 𝑀𝑒𝑑𝑎𝑙𝑡,𝑠𝑝𝑜𝑟𝑡. These variable m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m measures event-specific competitive intensity, with variations in medal distribution signifi- cantly impacting national performance outcomes, particularly in a country's specialized events.

5.1.6 Number of Medals Won by Each Country in Each Event

The total number of medals that country 𝑖 wins in the 𝑠𝑝𝑜𝑟𝑡 event at the 𝑡-year Olym- pics is defined as 𝑀𝑒𝑑𝑎𝑙𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡. These metric captures both a nation's event-specific compet- itive strength and its strategic sports development priorities. Event-level granularity enables more precise evaluation of competitive advantages.

5.2 Developing of the XGBoost Classifier

XGBoost, an efficient gradient-boosting algorithm, has shown remarkable performance in supervised learning [4]. Its superior predictive power and broad application scope lead us to select this algorithm for developing a binary classifier. The algorithm's schematic diagram is presented below:

Specifically, XGBoost's objective function comprises two components: the loss function and the regularization term:

(3)

The loss function 𝑙(𝑦𝑖, 𝑦𝑖̂) measures the discrepancy between the predicted value 𝑦𝑖̂ and 𝐾 the true value 𝑦𝑖. The regularization term ∑ controls the model's complexity. The 𝛺(𝑓𝑘) 𝑘=1 model's predicted value is the sum of the predictions from 𝐾 decision trees:

(4)

Where 𝑓𝑘(𝑥𝑖)  denotes the prediction of the 𝑘 th decision tree for sample 𝑥𝑖 . The XGBoost model generates the final prediction by aggregating the forecasts of multiple decision trees. Each decision tree, to some degree, captures diverse patterns and characteristics.

When building a medal-number classifier using the XGBoost model, we need to binarize the total number of medals won by different countries. For country 𝑖's performance at the 𝑡 year Olympics, we define the binary variable as:

(5)

关注数学模型 To optimize the binary classifier's performance and address the data imbalance between large and small participating countries, thereby better capturing the competitive characteristics of small-scale participants, we only consider four indicators—𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡 , 𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡 , 微信公众号：数学模型 𝑔𝑜𝑙𝑑, 𝐻𝑜𝑠𝑡, and 𝑦𝑒𝑎𝑟—as independent variables. By incorporating the dependent variables 𝑦𝑖,𝑡 𝑠𝑖𝑙𝑣𝑒𝑟, and 𝑦𝑖,𝑡 𝑏𝑟𝑜𝑛𝑧𝑒 into the objective function for XGBoost model training, we obtain three 𝑦𝑖,𝑡 target binary classifiers.

To systematically evaluate the classifier's performance, we take total-medal prediction as an example and compare three models: XGBoost, binary logistic regression, and random forest. We use the ROC (Receiver Operating Characteristic) curve as an evaluation tool, which com- prehensively reflects the binary-classification model's discriminatory ability under different decision thresholds [5]. The resulting ROC curve is as follows:

XGBoost Random Forest Multiple Logistic Regression 微信号：MATHmodels

Experimental results show that the XGBoost model significantly outperforms the others in classification, with the highest AUC (Area Under Curve) value of 0.957. This indicates a 95.7% accuracy in distinguishing between countries that "won gold medals" and those that "did not". This highly accurate prediction not only validates XGBoost's excellence in handling com- plex non-linear classification problems but also shows its ability to effectively capture multi- dimensional factors influencing Olympic medal winning. Based on these findings, choosing XGBoost as the final classifier is well-supported empirically.

5.3 Developing of the TPE-XGBoost Regressor

Next, we aim to build a machine-learning regressor for the countries predicted to win medals by the classifier. To enhance the regressor's prediction accuracy, we select six indicators —𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡,𝑃𝑒𝑜𝑝𝑙𝑒𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡, 𝐻𝑜𝑠𝑡, 𝑦𝑒𝑎𝑟, 𝑀𝑒𝑑𝑎𝑙𝑡,𝑠𝑝𝑜𝑟𝑡, and 𝑀𝑒𝑑𝑎𝑙𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡—as independent variables for precise model developion. Given the continuous nature of Olympic medal-count prediction, we adopt the mean squared error as the loss function:

(6) As every machine-learning regressor involves a set of hyperparameters, when the dimen- sionality of our independent variables is high, the proper setting of hyperparameters signifi- cantly affects the model's prediction accuracy and generalizability [6]. Commonly used hy- perparameter optimization methods include grid search (GS) and random search (RS). How- ever, these two methods demand substantial computational resources [7, 8]. Therefore, we em- ploy the Bayesian algorithm, specifically the Tree-structured Parzen Estimator (TPE), to de- velop a TPE-XGBoost model for optimizing XGBoost's feature selection and hyperparameter tuning.

We continuously optimize the hyperparameter configuration, such as the maximum tree depth, learning rate, and minimum child weight, using TPE. This optimization process adap- tively balances the model's fitting capacity and generalization performance.

To evaluate the machine-learning results, we introduce the coefficient of determination R²:

n ∑(yi − yi)2 i=1 R² =1− (7) n ∑(yi− y)2 j=1 For the XGBoost model, we obtain the changes in R² of the prediction regression models for gold, silver, and bronze medals after TPE hyperparameter optimization, as presented in the following table:

After Optimization Before Optimization Gold 0.910 0.938 Silver 0.828 0.905 0.893 Bronze 0.841 To further prevent overfitting, we divide the dataset into a training set and a validation set using cross-validation. The training data is used to train the model, while the validation data is employed to ensure the model's ability to generalize beyond the training sample. Given the temporal evolution and dependency between the independent and dependent variables in this regression model, randomly splitting the dataset to build the model is inappropriate. Thus, we adopt the last block cross-validation method, which takes the time series into account by using the most recent data points as test data. This is reflected in our approach to using data from the 2008-2021 Olympic Games as the training set to predict the medal table of the 2024 Olympic Games when selecting the best machine-learning model to develop the regressor, as shown in the following figure:

Years of Olympic Games 1952 1956 2008 2012 2016 2020 2024 2028 Training of VaL Train Different Models Model Selection Train Test Model Benchmarking Train Test Model Benchmarking F.c. Forecasting Train

We selected the Random Forest and Multiple Logistic Regression models for compara- tive analysis. The following is the visualized chart of R² for the three different models after

关注数学模型 TPE hyperparameter optimization:

XGBoost Random Forest Multiple Logistic Regression

微信公众号：数学模型 微信号：MATHmodels

Based on the 𝑅2 values of the test and training sets, the XGBoost model exhibits the best performance. In gold-medal prediction, XGBoost achieves a test-set 𝑅2 of 0.938 and a train- ing – set 𝑅2 of 0.983. The random forest model, in contrast, has a test-set 𝑅2 of 0.724, while the linear regression model only reaches 0.570, indicating a significant performance disparity. This superiority is also evident in the prediction of silver and bronze medals.

Observing the scatter-point distribution, the prediction points of the XGBoost model are more closely clustered around the diagonal, suggesting the highest consistency between pre- dicted and actual values. Particularly when predicting many medals, XGBoost shows signifi- cantly less prediction deviation than the other two models.

Based on the width of the confidence interval, the XGBoost model yields the narrowest confidence band for its predictions, reflecting the highest level of stability and reliability.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Finally，a dual-stage XGBoost framework can be established, where the first stage em- ploys an XGBoost classifier for preliminary screening, followed by a second stage utilizing a TPE-XGBoost regressor for precise prediction. The detailed workflow is illustrated as follows:

6 Evaluation and Application of the Dual-Stage XGBoost Model

6.1 Model Evaluation Metrics

To further quantitatively assess the medal-prediction performance of the dual-stage XGBoost model, we introduce four evaluation parameters, 𝑀1–𝑀4.

- 𝑀1 is the overall prediction accuracy, used to evaluate the model's overall prediction capability.

- 𝑀2 refers to the prediction accuracy for medal-winning countries, measuring how ac- curately the model predicts countries that will win medals.

- 𝑀3 represents the prediction accuracy for zero-medal countries, evaluating the model's prediction accuracy for countries that won't win any medals.

- 𝑀4 is the accuracy within the 95% confidence interval, which gauges the stability and reliability of the model's predictions.

, (8) ,

Here, 𝐶𝑜𝑟𝑟𝑒𝑐𝑡𝑡𝑜𝑡𝑎𝑙denotes the total number of countries for which the medal count is accurately predicted. 𝑁𝑎𝑡𝑖𝑜𝑛𝑠𝑡𝑜𝑡𝑎𝑙 stands for the total number of countries included in the prediction. 𝐶𝑜𝑟𝑟𝑒𝑐𝑡𝑛𝑜𝑛𝑧𝑒𝑟𝑜 represents the number of countries for which medal-winning is accurately predicted, while Nationsmedal is the total number of countries that actually win medals. 𝐶𝑜𝑟𝑟𝑒𝑐𝑡𝑧𝑒𝑟𝑜 is the number of countries for which zero-medal status is accurately pre- dicted, and 𝑁𝑎𝑡𝑖𝑜𝑛𝑠𝑧𝑒𝑟𝑜  is the total number of countries with zero medals in reality. 𝑁𝑎𝑡𝑖𝑜𝑛𝑠𝑐𝑜𝑛𝑓𝑖𝑑𝑒𝑛𝑐𝑒 refers to the number of countries whose predicted values fall within the 95% confidence interval.

6.2 Evaluation of Model Prediction Accuracy

Subsequently, the dual-stage XGBoost model is evaluated by continuously applying the

关注数学模型 last block cross-validation method. To be specific, the data from the Olympic Games held be- tween 1952 and 2016 are utilized to build a training set. After that, the trained model is em- ployed to predict the medal distribution of the 2021 Tokyo Olympics.

Following this, the actual data of the 2021 Tokyo Olympics are incorporated into the train- ing set. The model is then retrained to predict the medal distribution of the 2024 Paris Olympics. The detailed process is depicted in Figure 5 Model selecting, benchmarking and applying.

Based on the quantitative assessment results of the dual-stage XGBoost model, we con- duct a systematic analysis of the prediction performance for the 2020 Tokyo Olympics and the 2024 Paris Olympics. Table below presents the prediction accuracy indicators (𝑀1–𝑀3) for different medal levels. 微信公众号：数学模型

2020 Tokyo 20204 Paris Prediction 𝑀1 𝑀2 𝑀3 𝑀1 𝑀2 𝑀3 Gold 59% 11% 92% 68% 22% 95% Silver 61% 14% 92% 63% 19% 95% Bronze 57% 13% 92% 68% 17% 95% Quantitative analysis reveals that the model's prediction accuracy for the 2024 Paris Olympics far exceeds that for the 2020 Tokyo Olympics. We can attribute this variance in pre- 微信号：MATHmodels diction precision to the unique impact of the COVID-19 pandemic on the 2021 Olympics. The pandemic significantly altered the training schedules and preparatory strategies of participating countries.

Notably, the 2024-oriented prediction model demonstrates astonishing accuracy. For in- stance, in gold-medal prediction, our dual-stage XGBoost model significantly outperforms cur- rent mainstream prediction models, such as the Dual-staged Random Forest and Tobit models [9], in terms of both gold-medal prediction accuracy (68%) and range prediction accuracy (22%).

6.3 Solving Confidence Intervals with the Non-parametric Bootstrap Algo-

rithm

When evaluating the confidence intervals of neural network models, traditional ap- proaches predominantly rely on the Delta method and the Mean-Variance Estimation (MVE) method. However, these methods exhibit limitations such as high computational costs and low coverage rates in practical applications [10].

Given that machine-learning prediction results typically do not conform to the normal- distribution assumption and are influenced by multiple non-linear factors, this study employs the non-parametric Bootstrap method to develop the confidence interval for the regressor part within the dual-stage XGBoost model.

During the model-building process, we generate B Bootstrap samples. In this paper, B is set to 1000. For each sample, we train an XGBoost model to obtain the predicted value yib̂ of 2̂ and the 𝑖th sample under 𝑏 Bootstrap models. Then, we calculate the model's variance 𝜎𝑦̂ regression mean 𝑦̂ as follows:

, (9)

2 using the data from the validation set. Next, we estimate the error variance σe (10) Finally, for a new observation 𝑖, we develop its (1 −α) × 100% prediction interval as:

(11) Here, 𝛼 represents the significance level. Since we are conducting an evaluation with a 95% confidence factor, 𝛼 is set to 0.05. 𝑡1−𝛼/2 is the critical value of the t-distribution with (B-1) degrees of freedom.

To assess the performance of this prediction interval, we use the Prediction Interval Cov- erage Probability (PICP), calculated as follows:

(12)

where ci = 1 when the actual value falls within the prediction interval, andci = 0 oth- erwise.

After 1000 rounds of Bootstrap-sample training, the PICP values of the dual-stage XGBoost model all exceed 0.95, validating the reliability of the confidence-interval estimation.

We conduct a visual analysis of the prediction interval, taking the gold-medal prediction of the 2020 Tokyo Olympics as an example.

Evidently, for countries with a relatively small number of medals per year, the probability that their actual results fall within the predicted confidence interval is markedly higher than that of Olympic powerhouses.

This phenomenon is attributed to the algorithmic features of the machine-learning model. When handling data points distant from the main sample distribution, the model tends to treat them as potential outliers, thereby moderately reducing the degree of fitting to these extreme situations.

Subsequently, we calculate the 𝑀4 values for the 2020 Tokyo Olympics and the 2024 Paris Olympics, as presented in the following table:

关注数学模型 Gold Model Silver Model Bronze Model 2020 Tokyo 72% 75% 71% 2024 Paris 82% 81% 78% The relatively high 𝑀4 values suggest that the model can reliably capture the underlying patterns of Olympic medal counts.

微信公众号：数学模型 Considering the sociological impact of the pandemic, the data for 2024 outperform those for 2021.

6.4 Application and Analysis of the Model for the 2028 Olympics

6.4.1 Prediction of Olympic Medal Counts and Confidence Intervals

Finally, we use the dataset from 1952 to 2024 to build the final dual-stage XGBoost pre- diction model and calculate the confidence interval with the non-parametric Bootstrap algo- rithm. The resulting table is presented below:

Sil- Bron- 95% CI Sil- 95% CI 微信号：MATHmodels Rank Team Gold Total 95% CI Gold ver ze ver Bronze 1 USA 45 48 49 142 [39.7, 51.0] [42.0, 54.0] [43.2, 55.0] 2 CHN 40 27 24 91 [35.0, 46.0] [23.0, 31.0] [20.0, 27.0] 3 JPN 20 12 13 45 [17.0, 23.0] [10.0, 14.0] [11.0, 15.0] 4 AUS 18 19 16 53 [15.0, 21.0] [16.0, 22.0] [13.0, 18.0] 5 FRA 16 26 22 64 [13.0, 18.0] [22.0, 30.0] [19.0, 25.0] By systematically comparing the actual results of the 2024 Olympics with the predicted results of the 2028 Olympics, we can observe the dynamic evolution of the Olympic competi- tive landscape, as the table shown below:

Increased Cases Decreased Cases REF USA ROM SRB AZE KOR KEN IRI BUL CUB 2024 1 126 9 5 7 32 11 12 7 9 2028 4 142 19 10 9 25 7 9 5 8 Dif. 3 16 10 5 2 -7 -4 -3 -2 -1

6.4.2 Quantitative Analysis of First-Medal-winning Probability

In the Dual-stage XGBoost model, we developed an accurate probability assessment mechanism to quantify the likelihood of small participating countries winning their first Olym- pic medal.

For countries classified as having no winning possibility by the classifier (𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑦(i) = 0), we directly assign a winning probability of 0. For countries classified as having winning potential (𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑦(i) = 1), we transform the probability based on the predicted value of the regressor. If the regression-predicted value is less than 1, it is directly taken as the winning probability. If the predicted value is greater than 1, we consider it a certain-winning event and set the probability to 100%. For any country 𝑖 that has never won an Olympic medal, the probability 𝑃(𝐹𝑖𝑟𝑠𝑡𝑀𝑒𝑑𝑎𝑙|𝑖) of winning its first Olympic medal is defined as:

(13)

Where 𝐶𝑙𝑎𝑠𝑠𝑖𝑓𝑦(𝑖)  reflects the binary-classification result of the classifier, and 𝑅𝑒𝑔𝑟𝑒𝑠𝑠𝑖𝑜𝑛(𝑖) represents the predicted value of the regressor.

Based on this framework, we set the winning-probability threshold at 0.2. When 𝑃(𝐹𝑖𝑟𝑠𝑡𝑀𝑒𝑑𝑎𝑙|𝑖) > 0.2, we consider the country to have significant potential to win medals in the next Olympics, as shown in table below:

NOC NGA EST LAT FIN VEN MNE KSA SYR PRY 0.76 0.48 0.45 0.44 0.40 0.35 0.28 0.25 0.20 𝑃(𝐹𝑖𝑟𝑠𝑡𝑀𝑒𝑑𝑎𝑙|𝑖)

6.5 Analysis of the Correlation between China-US Olympic Medals and

Events Based on SHAP Values

SHAP (Shapley Additive Explanations), a sophisticated machine-learning model interpre- tation tool, can effectively quantify the contribution of features to prediction results.

Given that the XGBoost model intrinsically supports the calculation and integration of SHAP values, this study opts to apply it to explore the underlying relationship between event settings and a country's medal attainment [11].

Taking the prediction of the 2028 Olympics as an instance, we performed a SHAP-value 𝑔𝑜𝑙𝑑 analysis of the number of gold medals 𝑀𝑒𝑑𝑎𝑙𝑖,𝑡,𝑠𝑝𝑜𝑟𝑡 that China and the United States are expected to win in each event:

Medals in China and the United States The SHAP value magnitude directly reflects the influence degree of a specific event on a

关注数学模型 country's gold-medal winning. For instance, the United States shows the largest SHAP value in the Athletics event, while China's SHAP value in this event is relatively small. This disparity indicates that the United States enjoys a significant competitive advantage in Athletics.

Conversely, in the Weightlifting and Diving events, China demonstrates significantly 微信公众号：数学模型 higher SHAP values than the United States, suggesting that these are China's traditional strong- suit events.

To gain a deeper understanding of how event settings affect different countries, we carried out a more meticulous study. We used the SHAP method to conduct a quantitative analysis of the silver-medal prediction models for the 2028 Olympics in China and the United States.Fig- ures below respectively present the waterfall plots of event contribution levels for the United States and China:

微信号：MATHmodels

We can observe from the SHAP-value distribution of the United States (Figure 6.6) that the Swimming and Athletics events make significant positive contributions, with their SHAP values markedly higher than those of other events.This distribution feature indicates that the United States retains a strong competitive edge in these traditional advantageous events.

Observing from the SHAP-value distribution of the United States, the Swimming and Athletics events exhibit significant positive contributions, with their SHAP values markedly higher than those of other events. This distribution feature reveals that the United States retains a strong competitive edge in these traditional strong-suit events.

In contrast, the SHAP-value distribution in China presents a distinct pattern.The Swim- ming and Shooting events exert the most significant positive influences, suggesting a strong positive correlation with China's silver-medal-winning probability. This reflects the crucial im- portance of these events for China to achieve excellent results.

A comparative analysis reveals significant differences in the composition of advantageous events among different countries, which directly impacts their overall Olympic performance. The historical performance and development potential of an event are mirrored in the predic- tion model through the SHAP-value magnitude.

However, a country's final Olympic achievements are related not only to its own advan- tageous event types but also, to a greater extent, to the total number of medals allocated to each event in the Olympics. For events with a relatively large number of total medals, a country's investment in the development of these events is more likely to boost its final medal count.

7 Model II: DID Regression Evaluating the Great Coach Effect

The “great coach” effect means that outstanding coaches can inspire the potential of teams or individuals through professional guidance, enabling them to surpass their limits and achieve remarkable results. Nevertheless, a country's medal count is influenced by multiple factors, including the host-country effect and athlete turnover.

7.1 Identifying Independent Variables

To precisely verify and quantify the great coach effect, we first identify the independent variables necessary for developing this model:

7.1.1 Calculation of medal scores

For each athlete's medal results, we convert medal types into numerical values using map- ping rules to facilitate subsequent statistical analysis. The specific mapping rules are as follows:

0, Medal𝑖= “𝑁𝑜 𝑀𝑒𝑑𝑒𝑙” 1, Medal𝑖= “𝐵𝑟𝑜𝑛𝑧𝑒” (14) Score𝑖= { 2, Medal𝑖= “𝑆𝑖𝑙𝑣𝑒𝑟” 3, Medal𝑖= “𝐺𝑜𝑙𝑑” These rules transform medal types into numerical values, facilitating quantitative pro- cessing. Subsequently, we group the data by year and calculate the total medal score TotalScore𝑦𝑒𝑎𝑟for each year:

𝑛 (15) TotalScore𝑦𝑒𝑎𝑟= ∑ Score𝑖 𝑖=1 Where 𝑖 represents the 𝑖 th athlete in that year, and 𝑛 is the total number of athletes competing that year. Using this approach, we can obtain the annual total medal score of the m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Chinese men's table-tennis team at the Olympics. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

7.1.2 Developion of the "Coaching Status" Variable

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m To assess the coaching impact of Coach Alyson Annan, following the developion of pre- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m vious variables, we define a new variable, "Coaching Status". This variable is determined based m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

on whether Alyson Annan coached the Chinese and Dutch women's hockey teams in a given year, as described by the following formulas:

For the Chinese women's hockey team, we define the variable 𝐶𝑜𝑎𝑐ℎ_𝐶ℎ𝑖𝑛𝑎:

𝐶𝑜𝑎𝑐ℎ_𝐶ℎ𝑖𝑛𝑎= {0, 𝑌𝑒𝑎𝑟< 2022 (16) 𝑌𝑒𝑎𝑟≥2022 1, For the Dutch women's hockey team, we define the variable 𝐶𝑜𝑎𝑐ℎ_𝑁𝑒𝑡ℎ𝑒𝑟𝑙𝑎𝑛𝑑𝑠:

0, 𝑌𝑒𝑎𝑟< 2015 2015≤𝑌𝑒𝑎𝑟< 2022 (17) 𝐶𝑜𝑎𝑐ℎ_𝑁𝑒𝑡ℎ𝑒𝑟𝑙𝑎𝑛𝑑𝑠= { 1, 0, 𝑌𝑒𝑎𝑟≥2022 Using these variables, we can partition the data into pre-coaching and post-coaching seg- ments, which will serve as the basis for subsequent hypothesis testing.

关注数学模型 微信公众号：数学模型 微信号：MATHmodels

Through these steps, we have processed the data on Chinese and Dutch women's hockey teams from 1988 to 2024 in the summerOly_athletes dataset. The processed data now includes the total medal scores and "Coaching Status" identifiers, providing the necessary data founda- tion for developing and analyzing a difference-in-differences model. This pre-processing step ensures data consistency and reliability, which is crucial for quantitatively evaluating the “great coach” effect.

7.2 DID Model Building

We have developed a linear regression model to investigate how the coaching change (whether Coach Alyson Annan is in charge) affects the medal scores of the Chinese and Dutch women's hockey teams. To achieve our research objective, we adopt the ordinary least squares (OLS) method, which effectively estimates the linear relationship between independent and dependent variables.

To quantify the impact of the coaching change on the medal count, we formulate the fol- lowing DID regression model:

(18) 𝑠𝑐𝑜𝑟𝑒𝑖= 𝛽0 + 𝛽1Coach𝑖+ 𝛽2Time𝑖+ 𝛽3Coach_Time𝑖+ 𝜖𝑖 Here, scorei represents the medal score of the Chinese or Dutch women's hockey team in year 𝑖. Coacℎi is a binary variable: 1 when Coach Alyson Annan is coaching, 0 otherwise, differentiating coaching and non-coaching periods. Timei is also binary, 1 after a predefined time node, 0 before, distinguishing post and pre-coaching change periods.

𝐶𝑜𝑎𝑐ℎ𝑖× 𝑇𝑖𝑚𝑒𝑖 , the interaction term of 𝐶𝑜𝑎𝑐ℎ𝑖 and 𝑇𝑖𝑚𝑒𝑖 , is the core of the DID model. Its coefficient 𝛽3 reflects the differential effect between coaching and non coaching periods before and after the coaching change, capturing the additional impact of Coach Alyson Annan's coaching on medal scores.

𝛽0 is the regression model's intercept, representing the medal score unaffected by Coach Alyson Annan's coaching. 𝛽1 and 𝛽2 are regression coefficients for the impacts of coaching change and post-node time on medal scores respectively. ϵi is the error term for unobservable m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m factors affecting medal scores, helping to determine time-period impacts.

The regression coefficient 𝛽3 is crucial for evaluating the great-coach effect. Its signifi- cance is determined by the t statistic and p value. If 𝑝< 0.05, the null hypothesis is rejected, indicating a significant impact on medal numbers. If 𝑝≥0.05, the null cannot be rejected, meaning no significant impact.

Based on regression results, we test the impacts of coaching, time, and their interaction on medal scores. A significant positive coefficient implies a positive correlation, otherwise a negative one. Using regression and DID, we quantify the "great coach" (Alyson Annan) effect on medal scores of Chinese and Dutch women's hockey. High statistical significance of 𝛽3 supports the “great coach” effect.

7.3 Solution of the Model

Based on the results of the Ordinary Least Squares (OLS) regression analysis, the model successfully quantified the impact of the "Great Coach" (Coach Alyson Annan) effect on the medal scores of the Chinese and Dutch women's hockey programs. Through regression model analysis, we evaluated the relationship between Coach Alyson Annan's coaching and the num- ber of medals, obtaining the following regression coefficients and statistics.

𝑅2 Team 𝛽3 𝑡 𝑝 𝛽0 9.556 2.45 0.03 0.92 China 5.33 Dutch 4.875 2.131 0.05 0.83 28.37 The regression analysis results reveal that Coach Alyson Annan's coaching significantly influences the medal scores of both the Chinese and Dutch women's hockey teams. The change in coaching by Coach Alyson Annan has significantly boosted the medal scores. Specifically, the Chinese women's hockey team's medal score has increased by an average of 9.556 points, and the Dutch women's hockey team's has increased by an average of 4.875 points.

This conclusion suggests that the “great coach” effect plays a crucial role in the perfor- mance of the Chinese and Dutch women's hockey teams. The regression coefficients and their significance strongly support investment in coaching, especially in terms of coaching-resource allocation and strategic decision-making. Based on this analysis, when other countries recruit top-level coaches, they can predict the return on coaching investment based on this effect and make corresponding strategic arrangements.

7.3.1 Investment Analysis of Excellent Coaches

m m m m m m m m m m m m m m m m m m m m m m By analyzing the data from 2000 to 2024, we screened out the data of women's hockey m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m teams from different countries and counted the scores of each year according to country and m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m year. To draw more representative conclusions, we calculated the average annual score for each m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m country and ranked them accordingly. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m We set two-fold screening criteria. First, a country should have shown unsatisfactory per- m m m m m m m m m m m m m m m m m m m m m m m m m

formance in the women's hockey event in the last two Olympic Games. Second, it should have demonstrated excellent overall performance from 2000 to 2024, measured by the average an- nual score. Based on these criteria, we selected the top three countries with the highest average annual scores to determine the priority targets for coach investment.

After data processing, we found that the countries meeting the screening criteria were

关注数学模型 Australia, Great Britain, and Germany. These countries had an outstanding overall perfor- mance in the women's hockey event from 2000 to 2024, yet their performance in the last two Olympics was poor. This indicates that they possess a solid foundation and potential in this sport, perhaps only lacking a "great coach" to unlock their potential.

Therefore, for the coach-investment strategies in these countries, we recommend focusing on the women's hockey event, with the aim of significantly enhancing medal-winning perfor- 微信公众号：数学模型 mance based on the existing good foundation.

7.3.2 Impacts of Excellent Coach Investment

To quantify the return on coach investment, we'll, based on the previous analysis frame- work, predict the returns of coach investment in different countries, providing a reference for future coach-resource allocation. We'll analyze the medal performance of women's hockey in various countries to predict the potential impact of great-coach investment on medal-count growth.

1. Definition of Medal Benchmark Score

The benchmark score is the average score calculated above, defined as ccountry.

微信号：MATHmodels

2. Adjustment Coefficient

During Coach Alyson Annan's non-coaching period, assume the average medal score of a reference women's hockey team is c𝑐𝑜𝑢𝑛𝑡𝑟𝑦 . We calculate the adjustment coefficient 𝑎𝑑𝑗𝑢𝑠𝑡𝑚𝑒𝑛𝑡 for each investing country by computing the ratio of its average medal score c𝑐𝑜𝑢𝑛𝑡𝑟𝑦 to that of the reference team. The formula is:

𝑎𝑑𝑗𝑢𝑠𝑡𝑚𝑒𝑛𝑡= c𝑐𝑜𝑢𝑛𝑡𝑟𝑦 (19) 𝑐𝑟𝑒𝑓𝑒𝑟𝑒𝑛𝑐𝑒 This adjustment coefficient reflects each country's medal performance relative to the ref- erence team under the same conditions. The larger the coefficient, the more competitive the country is under similar circumstances.

3. Prediction of Medal Score Increase

We calculate the predicted medal-increase value for each country after coach investment by multiplying the adjustment coefficient by the effect value 𝛽3 of Coach Alyson Annan. The formula is:

(20) 𝑃𝐼𝑐𝑜𝑢𝑛𝑡𝑖 = 𝑎𝑑𝑗𝑢𝑠𝑡𝑚𝑒𝑛𝑡𝑖× 𝛽3 Here, 𝑃𝐼𝑐𝑜𝑢𝑛𝑡𝑖 represents the predicted medal-increase value for the 𝑖th country after investing in an excellent coach.

4. Prediction of Final Medal Score

Finally, we obtain the predicted medal score by adding the predicted medal-score increase value to the benchmark medal score of each country. The formula is:

𝑃𝑐𝑜𝑢𝑛𝑡𝑖= 𝑐𝑐𝑜𝑢𝑛𝑡𝑟𝑦+ 𝑃𝐼𝑐𝑜𝑢𝑛𝑡𝑖 (21) This value represents the medal score a country may reach after coach investment, assum- ing the effect of Coach Alyson Annan. Based on these calculations, we get the prediction results.

The final prediction results are as follows:

Great Australia Great Britain Germany Year Australia Germany Britain Predicted Predicted Predicted

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 1984 0 0.0 0.0 11.8 8.3 7.7 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

1988 48 0.0 0.0 58.5 6.6 7.7 1992 0 16.0 32.0 10.9 22.5 39.6 1996 48 0.0 0.0 57.9 9.0 11.2 2000 48 0.0 0.0 66.0 11.3 7.3 2004 0 0.0 48.0 11.9 7.6 57.3 2008 0 0.0 0.0 11.8 6.4 6.5 2012 0 16.0 0.0 10.1 23.7 10.5 2016 0 48.0 17.0 10.0 56.6 29.1 2020 0 18.0 0.0 9.6 28.6 9.2 2024 0 0.0 0.0 9.6 15.9 7.4 The British women's hockey team has had a mediocre track record in the past, often rank- ing in the lower-middle positions in international competitions. With the new coach on board, the team has demonstrated a clear upward trend, and we anticipate a significant rise in its medal-winning rate in various future events.

Australia, a traditional powerhouse, achieved an outstanding five-consecutive-champion- ship feat in the 1990s and claimed gold medals in numerous Olympic Games. Despite signifi- cant performance fluctuations in recent years, under the new coach's guidance, we expect the number of medals it wins to increase steadily. However, as the team already has a well-estab- lished system, it will take time for the new and old coaching concepts to be harmonized.

The German team has long struggled with performance instability. Even after the new coach took over, this situation has not seen fundamental improvement. This suggests that the team may be facing profound challenges in areas such as player selection and tactics, and it will be difficult for the coach alone to overcome these bottlenecks in the short term.

8 Novel Insights from SHAP Analysis in Olympic Performance

SHAP values provide a sophisticated framework for model interpretation through SHAP Summary Plots. These plots offer two complementary visualization approaches to demonstrate feature impacts on model predictions [12]: feature importance ranking and feature effect sum- mary:

关注数学模型 微信公众号：数学模型 微信号：MATHmodels

The SHAP Summary Plot reveals intricate patterns of feature influence through point dis- tribution and color coding, illustrating both the direction and magnitude of feature effects on prediction outcomes. For instance, in the case of country_Athletics, the concentration of yellow points (indicating high participation) in the positive SHAP value region demonstrates a strong positive correlation between high participation in athletics and improved medal predictions.

The bar chart component displays mean absolute SHAP values, quantifying each feature's overall importance to prediction outcomes. Total participation emerges as the dominant factor, exhibiting the highest SHAP value and confirming its critical role in Olympic medal acquisition. Following closely are country_Athletics and country_Swimming, validating these disciplines' fundamental importance in Olympic competition.

Based on these SHAP analyses, we propose a dual-track approach to optimizing Olympic competitive strategies. The first track involves maintaining competitiveness in traditional strength events while strategically expanding participation scales. The second track emphasizes data-driven identification and development of emerging events with potential competitive ad- vantages. This quantitative approach to strategy optimization not only enhances performance in individual events but also promotes balanced development of national Olympic capabilities.

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

9 Sensitivity Analysis

In the model-building process, when performing a sensitivity analysis of XGBoost's hy- perparameters, the max_depth parameter is selected as a crucial factor in controlling the com- plexity of the decision tree.

40 max_depth=4 (default) max_depth=3 Gold Medal Number 30 max_depth=6 max_depth=9 20

10

0

20 40 60 80 0

max_depth directly determines the tree's depth, thereby influencing the model's capacity to learn data features and its generalization ability. A large value of max_depth tends to result in over-fitting, while a small value may lead to under-fitting. Based on the results presented in the line chart, the prediction curves for different max_depth values exhibit significant discrep- ancies.

With an initial setting of max_depth = 4, the model's prediction results are at a certain level. When max_depth is decreased to 3, the prediction curve experiences an increased fluc- tuation range, suggesting heightened instability in the predicted values. When max_depth is set to 6, the prediction curve remains relatively stable, indicating that the model performs stably at this point. When max_depth = 9, the prediction curve shows a substantial upward trend in the later phase.

These results demonstrate that the choice of the max_depth hyperparameter significantly impacts the accuracy and stability of the model's gold-medal-count prediction. In practical ap- plications, it is essential to finely tune this parameter according to the dataset characteristics and model performance metrics to optimize the model's performance.

10 Model Evaluation

10.1 Strengths

1. Model innovation: The dual-staged XGBoost model combines classifiers and regres-

sors, enhancing the accuracy of medal predictions.

f  st do so-dd at  ss ds ssd at amosns ts ensure data quality.

关注数学模型 3. Comprehensive model evaluation: Various evaluation indicators are adopted to com- prehensively measure the performance of the dual-stage XGBoost model and display its pre- diction effects from multiple dimensions.

4. In-depth variable analysis: Variables are analyzed and quantified in detail, and SHAP values are used to analyze the influence of events on medal acquisition in China and the US, exploring variable relationships and providing a basis for practical applications.

10.2 Weaknesses

1.  There is a lack of exploration of the impact of more factors on medal performance.

2.  The model for the "coaching effect" can be further optimized.

微信公众号：数学模型
