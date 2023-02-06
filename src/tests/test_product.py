import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_search_product_wrong_keyword(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "keyword": "string",
        "price_sorted": "default",
        "name_sorted": "default"
    })
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.anyio
async def test_search_all_product_without_keyword(client: AsyncClient):
    response = await client.post("/api/product/search", json={})
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Nokia 3310",
            "price": 1000
        },
        {
            "name": "Motorola V3",
            "price": 3000
        },
        {
            "name": "Samsung G1000",
            "price": 52200
        },
        {
            "name": "Xiaomi Note10 Pro",
            "price": 13000
        },
        {
            "name": "Iphone 14",
            "price": 20000
        },
        {
            "name": "Nokia XS",
            "price": 12000
        },
        {
            "name": "Iphone 15",
            "price": 22000
        },
        {
            "name": "Nokia A",
            "price": 26000
        }
    ]


@pytest.mark.anyio
async def test_search_product_keyword_nokia_lowercase_without_sorting(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "keyword": "nokia",
        "price_sorted": "default",
        "name_sorted": "default"
    })
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Nokia 3310",
            "price": 1000
        },
        {
            "name": "Nokia XS",
            "price": 12000
        },
        {
            "name": "Nokia A",
            "price": 26000
        }
    ]


@pytest.mark.anyio
async def test_search_product_keyword_nokia_uppercase_without_sorting(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "keyword": "Nokia",
        "price_sorted": "default",
        "name_sorted": "default"
    })
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Nokia 3310",
            "price": 1000
        },
        {
            "name": "Nokia XS",
            "price": 12000
        },
        {
            "name": "Nokia A",
            "price": 26000
        }
    ]


@pytest.mark.anyio
async def test_search_product_keyword_nokia_price_sorted_asc(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "keyword": "nokia",
        "price_sorted": "asc",
        "name_sorted": "default"
    })
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Nokia 3310",
            "price": 1000
        },
        {
            "name": "Nokia XS",
            "price": 12000
        },
        {
            "name": "Nokia A",
            "price": 26000
        }
    ]


@pytest.mark.anyio
async def test_search_product_keyword_nokia_price_sorted_desc(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "keyword": "nokia",
        "price_sorted": "desc",
        "name_sorted": "default"
    })
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Nokia A",
            "price": 26000
        },
        {
            "name": "Nokia XS",
            "price": 12000
        },
        {
            "name": "Nokia 3310",
            "price": 1000
        }
    ]


@pytest.mark.anyio
async def test_search_product_keyword_nokia_name_sorted_asc(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "keyword": "nokia",
        "price_sorted": "default",
        "name_sorted": "asc"
    })
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Nokia 3310",
            "price": 1000
        },
        {
            "name": "Nokia A",
            "price": 26000
        },
        {
            "name": "Nokia XS",
            "price": 12000
        }
    ]


@pytest.mark.anyio
async def test_search_product_keyword_nokia_name_sorted_desc(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "keyword": "nokia",
        "price_sorted": "default",
        "name_sorted": "desc"
    })
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Nokia XS",
            "price": 12000
        },
        {
            "name": "Nokia A",
            "price": 26000
        },
        {
            "name": "Nokia 3310",
            "price": 1000
        }
    ]


@pytest.mark.anyio
async def test_search_product_without_keyword_name_sorted_desc(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "price_sorted": "default",
        "name_sorted": "desc"
    })
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Xiaomi Note10 Pro",
            "price": 13000
        },
        {
            "name": "Samsung G1000",
            "price": 52200
        },
        {
            "name": "Nokia XS",
            "price": 12000
        },
        {
            "name": "Nokia A",
            "price": 26000
        },
        {
            "name": "Nokia 3310",
            "price": 1000
        },
        {
            "name": "Motorola V3",
            "price": 3000
        },
        {
            "name": "Iphone 15",
            "price": 22000
        },
        {
            "name": "Iphone 14",
            "price": 20000
        }
    ]


@pytest.mark.anyio
async def test_search_product_without_keyword_price_sorted_asc(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "price_sorted": "asc",
        "name_sorted": "default"
    })
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Nokia 3310",
            "price": 1000
        },
        {
            "name": "Motorola V3",
            "price": 3000
        },
        {
            "name": "Nokia XS",
            "price": 12000
        },
        {
            "name": "Xiaomi Note10 Pro",
            "price": 13000
        },
        {
            "name": "Iphone 14",
            "price": 20000
        },
        {
            "name": "Iphone 15",
            "price": 22000
        },
        {
            "name": "Nokia A",
            "price": 26000
        },
        {
            "name": "Samsung G1000",
            "price": 52200
        }
    ]


@pytest.mark.anyio
async def test_search_product_without_keyword_price_and_name_sorted_asc(client: AsyncClient):
    response = await client.post("/api/product/search", json={
        "price_sorted": "asc",
        "name_sorted": "asc"
    })
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Iphone 14",
            "price": 20000
        },
        {
            "name": "Iphone 15",
            "price": 22000
        },
        {
            "name": "Motorola V3",
            "price": 3000
        },
        {
            "name": "Nokia 3310",
            "price": 1000
        },
        {
            "name": "Nokia A",
            "price": 26000
        },
        {
            "name": "Nokia XS",
            "price": 12000
        },
        {
            "name": "Samsung G1000",
            "price": 52200
        },
        {
            "name": "Xiaomi Note10 Pro",
            "price": 13000
        }
    ]


@pytest.mark.anyio
async def test_create_new_product(client: AsyncClient):
    response = await client.post("/api/product/", json={
        "name": "Samsung",
        "price": 101010
    })
    assert response.status_code == 201
    assert response.json() == {
        "name": "Samsung",
        "price": 101010
    }


@pytest.mark.anyio
async def test_create_new_poduct_with_wrong_price(client: AsyncClient):
    response = await client.post("/api/product/", json={
        "name": "Samsung",
        "price": 10101093284928490239482942948
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "price"
                ],
                "msg": "Product price must be less 99999999999.9",
                "type": "value_error"
            }
        ]
    }


@pytest.mark.anyio
async def test_create_new_poduct_with_wrong_price_and_name(client: AsyncClient):
    response = await client.post("/api/product/", json={
        "name": "Samsung_bararararaksfdsklfklsnfklsdjfklsjfklndaklfnskadlnflskfjnsjfopsfmkldsnmkldsafmsdfklmjjfsfj"
                "*sdfdjsfksjdflksjflaksjdfklndjkfnsjkfnsdkjfsjkanfjksnfjkasdnfkjsdnfjksdnfsjkdf",
        "price": 10101093284928490239482942948
    })
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "name"
                ],
                "msg": "Product name must be less than 150  but more than 0 characters",
                "type": "value_error"
            },
            {
                "loc": [
                    "body",
                    "price"
                ],
                "msg": "Product price must be less 99999999999.9",
                "type": "value_error"
            }
        ]
    }
