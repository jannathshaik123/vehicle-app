# vehicle-app

buyers: user -> buyer, post-save *creates a new sales*

cars: car -> buyer, post_save vs pre_save, pre_save vs save *car inform  buyer*

orders: order, m2m_changed, order -> sale, post_save *updates*

sales: sale -> order, pre_delete

*there  are 2  ways  to set up  signalsl:CHECK  DOCS

1. set a  signal  between   the  user  and buyer model
--  this signal will create a buyer model instance when a user is created
-- working the  user with reciever signal
-- sender is "User", reciever: "Buyer"
-- True is returned only once  while  creation of  the  user