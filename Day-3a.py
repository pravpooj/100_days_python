


from ast import Break


print(''' |   [  | v':    :              |        |_,;c    
 | ]    |/; |,   |              |   [  ( __,/     
 |    ,-'/  ;\ ,<  _',\.-._,;   |      ] |    n   
 |   -' /   _;';    '=_'-' ,)  ,\        |   ,;   
 |  ]  / \,'__/--,_,-- 'mm'J -"_  ]       '-,+_   
 |    /    / "''-.,;"---''--'"" \      ]   __  "-'
;' [      / :    : _c           /         /  ",_,'
|      [ | v|  , '/             c c    \ |        
\    ]   |  \ /| :        __,-,v;|]   . \|        
  [      /"--'/  |      (7_   c@  )    )/|        
\     ]    ,-"'<':       '--,    (    /^ |        
| ]       / :   '|           \ |  )      |        
| |   /  |  |    ;,-;,        \ ,)(     ]|        
|  \^ |  |  :  |\ ,'           \ / \ [   |        
|  ?  /  \_ |  /|:              | , \    |        
|  | ('.   "--' |:,    ;        :\  ,\  [|        
|  ;\~)   _     \_) ',_|   ,    | ),  \_ :        
|   |/ [ /""-,_   '-'(    /.'   | \   |  '-_      
| [      |  |  "---,__"'=';=,_  |  \ /|\    '"-,__
|     ]  |  :    |    ""'^.\    |   | |    \      
|  [    ]|  |    :              | ]  \ \   /  _AsH''')


print("Welcome to Tresure Island, Go and find the Tresure else you will be Alladin")

direction = input("Do you wnat to go to left or right (l,r)").lower()

if direction == 'l':
    print(" you are lucky, keep going, go to next level")

    swim = input("Lucky you,to go to next level, Do you want to swim or wait for crocodile to pickup?(swim,wait):").lower()
    if swim == 'wait':
        print('Good game, go to the next level!')

        select_door = input('Which door do you want to get out ? :(Red,Blue or Yellow)?').lower()
        if select_door == 'Yellow':
            print('you are the winner')
        else:
            print('you are killed by hummingbird, you are alladdin,  game over!')





    else:
        print("you are killed by gold fish, you are Alladin, Game Alladin!")


else:
    print("you are hit by an ant, you are Alladin, Game Alladin!")
