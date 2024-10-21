## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys
def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
    x = int(x)
    i = 1
    m = 0
    while i < x :
        j = 1
        c = 0
        while j < i : 
            if i % j == 0 :
                c = c + 1
            j = j + 1
        if c > m :
            m = c
        i = i + 1

    j = 1
    c = 0
    while j < x :  
        if x % j == 0 :
            c = c + 1
        j = j + 1
    if c > m :
        return "anti-prime"
    else :
        return "not anti-prime"

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
    

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
    args = sys.argv
    if len(args) > 1 :
    	x = args[1]
    	print(main(x))
    else :
    	print("error escriu un número")
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
  
