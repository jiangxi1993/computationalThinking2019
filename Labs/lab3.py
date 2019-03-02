import itertools as iter
# Name: JIANGXI
# Section: G5

# lab3

def select_tweeters(followers):
    block_size=5
    total_len=len(followers)
    index_list=[]
    if total_len<+block_size:
        return get_subgroup_followers(followers)

    loop=total_len//block_size
    final_round_position=total_len-total_len%15
    followerX=followers.copy()
    followerX.reverse() 
    result=[]
    result2=[]
    pointer_start=0
    pointer_end=block_size
    buffer=[]
    
    for value in range (loop):
        pointer_start=value*block_size
        pointer_end=pointer_start+block_size
        
        buffer=followers[pointer_start:pointer_end]
        
        result.extend(get_subgroup_followers(buffer))
        result=get_subgroup_followers(result)
        
        
    #result.extend(get_subgroup_followers(result+followers[final_round_position:-1],followers))

    result=get_subgroup_followers(result+followers[final_round_position:-1])

    for value in range (loop):
            pointer_start=value*block_size
            pointer_end=pointer_start+block_size
            buffer=followerX[pointer_start:pointer_end]
            result2.extend(get_subgroup_followers(buffer))
            result2=get_subgroup_followers(result2+result)

    result=get_subgroup_followers(result+result2+followerX[final_round_position:-1])


    for item in result:
        index_list.append(followers.index(item))
    return index_list



def get_subgroup_followers(followerX):

    bestCombination=0
    bestCombinationList=[]
    length=0
    for item in iter.combinations(followerX,5):
        setX=list(set(item[0]+ item[1]+ item[2] +item[3] + item[4]))
        length=len(setX)

        if length>bestCombination:
            bestCombination=length
            bestCombinationList=list(item)
         
    return bestCombinationList