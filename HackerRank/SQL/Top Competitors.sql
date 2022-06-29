select hackers.hacker_id, hackers.name
from hackers
join submissions
on hackers.hacker_id = submissions.hacker_id
join challenges
on submissions.challenge_id = challenges.challenge_id
join difficulty
on challenges.difficulty_level = difficulty.difficulty_level
where difficulty.score = submissions.score
group by hackers.hacker_id, hackers.name
having count(*) > 1
order by count(*) desc, hackers.hacker_id asc
