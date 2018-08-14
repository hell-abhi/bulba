from connection import Connect
from selectQuery import Select

connection = Connect("localhost", "root", "abhi6355", "form")

select_result = Select(
    connection=connection,
    columns=["first_name", "last_name"],
    tables=["user_details"]
    )
select_result.limit(10)
ans = select_result.execute_query()
print(ans)
