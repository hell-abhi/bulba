from connection import Connect
from selectQuery import Select
from comparisonOperators import __eq, __ne, __gt
from logicalOperators import __and

connection = Connect("localhost", "root", "abhi6355", "form")

select_result = Select(
    connection=connection,
    columns=["first_name", "last_name"],
    tables=["user_details"]
    )
select_result.limit(10)
ans = select_result.execute_query()
select_result.print_query_string()
print(ans)

print(__and([__eq('A', 10), __ne('B', 20), __gt('C', 30)]))
print(__and(__eq('A', 10), __gt('B', 10)))
