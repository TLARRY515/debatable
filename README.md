# debatable
"It's just words, folks, just words"

A suite of analytic and visual features to examine the language used in the 2016 presidential debates

# aims
The primary aim of this mini-project is to create a scalable set of analytical methods to quickly visualize differences in candidates' language. Although the project is public, I expect many of the initial members, including myself, will have varying degrees of experience with coding and varying comfortability in working in coding teams. For at least the first few of us, this will be undertaken as a learning process; any outcome beyond this experience (such as an infographic?) will be added bonus.

# approach
Both the data set and the code required for this project are relatively small. Still, it will be good practice to break up functionality by team members based on their skills and be mindful of the reusability of this code for future debates and conversations more generally in the future. My first set of questions for the debate include the following:

1. How do the vocabularies of each candidate compare?
2. Who speaks more? Who interrupts more?
3. What is being repeated by each candidate? On what issues do they tend to focus?
4. Do elements of their responses match elements of the questions?
5. Do differences in results from each of these categories correlate with differences in the polls?

Undoubtedly, we will come up with more questions to explore as we get to work, and I invite every member to explore their own questions and contribute to our working hypotheses.

# functions
First, it will be important to organize the responses by candidate and eliminate articles (a, an, the)
Second, we will need a way to consolidate repetitions of root words used in different forms (people/person)

Once we get this foundation, we can start looking at each of the above questions more specifically by quanitfying for each candidate average word length, quantity of unique words, and the frequency of key words. The above methods should all have out-of-the-box visualizations generated from textual input.

From there, more difficult analyses can evaluate sentiment or relate debate data with data in the polls. This is where the most interesting conclusions can be drawn, but these initial functions should be the focus before the third and final debate.
