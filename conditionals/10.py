#True. 
# bonus: need the parentheses, as short-circuiting will give False. This is due to
#       braking_force < acceleration and speed > 0: speed is NOT > 0, so that evaluates to False. the "and" then gets interpreted that the whole expression is False. 

# bonus correction: we DO need parens, but the end result is still True. parens needed due to higher operator precedence of and vs or.
