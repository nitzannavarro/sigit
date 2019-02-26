
#chack how win in tik tak to
def fun(mat):
    playrs = [0,0]
    if mat[0][0]==mat[1][1]==mat[2][2] and mat[0][0]!=0:#chack the fitst diagonal
        playrs[mat[0][0]-1]+=1
    if mat[0][0]==mat[1][0]==mat[2][0]and mat[0][0]!=0:#chack the secend diagonal
        playrs[mat[0][0]-1]+=1
    if mat[0][1]==mat[1][1]==mat[2][1]and mat[0][1]!=0:#chack the fitst row
        playrs[mat[0][1]-1]+=1
    if mat[0][2]==mat[1][2]==mat[2][2]and mat[0][2]!=0:#chack the secend row
        playrs[mat[0][2]-1]+=1
    if mat[0][0]==mat[0][1]==mat[0][2]and mat[0][0]!=0:#chack the thred row
        playrs[mat[0][0]-1]+=1
    if mat[1][0]==mat[1][1]==mat[1][2]and mat[1][0]!=0:#chack the fitst col
        playrs[mat[1][0]-1]+=1
    if mat[2][0]==mat[2][1]==mat[2][2]and mat[2][0]!=0:#chack the secend col
        playrs[mat[2][0]-1]+=1
    if mat[0][2]==mat[1][1]==mat[2][0]and mat[0][2]!=0:#chack the thred col
        playrs[mat[0][2]-1]+=1
    if playrs[0]==0 and playrs[1]==playrs[0]:
        print ('draw')
    elif playrs[0]> playrs[1]:
        print ('payer 1 win')
    elif playrs[0] < playrs[1]:
        print('payer 2 win')



matrix=[[0,0,0],[1,2,0],[1,2,1]]
fun(matrix)