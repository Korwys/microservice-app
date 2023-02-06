import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_cart_add_product_with_wrong_id(client: AsyncClient):
    response = await client.post("/api/cart/add", json={
        "product": 0,
        "quantity": 1
    })
    assert response.status_code == 404
    assert response.json() == {
        "Message": "Product with this ID not found. Can't add to cart."
    }


@pytest.mark.anyio
async def test_cart_add_product(client: AsyncClient):
    response = await client.post("/api/cart/add", json={
        "product": 1,
        "quantity": 1
    })
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "product": 1,
        "price": 1000,
        "quantity": 1
    }


@pytest.mark.anyio
async def test_cart_update_product_quantity(client: AsyncClient):
    response = await client.patch("/api/cart/update_quantity", json={
        "product": 1,
        "quantity": 10
    })
    assert response.status_code == 200
    assert response.json() == {
        "product": 1,
        "quantity": 10
    }


@pytest.mark.anyio
async def test_cart_update_product_quantity_which_no_in_cart(client: AsyncClient):
    response = await client.patch("/api/cart/update_quantity", json={
        "product": 999,
        "quantity": 10
    })
    assert response.status_code == 404
    assert response.json() == {
        "Message": "No product with same ID in the cart. Check product ID"
    }


@pytest.mark.anyio
async def test_cart_update_product_quantity_for_zero_value(client: AsyncClient):
    response = await client.patch("/api/cart/update_quantity", json={
        "product": 1,
        "quantity": 0
    })
    assert response.status_code == 404
    assert response.json() == {
        "Message": "Product quantity must be greater than 0"
    }


@pytest.mark.anyio
async def test_cart_get_all_product_from_cart(client: AsyncClient):
    response = await client.get("/api/cart/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "product": 1,
            "price": 1000.0,
            "quantity": 10
        }
    ]
