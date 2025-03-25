from django.shortcuts import render
import asyncio

# Create your views here.
async def header_view(request):
    await asyncio.sleep(0)  # Placeholder for future async operations
    return render(request, "header.html")

async def footer_view(request):
    await asyncio.sleep(0)  # Placeholder for future async operations
    return render(request, "footer.html")

async def index_view(request):
    await asyncio.sleep(0)  # Placeholder for future async operations
    return render(request, "index.html")

async def about_view(request):
    await asyncio.sleep(0)  # Placeholder for future async operations
    return render(request, "about.html")

async def services_view(request):
    await asyncio.sleep(0)  # Placeholder for future async operations
    return render(request, "services.html")

async def portfolio_view(request):
    await asyncio.sleep(0)  # Placeholder for future async operations
    return render(request, "portfolio.html")

async def blog_view(request):
    await asyncio.sleep(0)  # Placeholder for future async operations
    return render(request, "blog.html")

async def contact_view(request):
    await asyncio.sleep(0)  # Placeholder for future async operations
    return render(request, "contact.html")
