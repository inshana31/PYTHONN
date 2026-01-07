blog_views=[150,800,2500,600,1200,450,3000]
total_views=0
trending_post=0
for views in blog_views:
    if views > 1000:
        print("trending")
        trending_post=trending_post+1
    elif views >=500 and views <=1000:
        print("average")
    else:
        print("low traffic")
    total_views=total_views+views
print("total view:",total_views)
print("trending posts:",trending_post)