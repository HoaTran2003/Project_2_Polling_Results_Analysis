# Project_2_Polling_Results_Analysis

PROJECT 2 REPORT

I. Introduction: 

The main goal of this project is to investigate whether a small poll sample will affect the outcoming result when considering the bigger picture. That is to say that this also helps to find out how reliably large a poll sample must be in able to represent an entire population. The reason behind for this is there are many confounding factors that can influence a poll’s result, meaning that it is much harder to apply the results of a sample to an entire population. Moreover, the aforementioned problem also includes the idea of random sampling and margin of error which serves as a basic introduction to data analytics. With this, one will have more experience and a more holistic perspective in how to utilize computational problem solving with data analytics. 

II. Methods: 
1. Explaining the algorithm: 
- For the first section, the goal is to simulate the results of a random poll. The idea is that we know beforehand a certain percentage of the population will say yes ( in this case it is 30%). Therefore, we iterate the number of people that are being surveyed in this poll and count the one who said yes with a probability equal to said percentage ( in this case it is 0.3). After we are done counting, we will be able to know the poll result by divide the number of people who said yes with the total number of people in this poll (poll size).
- For the second section, we want to know the variation in the polling results in the first section. In order to accomplish this task, we must calculate the number of people who said yes with many trials. After that, we return the highest and lowest percentage of people who said yes in those trials. With the result, we can see how varied the poll results are. 
- For the third part, we want to plot the low- and high-end percentage of people who said yes in the same graph with the poll size. To do this, we want to know the lowest and highest percentage of people who said yes after each trial (results taken from the second part) and plot them with the increasing poll size (from minimum to maximum poll size). The purpose of this is to find the sufficient poll size that can be used to predict a larger population. Moreover, we also want to know the margin of error and we could calculate based on the formula. 
- For the fourth part, we want to plot the margin of error and actual percentage to see if they are related or not. We want to take the calculations of margin of error from the formula above and calculate it. Then we graph each margin of error in accordance with the actual percentage ranging from minimum percentage to maximum percentage. The end result should be a plot with margin of error on the y axis and the actual percentage on the x-axis.  

2. Algorithm implementation: 
Our program has four functions: poll(), main(), pollExtremes(), plotResults(), and plotErrors(). 

The poll function takes percentage, a float value, and pollSize, an integer value, as its parameter. In this function, we will calculate the actual percentage of people who said yes and return it. To do so, we first initialize count before the for loop so that we could increment it by one. This is used to calculate the number of people who said yes. For the for loop, we take pollSize as the range and inside it, we assign a as a random number between 1 and 100 using the random function. If a is smaller than percentage (30), the we increment count by 1. After the condition for the if statement is false, we end the for loop and return the value of actual percentage by the following formula: (count/pollSize)*100. 

The  pollExtremes function takes percentage, pollSize, trials as its parameter, all of which are integer value except for percentage since it is a float value. The main goal of the function is to return the min and max value of pollResults(a list we initialize inside this function) by using the min and max functions. To accomplish this task, we use a for loop in range of the value of trials. For each iteration, we call the result of the previous function poll(percentage, pollSize) and named the result pollres. After that, we append the value of pollres to the pollResults list. When the loop finishes, we should be able to find the min and max value of the pollResult list. 

The plotResults function takes percentage, minPollSize, maxPollSize, step, trials as its parameter, all of which are all integer value except for percentage since it is a float value. This function aims to call the results of the pollExtremes function and plot the different iterations of min and max on the plot at various different poll size ranginging from minPollSize to maxPollSize. To do this, we create three lists for each of the tasks required: a list for high percentage, low percentage and for the pollSize. After that, we create a for loop in range from minPollSize to maxPollSize + step with an increment of step. In this loop, we call the results of pollExtremes by the following order: low and high. This means that we call the min value and max value of the pollResult list and named it low and high. In each iteration of the for loop, we append the value of low and high to their respective list as well as the value of poll size ( named size in the for loop) to its list. When the loop is done, we graph these values on a plot. The end result should be a complete plot with poll size on the x-axis and percentage on the y-axis with two curves for low and high percentage. 

The plotErrors function take pollSize, minPercentage, maxPercentage, step, trials as its parameter. This function is used to graph the margin of error and the actual percentages to see the relations between them. To do this, we create two lists for margin of error and actual percentage. After that, we implement a for loop in the range of minPercentage and maxPercentage with step increment. For each iteration, we call the results of the pollExtremes function similar to what we did in the plotResults function. Then, we calculate the margin of error based on the given formula. Next, we append these values to their appropriate list so that we could plot them afterwards. When the loop is done, the two lists should have all of their required values so that in the end, a complete plot is created. The end result should be a graph showing the margin of errors on the y-axis and the actual percentage on the x-axis. We also call this function outside of the main function. 
The main function is where the program begins. It is used to call plotResults function so that it could operate properly. 

III. Results and conclusion: 

[](https://github.com/HoaTran2003/Project_2_Polling_Results_Analysis/blob/main/pol_size_per.png)

For a relatively small poll size of 1000, in 100 trials, we could see the changes in the high and low percentage in the graph above. The most noticeable trend is that when the poll number is below 200, the difference in the low and high percentage is significance. However, as the poll size increases, so does the difference between the two percentages. This means that as there are more people, the actual percentage of those who said yes, in the low and high end, increase to nearly 30%. The margin of error for this poll size is approximately + 3.85%, which is a relatively acceptable number. With this in mind, we could think of increasing the number to reduce the margin of errors to make it more reliable to apply the results to a larger population. 

[](https://github.com/HoaTran2003/Project_2_Polling_Results_Analysis/blob/main/images_projects_2.jpg)
 
In the same number of trials, if the poll size is 3000, the same trend for the two percentages can clearly be seen in the graph above. Both curve are approaching 30%, however, with a larger poll size, the two curves are nearer to the 30% mark compared to the previous graph (the one with 1000 people). The margin of error for this poll is + 2.25%, which is a really good number. This makes the results of the given poll more reliable compared to the previous one as there are less errors involved and both polls are surveyed with the same random sampling method. 
==> Therefore, if we want to balance a low margin of error with the labor involved in polling more people, a poll size of 3000 people would be reasonably acceptable as the margin of error of 2.25 is relatively low so we are more confident in the results. Although we know that by increasing the poll size to, let us say 5000 or even 10000 will produce a lower margin of error and make our results even more trustworthy, the challenges of polling so many people could be a great deterrent. This means that if we poll a large number of people, there could be many human factors involved which could affect our end results. 

 [](https://github.com/HoaTran2003/Project_2_Polling_Results_Analysis/blob/main/margin_error.jpg)

The above graph shows that for some cases, lower percentage seems to have a lower margin of error. However, this is not the overall trend as there are lots of fluctuations in between the margin of errors and the actual percentage. It also depicts that around the 60%, 68% and 77% mark, the margin of error are relatively low for such high percentages. There is also some high margin of error values for lower percentages, such as for 30%, the margin of error is around 3.5. All of this means that there are lots of variations in the relationship between these two values and no clear trend can be inferred from this graph. 
==> With this in mind, my answer from the previous sections would not change due to the drastic difference in the margin of errors for different value of actual percentage.

IV. Conclusion
In conclusion, we encounter some problems regarding the process of implementing the algorithm as the problem of recreating the 0.3 probability was quite challenging. Moreover, interpreting the two graphs has also deepened my knowledge in terms of how to interpret the results of random sampling. The project overall has given us a more holistic perspective in how to interpret polling results and how to comprehend margin of error. 
