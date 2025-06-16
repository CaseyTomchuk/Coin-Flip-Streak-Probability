This was a project from the book "Automate the Boring Stuff with Python." I enjoyed working with probability in this project.

How it works:
If you flip a coin 100 times, there is around an 80% probability that there is a streak of at least 6 heads or at least 6 tails. This code runs that experiment 10,000 times, printing the number of times an experiment had a streak and the probability of a streak occuring.

Once I implemented the probability calculator element, I found that I was getting a percent around 160%. I failed to properly reset the coinList and streakChecker. The if statement that involves streakChecker had conditions that reset the checker, but wouldn't properly reset if a 'partial streak' (for example a streak of 4) was found, so a streak could continue into the next iteration of the experiment. The code was counting streaks across the entire sample, rather than checking if there was a streak in an individual experiment.
