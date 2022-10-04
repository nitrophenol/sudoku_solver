from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
    """Function to take input a sudoku from stdin and return
    it as a list of lists.
    Each row of sudoku is one line.
    """
    sudoku= list()
    for _ in range(9):
        row = list(map(int, input().rstrip(" ").split(" ")))
        sudoku.append(row)
    return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
    """Helper function to print sudoku to stdout
    Each row of sudoku in one line.
    """
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end = " ")
        print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
    a=pos[0]
    b=pos[1]
    if a>=1 and a<=3 and b>=1 and b<=3:
        return 1
    if a>=1 and a<=3 and b>=4 and b<=6:
        return 2
    if a>=1 and a<=3 and b>=7 and b<=9:
        return 3        
    if a>=4 and a<=6 and b>=1 and b<=3:
        return 4    
    if a>=4 and a<=6 and b>=4 and b<=6:
        return 5
    if a>=4 and a<=6 and b>=7 and b<=9:
        return 6
    if a>=7 and a<=9 and b>=1 and b<=3:
        return 7
    if a>=7 and a<=9 and b>=4 and b<=6:
        return 8
    if a>=7 and a<=9 and b>=7 and b<=9:
        return 9                
def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
    """This function takes parameter position
    and returns the index of the position inside the corresponding block."""
    a=pos[0]
    b=pos[1]
    if a>3:
     a=a%3
    if b>3: 
     b=b%3
    if a==1:
        return int(b)
    if a==2:
        return int(b+3)
    if a==3:
        return int(b+6)	
def get_block(sudoku:List[List[int]], x: int) -> List[int]:
    """This function takes an integer argument x and then
    returns the x^th block of the Sudoku. Note that block indexing is
    from 1 to 9 and not 0-8.
    """
    a=0
    b=0
    if x<4:
        a=0
        b=3*(x-1)
    if x>=5 and x <=6:
        a=3
        b=3*(x-4)
    if x>=7 and x<=9:
        a=6
        b=3*(x-7)
    m2=[]	
    for i in range(3):
        for j in range (3):
            m2.append(sudoku[i+a][j+b])
    return m2
    

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
    """This function takes an integer argument i and then returns
    the ith row. Row indexing have been shown above.
    """
    l=[]
    for x in range (9):
        l.append(sudoku[i-1][x])
    return l

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
    """This function takes an integer argument i and then
    returns the ith column. Column indexing have been shown above.
    """
    l=[]
    for i in range(9):
        l.append(sudoku[i][x-1])

    return l

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
    """This function returns the first empty position in the Sudoku. 
    If there are more than 1 position which is empty then position with lesser
    row number should be returned. If two empty positions have same row number then the position
    with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
    """
    for i in range (9):
        for j in range (9):
            if sudoku[i][j]==0:
                return (i+1,j+1)
    return (-1,-1)

def valid_list(lst: List[int])-> bool:
    """This function takes a lists as an input and returns true if the given list is valid. 
    The list will be a single block , single row or single column only. 
    A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
    """
    m2=[]
    for i in range (9):
        if lst[i]!=0:
            m2.append(lst[i])
    for i in range (len(m2)):
        for j in range (len(m2)):
            if i!=j:
             if m2[i]==m2[j]:
                return False
    return True
     
def valid_sudoku(sudoku:List[List[int]])-> bool:
    """This function returns True if the whole Sudoku is valid.
    """
    
    for i in range (9):
        if valid_list(get_row(sudoku,i))==False:
            return False
    for i in range (9):
        if valid_list(get_column(sudoku,i))==False:
            return False
    for i in range(9):
        if valid_list(get_block(sudoku,i))==False:
            return False
                      
    return True


def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
    """This function takes position as argument and returns a list of all the possible values that 
    can be assigned at that position so that the sudoku remains valid at that instant.
    """
    a=pos[0]
    b=pos[1]
    m2=[[0 for i in range (9)]for j in range (9)]
    for i in range (len(sudoku)):
        for j in range (9):
            m2[i][j]=sudoku[i][j]
    l=[]
    for i in range (1,10):
        m2[a-1][b-1]=i
        may=get_block_num(m2,(a,b))
        if valid_list(get_column(m2,b))==True and valid_list(get_row(m2,a))==True and valid_list(get_block(m2,may))==True:
            l.append(i)  
    return l

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
    """This function fill `num` at position `pos` in the sudoku and then returns
    the modified sudoku.
    """
    # your code goes here
    sudoku[pos[0]-1][pos[1]-1]=num

    return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):

    """This function fills `0` at position `pos` in the sudoku and then returns
    the modified sudoku. In other words, it undoes any move that you 
    did on position `pos` in the sudoku.
    """
    sudoku[pos[0]-1][pos[1]-1]=0
    return sudoku


def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
    def sudo(s:list[list[int]]):
         (x,y)=find_first_unassigned_position(s)
         if x==-1:
              if valid_sudoku(s):
                return True
              return False  
         else:
             for i in get_candidates(s,(x,y)):
                 s[x-1][y-1]=i              
                 if sudo(s):
                    return True
                 else:   
                  s[x-1][y-1]=0          
             return False
    a=sudo(sudoku)
    return a,sudoku
  
          

            
                
                


    
  
      
                           


               
               
 

    # to complete this function, you may define any number of helper functions.
    # However, we would be only calling this function to check correctness.



# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

def in_lab_component(sudoku: List[List[int]]):
    print("Testcases for In Lab evaluation")
    print("Get Block Number:")
    print(get_block_num(sudoku,(4,4)))
    print(get_block_num(sudoku,(7,2)))
    print(get_block_num(sudoku,(2,6)))
    print("Get Block:")
    print(get_block(sudoku,3))
    print(get_block(sudoku,5))
    print(get_block(sudoku,9))
    print("Get Row:")
    print(get_row(sudoku,1))
    print(get_row(sudoku,5))
    print(get_row(sudoku,9))
    print(get_position_inside_block(sudoku,(5,3)))
    print(get_candidates(sudoku,(1,3)))
    make_move(sudoku,(1,3),9)
    print(valid_list(sudoku))
    print(find_first_unassigned_position(sudoku))

# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

    # Input the sudoku from stdin
    sudoku = input_sudoku()

    # Try to solve the sudoku
    possible, sudoku = sudoku_solver(sudoku)

    # The following line is for the in-lab component
    #in_lab_component(sudoku)
    # Show the result of the same to your TA to get your code evaulated

    # Check if it could be solved
    if possible:
        print("Found a valid solution for the given sudoku :)")
        print_sudoku(sudoku)

    else:
        print("The given sudoku cannot be solved :(")
        print_sudoku(sudoku)