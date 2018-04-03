'''
problem:
Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.
ref: https://www.hackerrank.com/challenges/full-score/problem
'''


select hackers.hacker_id, hackers.name 
    from submissions 
    join challenges 
        on submissions.challenge_id = challenges.challenge_id 
    join difficulty
        on challenges.difficulty_level = difficulty.difficulty_level
    join hackers 
        on submissions.hacker_id = hackers.hacker_id 
    where submissions.score = difficulty.score 
        and difficulty.difficulty_level = challenges.difficulty_level 
    group by hackers.hacker_id, hackers.name 
        having count(*)>1 
    order by count(*) desc, hackers.hacker_id;
