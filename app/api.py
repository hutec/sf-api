from flask_restful import Resource
import sf_parser
import json

class Thread(Resource):
    def get(self, thread_id):
        return sf_parser.get_thread(thread_id, 2)
        # return {#}

