

# Taps 
The data source from which data will be extracted is known as the tap. There are ready-made Taps available on the Singer site which can be used as it is, or custom taps can also be created.
For this test we will be building a custom tap to get astronomy data from sunrise-sunset.org/api. 

API Documentation: https://sunrise-sunset.org/api

We want to build a dataset for Sunrise and Sunset timing for Pune( lat=18.5204 long=73.8567). 

Your tap should perform the following function:
Historical Load : load historical data since 1 Jan 2020
Incremental Load : Append today’s data in existing target
Transform data : Transform the timestamp from UTC to IST 


To load data we use Target. Use the following pre-built target to load your data:


# target-sqlite

This is a [Singer](https://singer.io) target that reads JSON-formatted data
following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md)
and loads them to SQLite.


meltano / target-sqlite · GitLab : https://gitlab.com/meltano/target-sqlite

