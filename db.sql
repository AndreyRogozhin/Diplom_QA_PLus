

select login, count(*) from "Couriers" cr 
         JOIN "Orders" ord  
on cr.id = "courierId" 
where "inDelivery"                                   
group by login;




SELECT track,
       CASE
           WHEN finished   THEN 2
           WHEN cancelled  THEN -1
           WHEN "inDelivery" THEN 1
    else 0
       END as  status
from "Orders";

