from src.utils.env import env_or_exit

PROXY_SERVER_ADDRESS = env_or_exit('PROXY_SERVER_ADDRESS', cast=str)
PROXY_SERVER_PORT = env_or_exit('PROXY_SERVER_PORT', cast=int)
