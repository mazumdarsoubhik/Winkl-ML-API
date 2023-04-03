
import requests
import time

# generate_hashtag_id = 'https://graph.facebook.com/v10.0/ig_hashtag_search?user_id=17841403112088479&q='
get_top_media_base = 'https://graph.facebook.com/v10.0/'
def get_top_media_api(user_id,post_limit): 
    return '/top_media?user_id={}&fields=id,media_type,comments_count,like_count&limit={}&access_token='.format(user_id,post_limit)


acc_handle,acc_user_id,acc,access_token, generate_hashtag_id= [0]*3,[0]*3,[0]*3,[0]*3,[0]*3
# Rahul Singh
acc_handle[0] = 'therahul_singh'
acc[0] = 'https://graph.facebook.com/v10.0/17841402962813025?fields=business_discovery.username('
access_token[0] = 'EAAEg6RZCDs8QBAPIxJzffxqROAtHGH46kWdZBGHDwHMXYnEOaJmENYbSiD4KtkL08w0aZBYJiFVHPmqT4zixafUWgRCZBCEiZA9S6o0DNzWM4YuQHpqD92FatakX7heZALptBYUpz6KpeZAkLSC2N54PNTOUeF1eLniA2KS6SI6kspCxGWnHoKmgZBJEnQe5fZBN9O0NEMripaE4fHODSa2Ky'

# Deepansh Mittal
acc_handle[1] = 'deepansh143'
acc[1] = 'https://graph.facebook.com/v10.0/17841401916769480?fields=business_discovery.username('
access_token[1] = 'EAAEg6RZCDs8QBAJkpuQZByF9tfq96W6kb7KdRa67Cn8wFjZBdpXWCRwN6RvWt4B2x7GZAhyHoqk2qVaU3eXy3tdVlLajJvZABlL8HQ2i3ZBuWcV5UlEl5gDnTXiFC4XD5aEF7gF2GEeAWfteQuCOZCcIf58lDNNqQ5hP4naZBV3O7KpYq7phZC0uLBXOehLo55kAZD'

# Winkl App
acc_handle[2] = 'winklapp'
acc_user_id[2] = '17841403112088479'
generate_hashtag_id[2] = 'https://graph.facebook.com/v10.0/ig_hashtag_search?user_id={}&q='.format(acc_user_id[2])
acc[2] = 'https://graph.facebook.com/v10.0/{}?fields=business_discovery.username('.format(acc_user_id[2])
access_token[2] = 'EAAEg6RZCDs8QBALDnV51Cj4oth54ZAi7iS72AZBwv52rJgnYHHS7ZCaoC4GGsZAZCVswIZCUq2h2o2DZBcuBHSe1mRrSc3m3Eujn3HXUpWZCKoQjdyU66Y0uQjXB7vZAk4yZAhDXqnFk01Mv16W9jGJO341JbptdUcOLXceZA2sZAQvIjf3VCKGR1ZCPJZCOvEk8Mpw2MLD9wX3hSUZCPuIs0nk0sB2x'

def get_hashtag_id(hashtag):
    response = requests.get(generate_hashtag_id[2] + str(hashtag) + '&access_token=' + access_token[2]).json()
    if 'error' in response:
        if response['error']['code'] == 4:
            print('Too Many API Calls')
            return 4
        elif response['error']['error_subcode'] == 2207024:
            print('Invalid Hashtag')
            return 2207024
        elif response['error']['error_subcode'] == 460:
            print('User changed their password')
            return 460
    if 'error' not in response:
        id = response['data'][0]['id']
    else:
        print('Some error in get_hashtag_id')
        return 0
    print(hashtag + " : " + id)
    return id


def get_hashtag_media(hashtag_id, post_limit):
    if post_limit > 50:
        post_limit = 50
    posts = []
    response = requests.get(get_top_media_base + str(hashtag_id) + get_top_media_api(acc_user_id[2],post_limit) + access_token[2]).json()
    # print(response)
    for post in response['data'][:post_limit]:
        posts.append(post)
    # length += len(response['data'])
    # # print(length)
    # if 'paging' in response:
    #     flag = True
    #     while flag == True:
    #         response = requests.get(str(response['paging']['next'])).json()
    #         for post in response['data']:
    #             posts.append(post)
    #         length += len(response['data'])
    #         # print(length)
    #         if length >= (post_limit - 1):
    #             flag = False
    #             break
    #         if 'paging' in response:
    #             flag = True
    #         else:
    #             flag = False
    return posts


def calc_hashtag_reach(posts, hashtag):
    likes_total = 0
    comments_total = 0
    reach = 0
    for post in posts:
        if post['media_type'] == "VIDEO":
            result = 0
            result = int((7.08867055 * post['like_count'] + 456.97100922))
            reach = reach + result
            likes_total += post['like_count']
            comments_total += post['comments_count']
        else:
            result = 0
            result = int((5.23701779 * post['like_count']) + 421.65315056)
            reach = reach + result
            likes_total += post['like_count']
            comments_total += post['comments_count']
    
    # print("#" + str(hashtag))
    # print("REACH : " + str(reach))
    # print("LIKES COUNT : " + str(likes_total))
    # print("COMMENTS COUNT : " + str(comments_total))
    # print("TOTAL POSTS : " + str(len(posts)))
    hash_reach = {  'hashtag': hashtag,
                    'reach': reach,
                    'likes': likes_total,
                    'comments': comments_total,
                    'total posts': len(posts)}
    return hash_reach

'''
def calc_post_reach(handle, url):
    response = requests.get(acc_2 + str(handle) + "){followers_count,username,media_count,media{comments_count,like_count,media_type,media_url,caption,timestamp,permalink}}&access_token=" + access_token_1)
    insta_user = response.json()
    likes = 0
    comments  = 0
    reach = 0
    if 'media' in insta_user['business_discovery']:
        posts = insta_user['business_discovery']['media']['data']
        for post in posts:
            if post['permalink'] == str(url):
                
                if post['media_type'] == "VIDEO":
                    result = 0
                    result = int((7.08867055 * post['like_count'] + 456.97100922))
                    reach = reach + result
                    likes = post['like_count']
                    comments = post['comments_count']

                else:
                    result = 0
                    result = int((5.23701779 * post['like_count']) + 421.65315056)
                    reach = reach + result
                    likes = post['like_count']
                    comments = post['comments_count']              

    # print("HANDLE : " + str(insta_user['business_discovery']['username']))
    # print("URL : " + str(url))
    # print("REACH : " + str(reach))
    # print("LIKES : " + str(likes))
    # print("COMMENTS : " + str(comments))
    post_reach = {  'handle': insta_user['business_discovery']['username'],
                    'url': url,
                    'reach': reach,
                    'likes': likes,
                    'comments': comments}
    return post_reach
'''

def get_reach_by_hashtag(hashtag, past_post_count = 50):
    hashtag_id = get_hashtag_id(str(hashtag))
    if hashtag_id == 4:
        return { "status": False,
                 "extra": "Too many api call, try again after 1hr"}
    elif hashtag_id == 2207024:
        return { "status": False,
                 "extra": "Invalid Hashtag"}
    elif hashtag_id == 460:
        return { "status": False,
                 "extra": "User changed password"}
    elif hashtag_id == 0:
        return { "status": False,
                 "extra": "Some other error in get_hashtag_id"}
    else:
        posts = get_hashtag_media(str(hashtag_id), past_post_count)
    return calc_hashtag_reach(posts, hashtag)

# print(get_reach_by_hashtag('MagicWithBatter'))
