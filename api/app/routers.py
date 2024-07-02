from fastapi import APIRouter
import grpc
from google.protobuf.json_format import MessageToJson
from fastapi.responses import JSONResponse

from .blog_pb2 import BlogListResponse, BlogRequest, BlogCreate
from .blog_pb2_grpc import BlogServiceStub
import json

router = APIRouter()

# استفاده از localhost به جای blog_grpc
channel = grpc.aio.insecure_channel('localhost:50051')
stub = BlogServiceStub(channel)

@router.get('/blogs')
async def get_allBlogs():
    response = await stub.List(BlogListResponse())
    return JSONResponse(content=json.loads(MessageToJson(response)))



@router.get('/blogs/{blog_id}')
async def get_blog(blog_id: int):
    response = await stub.Read(BlogRequest(id=blog_id))
    return JSONResponse(content=json.loads(MessageToJson(response)))


@router.post("/blogs")
async def create_blog(title: str, content: str, user_id: int):
    # Create a new Todo using the gRPC stub
    response = await stub.Create(BlogCreate(
        title=title,
        content=content,
        user_id=user_id,

    ))
    # Convert the gRPC response message to JSON and return it
    return JSONResponse(content=json.loads(MessageToJson(response)))