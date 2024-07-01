import grpc
import blog_pb2
import blog_pb2_grpc

from blog_grpc.core.models import BlogModel


class BlogService(blog_pb2_grpc.BlogService):
    def Create(request,
               target,
               options=(),
               channel_credentials=None,
               call_credentials=None,
               insecure=False,
               compression=None,
               wait_for_ready=None,
               timeout=None,
               metadata=None):
        print(request.title)

    def List(self):