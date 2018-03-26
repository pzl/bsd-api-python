from bsdapi import BsdApiClient

c = BsdApiClient('https://bmdowning-005-sandbox.bsdinternal.com', 'apitest', '6aaf89b14750dad7e872bc9a576366946ebb7997')

r = c.get('core/blue_config_get', {
    'category': 'main',
    'name': 'secure_url_base'
})

print r.status_code
print r.content
