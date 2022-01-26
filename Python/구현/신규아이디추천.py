def solution(new_id):
    answer = ''
    id = ''

    # step 1. 대문자 -> 소문자
    new_id = new_id.lower()
    
    # step 2
    for word in new_id:
        if word.islower() or word.isdigit() or (word in ['-','_','.']):
            id += word
    
    # step 3
    while ".." in id:
        id = id.replace("..", ".")
        
    # step 4
    if id[0] == ".":
        if len(id) > 1:
            id = id[1:]
        else:
            id = "."
    
    if id[-1] == ".":
        id = id[:-1]

    # step 5
    if id == "":
        id = 'a'
    
    # step 6
    if len(id) >= 16:
        id = id[:15]
        if id[-1] == ".":
            id = id[:-1]
    
    # step 7
    while len(id) < 3:
        id += id[-1]
        
    answer = id
    return answer

