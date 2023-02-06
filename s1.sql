select * from problems  where id in
  (select problem_id from submissions
  where success
  group by problem_id
  having count(DISTINCT user_id) > 1)
order by id
