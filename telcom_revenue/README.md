# Data:

*Users table (users data):*

* user_id — unique user identifier 
* first_name — user name 
* last_name — user surname 
* age — users's age (years) 
* reg_date — suscrption date (dd, mm, yy)
* churn_date — the date when the user stop using the service (if nan, the cost was in place whe the data was retrieved)
* city — user's city of residence 
* plan — name of the fee 

*Calls table (calls data):*

* id — unique calls identifier 
* call_date — date of the call
* duration — call duration (minutes) 
* user_id — unique user identifier of the person who makes the call

*Messages table (SMS data):*

* id — unique sms identifier 
* message_date — date of the sms 
* user_id — unique user identifier of the person who sends the sms

*Internet table (web data):*

* id — unique session identifier 
* mb_used — mb used in the session (en megabytes)
* session_date — web session date
* user_id — unique user identifier 

*Plans table (Fee package data):*

* plan_name — name of the contract fee package
* usd_monthly_fee —monthly payment in US dollars
* minutes_included — monthly minutes included
* messages_included — monthly sms included
* mb_per_month_included — monthly data included (in megabytes)
* usd_per_minute — exceding price per minute of the package 
* usd_per_message — exceding price per sms of the package 
* usd_per_gb — exceding price per GB of the package 

# Goals:

* Analyze client's consumer behaviour.
* Establish which telcom package generates greater income.

# Libraries:

pandas, matplotlib, math, scipy, datetime, 
