select * from
(select users.*,
	case when t1.solved_at_least_one_contest_count is null then 0 else t1.solved_at_least_one_contest_count end solved_at_least_one_contest_count,
    case when t2.take_part_contest_count is null then 0 else t2.take_part_contest_count end take_part_contest_count from users
left join
  (select user_id, count(distinct contest_id) solved_at_least_one_contest_count from submissions
   join problems on submissions.problem_id = problems.id
   where success
   group by user_id) t1 on users.id = t1.user_id
left join
	(select user_id, count(distinct contest_id) take_part_contest_count from submissions
	join problems on submissions.problem_id = problems.id
    group by user_id) t2 on users.id = t2.user_id) t
order by solved_at_least_one_contest_count desc, take_part_contest_count desc, id