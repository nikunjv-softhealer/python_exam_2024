# [
# /blog/tag/tag-a-1
# /blog/tag/tag-b-2
# https://softhealer.com/blog/career-5/feed
# https://softhealer.com/blog/odoo-2/feed
# https://softhealer.com/blog/career-5/unforgettable-gir-trip-2086
# https://softhealer.com/blog/career-5/christmas-celebration-2022-1954
# https://softhealer.com/shop/product/accounting-fiscal-year-565
# https://softhealer.com/shop/product/accounting-transaction-charges-407
# ]
# I have above list and make sure it's a dynamic and content any number of value like
# above list
# Now i want to convert it to below
# A)
# https://softhealer.com/blog/career-5/unforgettable-gir-trip-2086 url to
# https://softhealer.com/blog/career-5/post/unforgettable-gir-trip-2086
# B)
# https://softhealer.com/shop/accounting-fiscal-year-565 to
# https://softhealer.com/shop/accounting-transaction-charges-407
list_one = [
'/blog/tag/tag-a-1',
'/blog/tag/tag-b-2',
'https://softhealer.com/blog/career-5/feed',
'https://softhealer.com/blog/odoo-2/feed',
'https://softhealer.com/blog/career-5/unforgettable-gir-trip-2086',
'https://softhealer.com/blog/career-5/christmas-celebration-2022-1954',
'https://softhealer.com/shop/product/accounting-fiscal-year-565',
'https://softhealer.com/shop/product/accounting-transaction-charges-407'
]

list_one[4] = 'https://softhealer.com/blog/career-5/post/unforgettable-gir-trip-2086'
list_one[7] = 'https://softhealer.com/shop/accounting-transaction-charges-407'
print(list_one[4])
print(list_one[7])

