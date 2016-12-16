--creating view of tweets with product names and subcategory names
create view tweet_product_view
as select tweet.tweet_id, tweet.screen_name, tweet.created_at, json_extract(tweet_doc, '$.text'), twitter_search.product_name, twitter_search.product_subcategory_name
FROM tweet INNER JOIN twitter_search
ON tweet.product_id = twitter_search.product_id;
--count of tweets by product name
select product_name, count(*)
FROM tweet_product_view
group by product_name
order by count(*) desc;
--count of tweets by product subcategory
select product_subcategory_name, count(*)
from tweet_product_view
group by product_subcategory_name
order by count(*) desc;
-------------------------------------------------------------------------
--creating a view of retweets
create view rt_view
as select json_extract(tweet_doc, '$.text'), ts.product_name, ts.product_subcategory_name
from tweet inner join twitter_search ts
on tweet.product_id = ts.product_id
where json_extract(tweet_doc, '$.text') LIKE '%RT%';
--getting count of retweets by product name
select product_name, count(*) from rt_view
group by product_name;
--getting count of retweets by product subcategory name
select product_subcategory_name, count(*) from rt_view group by product_subcategory_name;



