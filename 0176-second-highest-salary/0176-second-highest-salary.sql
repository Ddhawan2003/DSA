SELECT IFNULL((
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
), null) AS SecondHighestSalary;