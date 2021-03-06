# AssociationRuleMining
Association Rule Mining for IS392. 

Association Rule Mining is a very important problem in web mining. Given a set of records, it can find rules that will predict the occurrence of an item based on the occurrences of other items in the records.

Given a set of items I = {I1,I2,…,Im} and a database of transactions D = {t1,t2, …, tn} where ti={Ii1,Ii2, …, Iik} and Iij is an item in I, the Association Rule Mining Problem is to identify all association rules X => Y with a minimum support and confidence.

If a document is considered as a record, and the terms or words in the document are considered as items, association rule mining can be used to predict the occurrence of a word based on the occurrences of other words in the document.  For example, it can generate the association rule like {'information', 'retrieval'} => {'search'} with support =0.6 and confidence =0.65. The rule means the probability of the three words co-occur with each other is 0.6, and the probability that the word 'search' occurs in a document given 'information' and 'retrieval' both occur in that document is 0.65.

In this assignment, your program should produce associate rules, from the documents you crawled in assignment #2, using the two-step approach described on page 22 in this file:

http://njit2.mrooms.net/pluginfile.php/383024/mod_folder/content/0/IS392_2016_WebMining.pptx 

You need to discover all rules having support ≥ minsup and confidence ≥ minconf thresholds.  Play with different thresholds and examine results produced by different thresholds.  (If you cannot generate any associate rules, please reduce the thresholds.) 

Here is another document which describes the algorithm for association rule mining: http://www-users.cs.umn.edu/~kumar/dmbook/ch6.pdf

The first step of association rule mining is to generate the frequent itemsets. In this step, you will need to use the index file you have created for assignment #3. From the index file, you can easily identify the number of documents in which a term occurs. Then you can use the document frequency information to determine which of the 1-itemsets are frequent.

Input:

1. 500 downloaded pages from Assignment #2,

2. The index file generated from Assignment #3,

3. 20 related terms (10 terms you picked for Assignment #2 Crawler, plus 10 additional terms newly picked for this assignment.)

If you did not complete either assignment 2 or 3, you can choose to use the attached dataset posted on Moodle under the assignment description. However you will lose 20% of points for this assignment.

Output:  Association Rules stored in a plain text file. The format should like this:

{term1, term2} => {term 3}; support=0.5, confidence=0.5

{term5, term7} => {term 2}; support=0.7, confidence=0.56

For this assignment, the requirement has been reduced so that: the association rules only need to cover the 20 related terms AND the right-hand side of each association rule only needs to have 1 term. That is to say, the rules are used to predict the occurrence of one word based on the occurrences of other words in the document.

Report:

Part 1. How the program was developed (programming language used, and major functions);

Part 2. How many Association Rules were generated given a specified minsup and minconf value (play with a few sets of thresholds).

Part 3: Discuss the relationship between the thresholds and the number and quality of resultant association rules. 

 Part 4: Finally, list the top 10 association rules with their support and confidence value in decreasing order. 

Deliverables: a zip file containing 1. source code, and 2. report

Presentation: The assignment is due on April 15. On April 18, you will be required to demo your program, show the outputs, and explain the codes in class. 
