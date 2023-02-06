-- this is not correct decision
select
		rank() over (order by problem_count desc, submitted_at) rank,
		user_id,
        name user_name,
        problem_count,
        submitted_at latest_successful_submitted_at
from
  (select  user_id,
   		  name,
          problem_id,
          success,
          SUM(case when success then 1 else 0 end) OVER(partition by user_id, problem_id) problem_count,
          case when success then max(submitted_at) else null end submitted_at
  from
        (select  user_id, users.name, problem_id, success, min(submitted_at) submitted_at  from submissions
        join problems on submissions.problem_id = problems.id
        join users on submissions.user_id = users.id
        where  contest_id in (select max(contest_id) from problems)
        group by user_id, problem_id, success, name) t
  group by user_id, problem_id, success, name) t2
  where success or problem_count = 0