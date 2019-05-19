# Redis数据库地址
REDIS_HOST = '192.168.43.68'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 're123456'

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://m.weibo.cn/'

# API配置
API_HOST = '192.168.43.212'
# API_HOST = '127.0.0.1'
API_PORT = 5556
# http://192.168.43.212:5556/random

# 开关
GETTER_ENABLED = True
TESTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10
