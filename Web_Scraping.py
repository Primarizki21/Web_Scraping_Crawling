url_target = 'https://gql.tokopedia.com/graphql/ShopProducts'
headers = {'sec-ch-ua-platform': '"Windows"',
   'X-Version': '3ffc927',
   'Referer': 'https://www.tokopedia.com/anker-indonesia',
   'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
   'sec-ch-ua-mobile': '?0',
   'X-Source': 'tokopedia-lite',
   'X-Device': 'default_v3',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
   'accept': '*/*',
   'DNT': '1',
   'content-type': 'application/json',
   'X-Tkpd-Lite-Service': 'zeus'}
query =f'[{{"operationName":"ShopProducts","variables":{{"source":"shop","sid":"1645551","page":1,"perPage":80,"etalaseId":"etalase","sort":1,"user_districtId":"2274","user_cityId":"176","user_lat":"0","user_long":"0"}},"query":"query ShopProducts($sid: String\u0021, $source: String, $page: Int, $perPage: Int, $keyword: String, $etalaseId: String, $sort: Int, $user_districtId: String, $user_cityId: String, $user_lat: String, $user_long: String) {{\\n  GetShopProduct(shopID: $sid, source: $source, filter: {{page: $page, perPage: $perPage, fkeyword: $keyword, fmenu: $etalaseId, sort: $sort, user_districtId: $user_districtId, user_cityId: $user_cityId, user_lat: $user_lat, user_long: $user_long}}) {{\\n    status\\n    errors\\n    links {{\\n      prev\\n      next\\n      __typename\\n    }}\\n    data {{\\n      name\\n      product_url\\n      product_id\\n      price {{\\n        text_idr\\n        __typename\\n      }}\\n      primary_image {{\\n        original\\n        thumbnail\\n        resize300\\n        __typename\\n      }}\\n      flags {{\\n        isSold\\n        isPreorder\\n        isWholesale\\n        isWishlist\\n        __typename\\n      }}\\n      campaign {{\\n        discounted_percentage\\n        original_price_fmt\\n        start_date\\n        end_date\\n        __typename\\n      }}\\n      label {{\\n        color_hex\\n        content\\n        __typename\\n      }}\\n      label_groups {{\\n        position\\n        title\\n        type\\n        url\\n        __typename\\n      }}\\n      badge {{\\n        title\\n        image_url\\n        __typename\\n      }}\\n      stats {{\\n        reviewCount\\n        rating\\n        averageRating\\n        __typename\\n      }}\\n      category {{\\n        id\\n        __typename\\n      }}\\n      __typename\\n    }}\\n    __typename\\n  }}\\n}}\\n"}}]'


