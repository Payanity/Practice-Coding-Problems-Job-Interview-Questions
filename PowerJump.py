def powerJump(game):
    # Write your code here
   i = 0
   iter=1
   power = -1
   if len(game) ==1:
        return 1

   while i< len(game):
       if (game[i] == game[len(game) - 1]):
           while(i+iter<len(game)):
                if int(game[i]) == int(game[i+iter]):
                    if(iter<power) or power == -1:
                         power = iter
                iter+=1
       i+=1
       iter = 1

   return power

print(powerJump("1011"))