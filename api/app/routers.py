
from fastapi import APIRouter
import grpc
from google.protobuf.json_format import MessageToJson
from fastapi.responses import JSONResponse

from blog_grpc.blog_pb2 import BlogListResponse
from blog_grpc.blog_pb2_grpc import BlogServiceStub
import json

router = APIRouter()

channel = grpc.insecure_channel('blog_grpc:50051')
stub = BlogServiceStub(channel)

@router.get('/blogs')
def get_allBlogs():
    response = stub.List(BlogListResponse())
    return JSONResponse(content=json.loads(MessageToJson(response)))