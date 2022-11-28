import random

movie_name_list = ['lagaan', '3 idiots', 'swades', 'shershaah', 'dangal', 'queen']

movie_name = random.choice(movie_name_list)

print(str(movie_name))

number_of_guess = 0
player_guess = ''
player_won = False
movie_name_len = len(movie_name)
final_guess_list = ['-'] * movie_name_len
final_guess_string = ''

while not player_won:
    if final_guess_string.join(final_guess_list) == movie_name: #if player guess one by one
        print('Guessed')
        player_won = True
        break
    print(*final_guess_list, sep='') #printing guessed name
    player_guess = input('Guess an alphabet of movie name or the full movie name : ')
    number_of_guess += 1
    if player_guess == movie_name: #if player guessed full movie name at a time
        print('guessed')
        player_won = True
    for i in range(movie_name_len): #storing the guessed alphabets in list to display
        if movie_name[i] == player_guess:
            final_guess_list[i] = player_guess

if player_won:
    print('Congrats! you won in ', number_of_guess, ' attempts.')