--creating a table of products that are calculators or keyboards; exclude 'Acco' due to unicode error
drop table if exists Calculators_Keyboards;
create table Calculators_Keyboards AS select p.product_id, p.product_name, psc.product_subcategory_name
from products p INNER JOIN product_subcategory psc ON
p.product_subcategory_id = psc.product_subcategory_id
where p.product_name LIKE '%calculator%' OR p.product_name LIKE '%keyboard%' AND p.product_name NOT LIKE '%Acco%';

alter table Calculators_Keyboards
add constraint fk_product_id
foreign key(product_id) references Products(product_id);

drop table if exists Tweet;
create table Tweet (
  tweet_id varchar(32) generated always
     as (json_unquote(json_extract(tweet_doc, '$.id_str'))) stored primary key,
  screen_name varchar(32) generated always
     as (json_unquote(json_extract(tweet_doc, '$.user.screen_name'))) stored,
  created_at datetime generated always
     as (str_to_date(json_unquote(json_extract(tweet_doc, '$.created_at')),
     '%a %b %d %H:%i:%s +0000 %Y')) stored,
  tweet_doc json,
  product_id INT,
  foreign key (product_id) references Calculators_Keyboards(product_id)
);