import asyncio

import grpc
from grpc import aio
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.empty_pb2 import Empty
import blog_pb2
import blog_pb2_grpc
from core.database import SessionLocal
from core.models import BlogModel
from datetime import datetime


class BlogService(blog_pb2_grpc.BlogServiceServicer):
    def Create(self, request, context):
        db = SessionLocal()
        blog = BlogModel(
            title=request.title,
            content=request.content,
            created=datetime.utcnow(),
            is_published=request.is_published,
            user_id=request.user_id
        )
        db.add(blog)
        db.commit()
        db.refresh(blog)

        created_timestamp = Timestamp()
        created_timestamp.FromDatetime(blog.created)

        response = blog_pb2.Blog(
            id=blog.id,
            title=blog.title,
            content=blog.content,
            created=created_timestamp,
            is_published=blog.is_published,
            user_id=blog.user_id
        )
        db.close()
        return response

    def List(self, request, context):
        db = SessionLocal()
        blogs = db.query(BlogModel).all()
        db.close()
        response = blog_pb2.BlogListResponse()
        for blog in blogs:
            created_timestamp = Timestamp()
            created_timestamp.FromDatetime(blog.created)

            response.blogs.add(
                id=blog.id,
                title=blog.title,
                content=blog.content,
                created=created_timestamp,
                is_published=blog.is_published,
                user_id=blog.user_id
            )
        return response

    def Read(self, request, context):
        db = SessionLocal()
        blog = db.query(BlogModel).filter(BlogModel.id == request.id).first()
        db.close()
        if blog is None:
            context.abort(grpc.StatusCode.NOT_FOUND, "Blog not found")

        created_timestamp = Timestamp()
        created_timestamp.FromDatetime(blog.created)

        return blog_pb2.Blog(
            id=blog.id,
            title=blog.title,
            content=blog.content,
            created=created_timestamp,
            is_published=blog.is_published,
            user_id=blog.user_id
        )

    def Update(self, request, context):
        db = SessionLocal()
        blog = db.query(BlogModel).filter(BlogModel.id == request.id).first()
        if blog is None:
            db.close()
            context.abort(grpc.StatusCode.NOT_FOUND, "Blog not found")

        blog.title = request.title
        blog.content = request.content
        blog.is_published = request.is_published
        blog.user_id = request.user_id
        db.commit()
        db.refresh(blog)

        created_timestamp = Timestamp()
        created_timestamp.FromDatetime(blog.created)

        response = blog_pb2.Blog(
            id=blog.id,
            title=blog.title,
            content=blog.content,
            created=created_timestamp,
            is_published=blog.is_published,
            user_id=blog.user_id
        )
        db.close()
        return response

    def Delete(self, request, context):
        db = SessionLocal()
        blog = db.query(BlogModel).filter(BlogModel.id == request.id).first()
        if blog is None:
            db.close()
            context.abort(grpc.StatusCode.NOT_FOUND, "Blog not found")

        db.delete(blog)
        db.commit()
        db.close()
        return Empty()


async def run(addr):
    server = aio.server()
    blog_pb2_grpc.add_BlogServiceServicer_to_server(BlogService(), server)
    server.add_insecure_port(addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    print('run')
    asyncio.run(run('[::]:50051'))