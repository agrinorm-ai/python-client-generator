from typing import Any, Dict, Optional, Union

import httpx

from .base_client import BaseClient
from .models import *


class Api(BaseClient):
    """
    Autogenerated httpx async client
    """
    async def read_foo_api_foo__foo_id__get(
        self,
        foo_id: UUID,
        **kwargs: Any
    ) -> Foo:
        """
        
        """ # noqa 

        response = await self._request(
            "GET",
            f"/api/foo/{foo_id}",
            **kwargs
        )
        response.raise_for_status()
        return Foo.model_validate_json(response.content)

    async def update_foo_api_foo__foo_id__patch(
        self,
        foo_id: UUID,
        **kwargs: Any
    ) -> Foo:
        """
        
        """ # noqa 

        response = await self._request(
            "PATCH",
            f"/api/foo/{foo_id}",
            **kwargs
        )
        response.raise_for_status()
        return Foo.model_validate_json(response.content)

    async def put_foo_api_foo__foo_id__put(
        self,
        foo_id: UUID,
        **kwargs: Any
    ) -> Foo:
        """
        
        """ # noqa 

        response = await self._request(
            "PUT",
            f"/api/foo/{foo_id}",
            **kwargs
        )
        response.raise_for_status()
        return Foo.model_validate_json(response.content)

    async def delete_foo_api_foo__foo_id__delete(
        self,
        foo_id: UUID,
        **kwargs: Any
    ) -> Foo:
        """
        
        """ # noqa 

        response = await self._request(
            "DELETE",
            f"/api/foo/{foo_id}",
            **kwargs
        )
        response.raise_for_status()
        return Foo.model_validate_json(response.content)

    async def list_foos_api_foo_get(
        self,
        some_field: Optional[str] = None,
        show_deleted: bool = False,
        offset: Optional[int] = 0,
        limit: Optional[int] = 10,
        **kwargs: Any
    ) -> PaginatedFoo:
        """
        
        """ # noqa 

        _query_params = { 
            "some_field": some_field,
            "show_deleted": show_deleted,
            "offset": offset,
            "limit": limit,
        }

        response = await self._request(
            "GET",
            "/api/foo",
            _query_params=_query_params, 
            **kwargs
        )
        response.raise_for_status()
        return PaginatedFoo.model_validate_json(response.content)

    async def create_foo_api_foo_post(
        self,
        body: Foo,
        x_custom_header: Optional[str] = "default_value",
        body_serializer_args: Dict[str, Any] = {},
        **kwargs: Any
    ) -> Foo:
        """
        
        """ # noqa 

        _headers = { 
            "x-custom-header": x_custom_header,
        }

        response = await self._request(
            "POST",
            "/api/foo",
            _headers=_headers,
            _body=body,
            body_serializer_args=body_serializer_args,
            **kwargs
        )
        response.raise_for_status()
        return Foo.model_validate_json(response.content)

    async def upload_doc_api_foo__foo_id__documents_post(
        self,
        file: httpx._types.FileTypes,
        foo_id: UUID,
        **kwargs: Any
    ) -> Document:
        """
        
        """ # noqa 

        _files = { 
            "file": file,
        }

        response = await self._request(
            "POST",
            f"/api/foo/{foo_id}/documents",
            files=_files,
            **kwargs
        )
        response.raise_for_status()
        return Document.model_validate_json(response.content)


