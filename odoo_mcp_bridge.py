import os
import xmlrpc.client
import asyncio
from mcp.server.fastmcp import FastMCP

# Odoo Connection Details
URL = os.environ.get('ODOO_URL', 'http://localhost:8069')
DB = os.environ.get('ODOO_DB', 'cupsandcontainers')
USER = os.environ.get('ODOO_USER', 'admin')
PWD = os.environ.get('ODOO_PASSWORD', 'Fuckoff2019!@#@#$')

mcp = FastMCP("Odoo")

def get_odoo_client():
    common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
    uid = common.authenticate(DB, USER, PWD, {})
    models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")
    return models, uid

@mcp.tool()
def list_products(limit: int = 10):
    """List products from Odoo"""
    models, uid = get_odoo_client()
    products = models.execute_kw(DB, uid, PWD, 'product.template', 'search_read', [[]], {'fields': ['name', 'list_price'], 'limit': limit})
    return products

@mcp.tool()
def create_product(name: str, price: float):
    """Create a new product in Odoo"""
    models, uid = get_odoo_client()
    product_id = models.execute_kw(DB, uid, PWD, 'product.template', 'create', [{'name': name, 'list_price': price}])
    return f"Product created with ID: {product_id}"

@mcp.tool()
def search_partners(name: str):
    """Search for customers/partners by name"""
    models, uid = get_odoo_client()
    partners = models.execute_kw(DB, uid, PWD, 'res.partner', 'search_read', [[['name', 'ilike', name]]], {'fields': ['name', 'email']})
    return partners

if __name__ == "__main__":
    mcp.run()
