class TaskManager:
    task_lst = []

    def __init__(self):
        print('Task manager is started!')
        self.usage_info()

    def set_task(self, args: list):
        self.task_lst.append({args[1]: [args[2], args[3]]})

    def get_task(self, args: list):
        out_lst = self.task_lst[:int(args[1])]
        if out_lst:
            if args[0] == 's':
                print('Info of nearest tasks:')
                print('\tname task\tnext iteration')
                print('\t---------\t--------------')
                for itm in out_lst:
                    for k, v in itm.items():
                        print(f'\t{k}\t{v[0]}')
            elif args[0] == 'i':
                print('Info of last tasks:')
                print('\tbegin task\tend task\tname task')
                print('\t----------\t--------\t---------')
                for itm in out_lst:
                    for k, v in itm.items():
                        print(f'\t{v[0]}\t{v[1]}\t{k}')

    @staticmethod
    def usage_info():
        print('Usage info:[\033[31m keys\033[0m] [optional keys]')
        print(
            '\t[\033[31mc\033[0m][\033[33m task name\033[0m] [date start task -> date format YYYY-MM-DD]'
            ' [date end task -> date format YYYY-MM-DD]')
        print('\t[\033[31mi\033[0m] [count last run tasks -> int, default=2]')
        print('\t[\033[31ms\033[0m] [count list nearest tasks -> int, default=2]')
        print('Samples:\033[31mc\033[0m\033[33m name_task\033[0m 2022-03-02 2022-04-02, or t 5, or s 5')
