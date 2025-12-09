def merge_guest_lists(*lists):
    merge=[]
    for list in lists:
        for i in list:
            if i not in merge:
                merge.append(i)
    merge.sort()
    return merge

Instagram =['Maria','Denis','Maria','Sasha','Kostya']
Facebook=['Maria','Sonya', 'Maria','Sasha','Sofia']
print(merge_guest_lists(Instagram,Facebook))

TikTok=['Kek', 'Churchhella', 'Mops', 'Mops']
Snapchat=['Faya','Mops','Kitik']
print(merge_guest_lists(TikTok,Snapchat))

OnlyFriends=['Oleksandr','Denis','Konstyantyn','Vlad']
Twitter=['Yana','Olya','Nadya','Polya']
print(merge_guest_lists(OnlyFriends,Twitter))