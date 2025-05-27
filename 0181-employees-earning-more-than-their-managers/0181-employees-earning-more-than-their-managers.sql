# Write your MySQL query statement below
SELECT name as Employee from Employee e1
Where salary > (
    select salary from Employee as e2
    where e2.id = e1.managerId
);
