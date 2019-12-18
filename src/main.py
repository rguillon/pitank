#!/usr/bin/python
from web_srv import config_mws, mws2

import asyncio

from tasks import tasks

def main():

    config_mws()

    main_loop = asyncio.get_event_loop()

    for task_name in tasks.get_tasks_names():
        main_loop.create_task(tasks.get_task(task_name).get_task())


    # Starts the server as easily as possible in managed mode,
    mws2.StartManaged()

    main_loop.run_forever()

if __name__ == "__main__":
    # execute only if run as a script
    main()
