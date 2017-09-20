def my_function(r1,r2):
    if r1['left_x'] < r2['left_x']:
        left_r = r1
        right_r = r2
    else:
        left_r = r2
        right_r = r1
        
    if r1['bottom_y'] < r2['bottom_y']:
        bottom_r = r1
        top_r = r2
    else:
        bottom_r = r2
        top_r = r1

        
    if right_r['left_x'] <= left_r['left_x'] + left_r['width'] and top_r['bottom_y'] <= top_r['bottom_y'] + top_r['height']:
        x = right_r['left_x']
        y = top_r['bottom_y']
        if right_r['left_x'] + right_r['width'] <= left_r['left_x'] + left_r['width']:
            w = right_r['width']
        else:
            w = left_r['left_x'] + left_r['width'] - right_r['left_x']

        if top_r['bottom_y'] + top_r['height'] <= bottom_r['bottom_y'] + bottom_r['height']:
            h = top_r['height']
        else:
            h = bottom_r['bottom_y'] + bottom_r['height'] - top_r['bottom_y']

    else:
        return "no intersection"
            
    return({'left_x': x, 'bottom_y': y,'width': w,'height': h})
    

    
    
# run your function through some test cases here
# remember: debugging is half the battle!
r1 = {'left_x': 1, 'bottom_y': 5,'width': 10,'height': 4}
r2 = {'left_x': 3, 'bottom_y': 6,'width': 6,'height': 8}  
print my_function(r1,r2)