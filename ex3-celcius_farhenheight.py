places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

lambda_var = lambda t: (t[0],t[1] * (9/5) + 32)
print(list(map(lambda_var,places)))