# ORM - Object Relational Mapping

ORM is used in order to translate relational table data into object data (in this case Python objects). We 
will first take a look at connecting `MySQLdb` to python to make direct queries from python as well as use 
`SQLAlchemy` for ORM interaction with the MySQL database

## Directory Files

* [0-select_states.py](0-select_states.py) - a script that lists all states from the database hbtn_0e_0_usa
* [1-filter_states.py](1-filter_states.py) -  a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
* [2-my_filter_states.py](2-my_filter_states.py) - a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
* [3-my_safe_filter_states.py](3-my_safe_filter_states.py) -  a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
* [4-cities_by_state.py](4-cities_by_state.py) - a script that lists all cities from the database hbtn_0e_4_usa
* [5-filter_cities.py](5-filter_cities.py) - a script that takes in the name of a state as an argument and lists all cities of that state, using the database
* [model_state.py](model_state.py) - create State class that represents states table
* [7-model_state_fetch_all.py](7-model_state_fetch_all.py) -  a script that lists all State objects from the database hbtn_0e_6_usa
* [8-model_state_fetch_first.py](8-model_state_fetch_first.py) -  a script that prints the first State object from the database hbtn_0e_6_usa
* [9-model_state_filter_a.py](9-model_state_filter_a.py) -  a script that prints the first State object from the database hbtn_0e_6_usa
* [10-model_state_my_get.py](10-model_state_my_get.py) - a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
* [11-model_state_insert.py](11-model_state_insert.py) - a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
* [12-model_state_update_id_2.py](12-model_state_update_id_2.py) - a script that lists all State objects from the database hbtn_0e_6_usa
* [13-model_state_delete_a.py]() - a script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
* [14-model_city_fetch_by_state.py]() - a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa
* [model_city.py]() - a script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
