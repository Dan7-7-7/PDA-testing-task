### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #this is an assignment operator, it should be ==
      return True
    else #missing colon
      return False
   

  dif highest_card(self, card1 card2): #this should be def, not dif; and there is a missing comma between the parameters
  if card1.value > card2.value: #this line and the three following lines should be indented by one more step
    return card #there is no parameter named card. Should be card1
  else:
    return card2
  


def cards_total(self, cards): #this function is not indented and is consequently outside the class
  total #total is not assigned to anything
  for card in cards:
    total += card.value
    return "You have a total of" + total #return statement is inside for loop due to incorrect indentation
    # total will be an integer, so the string concatenation in the return statement will not work.
  
```
