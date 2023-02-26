Problem Statement 12

Subject: Text Processing

Problem Statement: Given a text file, find if any URL is present in the text file or not, if present extract first occurrence.
Ans: code in link_from_text file
explanation:
step1: I import re(regular expression ) module.
step2: taking input for the location of text file from the user.
step3:open the file in read mode using "with open function" and read the content of the file.
step4: then i use regular expression to check if there is a url present in the given text file.
step5:then i use a list(url_matches) that store all url that are present in the text.
step6:if the length of list(url_matches) is greater than 0 it will print number of urls and first occurences of url else return 0;

-----------------------------------------------------------------------


