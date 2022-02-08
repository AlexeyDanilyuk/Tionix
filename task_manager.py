from manager.task_class import TaskManager

if __name__ == '__main__':
    start_task = TaskManager()
    while True:
        task_query = input('Enter the required command: ').split()
        if task_query[0] == 'c' and len(task_query) == 4:
            start_task.set_task(task_query)
        elif task_query[0] in ('i', 's'):
            if len(task_query) == 2:
                start_task.get_task(task_query)
            elif len(task_query) == 1:
                task_query.append('2')
                start_task.get_task(task_query)

        else:
            print('\033[31m*** Enter invalid syntax command line! ***\033[0m')
            start_task.usage_info()
