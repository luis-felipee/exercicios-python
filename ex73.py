#A  Fatiamento
#B  Fatiamento
#C Sorted
#D index
premier = ('Manchester City FC', 'Liverpool FC', 'Chelsea FC', 'Arsenal FC', 'Tottenham Hotspur FC', 'Manchester United FC', 'West Ham United FC', 'Wolverhampton Wanderers FC', 'Aston Villa FC', 'Leicester City FC', 'Southampton FC', 'Crystal Palace FC', 'Brighton & Hove Albion FC', 'Newcastle United FC', 'Brentford FC', 'Leeds United', 'Everton FC', 'Watford FC', 'Burnley FC', 'Norwich City FC')

print('=-=' * 20)
print(f'Lista de times da Premier League: {premier}')
print('=-=' * 20)
print(f'Os quatros primeiros são {premier[0:5]}')
print('=-=' * 20)
print(f'Os 4 últimos são {premier[16:]}')
print('=-=' * 20)
print(f'Times em ordem alfabética: {sorted(premier)}')
print('=-=' * 20)
print(f"O Liverpool está na {premier.index('Liverpool FC') + 1}ª posição")