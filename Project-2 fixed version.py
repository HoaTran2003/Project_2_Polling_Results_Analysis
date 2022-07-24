
"""
Created on Monday Feb 28 18:26:37 2022

@author: Hoa Tran

Project_2: Polling Analysis
"""

"Part 1:"

import random


def poll(percentage, pollSize): 
    
    '''
Parameters:
    percentage: the given percentage (between 0 and 100) will respond "yes"
    pollSize: the polling of individuals from a large population
Function is used to stimluate the polling process

Return value: the acutal percentage that actually said yes
    '''

    count = 0 #set the count variable to 0
    for i in range(pollSize): # the for loop function is used to repeat the assigned block of code a pollSize number of times
        a = random.randrange(0,101) #set the a variable to a random number from 0 fo 100

        if a<=percentage: #set the condition that the value of a is equal or less than the value of the percentage

            count = count+1 #if the condition is true, one will be added to the count variable

    return (count/pollSize)*100 #return the result acutal percentage (of the number of count divided by the poll size and then time 100)

    
"Part 2:"

def pollExtremes(percentage, pollSize, trials):
    '''
Parameters:
    percentage: the given percentage (between 0 and 100) will respond "yes"
    pollSize: the polling of individuals from a large population
    trials: the number of time that we call the poll() function

This function is used to build a list of poll results by calling the poll() 
function multiple times to investigate how much variation there can be in a 
poll of particular size by returning the minimum and maximu percentages in 
this list

Return value: the min and max value of the poll result
    '''
    pollResults = [] #List of poll results
    for k in range(trials): #for loop function is used to repeat the assigned block of code trials number of time
        pollres = poll(percentage, pollSize) #set the pollres variable to the value that the poll() function returns
        pollResults.append(pollres) #Assign value to the list of poll results
    return min(pollResults), max(pollResults) #return the min and max of the poll results


"Part 3"
import matplotlib.pyplot as mpl

def plotResults(percentage, minPollSize, maxPollSize, step, trials):
    
    '''
Parameters:
    percentage: the given percentage (between 0 and 100) will respond "yes"
    minPollSize: the minimum value of the poll size
    maxPollSize: the maximum value of the poll size
    step: the number of steps
    trials: the number of time that we call the poll() function
This function is used to plot the low and high percentage of poll results 
and return the value of margin of error
Return value: Margin of error
    '''
    
    lowpercent=[] #list of the values on the low end
    highpercent=[] # list of the values on the high end
    pollsize_list=[] # list of the poll sizes
    
    for size in range(minPollSize, maxPollSize+step, step): # repeat the assigned block of code the number of time between the min and max of the poll size with the number of steps the same as the value of step 
        low, high = pollExtremes(percentage,size,trials) #call and assign the pollExtremes() function to the low and high variables
        lowpercent.append(low) #assign value to the list of values on the low end
        highpercent.append(high) #assign value to the list of values on the high end
        pollsize_list.append(size) #Assign value to the list of poll sizes

    
    mpl.plot(pollsize_list,lowpercent, label = "Low percent")  #plot the low percentage
    mpl.plot(pollsize_list,highpercent, label = "High percent") #plot the high percentage
    mpl.legend(loc = "center left") 
    mpl.xlabel("Poll Size")
    mpl.ylabel("Percentage")
    mpl.show()
    margin_error=(high-low)/2 #calculate the margin of error and then assign it to a variable
    return margin_error
def main():
    plotResults(30, 10, 1000, 10,100)
    print(plotResults(30, 10, 1000, 10,100))
main()


"Part 4:"
import matplotlib.pyplot as pyplot

def plotErrors(pollSize, minPercentage, maxPercentage, step, trials):
    '''
Parameters:
    pollSize: the polling of individuals from a large population
    minPercentage: the minimum value of percentage
    maxPercentage: the maximum value of percentage
    step: the number of steps
    trials: the number of time that we call the poll() function
This function is used to plot the margin of errors as well as the actual percentages,
ranging from minPercentage to maxPercentage in increment of steps.
Return value: None
    '''
    percent_list=[] #Create a list of percentage
    margin_error_list=[] #Create a list of margin error
    for p in range(minPercentage, maxPercentage+1, step): # repeat the assigned block of code the number of time between the min and max of the percentage with the number of steps the same as the value of step 
        low,high=pollExtremes(p,pollSize,trials) #assign value to the low and high variable by calling the pollExtremes() function
        margin_error=(high-low)/2 #calculate the margin of error
        percent_list.append(p) #Assign value to the list of percentage
        margin_error_list.append(margin_error) #Assign value to the list of margin error
    pyplot.plot(percent_list,margin_error_list, label = "Margin of error")  #plot the margin of error
     
    
    pyplot.xlabel("Percentage")
    pyplot.ylabel("Margin of error")
    pyplot.show()


plotErrors(1000,10,80,1, 100)





