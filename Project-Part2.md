# Group Project, part 2

## Rules
1. To be delivered until March 12, 23:59.
1. The submission will be a link to a git repository.
1. The final delivery is 3/4 of the total grade of the project.

---
## Scenario (continuation)

Your company is participating in a two-day hackathon promoted to study the mobility of bicycle users . They send your group, the best team of Data Scientists in the company's roster. By promoting cycling awareness, your company expects to contribute to the green transition.

You spent the first day doing the most important task a Data-Scientist can do: understanding the data. You now need to finalise your report on the challenge and polish it. As you know your project might be picked up for an analysis presentation, you add a very brief introduction about your group on the README.md file. Be sure to add your name and your e-mail. It is time to add more features to the class so you can present the analysis in the showcase notebook.

## Goal

The goal of the project is now to analyse which month has the most bike rentals.

During a meeting at the beginning of day 2 you decide the steps before the final delivery:

### Day 2, Phase 1

- [ ] Make a list of all the packages you used. Create a conda environment that has all that packages. Export the conda environment into a configuration file and add it to git, so someone who clones your repo can figure out the dependencies.
- [ ] Enforce that you are documenting your modules, your classes, and your functions/methods.

### Day 2, Phase 2

- [ ] Change the method you are using to read the dataframe to convert the dataframe index to hold daily datetime information.
- [ ] Change the __plot()__ method of the class you already developed to be compatible with the changes.

### Day 2, Phase 3

- [ ] Add a method to the class that plots the average total rentals by month of the year. You decide the name, just make sure you add it to the Class' documentation.
- [ ] The method should plot a barchart where the x-axis is the month and the y-axis is the total average rentals. For example, for January: 0.5*(sum(January 2011) + sum(January 2012)). 

### Day 2, Phase 4

Add a __forecast()__ method to the class.

- [ ] The forecast method receives only one argument. The user can only selct Month, either as a Month number (int) or as a string. Be sure to document how you implement it.
- [ ] Select all days from the dataframe corresponding to the input description and create an "Average" and "Standard Deviation" arrays for the hours of an entire week. You now have to force a Monday-Sunday analysis (weekday 0-6).
- [ ] The __forecast()__ method should then plot a 168-hour period (a Mon-Sun week) corresponding to the average rental with a shaded area corresponding to an interval of [-1 std deviation, +1 std deviation.]. The title of the plot should be something like "Expected weekly rentals in June" if the selected month is June.

<div class="alert alert-warning">
    <b> Make sure you document all modules, functions, and classes. At this point, pylint should not complain. </b>
</div>

### Day 2, Phase 5

- [ ] Change the "showcase notebook". Import your __Class__ and showcase all the methods (both from day 1 and day 2) you developed. Tell a story about your analysis and findings in the showcase notebook. Make a statement about when bicycle rental is more frequent and when it is rarer. State in which month should more bicycles be available, based of you observations.

At this point it is best to double-check if ALL the packages in your current conda environment were added to the exported file you have on github.

<div class="alert alert-danger">
    <b> REMEMBER: IT IS OK TO PROTOTYPE CODE IN NOTEBOOKS, BUT THE FINAL CLASS MUST BE IN A SINGLE .py FILE! </b>
    <br>
    <b> The final delivery of the project is the "showcase" notebook from Day 2, Phase 4. Don't place this notebook together with prototyping notebooks.</b>
    <br>
    <b> We will only consider contents in your "master" repository.</b>
</div>

## Debriefing

At the end of the coding session, meet with your colleagues and discuss what you developed during the project. This is a collaborative project. It is not mandatory you know the exact details of every single aspect of the project, but it is important the final result has consensus among you.

## Delivery

Send the gitlab link of your repository by e-mail to "luis.guimarais at novasbe.pt" and "claudio.vieira at novasbe.pt".  
We will __push__ the contents of the repo, to reflect the updates you performed.
We will then create the conda environment, and run the notebook in the environment you have defined.

## Grading

The project has two deliveries. There are __10__ checkable items in both Delivery 1 and 2. The 10 checkable items in Delivery 1 each account for 0.5/20 for a maximum project grade of 5/20. You will have the chance to correct them during Delivery 2 __but you need to list the corrections (see below)__. Each of the chackable items in Delivery 2 accounts for 1.5/20, for a maximum project grade of 15/20.

### Listing Corrections

Add a "CHANGELOG" file to git on GitLab and add it to your project.

<img src="../Figures/changelog.png">

Write a short comment about the changes you made betwee the first delivery and the second delivery so you can be re-graded.  
