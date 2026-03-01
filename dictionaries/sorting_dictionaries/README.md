Docstring for dictionaries.sorting_dictionaries
Student lists
Report a typo

We have a dictionary called student_list that represents the enrollment of students in various subjects at a small school. In this dictionary, the keys are subject names, and the values are lists of students taking each subject.

Your task is to print the name of the most popular subject. The most popular subject is the one with the highest number of enrolled students.

For example, given the following student_list:

student_list = {
    "English": ['Tim', 'Carl', 'Dean', 'Jane'],
    "Maths": ['Jane', 'Mike', 'Ann', 'Kate', 'Nick', 'Jenny'],
    "Chemistry": ['Tim', 'Carl', 'Dean']
}

Your program should output:

Maths

since Maths has the highest number of students (6) compared to the other subjects. Note that this is a synthetic example and your code will be tested with a different student_list.
Hint by
Zhijie Li avatar
Zhijie Li
If you are one true beginner for operator itemgetter or lambda effected on dictionaries , and tried almost everything thing you could, try my walkround mind:1. Create a same another dictionary with student_list (using dict(list_tobe_dict)) for transformation2. Transform the complex structure to a easy one from your new copy dictionary, using(for...in...,new value=len(..))3. Then you got a easy dictionary with {"subject1": 3, "subject2":2.....}4. Sorted it or using Max() or any one of ways mentioned in Theory article5. Print out the only SUBJECT6. After you passed, go Solutions section to get a formal or perfect solution coding style about Itemgetter and lambda from other people. Try to create a really easy and simple test data by yourself to troubleshooting LOCALLY,  when you are blinding in Failure Feedback, is a good step towards the final stage. Good luck!