
team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print('В команде Мастера кода участников: %s' % (team1_num))
print('Итого сегодня в командах участников: %s и  %s' % (team1_num, team2_num))
print()
print('Команда Волшебники данных решила задач:  {}!'.format(score2))
print('Волшебники данных решили задачи за {0:6.2f} с !'.format(team2_time))
print()
print(f"{'Команды решили: '}{score1:^5}{'и'}{score2:^5}{'задач'}")
print(f"{'Результат битвы:  '}{challenge_result}")
print(f"{'Сегодня было решенно '}{score1+score2:^5}{'задач,'}{' в среднем по  '}{time_avg }{' секунды на задачу!.'}")

score1 = 42
score2 = 42
team1_time = 1552.512
team2_time = 1552.512
time_avg = round((team1_time+team2_time)/(score1+score1),2)


if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print()
print(f"{'Сегодня было решенно '}{score1+score2:^5}{'задач,'}{' в среднем по  '}{time_avg }{' секунды на задачу!.'}")
print(f"{'Результат битвы:  '}{result}")