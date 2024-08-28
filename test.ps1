$headers = @{ "Content-Type" = "application/json" }
# $body_owner = @{
#     name = "John"
#     last_name = "Doe"
#     email = "john.doe@example.com"
#     cars = @(
#         @{
#             brand = "Toyota"
#             model = "Corolla"
#             production_date = "2015-05-20"
#         },
#         @{
#             brand = "Tesla"
#             model = "Model 3"
#             production_date = "2020-03-15"
#         },
#         @{
#             brand = "BMW"
#             model = "X5"
#             production_date = "2018-08-10"
#         }
#     )
# } | ConvertTo-Json
# Invoke-RestMethod -Uri http://localhost:8000/owners/ -Method Post -Headers $headers -Body $body_owner

# $body_car = @{
#             brand = "Opel"
#             model = "Corsa"
#             production_date = "1999-10-10"
#             owner_id = 1
#         } | ConvertTo-Json
Invoke-RestMethod -Uri http://127.0.0.1:8000/owners/3/cars -Method Get -Headers $headers