from flask import Flask
from flask import request
from flask import jsonify

import redis
import os

REDIS_FILE = 'file'
REDIS_FILE_INFO ='fi'

FILE_FILE = 'file'
FILE_NAME = 'name'
FILE_HASH = 'hash'
FILE_USER = 'user'
FILE_PRIORITY = 'priority'
REDIS_FILE_COUNTER = 'fcounter'

app = Flask(__name__)

red = redis.Redis(host=os.environ['REDIS_HOST'], port=6379, decode_responses=True)

@app.route('/file', methods=['POST'])
def file():
    try:
        print(request.form)
        file_data = request.get_json(force=True)
        file_hash = str(hash(file_data[FILE_FILE]))
        file_data[FILE_HASH] = file_hash
        
        red.hset(REDIS_FILE, file_hash, file_data[FILE_FILE])
        red.hset(REDIS_FILE_INFO + file_hash, mapping=file_data)
        
        # b)
        #red.sadd(file_data[FILE_USER], file_hash)
        
        # c)
        red.zadd(file_data[FILE_USER], {file_hash: file_data[FILE_PRIORITY]}, nx=True)
        
        red.incr(REDIS_FILE_COUNTER)
        
        return f"Success, file hash is {file_hash}"
    except redis.RedisError as e:
            return jsonify({"error": f"Redis error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/files/<user>', methods=['GET'])
def files(user):
    # b)
    #hashes = red.smembers(user)
    
    # c)
    hashes = red.zrange(user, 0, -1)
    
    files_list = list()
    for h in hashes:
        files_list.append(red.hgetall(REDIS_FILE_INFO+str(h)))
    
    return jsonify(files_list)

@app.route('/filesprio/<user>', methods=['GET'])
def files_prio(user):
    hashes = red.zrange(user, -5, -1)
    files_list = list()
    for h in hashes:
        files_list.append(red.hgetall(REDIS_FILE_INFO+str(h)))
    return jsonify(files_list)
    
@app.route('/counter', methods=['GET'])
def file_count():
    return red.get(REDIS_FILE_COUNTER)