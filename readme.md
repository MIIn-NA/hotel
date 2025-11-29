Booking 4 2 ->Reservation
Cancellation 4 2 ->Booking 
CheckIn 4 2 ->Guest
Check0ut 4 2 ->Guest
Discount 3 2 ->
Invoice 3 2 ->
RatePlan 3 2 ->
Payment 4 2 ->Invoice 
Reservation 5 2 ->Guest,Room
Season 3 2 ->
BaseModel 3 2 ->
CacheManager 4 2 ->
Config 3 2 ->
DatabaseManager 3 2 ->
Logger 3 2 ->
Notifier 3 2 ->
SecurityManager 3 2 ->HotelException
TaskScheduler 4 2 ->
Validator 3 2 ->
Amenity 3 2 ->
Building 4 2 ->Facility
Equipment 3 2 ->
Facility 3 2 ->
Floor 4 2 -> Room
Hotel 5 2 -> Floor,Location 
InventoryItem 3 2 ->
Location 3 2 ->
Room 4 2 ->RoomType 
RoomType 3 2 ->
Analytics 3 2->
Admin 4 2→ User
Attendance 4 2→Employee 
Department 3 2→
Employee 4 2 → Department 
Guest 4 2→Profile
Permission 3 2 →
Profile 3 2→
Role 3 2→
Shift 4 2→Employee 
User 4 2→Role
ConferenceRoom 4 2→Equipment 
Event 4 2→ConferenceRoom
Housekeeping 4 2→Housekeeping 
Maintenance 4 2→Equipment 
Menu 4 2→
Order 4 2→Guest
Restaurant 4 2→Menu
Spa  4 2→Treatment 
Transportation 4 2→Guest
Treatment 3 2→
DashBoard 3 2→
EmployeeReport 4 2→ Employee 
AnalyticsException 0 0-
FinancialReport 0 0→
FinancialReportException 0 0
Forecast 3 2 →
GuestReport 4 2→
InventoryReport 3 2→
GuestReportException 0 0
OccupancyReport 4 2→
OccupancyReportException 0 0
RevenueReport 3 2→
ServiceReportException 0 0
ServiceReport 3 2→
ServiceReportException 0 0
Классы:65
Поля:210
Методы:116
Ассоциации:30
Исключения:12
