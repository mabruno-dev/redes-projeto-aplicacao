from uvicorn import run
import os
import funcoes as fn
import api


if __name__ == '__main__':
    
    run('api:app', 
        host='localhost', 
        port=5000, 
        reload=True,
        log_level='info',
        use_colors=False,)