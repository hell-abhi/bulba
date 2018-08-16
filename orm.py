from connection import Connect
from selectQuery import Select
from comparisonOperators import __eq, __lt
from logicalOperators import __and
import os


connection = Connect(
    "localhost",
    "root",
    os.environ.get('MYSQL_PASSWORD'),
    "form"
    )

select_result = Select(
    connection=connection,
    columns=["user_id", "first_name", "last_name"],
    tables=["user_details"]
    )
condition = __and(__lt('user_id', 6), __eq('first_name', 'David'))
print(select_result.condition(condition).execute_query())
