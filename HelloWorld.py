"""import randomteachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']work_room = [[], [], []]for teacher in teachers:    temp = random.randint(0, 2)    work_room[temp].append(teacher)# print(work_room)for room in work_room:    print(f"有{len(room)}位老师，分别为{room}")"""t1 = (10, 20, 30, 'aaa')t2 = ['a', 'b', 'c']t3 = {'a', 'b', 'c'}dict1 = {'a': 1, 'b': 3}print('a' not in dict1)