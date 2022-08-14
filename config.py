URL = "https://twitter.com/i/api/2/search/adaptive.json"

PARAMS = {
    'include_profile_interstitial_type': '1',
    'include_blocking': '1',
    'include_blocked_by': '1',
    'include_followed_by': '1',
    'include_want_retweets': '1',
    'include_mute_edge': '1',
    'include_can_dm': '1',
    'include_can_media_tag': '1',
    'skip_status': '1',
    'cards_platform': 'Web-12',
    'include_cards': '1',
    'include_ext_alt_text': 'true',
    'include_quote_count': 'true',
    'include_reply_count': '1',
    'tweet_mode': 'extended',
    'include_entities': 'true',
    'include_user_entities': 'true',
    'include_ext_media_color': 'true',
    'include_ext_media_availability': 'true',
    'send_error_codes': 'true',
    'simple_quoted_tweet': 'true',
    'count': '20',
    'pc': '1',
    'spelling_corrections': '1',
    'ext': 'mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,enrichments,superFollowMetadata,unmentionInfo,editControl,vibe',
}



HEADERS = {
    "cookie": 'personalization_id="v1_jd1JpIOeGP+MIoQL1RrHmA=="; guest_id_marketing=v1:165597783779327387; guest_id_ads=v1:165597783779327387; guest_id=v1:165597783779327387; ads_prefs="HBERAAA="; kdt=5KerPnth2v8TIW5aNRcktIodea6TjxezzzFcNRhy; auth_token=f4188c7b841634308bef241a1e1ade23810e3047; twid=u=1261588055405649920; ct0=cf8ccc52f9b37c5190f3b3324dcce48a6f2b723cc7054f6bbfd011633be5d5de37205fdbc30101c7e163ce043429bd508a842e53f45bacfc0665eb7a40589e3d8ccac5127022cc9cfc497d21197b8894; _ga=GA1.2.1803957142.1656393888; _gid=GA1.2.1146839846.1660458163; lang=en',
    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    'refer': "https://twitter.com/search?q=happy&src=typed_query&f=top",
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'x-csrf-token': 'cf8ccc52f9b37c5190f3b3324dcce48a6f2b723cc7054f6bbfd011633be5d5de37205fdbc30101c7e163ce043429bd508a842e53f45bacfc0665eb7a40589e3d8ccac5127022cc9cfc497d21197b8894',
}

KEY = "deposit"
MAX_PAGE = 10

PROXIES = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890", }
# PROXIES = None

OUTPUT_FILE = "data.xlsx"
