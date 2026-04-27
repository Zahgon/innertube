from typing import Optional

from httpx import Client, Request, Response

from . import api
from .config import config
from .errors import RequestError, ResponseError
from .models import ClientContext


class InnerTubeAdaptor:
    context: ClientContext
    session: Client

    def __init__(
        self, context: ClientContext, session: Optional[Client] = None
    ) -> None:
        self.context = context
        self.session = session or Client(base_url=config.base_url)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(context={self.context!r})"

    def _build_request(
        self, endpoint: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> Request:
        pass

    def _request(
        self, endpoint: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> Response:
        pass

    def dispatch(
        self, endpoint: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> dict:
        pass
